import glob
import os
import commands
repoName =glob.glob("*")

for repo in repoName:
    if(repo =="script.py"):
        continue
    print("prepare started for ",repo)
    os.system('ghe-migrator prepare'+repo+' > file.txt')   
    status,guid = commands.getstatusoutput("grep -i guid file.txt | awk '{print $3}'")
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    os.system('ghe-migrator import '+repo+' -g'+guid+'-u ssrcdevops -p' )
    os.system('ghe-migrator unlock -g'+guid)
    


   



