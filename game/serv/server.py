import socket, threading, os

class Server :
    def __init__(self, host='localhost', port=5000):
        self.lClient = {}
        self.host = host
        self.port = port
        self.server = None
        self.is_running = False

    def handle_client(self,client_socket, id):
        while True:
            try : 
                data = client_socket.recv(1024).decode()
            except : 
                client_socket.close()
                
            if not data:
                break
            print(f"Reçu : {data}")

            # Envoyer le message à tous les clients encore connectés
            for client in self.lClient:
                try:
                    client.send(f"{data}".encode())
                except OSError:
                        # Si le socket n'est plus valide, on l'enlève de la liste
                    if self.lClient[client]["Host"]==True:
                        print("Le host a quitté, tous les clients vont être déconnectés.")  
                        self.stop_server()   

        client_socket.close()

    def stop_server(self):
        """Arrête le serveur et déconnecte tous les clients."""
        for client in self.lClient:
            client.close()
        self.lClient.clear()

        self.is_running = False
        if self.server:
            self.server.close()
            self.server = None
        print("Serveur arrêté.")

    def start_server(self,host,port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port)) #Lance le serveur 
        self.server.listen()
        print(f"Serveur en écoute sur le port {port}...")

        while self.is_running:

            client_socket, addr = self.server.accept()
            if self.lClient == []:
                self.lClient[client_socket] = {"Host":True}
            else : 
                self.lClient[client_socket] = {"Host":False}

            print(f"Connexion de {addr}")

            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,id))
            client_handler.start()

# print("Quel mode de serveur voulez vous lancer ?\n1. Serveur Local\n2. Serveur sur le réseau local\n3. Serveur sur internet (ngrok)")
# rep=input("-> ")
# if rep=="3":
#     port=5000
#     ip="localhost"
#     os.system("start ngrok tcp 5000")
# elif rep=="2":
#     ip="0.0.0.0"
#     port=int(input("Quel port : "))
# else:
#     ip="localhost"
#     port=int(input("Quel port : "))
# clear()
# start_server(ip,port)