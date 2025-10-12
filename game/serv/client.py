import socket, json, threading
import time

class Client:

    def __init__(self, ip="localhost", port=5000):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.client = None
        self.connected = None
        self.err_message = ""
        self.dic = {}

    def return_ip(self,ip_port):
        try :
            ip, port = ip_port.split(":")
            return ip, int(port)

        except ValueError:
            return None, None
        
    def connexion_serveur(self, ip_port="localhost:5000"):
        ip, port = self.return_ip(ip_port)

        if ip is None or port is None:

            self.return_err("Utilisez le format ip:port")
            return

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        essais = 0
        max_essais = 3
        while essais < max_essais and self.connected is not True:
            print(self.connected)
            try:
                print(f"Trying to connect with : {ip}, {port}")
                self.client.connect((ip, port)) #Si connexion marche pas alors renvoie erreur = except

                self.connection_succes()

            except:
                essais += 1
                print(f"Échec {essais}/{max_essais} — nouvelle tentative dans 0.5s…")
                time.sleep(0.5)

        if self.connected is not True:
            self.return_err("Ip ou port incorrect")

    def return_err(self,mess):
        print(mess)
        self.err_message = mess
        self.connected = False

    def connection_succes(self):
        self.connected = True
        
        self.client.send(json.dumps({"id":"new client connection",
                                    "client":self.client}).encode())
        
        print("Connecté au serveur")

        #Start loop for a data for data and client
        threading.Thread(target=self.loop_reception_server, daemon=True).start()
        self.loop_client()

    def loop_client(self):

        # Envoi d'un message
        while True:
            pass
            #self.dic["pseudo"] = input("Ton pseudo: ")
            #self.dic["force"] = int(input("ta force"))

            #self.client.send(json.dumps(self.dic).encode())
            #print("Message envoyé")

        # Fermer la connexion
        print("Deco")
        self.client.close()

    def loop_reception_server(self):
        try : 
            while True:

                data = json.loads(self.client.recv(1024).decode())  #reception des datas
                
                if not data:
                    break
                # Réception de la réponse
                print(f"Réponse du serveur : {data["pseudo"]} ta force : {data["force"]}")
        except :
            print("server Stoppé")