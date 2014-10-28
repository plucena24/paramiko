'''
Example usage:

router1 = dict(host='1.1.1.1', username='user', password='pass')

rtr_obj = sshHelper(**router1)

rtr_obj.connect()

woo hoo
'''

import paramiko

class sshHelper(object):
    def __init__(self, host, username, password, port=22):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.host, username=self.username, password=self.password)
            self.chan = self.ssh.invoke_shell()
        except paramiko.AuthenticationException as e:
            print 'wrong username/password!', e
            self.chan.send('\n')
            self.chan.recv(65535)
            self.chan.send('\n')
