import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()



    def cmd_put(self,*args):
        cmd_split =  args[0].split()
        print(cmd_split)
        if len(cmd_split) >1:
            filename = cmd_split[1]
            msg_dic = {
                    "action": "put",
                    "filename":filename,
                    "size": filesize,
                    "overridden":True
                }
            self.client.send( json.dumps(msg_dic).encode("utf-8")  )
            print("send",json.dumps(msg_dic).encode("utf-8") )
                #防止粘包，等服务器确认
                server_response = self.client.recv(1024)
                f = open(filename,"rb")
                for line in f:
                    self.client.send(line)
                else:
                    print("file upload success...")
                    f.close()

            else:
                print(filename,"is not exist")