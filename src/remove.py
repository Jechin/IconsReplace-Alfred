#!/usr/bin/env python3

#!/usr/bin/env python3

import os, sys, json
import subprocess

def getapps(search_file):
	apps = []
	paths = []
	while len(search_file) > 0:
		file = search_file[-1]
		search_file.pop()
		for dirpath, dirnames, files in os.walk(file):
			for appname in dirnames:
				if appname.endswith('.app'):
					apps.append(appname[0: -4])
					paths.append(dirpath + appname)
				else:
					search_file.append(dirpath + appname + '/')
			break
	return apps, paths

search_file = os.getenv("app_filepath").split(',')
apps, paths = getapps(search_file)
icons_file = os.getenv('icons_filepath')
success = 0

#pipe = subprocess.Popen(["brew", "install", "fileicon"], shell=True, executable="/bin/zsh", stdout=subprocess.PIPE).stdout


if len(sys.argv) > 1 and sys.argv[1] == "all":
	icons_file = os.getenv('icons_filepath')
	for dirpath, dirname, files in os.walk(icons_file):
		break;
	for file in files:
		if file != ".DS_Store" and (file.endswith(".png") or file.endswith(".PNG") or file.endswith(".icns") or file.endswith(".ICNS")):
			icon = file[0: file.rfind('.')]
			path_index = [i for i, x in enumerate(apps) if icon == x]
			if len(path_index) != 0:
				for index in path_index:
					command = './fileicon rm ' + paths[index].replace(' ', '\ ')
					return_info = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,executable="/bin/zsh", stderr=subprocess.STDOUT)
					next_line = return_info.stdout.readline()
					return_line = next_line.decode("utf-8", "ignore")
					if return_line == '' and return_info.poll() != None:
						continue
					elif return_line.find("permission") != -1:
						print("sudo "+ os.getcwd() +command[2:])
					elif return_line.find("Custom") != -1:
						success += 1
						print(return_line, end="")
	print(success, end="")
	
else:
	file = ""
	for i in range(1, len(sys.argv)):
		file += sys.argv[i]
		if i != len(sys.argv) - 1:
			file += " "
			
	icon = file[0: file.rfind('.')]
	path_index = [i for i, x in enumerate(apps) if icon == x]
	if len(path_index) != 0:
		for index in path_index:
			command = ' ./fileicon rm ' + paths[index].replace(' ', '\ ') 			
			return_info = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,executable="/bin/zsh", stderr=subprocess.STDOUT)
			
			
			next_line = return_info.stdout.readline()
			return_line = next_line.decode("utf-8", "ignore")
			if return_line == '' and return_info.poll() != None:
				continue
			elif return_line.find("permission") != -1:
				print("sudo "+ os.getcwd() +command[2:])
			elif return_line.find("Custom") != -1:
				print(return_line, end="")
				
	else:
		print("ERROR: Can not find " + icon + ".app!", end="")
		
		