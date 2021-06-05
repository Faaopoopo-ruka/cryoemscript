#Author：Alex.Zhang
import socket


def handle_request(client):
    buf = client.recv( 1024 )
    f=open('s1.html','rb')
    data=f.read()
    client.send( b"HTTP/1.1 200 OK\r\n\r\n" )
    client.send( data )


def main():
    sock = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
    sock.bind( ('www.baidu.com' , 8000) )
    sock.listen( 5 )

    while True:
        connection , address = sock.accept()
        handle_request( connection )
        connection.close()


if __name__ == '__main__':
    main()