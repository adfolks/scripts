# github-migrator
A bash script to migrate all private/public repositories under an organization, and download archives in a single go, for restoring on to github enterprise or github.com.
Backups are downloaded and placed in working directory. Github access token required as owner of the organization.

Available commands - backup, download, status, delete and help.

## Changelog
v0.2 - backup, download and status checks with instructions.

v0.3 - add delete archive option.

## Dependencies
1. Github Access Token generated as owner of the organization.
2. curl

## How to

`git clone git@github.com:adfolks/scripts.git`

`cd scripts`

`chmod +x ./github-migrator`

`./github-migrator --help`

## Instructions

Edit github-migrator and add access token, organization name, and username. Provide execute permission and call the script from working directory.

Available commands are backup, download, status and help. Avoid running backup more than once as it creates seperate intances of backup on server side.

## Commands

### Help with instructions
`./github-migrator --help`

### Backup all repositories 
`./github-migrator --backup`

Note: Do not run 'backup' more than once to avoid duplicates.

### Check status of backups
`./github-migrator --status`

### Download all exported backups to working directory
`./github-migrator --download`

### Delete all current backup archives from Github.com
`./github-migrator --delete`

This will delete all current backup migration archives from github.com end, useful to clean up after download, or to start anew.
Alternately migration archives are automatically deleted after seven days.

## Roadmap
1. Add restore commands.
2. Add clean up of archives on github end after backups. #done
3. Accept token and username as arguments.
