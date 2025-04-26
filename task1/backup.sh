#!/bin/bash

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="logs_backup_$TIMESTAMP.tar.gz"

mkdir -p /backups

tar -czf /backups/$BACKUP_FILE /var/log/myapp

echo "Backup completed at $(date)"

