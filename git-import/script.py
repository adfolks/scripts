import glob
import os
# import commands
import subprocess as sp
repoName =glob.glob("*")

for repo in repoName:
    if(repo =="script.py"):
        continue
    print("Preparation started for ",repo)
    os.system('ghe-migrator prepare '+repo+' > file.txt')   
    status,guid = sp.getstatusoutput("grep -i guid file.txt | awk '{print $3}'")
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    print("Importing repo ",repo)
    os.system('ghe-migrator import '+repo+' -g'+guid+' -u ssrcdevops -p' )
    print("Unlocking repo ",repo)
    os.system('ghe-migrator unlock -g'+guid)
    os.system('echo'+repo+' '+guid+'>> guidfile.txt')
    os.system('rm conflicts.csv file.txt')



    


   



