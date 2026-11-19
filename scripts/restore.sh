#!/bin/bash
set -e

BACKUP_FILE="$1"

if [ -z "$BACKUP_FILE" ] || [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: Valid backup file required"
    exit 1
fi

tar -xzf "$BACKUP_FILE" -C .

echo "Recovery completed successfully!"
cat data/important.txt
