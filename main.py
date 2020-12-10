# This is the template code for the CNA337 Final Project
# Ahmed Alkhafaji ahmed_alkhafajy@yahoo.com
# December, 2020
# I have got help from Francisco, Many thanks 4 him.
from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server.py Automator v0.1 by Ahmed")
# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server.py object

    EC2server2 = '54.219.184.63' #EC2 address
    key_location= "C:\\Users\\ahmed\\.ssh\\id_rsa"
    root = "ubuntu"

    update= 'sudo apt update && sudo apt upgrade -y'  ## https://www.codegrepper.com/code-examples/objectivec/sudo+apt-get+update+%26%26+sudo+apt-get+upgrade
    EC2server2 = Server(EC2server2, key_location, root, update)

    # TODO - Call Ping method and print the results
    #http://docs.paramiko.org/en/stable/api/client.html
    print("\nUpdating server using ssh from paramiko")
    ssh_result = EC2server2.upgrade()

    print(EC2server2.ping())

    print('Done.')

