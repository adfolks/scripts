## github_migrator
A bash script to migrate all private/public repositories under an organization, and download archives in a single go, for restoring on to github enterprise or github.com.
Backups are downloaded and placed in working directory. Github access token required as owner of the organization.

Available commands - backup, download, status and help.

### Changelog
v0.2 - backup, download and status checks with instructions.

### Dependencies
1. Github Access Token generated as owner of the organization
2. curl command

### Download and give execute permission
`wget https://raw.githubusercontent.com/adfolks/scripts/main/github_migrator`

`chmod +x ./github_migrator`

### Instructions

Edit github_migrator and add access token, organization name, and username. Provide execute permission and call the script from working directory.

`./github_migrator --help`

Available commands are backup, download, status and help. Avoid running backup more than once as it creates seperate intances of backup on server side.

#### Help with instructions

`./github_migrator --help`

#### Backup all repositories 
`./github_migrator --backup`

Note: Do not run 'backup' more than once to avoid duplicates.

#### Check status of backups
`./github_migrator --status`

#### Download all exported backups to working directory
`./github_migrator --download`

### Roadmap
1. Add restore commands
2. Add clean up of archives on github end after backups
