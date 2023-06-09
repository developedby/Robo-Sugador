# communicator.py - Comunicador bluetooth que vai comunicar com o aplicativo de controle

import bluetooth
import threading
import os

class Communicator():
    uuid = "00001101-0000-1000-8000-00805f9b34fb"
    valid_messages = set(('mode:sleep', 'mode:jaguar', 'mode:manual', 'mode:patrol', 'mode:home', 'mode:shutdown',
                                       'manual:forward', 'manual:backward', 'manual:left', 'manual:right', 'manual:fan', 'manual:cover', 'manual:stop'))
    last_command = None
    connected = False

    def __init__ (self):
        self.thread = threading.Thread(target=self.bluetoothStart, name="Bluetooth communication thread")
        try:
            self.thread.start()
        except:
            os.system('systemctl reboot')
        
    def bluetoothStart(self):
        self.connect()
        self.receiveCommand()

    def connect(self):
        print('Tentando conexão')
        self.server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.server_socket.bind(("",bluetooth.PORT_ANY)) # Vulneravel a ataques -Nicolas
        self.server_socket.listen(1)
        self.port = self.server_socket.getsockname()[1]
        bluetooth.advertise_service( self.server_socket, "Robo Sugador",
                   service_id = self.uuid,
                   service_classes = [ self.uuid, bluetooth.SERIAL_PORT_CLASS ],
                   profiles = [ bluetooth.SERIAL_PORT_PROFILE ],
                    )
        self.client_socket, self.client_info = self.server_socket.accept()
        print('Conectado')
        self.connected = True

    def receiveCommand(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                self.last_command = self.decodeMessage(data)
                print('Comando recebido:', self.last_command)
            except IOError:
                print("erro de envio")
                self.connected = False
                self.connect()

    def decodeMessage(self, msg):
        msg = msg.decode('utf-8')
        if msg not in self.valid_messages:
            return None
        return msg
