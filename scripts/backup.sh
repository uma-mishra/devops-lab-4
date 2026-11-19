#!/bin/bash
set -e

mkdir -p backups

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="backups/backup_$TIMESTAMP.tar.gz"

tar -czf "$BACKUP_FILE" data

echo "Backup completed successfully!"
echo "Backup file: $BACKUP_FILE"
du -h "$BACKUP_FILE"
