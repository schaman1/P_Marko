import socket, threading, os, json

class Server :
    def __init__(self, host='0.0.0.0', port=5000):
        self.lClient = {}
        self.host = host
        self.port = port
        self.server = None
        self.is_running = False

    def handle_client(self,client_socket):
        while True:
            try : 
                data = json.loads(client_socket.client.recv(1024).decode())
            except : 
                client_socket.close()
                break
                
            print(f"Reçu : {data}")
            self.in_menu()
            

        client_socket.close()

    def in_menu(self,data):

        if data["id"] == "new client connection":
            pass

        # Envoyer le message à tous les clients encore connectés
        for client in self.lClient:
            try:
                pass
                #client.send(f"{data}".encode())
            except OSError:
                    # Si le socket n'est plus valide, on l'enlève de la liste
                if self.lClient[client]["Host"]==True:
                    print("Le host a quitté, tous les clients vont être déconnectés.")  
                    self.stop_server() 

                else : 
                    self.lClient[client].close()
                    #self.lClient.remove
        pass

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

    def start_server(self,port,client):

        host = socket.gethostbyname(socket.gethostname())  #192.10.27.1

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port)) #Lance le serveur 

        print(f"host : {host}, port : {port}")

        self.server.listen()

        self.is_running = True

        threading.Thread(target=self.loop_server).start()
        client.connexion_serveur(f"{client.ip}:{5000}")

    def loop_server(self) :

        self.server.settimeout(1) #En gros permet de revenir dans le while et evite que server.accept bloque indefiniment
        while self.is_running:

            try:
                #print("accept")
                client_socket, addr = self.server.accept()
            except socket.timeout:
                continue  # pas de client, on continue la boucle
            except OSError:
                break  # le socket a été fermé, on sort de la boucle

            if self.lClient == {}:
                self.lClient[client_socket] = {"Host":True}
            else : 
                self.lClient[client_socket] = {"Host":False}

            print(f"Connexion de {addr}")

            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
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