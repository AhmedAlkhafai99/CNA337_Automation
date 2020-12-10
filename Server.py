# I have got help from Francisco, Many thanks 4 him.
# Zak helped me to troubleshoot the error!Thanks!

import os
import paramiko
## This website showing how to use paramiko:
# https://mainlydata.kubadev.com/python/using-paramiko-to-control-an-ec2-instance/
# https://stackoverflow.com/questions/2224066/how-to-convert-ssh-keypairs-generated-using-puttygen-windows-into-key-pairs-us
class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip, key_file, username, upgrade_command):
        # TODO -

        self.username = username
        self.command = upgrade_command
        self.key_file = key_file
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        result = os.system("ping -n 4 %s" % self.server_ip)
        return result

    def upgrade(self):  # Run Update and Upgrade commands in the package manager
        # TODO - Use os module to ping the server

        # The code below will create a ssh client with paramiko and host policy
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Make the connection to the server
        ##https://www.programcreek.com/python/example/6085/paramiko.AutoAddPolicy
        ssh.connect(hostname=self.server_ip, username=self.username, key_filename=self.key_file)

        # execute the command
        stdin, stdout, stderr = ssh.exec_command(self.command)

        # Return the result from both stdout and error
        result = stdout.readlines() + stderr.readlines()

        # Disconnect from server
        ssh.close()

        return result
