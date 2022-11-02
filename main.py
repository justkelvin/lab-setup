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
	os.system('sudo apt update')
	sys.exit(0)

def package_check():
	program = ['node', 'git', 'docker', 'virtualbox']
	not_installed = []
	for i in program:
		installed = which(i)
		
		if installed == None:
			not_installed.append(i)
	print(not_installed)
	sys.stdout.write("This programs have not been detected in your system!! Installing\n")
			# print(f"Installing {i}")
			# os.system('sudo apt install {i}')


if __name__ == '__main__':
	python_check()
	# update()
	package_check()

