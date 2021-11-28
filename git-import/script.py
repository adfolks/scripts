import glob
import os
repoName =glob.glob("*")

# for repo in repoName:
#     # os.system('ghe-migrator prepare '+repo)
#     os.system('cat '+repo+' > file.txt')


os.system('ghe-migrator prepare migration_archive_cdsl4linux.tar.gz > file.txt')    
