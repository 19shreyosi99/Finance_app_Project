#!/bin/bash
DATE=$(date +%F)
mysqldump -u root -p'admin123' dbo users > ./backup_images/users_backup_$DATE.sql
mysqldump -u root -p'admin123' dbo budgets > ./backup_images/budgets_backup_$DATE.sql
mysqldump -u root -p'admin123' dbo transactions > ./backup_images/transactions_backup_$DATE.sql
