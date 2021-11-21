'''
	Creator : Kuaï
	Create : 16/11/2021
	Last update : 20/11/2021
	Github : Kuai-sama

	This program allows you to deploy qt applications automatically
	Start the program in admin mode
	Pay attention to the integrated cmd of your IDE if it is integrated in it (like VSC)
'''
# coding: utf-8
import os
import subprocess
from pathlib import Path

def reverse(path):
	if len(path) <=1: # if the path length is less than or equal to 1
		return ""
	else :
		return path[::-1] # Start at the end, count down to the beginning, stepping backwards one step at a time

def is_admin():
	subprocess.call("isCmdToAdmin.bat", shell=True) # Open the .bat, allows to know if the cmd is in admin mode

	file = open(os.getcwd() + os.path.sep + "cmdAdminOrNot.txt", "r") # Open the txt file in read mode
	allLines = file.readlines() # Read the lines of the file (return a list)
	ligne = allLines[0].rstrip("\n") # Remove the '\n'
	file.close

	if ligne == 'False' or ligne == 'False ': # if the CMD is executed in non-admin mode
		print("Please run your CMD in admin mode")

os.chdir(Path(__file__).parent) # Change the path directory of the program (.py) 
print("Current working directory :" + os.getcwd()) # Show the current directory
pathOfTxt = os.getcwd()

is_admin() # Check if the cmd is launched in admin mode

print("Please enter the path to your .exe")
originalPath = os.getcwd()

path = os.path.join(input()) # Get the path of the application to deploy

if not (path.endswith(".exe")):
	print("Please put the path of your .exe (you must have the .exe in the path")
	quit()

pathWithoutExe = path
if ".exe" in pathWithoutExe: # Remove / and the filename of the exe
	pathWithoutExe = reverse(pathWithoutExe)
	pathWithoutExe = pathWithoutExe[pathWithoutExe.find(os.path.sep)+1:] # Search and delete everything before '/' ('/' is included)

	pathWithoutExe = reverse(pathWithoutExe) # Path goes back to normal
	print("Path of your executable :{0}".format(pathWithoutExe))
	
listeExtension = os.listdir(pathWithoutExe + ".") # List all of extension in folder

for fichier in listeExtension: # Clear the folder and leave only the .exe
	if fichier.endswith("exe"):
		listeExtension = listeExtension[:listeExtension.index(fichier)] # Remove the .exe in the list
	else:
		os.remove(os.path.join(pathWithoutExe, fichier)) # Delete the file
		print(fichier + " has been deleted")

os.chdir(os.path.join(r"C:\qt")) # Change directory
print("Current working directory: {0}".format(os.getcwd())) # Print the current working directory

fileName = "qtenv2.bat" # The name of file that we want to open
for root, dirs, files in os.walk(os.getcwd()): # Search the filename into the qt directory
	if fileName in files:
		pathBat = os.path.join(root, fileName)

p = subprocess.Popen(pathBat, shell=True, stdout = subprocess.PIPE) # Checked if that the file can be opened
stdout, stderr = p.communicate()

if(p.returncode == 1): # is 0 if success
	print(p.returncode)
	quit()
else:
	file = open(os.path.join(pathOfTxt + "/Path_of_exe_to_deploy.txt"), 'w')
	file.write(os.path.join(path))
	file.close()

	file = open(os.path.join(pathOfTxt + "/Path_of_Qt_Dlls.txt"), 'w')
	file.write(os.path.join(pathBat.rstrip(fileName)))
	file.close()
	print (pathOfTxt + os.path.sep + "QTDeploying.bat")
	subprocess.call([pathOfTxt + os.path.sep + "QTDeploying.bat"], shell=True) # Run the bat (Allows you to deploy the app)