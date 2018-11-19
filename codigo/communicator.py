# communicator.py - Comunicador bluetooth que vai comunicar com o aplicativo de controle

import bluetooth
import threading

class Communicator():
    uuid = "777777-7777-7777-7777-777777777770"
    valid_messages = set(('mode:sleep', 'mode:jaguar', 'mode:manual', 'mode:patrol', 'mode:home', 'mode:shutdown',
                                       'manual:forward', 'manual:backward', 'manual:left', 'manual:right', 'manual:fan', 'manual:cover', 'manual:stop'))
    last_command = None
    connected = False

    def __init__ (self):
        self.connect()
        thread = threading.Thread(target=self.receiveCommand, name="Bluetooth communication thread")
        thread.start()

    def connect(self):
        self.server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        self.server_socket.bind(("",PORT_ANY)) # Vulneravel a ataques -Nicolas
        self.server_socket.listen(1)
        self.port = self.server_sock.getsockname()[1]
        bluetooth.advertise_service( self.server_socket, "Robo Sugador",
                   service_id = self.uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
#                   protocols = [ OBEX_UUID ]
                    )
        self.client_sock, self.client_info = server_sock.accept()
        self.connect = True

    def receiveCommand(self):
        while True:
            try:
                while True:
                    data = client_sock.recv(1024)
                    if len(data) == 0:
                        break
            except IOError:
                self.connected = False
                self.connect()
            self.last_command = self.decodeMessage(data)

    def decodeMessage(self, msg):
        if msg not in self.valid_messages:
            return None
        return msg
