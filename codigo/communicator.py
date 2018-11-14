# communicator.py - Comunicador bluetooth que vai comunicar com o aplicativo de controle

import bluetooth
import threading

class Communicator():
    valid_messages = set('mode:sleep', 'mode:jaguar', 'mode:manual', 'mode:patrol', 'mode:home', 'mode:shutdown',
                                       'manual:forward', 'manual:backward', 'manual:left', 'manual:right', 'manual:fan', 'manual:cover')
    last_command = None
    def __init__ (self, port):
        self.port = port
        thread = threading.Thread(target=self.receiveCommand, name="Bluetooth communication thread")
        thread.start()
    def receiveCommand(self):
        while (True):
            server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            server_socket.bind(("",self.port)) # Vulneravel a ataques -Nicolas
            server_socket.listen(1)
            client_socket, address = server_socket.accept() #sera? talvez nao caia a conexao nunca, dai fecha qd fechar o programa -Alefe
            data = client_socket.recv(1024) # Porque 1024 bytes? -Nicolas
            client_socket.close()
            server_socket.close() # Porque fechar o socket? Depois nao teria que abrir de volta pra ler de novo? -Nicolas
            self.last_command = self.decodeMessage(data)

    def decodeMessage(self, msg):
        if msg in self.valid_messages:
            return msg
        else:
            return None
