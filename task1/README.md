# Logs Backup

## Overview
This task automates the backup of application logs from `/var/log/myapp` by:
- Compressing logs into a timestamped `.tar.gz` file in `/backups/`
- Scheduling the task to run hourly using Ansible and a cron job

## Components
- **backup.sh**: Shell script to compress and backup logs
- **playbook.yml**: Ansible playbook to install dependencies, copy the script, and create the cron job
- **inventory.ini**: Ansible inventory file to define target hosts

## Prerequisites
- Ansible installed on the control machine
- SSH access to target servers

## Usage
1. Make the shell script executable:
   ```bash
   chmod +x backup.sh
