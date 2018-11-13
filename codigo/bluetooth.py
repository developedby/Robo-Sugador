import bluetooth

class Bluetooth():
    def __init__ ():
        self.server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)

    def read():
        client_sock,address = server_sock.accept()#sera? talvez nao caia a conexao nunca, dai fecha qd fechar o programa
        data = client_sock.recv(1024)
        client_sock.close()
        server_sock.close()
        return data
