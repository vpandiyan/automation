from git import Repo
import subprocess,os,git,shutil
import requests, json, sys, os.path
import glob
import errno
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
    print ("Deleting node modules")
    shutil.rmtree('node_modules', ignore_errors=True)
cmd = "npm i"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
print("node modules updated")
os.chdir("../../../")
try:
    shutil.copy2('Config/node_modules/angular2-signaturepad/signature-pad.js', config['paths']['propath']+'node_modules/angular2-signaturepad/signature-pad.js')
    shutil.copy2('Config/node_modules/signature_pad/dist/signature_pad.mjs', config['paths']['propath']+'node_modules/signature_pad//dist/signature_pad.mjs')
    os.chdir(config['paths']['propath'])
    # Directories are the same
except shutil.Error as e:
    print('Directory not copied. Error: %s' % e)
    os.chdir(config['paths']['propath'])
    # Any error saying that the directory doesn't exist
except OSError as e:
    print('Directory not copied. Error: %s' % e)
    os.chdir(config['paths']['propath'])
if os.path.exists("config.xml"):
    f = open("config.xml","r+")
    r = f.read()
    lines=r.find('version="')
    length = len('version=')+1
    f.seek(lines+length)
    version = f.read(4)
    f.seek(lines+length+4)
    ver = int(f.read(1))+1
    version = version+str(ver)
    f.seek(lines+length)
    f.write(version)
    print("Version Updated to",version)

if os.path.isdir("platforms"):
    print("Platforms already Added")
    shutil.rmtree('platforms', ignore_errors=True)

cmd = "ionic cordova platform add android@6.4.0"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
os.chdir("../../../")
path = config['paths']['propath']+'platforms/android/cordova-support-google-services/*.gradle'   
files = glob.glob(path)   
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name,'w') as f: # No need to specify 'r': this is the default.
            # sys.stdout.write(f.read())
            g = open("Config\gradle\config.gradle","r+")
            r = g.read()
            f.write(r)
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise 
os.chdir(config['paths']['propath'])
cmd = "ionic cordova build android --prod --release"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
os.chdir("../../../")

filePath = config['paths']['propath']+config['paths']['apkpath']+'android-release-unsigned.apk'
shutil.copy2(filePath ,config['paths']['buildpath']+'/android-release-unsigned.apk')
os.chdir(config['paths']['buildpath'])
cmd = "jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.jks -storepass Minuscule-1 android-release-unsigned.apk cmms"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()
if os.path.exists("app.apk"):
    os.remove("app.apk")
cmd = "zipalign -v 4 android-release-unsigned.apk app.apk"
p = subprocess.Popen(cmd, shell=True)
out, err = p.communicate()

if os.path.exists("app.apk"):
    print("You choosed : %s APK" % choice)
    shutil.copy2('app.apk',apkpath)
    build_file = config['paths']['buildpath']+'/'+apkpath
print("Apk Build")
# api_token = config['hockeyapp']['token']
# UPLOAD_URL = config['hockeyapp']['upload_url']
# params = {}
# params['notes'] = config['hockeyapp']['params']['notes']
# if os.path.exists(build_file):
#     print("File Exists",build_file)
#     files = {'ipa': open(build_file, 'rb')}
#     headers = {'X-HockeyAppToken' : api_token}
#     try:
#         req = requests.post(url=UPLOAD_URL, data=params, files=files, headers=headers)
#         if req.status_code == 201 or req.status_code == 200:
#             print("APK successfully uploaded to Hockeyapp...")
#             print (req.json())
#     except ConnectionError:
#         print('Connection error. Please try again.')
# else:
#     print("Apk not available for upload")