[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/GShuttleworth/Cisco-DNA-Center-Device-Config-To-Git)
[![Tested on Python 3.8.6](https://img.shields.io/badge/Tested%20-Python%203.8.6-blue.svg?logo=python)](https://www.python.org/downloads)
[![Contributions Welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Cisco-DNA-Center-Device-Config-To-Git

## Introduction

This is an example Python script to programmatically demonstrate collecting current running config from all devices managed by [Cisco DNA Center](https://www.cisco.com/c/en_uk/products/cloud-systems-management/dna-center/index.html) and storing each device config file in a Git repo.

This allows you to monitor for configuration changes and to track changes over time.

![Alt text](readme_images/git_diff.png 'Git Diff on Cisco DNA Center device config')

## Prerequisites

1. [Python](https://www.python.org/) - This has been tested on Python 3.8.6.
2. [Git](https://git-scm.com/) installed on your computer.
3. A remote Git repository. This has been tested on remote [GitHub](https://github.com/) repositories.
4. A Bash (or Bash compatible) terminal - The Python script runs Git Bash commands directly in a terminal instance using `subprocess`.
5. Access to a DNA Center API - See below for instructions on using a virtual Cisco DevNet Sandbox.

### Use a Virtual Cisco DNA Center API from Cisco DevNet Sandbox

If you don't want to try this against a physical DNA Center deployment, you can access a virtual DNA Center API from the [Cisco DevNet Sandbox](https://devnetsandbox.cisco.com/).

> This is optional

1. Go to [Cisco DevNet Sandbox](https://devnetsandbox.cisco.com/).
2. Select the Always-On version of the Cisco DNA Center Sandbox.

![Alt text](readme_images/dna_center_sandbox.png 'Cisco DNA Center always-on DevNet Sandbox')

## Getting Started

### Clone this GitHub Repository

```bash
$ git clone https://github.com/GShuttleworth/Cisco-DNA-Center-Device-Config-To-Git.git
$ cd Cisco-DNA-Center-Device-Config-To-Git
```

### Setup Python virtual environment

It is a good practice to run Python scripts in a virtual environment.

Create virtual environment

```bash
$ python3 -m venv venv
```

Open the virtual environment

```bash
$ source venv/bin/activate
```

Install Python dependencies

```bash
$ pip install -r requirements.txt
```

## Edit Python file

The `dna_center_to_git.py` Python script has some variables you need to define.

Edit `url`, `username` and `password` to match your DNA Center. By default the connection details are for the Cisco DevNet DNA Center Sandbox mentioned above.

You should also set `use_ssl_verification` to `True` if you are using this code in a production environment to ensure SSL certificates are respected (and used).

```python
# DNA Center Connection Details
username = "devnetuser"
password = "Cisco123!"
url = "https://sandboxdnac.cisco.com"
use_ssl_verification = False  # Always set to 'True' in production environments
```

Edit `git_repo_url` to match your Git repository URL.

Edit `commit_message` to specify what Git should use as the message for each commit. (Optional)

```python
# Git settings
git_repo_url = "https://github.com/your_repo_url"
commit_message = "Auto config sync with DNA Center devices"
```

## Run the Python script

To run the Python script

```bash
$ python3 dna_center_to_git.py
```

## Check the result

The script automatically deletes all created files after the Git push is complete. This means there's nothing to see locally after it has ran.

Go to your remote Git repository and you should see your config uploaded.

If you make changes to any device config and re-run the Python script, you will see that Git tracks the changes between the new config and the old config. Check the changes by viewing the most recent Git commit!

![Alt text](readme_images/config_files.png 'All Config in Git after running the python script')

## Troubleshooting

If you have problems running the script, it is likely that the Git installed on your computer hasn't authenticated with the remote Git repository. The Python script relies on connection authentication credentials being cached on your computer.

To fix, manually clone the repository, and if prompted, enter authentication details.

```bash
$ git clone <git_repo_url>
```

You may need to use an access token rather than a password. Check [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) for details on creating access tokens if you're using GitHub.
