__author__ = "Alex Li"

import paramiko
transport = paramiko.Transport(('192.168.120.191', 22))
transport.connect(username='zhn', password='1125')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('ssh.py', '/home/zhn')
# 将remove_path 下载到本地 local_path
#sftp.get('/home/klaus/examples.desktop', 'examples.desktop')

transport.close()