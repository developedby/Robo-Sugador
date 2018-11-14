# bluetooth.py - Bluetooth que vai comunicar com o aplicativo de controle

import bluetooth

class Bluetooth():
    def __init__ ():
        self.server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1 # Tem que definir a porta certa nao? -Nicolas
        server_socket.bind(("",port)) # Vulneravel a ataques -Nicolas
        server_socket.listen(1)

    def read():
        client_socket, address = server_socket.accept() #sera? talvez nao caia a conexao nunca, dai fecha qd fechar o programa -Alefe
        data = client_socket.recv(1024) # Porque 1024 bytes? -Nicolas
        client_socket.close()
        server_socket.close() # Porque fechar o socket? Depois nao teria que abrir de volta pra ler de novo? -Nicolas
        return data
