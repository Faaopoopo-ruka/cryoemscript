import paramiko,os,sys
base_dir=os.path.dirname(os.path.abspath(__file__))
os.chdir(base_dir)

print(os.getcwd())
transport = paramiko.Transport( ('192.168.120.191', 22) )
transport.connect( username='zhn' , password='1125' )
sftp = paramiko.SFTPClient.from_transport( transport )
sftp.put( 'sever.py', '/home/zhn' )
transport.close()

# D:\Pycharm\hadoop_spark\ssh_files\id_rsa      本地路径,（windows)
# /usr/local/id_rsa                             远端服务器路径，（Linux）
# 两边路径必须都写上文件名