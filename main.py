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
from banner import banner

try:
	from colorama import Fore, Style
except ModuleNotFoundError:
	print(banner())
	print("Install required modules. Check README.md for instructions\n")

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--update', help='Updates the system to latest release.')
parser.add_argument('-i', '--install', help='Install docker image of nahamsec lab')
parser.add_argument('-j', '--juice', help='Install juiceshop web lab')
args = parser.parse_args()
updates = args.update


def clear():
	"""Clean terminal screen"""
	os.system('clear')

def python_check():
	"""Check for python version"""
	if sys.version_info.major < (3):
		print(Fore.RED + "Your need a higher python version to use the script!!\n")
		clear()
		sys.exit(1)

def update():
	"""Debian apt update"""
	clear()
	print(Fore.LIGHTMAGENTA_EX + banner() + Fore.RESET)
	print(Fore.GREEN + "Performing repo update. Confirm with password when asked." + Fore.RESET)
	time.sleep(2)
	os.system('sudo apt update -y')
	return 0

def package_check():
	program = ['node', 'git', 'docker.io', 'virtualbox', 'docker', 'npm']
	not_installed = []
	for i in program:
		installed = which(i)
		
		if installed == None:
			not_installed.append(i)
	print(Fore.RED + "This programs have not been detected in your system!!\n" + Fore.RESET)
	print(Fore.CYAN + f"{not_installed}")

	return not_installed

def configure_all(packages):
	try:
		for package in packages:
			clear()
			print(Fore.CYAN + "Installing " + package + "\n" + Fore.RESET)
			os.system('sudo apt install ' + package + ' -y')
	except SystemExit:
		print(Fore.RED + "Failure, try again" + Fore.RESET)
		sys.exit(1)

def get_juice():
	clear()
	print(Fore.GREEN + "Getting tar ball from github latest releases\n" + Fore.RESET)
	sys.stdout.write("Total Size: 140MB...")
	os.system("wget https://github.com/juice-shop/juice-shop/releases/download/v14.3.0/juice-shop-14.3.0_node18_linux_x64.tgz")
	clear()
	print(Fore.CYAN + "[+] Download success.")
	time.sleep(2)
	print(Fore.GREEN + "[-] Preparing to extract archive...")
	os.system('tar -xvf juice-shop-14.3.0_node18_linux_x64.tgz')
	print(Fore.GREEN + "[+] Done")

def get_lab2():
	clear()
	os.system('git clone http://github.com/nahamsec/nahamsec.training')
	clear()
	os.system('cd nahamsec && sudo docker build -t nahamsec .')

def main():
	
	if args.install:
		package_check()
		get_lab2()
	elif args.update:
		update()
	elif args.juice:
		get_juice()
	else:
		python_check()
		configure_all(package_check())
		update()
		get_juice()
		get_lab2()

if __name__ == '__main__':
	main()