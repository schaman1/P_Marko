import socket, json, threading
import time

class Client:

    def __init__(self, font,screen,ip="localhost", port=5000):
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.client = None
        self.connected = None

        self.pseudo = "Coming soon"
        self.err_message = ""

        self.lClient_id = []
        self.dic = {}

        self.font = font
        self.screen = screen

    def return_ip(self,ip_port):
        try :
            ip, port = ip_port.split(":")
            return ip, int(port)

        except ValueError:
            return None, None
        
    def connexion_serveur(self, ip_port="localhost:5000"):
        print("connexion_serv")
        ip, port = self.return_ip(ip_port)

        if ip is None or port is None:

            self.return_err("Utilisez le format ip:port")
            return

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        essais = 0
        max_essais = 3
        while essais < max_essais and self.connected is not True:

            try:
                print(f"Trying to connect with : {ip}, {port}")
                self.client.connect((ip, port)) #Si connexion marche pas alors renvoie erreur = except
                self.connection_succes()

            except:
                essais += 1
                print(f"Échec {essais}/{max_essais} — nouvelle tentative dans 0.5s…")
                time.sleep(0.2)
                print(self.connected)

        if self.connected is not True:
            self.return_err("Ip ou port incorrect")

    def return_err(self,mess):
        print(mess)
        self.err_message = mess
        self.connected = False

    def connection_succes(self):
        print("Connecté au serveur")
        threading.Thread(target=self.loop_reception_server, daemon=True).start()
        
        self.connected = True
        
        self.client.send(json.dumps({"id":"new client connection"}).encode())
        

        #Start loop for a data for data and client

        #self.loop_client() #Test

    #def loop_client(self):

        # Envoi d'un message
        #while True:
            #pass
            #self.dic["pseudo"] = input("Ton pseudo: ")
            #self.dic["force"] = int(input("ta force"))

            #self.client.send(json.dumps(self.dic).encode())
            #print("Message envoyé")

        # Fermer la connexion
        #print("Deco")
        #self.client.close()

    def loop_reception_server(self):
        try : 
            buffer = ""
            while True:

                #Buffer car si plusieurs mess arrivent en même temps bah plb
                buffer += self.client.recv(1024).decode()

                if not buffer:
                    break

                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    data = json.loads(line)
                    print(f"Data recu : {data}")
                    self.traiter_data(data)

        except Exception as e:
            print(f"server Stoppé a cause de : {e}")

    def traiter_data(self,data):
                
        # Réception de la réponse
        if data["id"] == "new player" :
            print(f"New connection : {data["new connection"]}")
            text = data["new connection"]

            if data["sender"]:
                self.pseudo = text
                text = f"{text} (vous)"
            self.lClient_id.append(text)

    def display_clients_name(self):
        for idx,client in enumerate(self.lClient_id):
            self.draw_text(self.screen,self.font,client,idx)

    def draw_text(self,screen,font,text,idx):
            text = font.render(text, True, (255, 255, 255))
            screen.blit(text, (50, 50 + idx * 30))