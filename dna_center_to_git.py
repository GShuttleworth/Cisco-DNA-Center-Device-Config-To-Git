import requests
import base64
import tempfile
import subprocess
import json

# DNA Center Connection Details
username = "devnetuser"
password = "Cisco123!"
url = "https://sandboxdnac.cisco.com"
use_ssl_verification = False  # Always set to 'True' in production environments

# Git settings
git_repo_url = "https://github.com/your_repo_url"
commit_message = "Auto config sync with DNA Center devices"

# ------ Connect to DNA Center and get device configs ------

# Generate Base64 login string
auth_string = f"{username}:{password}"
auth_string = auth_string.encode("ascii")
auth_string = base64.b64encode(auth_string)
auth_string = str(auth_string, "utf-8")
auth_string = f"Basic {auth_string}"

# Get Authentication Token from DNA Center API
headers = {"Authorization": auth_string}
response = requests.post(
    f"{url}/dna/system/api/v1/auth/token", headers=headers, verify=use_ssl_verification
)
response_data = json.loads(response.text)
authToken = response_data["Token"]

# Get all Device Config
headers = {"x-auth-token": authToken}
response = requests.get(
    f"{url}/dna/intent/api/v1/network-device/config",
    headers=headers,
    verify=use_ssl_verification,
)
response_data = json.loads(response.text)

# ------ Clone git repo in temporary directory, replace files with new config file and push changes back to git repo  ------

# Create temporary directory
f = tempfile.TemporaryDirectory()

# Clone Git Repo
subprocess.call(f"cd {f.name} && git clone {git_repo_url} . && rm *.*", shell=True)

# Write all config to JSON files
for config in response_data["response"]:
    id = config["id"]
    running_config = config["runningConfig"]
    with open(f"{f.name}/{id}.txt", "w") as outfile:
        outfile.write(running_config)

# Git commit all changes
subprocess.call(
    f"cd {f.name} && git add -A && git commit -a -m 'Auto config sync with devices' && git push",
    shell=True,
)

# Delete temporary directory
f.cleanup()
