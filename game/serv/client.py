import socket, json, threading
import time

class Client:

    def __init__(self, ip="localhost", port=5000):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.client = None
        self.connected = None
        self.err_message = ""

    def return_ip(self,ip_port):
        try :
            ip, port = ip_port.split(":")
            return ip, int(port)

        except ValueError:
            return None, None

    def connexion_serveur(self,ip_port = "localhost:5000"):
        # Création de la socket

        ip,port = self.return_ip(ip_port)

        if ip is None or port is None:
            self.connected = False
            self.err_message = "Utilisez le format ip:port."
            return

        dic = {}
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for i in range(3):
            try : 
                print(f"Trying to connect with : {ip}, {port}")
                self.client.connect((ip, port))
                self.connected = True
            
                print("Connecté au serveur")

                # Démarrer un thread pour recevoir les messages du serveur
                threading.Thread(target=self.reception_server).start()

                # Envoi d'un message
                while True:
                    dic["pseudo"] = input("Ton pseudo: ")
                    dic["force"] = int(input("ta force"))

                    self.client.send(json.dumps(dic).encode())
                    print("Message envoyé")

                # Fermer la connexion
                self.client.close()

            except :
                time.sleep(0.5) #Attend o,5 sec que le serv soit pret ?

        print("IP ou port incorrect.")
        self.err_message = "IP ou port incorrect."
        self.connected = False

    def reception_server(self):
        try : 
            while True:

                data = json.loads(self.client.recv(1024).decode())  #reception des datas
                
                if not data:
                    break
                # Réception de la réponse
                print(f"Réponse du serveur : {data["pseudo"]} ta force : {data["force"]}")
        except :
            print("server Stoppé")