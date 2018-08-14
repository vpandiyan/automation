import shutil
import git
import os
from git import Repo
import subprocess
import requests, json, sys, os.path
from requests.exceptions import ConnectionError
import argparse
import json
import glob
import errno

path = 'D:/Pandiyan/Workspace/Automation/App/mobilecode/cryotos/platforms/android/cordova-support-google-services/*.gradle'   
files = glob.glob(path)   
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name,'w') as f: # No need to specify 'r': this is the default.
            # sys.stdout.write(f.read())
            g = open("D:\Pandiyan\Workspace\Automation\Config\gradle\config.gradle","r+")
            r = g.read()
            f.write(r)
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise 

# import hockeyapp
# with open('config.json', 'r') as f:
#     config = json.load(f)
# # print(config)

# choice = sys.argv[1]
# print(choice)
# print("You choosed : %s" % choice)
# tspath = config['paths'][choice]['tspath']
# xmlpath = config['paths'][choice]['xmlpath']
# jsonpath = config['paths'][choice]['jsonpath']    
# apkpath = config['paths'][choice]['apkpath']
# print(config['paths'][choice]['tspath'])
# os.chdir(config['paths']['propath'])
# retval = os.getcwd()

# print("Directory changed successfully %s" % retval)
# os.chdir("../")
# retval = os.getcwd()

# print("Directory changed successfully %s" % retval)
# os.chdir(r"D:/Pandiyan/Workspace/Practice/Python/Builds")
# f = open("config.xml","r+")
# r = f.read()
# lines=r.find('version="')
# length = len('version=')+1
# f.seek(lines+length)
# version = f.read(4)
# print(version)
# f.seek(lines+length+4)
# count = int(f.read(1))+1
# version = version+str(count)
# print(version)
# f.seek(lines+length)
# f.write(version)
# print(f.read())

# print (lines[1])
# print (lines[0])
# f.seek(10)
# lines[1].write("Queen")
# f.close()
# api_token = 'c92f0877cbd8409ebb29b0ae937f59b3'
# # app_id = 'ad2048dcffa6487b95d559d9c8347180'
# UPLOAD_URL = 'https://rink.hockeyapp.net/api/2/apps/upload'
# build_file = r"D:/Pandiyan/Workspace/Practice/Python/Builds/app.apk"
# params = {}
# params['notes'] = "Issues fixed"
# if os.path.exists(build_file):
#     print("File Exists")
#     files = {'ipa': open(build_file, 'rb')}
#     headers = {'X-HockeyAppToken' : api_token}
#     try:
#         req = requests.post(url=UPLOAD_URL, data=params, files=files, headers=headers)
#         print (req.json(), req.status_code)
#     except ConnectionError:
#         print('Connection error. Please try again.')
# else:
#     print("Not found")
# app_list = hockeyapp.apps.AppList(api_key)
# print (app_list)

# os.chdir(r"D:/Pandiyan/Workspace/IonicBuild")
# cmd = "jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1  -keystore my-release-key.jks -storepass Minuscule-1 android-release-unsigned.apk cmms"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()
# cmd = "zipalign -v 4 android-release-unsigned.apk auto-generate.apk"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()
# import shutil
# import git
# import os
# from git import Repo
# import subprocess
# import sys
# import requests, json, sys, os.path
# from requests.exceptions import ConnectionError
# with open('config.json', 'r') as f:
#     config = json.load(f)
# if os.path.isdir(config['paths']['gitrepopath']):
#     print ("Project already cloned")
#     # git.Git("App").pull("https://github.com/MinusculeTechnologiesLtd/mobilecode.git")
#     repo = git.Repo(config['paths']['gitrepopath']+'/mobilecode')
#     o = repo.remotes.origin
#     o.pull()
# else:
#     os.mkdir(config['paths']['gitrepopath'])
#     print ("This is a Fresh Checkout...")
#     # Repo.clone_from("https://github.com/MinusculeTechnologiesLtd/mobilecode.git", "App")
#     git.Git(config['paths']['gitrepopath']).clone(config['paths']['giturl'])
# # choice = input("Which version you want to build cryotos: /n1.Lincoln /n2.Unicorn /n ")
# choice = sys.argv[1]
# if choice == "1":
#     print("You choosed : Lincoln")
#     tspath = config['paths']['lincoln']['tspath']
#     xmlpath = config['paths']['lincoln']['xmlpath']
#     jsonpath = config['paths']['lincoln']['jsonpath']
#     apkpath = config['paths']['lincoln']['apkpath']
# elif choice == '2':
#     print("You choosed : Unicorn")
#     tspath = config['paths']['unicorn']['tspath']
#     xmlpath = config['paths']['unicorn']['xmlpath']
#     jsonpath = config['paths']['unicorn']['jsonpath']
#     apkpath = config['paths']['unicorn']['apkpath']
# elif choice == '3':
#     print("You choosed : Demo")
#     tspath = config['paths']['demo']['tspath']
#     xmlpath = config['paths']['demo']['xmlpath']
#     jsonpath = config['paths']['demo']['jsonpath']
#     apkpath = config['paths']['demo']['apkpath']
# elif choice == '4':
#     print("You choosed : Local")
#     tspath = config['paths']['local']['tspath']
#     xmlpath = config['paths']['local']['xmlpath']
#     jsonpath = config['paths']['local']['jsonpath']    
#     apkpath = config['paths']['local']['apkpath']
# else:
#     print("Please verify your choice")
#     # return
# print("You choosed : %s" % choice)
# tspath = config['paths'][choice]['tspath']
# xmlpath = config['paths'][choice]['xmlpath']
# jsonpath = config['paths'][choice]['jsonpath']    
# apkpath = config['paths'][choice]['apkpath']
# shutil.copy2(xmlpath,config['paths']['gitrepopath']+'/mobilecode/'+config['paths']['prod']['xmlpath'])
# shutil.copy2(tspath,config['paths']['gitrepopath']+'/mobilecode/'+config['paths']['prod']['tspath'])
# shutil.copy2(jsonpath,config['paths']['gitrepopath']+'/mobilecode/'+config['paths']['prod']['jsonpath'])

# os.chdir(config['paths']['propath'])
# retval = os.getcwd()

# print("Directory changed successfully %s" % retval)
# if os.path.isdir("node_modules"):
#     print ("Deleting node modules")
#     shutil.rmtree('node_modules', ignore_errors=True)
# cmd = "npm i"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()
# print("node modules updated")
# if os.path.exists("config.xml"):
#     f = open("config.xml","r+")
#     r = f.read()
#     lines=r.find('version="')
#     length = len('version=')+1
#     f.seek(lines+length)
#     version = f.read(4)
#     f.seek(lines+length+4)
#     ver = int(f.read(1))+1
#     version = version+str(ver)
#     f.seek(lines+length)
#     f.write(version)
#     print("Version Updated to",version)
# if os.path.isdir("platforms"):
#     print("Platforms already Added")
#     shutil.rmtree('platforms', ignore_errors=True)        
#     cmd = "ionic cordova platform add android@6.4.0"
#     p = subprocess.Popen(cmd, shell=True)
#     out, err = p.communicate()
#     cmd = "ionic cordova build android --prod --release"
#     p = subprocess.Popen(cmd, shell=True)
#     out, err = p.communicate()
#     # shutil.copy2('app.apk',r'D:/Pandiyan/Workspace/Practice/Python/Builds/lincoln/app.apk')
# else:
#     cmd = "ionic cordova platform add android@6.4.0"
#     p = subprocess.Popen(cmd, shell=True)
#     out, err = p.communicate()
#     cmd = "ionic cordova build android --prod --release"
#     p = subprocess.Popen(cmd, shell=True)
#     out, err = p.communicate()
#     # shutil.copy2(r'D:/Pandiyan/Workspace/Practice/Python/App/mobilecode/cryotos/platforms/android/build/outputs/apk/release/android-release-unsigned.apk',r'D:/Pandiyan/Workspace/Practice/Python/Builds/android-release-unsigned.apk')
#     # os.chdir(r"D:/Pandiyan/Workspace/Practice/Python/Builds")
#     # cmd = "jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.jks -storepass Minuscule-1 android-release-unsigned.apk cmms"
#     # p = subprocess.Popen(cmd, shell=True)
#     # out, err = p.communicate()
#     # if os.path.exists("app.apk"):
#     #     os.remove("app.apk")
#     # cmd = "zipalign -v 4 android-release-unsigned.apk app.apk"
#     # p = subprocess.Popen(cmd, shell=True)
#     # out, err = p.communicate()
#     # shutil.copy2('app.apk',r'D:/Pandiyan/Workspace/Practice/Python/Builds/lincoln/app.apk')

# filePath = config['paths']['apkpath']+'android-release-unsigned.apk'
# shutil.copy2(filePath ,config['paths']['buildpath']+'/android-release-unsigned.apk')
# os.chdir(config['paths']['buildpath'])
# cmd = "jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore my-release-key.jks -storepass Minuscule-1 android-release-unsigned.apk cmms"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()
# if os.path.exists("app.apk"):
#     os.remove("app.apk")
# cmd = "zipalign -v 4 android-release-unsigned.apk app.apk"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()
# if os.path.exists("app.apk"):
#     if choice == "1":
#         print("You choosed : Lincoln APK")
#         shutil.copy2('app.apk',apkpath+'/lincoln.apk')
#         build_file = config['paths']['buildpath']+'/'+apkpath+'/lincoln.apk'
#     elif choice == '2':
#         print("You choosed : Unicorn APK")
#         shutil.copy2('app.apk',rapkpath+'/unicorn.apk')
#         build_file = config['paths']['buildpath']+'/'+apkpath+'/unicorn.apk'
#     elif choice == '3':
#         print("You choosed : Demo APK")
#         shutil.copy2('app.apk',apkpath+'/demo.apk')
#         build_file = config['paths']['buildpath']+'/'+apkpath+'/demo.apk'
#     elif choice == '4':
#         print("You choosed : Test APK")
#         shutil.copy2('app.apk',apkpath+'/local.apk')
#         build_file = config['paths']['buildpath']+'/'+apkpath+'/local.apk'
#     else:
#         print("You choosed global apk")
#         build_file = "app.apk"

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
#         # print (req.json(), req.status_code)
#     except ConnectionError:
#         print('Connection error. Please try again.')
# else:
#     print("Apk not available for upload")
# cmd = "ionic serve"
# p = subprocess.Popen(cmd, shell=True)
# out, err = p.communicate()
# p = subprocess.run(["ionic", "info"], capture_output=True)
# CompletedProcess(args=['ionic', 'info'], returncode=0)
# p.wait()
# print(p)
# shutil.copy2('D:/Pandiyan/Workspace/Automation/mobilecode/cryotos/package.json','sample.json')
# print("Hello Python")
# f = open("sample.txt","a")
# f.write("Queen")
# v = open("sample.txt","r+")
# print(v.read())
# choice = input("Enter your input: ")
# print("Received input is : ", choice)