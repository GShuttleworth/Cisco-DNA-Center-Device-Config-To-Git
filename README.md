# Cisco-DNA-Center-Device-Config-To-Git

## Introduction

This is an example python script to demonstrate programmatically collecting current running config from all devices managed by [Cisco DNA Center](https://www.cisco.com/c/en_uk/products/cloud-systems-management/dna-center/index.html) and storing each device config file in a Git repo.

This allows you to monitor for configuration changes and track changes to over time.

![alt text](/readme_images/git_diff.png "Git diff on Cisco DNA Center device config")

## Prerequisites

1. [Python](https://www.python.org/) - this has been tested with Python 3.8.6.
2. [Git](https://git-scm.com/) installed on your computer.
3. A remote Git repository. This has been tested against remote [GitHub](https://github.com/) repositories.
4. A Bash (or Bash compatible) terminal - the python script runs Git Bash commands directly in a terminal instance using `subprocess`.
5. Access to a DNA Center API - see below for instructions on using a virtual DevNet Sandbox.

### Use a virtual Cisco DNA Center API from DevNet Sandbox

You can get a virtual instance of a Cisco IOS-XE device from the [DevNet Sandbox](https://devnetsandbox.cisco.com/) if you don't want to try this against a physical device.

> This is optional

1. Go to DevNet Sandbox https://devnetsandbox.cisco.com/
2. Select the always-on version of the Cisco DNA Center sandbox.

![alt text](/readme_images/dna_center_sandbox.png "Cisco DNA Center always-on DevNet Sandbox")

## Getting started

### Clone this Git Repository

```bash
git clone https://github.com/GShuttleworth/Cisco-DNA-Center-Device-Config-To-Git
```

Open new Git repo folder in terminal

```bash
cd Cisco-DNA-Center-Device-Config-To-Git
```

### Setup Python virtual environment

It is good practice to run Python scripts in a virtual environment.

Create virtual environment

```bash
python3 -m venv venv
```

Open the virtual environment

```bash
source venv/bin/activate
```

Install Python dependencies

```bash
pip install -r requirements.txt
```

## Edit Python file

The `dna_center_to_git.py` Python script has some variables you need to define.

Edit `url`, `username` and `password` to match your device. By default the connection details are for the DevNet IOS-EX Sandbox mentioned above.

You should also set `use_ssl_verification` to `True` if you are using this code in production to ensure ssl certificates are respected (and used).

```python
# DNA Center Connection Details
username = "devnetuser"
password = "Cisco123!"
url = "https://sandboxdnac.cisco.com"
use_ssl_verification = False  # Always set to 'True' in production environments
```

Edit `git_repo_url` to match your Git repository URL.

Optional - edit `commit_message` to specify what Git should use as the message for each commit.

```python
# Git settings
git_repo_url = "https://github.com/your_repo_url"
commit_message = "Auto config sync with DNA Center devices"
```

## Run the Python script

To run the Python script

```bash
python dna_center_to_git.py
```

## Check the result

The script automatically deletes all created files after the Git push is complete. This means there's nothing to see locally after it has ran.

Go to your remote Git repository and you should see your config uploaded.

If you make changes to any device config and re-run the Python script, you will see Git track the changes between the new config and the old config. Check the changes by viewing the most recent Git commit!

![alt text](/readme_images/config_files.png "All Config in Git after running the python script")

## Troubleshooting

If you have problems running the script, it is likely that the Git installed on your computer hasn't authenticated with the remote Git repository. The Python script relies on connection authentication credentials being cached on your computer.

To fix, manually clone the repository, and if prompted, enter authentication details.

```bash
git clone <git_repo_url>
```

You may need to use an access token rather than a password. Check [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) for details on creating access tokens if you're using GitHub
