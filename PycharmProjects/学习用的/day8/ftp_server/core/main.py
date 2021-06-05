import socketserver
import json,os
class MyTCPHandler(socketserver.BaseRequestHandler):


    def put(self,*args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        filesize = cmd_dic["size"]
        if os.path.isfile(filename):
            f = open(filename + ".new","wb")
        else:
            f = open(filename , "wb")

        self.request.send(b"200 ok")
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded..." % filename)

    def get(self , *args):
        '''接收客户端文件'''
        cmd_dic = args[0]
        filename = cmd_dic["filename"]
        if os.path.isfile( filename ):
            file_size = os.stat(filename ).st_size
            print( file_size )
            self.request.send( str( file_size ).encode() )

            f = open( filename , "rb" )
            for line in f:
                self.request.send( line )
            else:
                print( "file download success..." )
                f.close()
        else:
            self.request.send( 'file not exist' )

    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):
                    func = getattr(self,action)
                    func(cmd_dic)

            except ConnectionResetError as e:
                print("err",e)
                break

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()