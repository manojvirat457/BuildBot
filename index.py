import os
import subprocess

projectType = 'React'

# run_commands

def run_command(command, path):
    return subprocess.call(command, shell=True, cwd=path)

if(projectType == 'Angular'):
    if(run_command('npm install', 'G:\Maheshwaran\SheetAutomation') == 0):
        print("install Succeeded")
    else:
        print("install Failed")
        
    if(run_command('ng build', 'G:\Maheshwaran\SheetAutomation') == 0):
        print("Build Succeeded")
    else:
        print("Build Failed")
elif(projectType == 'React'):
    if(run_command('npm install', 'G:\React\demo') == 0):
        print("install Succeeded")
    else:
        print("install Failed")
        
    if(run_command('npm run build', 'G:\React\demo') == 0):
        print("Build Succeeded")
    else:
        print("Build Failed")
    