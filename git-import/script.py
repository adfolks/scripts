import glob
import os
import commands
repoName =glob.glob("*")

for repo in repoName:
    os.system('ghe-migrator prepare migration_archive_cdsl4linux.tar.gz > file.txt')   
    status,guid = commands.getstatusoutput("grep -i guid file.txt | awk '{print $3}'")
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    os.system('ghe-migrator import '+repo+' -g'+guid)
    


   



