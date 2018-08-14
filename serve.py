from git import Repo
import subprocess,os,git,shutil
import requests, json, sys, os.path
from requests.exceptions import ConnectionError
with open('config.json', 'r') as f:
    config = json.load(f)
if os.path.isdir(config['paths']['gitrepopath']):
    print ("Project already cloned")
    # git.Git("App").pull("https://github.com/MinusculeTechnologiesLtd/mobilecode.git")
    repo = git.Repo(config['paths']['gitrepopath']+'/mobilecode')
    o = repo.remotes.origin
    o.pull()
else:
    os.mkdir(config['paths']['gitrepopath'])
    print ("This is a Fresh Checkout...")
    # Repo.clone_from("https://github.com/MinusculeTechnologiesLtd/mobilecode.git", "App")
    git.Git(config['paths']['gitrepopath']).clone(config['paths']['giturl'])

choice = sys.argv[1]
print("You choosed : %s" % choice)
tspath = config['paths'][choice]['tspath']
xmlpath = config['paths'][choice]['xmlpath']
jsonpath = config['paths'][choice]['jsonpath']    
apkpath = config['paths'][choice]['apkpath']
shutil.copy2(xmlpath,config['paths']['gitrepopath']+'/mobilecode/'+config['paths']['prod']['xmlpath'])
shutil.copy2(tspath,config['paths']['gitrepopath']+'/mobilecode/'+config['paths']['prod']['tspath'])
shutil.copy2(jsonpath,config['paths']['gitrepopath']+'/mobilecode/'+config['paths']['prod']['jsonpath'])

os.chdir(config['paths']['propath'])
retval = os.getcwd()
print("Directory changed successfully %s" % retval)

if os.path.isdir("node_modules"):
    print ("Already node modules created")
    shutil.rmtree('node_modules', ignore_errors=True)
cmd = "npm i"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print("node modules updated")

cmd = "ionic serve"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print(out, err)