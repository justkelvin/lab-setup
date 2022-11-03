#!/usr/bin/env python3

# Title: Lab Environment Setup
# Description: Sets up updates, installs essential apps, set up node and juiceshop
# Author: Kelvin <redacted@gmail.com>
# Date: 2022-11-02
# Version: 1.0.0

# Imports
import os
import sys
from shutil import which
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--update', help='Updates the system to latest release.')
parser.add_argument('-i', '--install', help='Install docker image of nahamsec lab')


args = parser.parse_args()
updates = args.update

def python_check():
	"""Check for python version"""
	if sys.version_info.major < (3):
		sys.stderr.write("Your need a higher python version to use the script!!\n")
		sys.exit(1)

def update():
	"""Debian apt update"""
	sys.stdout.write("Performing repo update. Confirm with password when asked.")
	time.sleep(3)
	# os.system('sudo apt update')
	return 0

def package_check():
	program = ['node', 'git', 'docker.io', 'virtualbox', 'docker', 'npm']
	not_installed = []
	for i in program:
		installed = which(i)
		
		if installed == None:
			not_installed.append(i)
	print(not_installed)
	sys.stdout.write("This programs have not been detected in your system!!\n")

	return not_installed

def configure_all(packages):
	try:
		for package in packages:
			sys.stdout.write("Installing " + package + "\n")
			os.system('sudo apt install ' + package)
	except SystemExit:
		sys.stderr.write("Failed, try again")
		sys.exit(1)

def get_juice():
	os.system("wget ")

def get_lab2():
	os.system('git clone http://github.com/nahamsec/nahamsec.training')
	os.system('clear')
	os.system('cd nahamsec && sudo docker build -t nahamsec .')


def main():
	
	if args.install:
		package_check()
		get_lab2()
	elif args.update:
		update()
	else:
		configure_all(package_check())
		python_check()
		update()



if __name__ == '__main__':
	main()