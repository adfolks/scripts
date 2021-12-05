import glob
import os
# import commands
import subprocess as sp
repoName =glob.glob("*")
totalRepo = len(repoName) -1 
print("*******************************")
print(repoName)
print("*******************************")
i=0
for repo in repoName:
    if(repo =="script.py"):
        continue
    print(i,"-",totalRepo, "Preparation started for ",repo)
    os.system('ghe-migrator prepare '+repo+' > file.txt')   
    status,guid = sp.getstatusoutput("grep -i guid file.txt | awk '{print $3}'")
    print("Conflict file generating for ",repo)
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    print("Resolving conflict for ",repo)
    # Modify this the code below accroding to the requirement
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    os.system('ghe-migrator conflicts -g'+guid+' > conflicts.csv')  
    os.system('ghe-migrator map merge -i conflicts.csv -g'+guid)   
    #Make sure that all the conflicts are resolved before this line
    print("Importing repo ",repo)
    os.system('ghe-migrator import '+repo+' -g '+guid+' -u ssrcdevops -p' )
    print(i,"-",totalRepo,"Unlocking repo ",repo)
    os.system('ghe-migrator unlock -g '+guid)
    os.system('echo '+repo+' '+guid+'>> guidfile.txt')
    os.system('rm conflicts.csv file.txt')
    i+=1