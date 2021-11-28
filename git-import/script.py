import glob
import os
repoName =glob.glob("*")

for repo in repoName:
    os.system('ghe-migrator prepare '+repo)
    
