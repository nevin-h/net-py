#!/usr/bin/env python3
import sys
import getpass
from time import sleep
import paramiko


def main():

    check_params()
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    targets = get_ips()
    commands = get_commands()

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for target in targets:
        print(f"Connecting to {target}...")
        client.connect(target, username=username, password=password)
        print("Connected!")
        shell = client.invoke_shell()
        sleep(2)
        for command in commands:
            shell.send(command)
            sleep(2)
            output = shell.recv(4096).decode("utf-8")
            print(output)
        shell.close()
        client.close()

def check_params():

    # Check for parameter length and print the hello message
    # Or whine about too many parameters
    match len(sys.argv):

        case 1 | 2 | 3:
            w = 75
            print("***Welcome to the net automation script!***.".center(w))
            print("Usage:  python net.py {ip-list.txt} {command-list.txt}".center(w))
            print("You can also create a list of IPs and commands".center(w))
            print("in the script however, these will not be saved :(\n".center(w))
            print("Now, let's get some data!")

        case _:
            print("Too many parameters.\n")
            print("Usage: python net.py {ip-list.txt} {command-list.txt}")
            sys.exit(1)

def get_ips():

    # If there are 2 or 3 parameters, the user has passed
    # an ip list (2) or and ip list and a command list (3)
    if len(sys.argv) == 2 | 3:
        with open(sys.argv[1], 'r') as file:
            ips = [ip.strip('\n') for ip in file.readlines()]
            # Testing list
#             for ip in ips:
#                print(ip)
        return ips
    # If there are no additional parameters, we'll have to
    # build the list in the script itself.
    else:
        ips = []
        print("Which targets are we connecting to?")
        print("Type 'done' to stop")
        while True:
            ip = input("ip: ")
            if ip == 'done':
                break
            ips.append(ip)
        return ips

def get_commands():

    # If there are 3 parameters, the third should be the command-list file.
    if len(sys.argv) == 3:
        with open(sys.argv[2], 'r') as file:
            commands = file.readlines()
        return commands
    # Or we can build the list on the fly if they didn't provide a file.
    else:
        commands = []
        print("What commands would you like to run?")
        print("Type 'done' to stop")
        while True:
            cmd = input("cmd: ")
            if cmd == 'done':
                break
            commands.append(cmd)
        return commands

# Hardcoded commands
#commands = [
#    'pwd',
#    'ls',
#    'uname -a',
#]

main()
