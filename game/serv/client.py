import socket, json, threading

class Client:

    def __init__(self, ip="localhost", port=5000):
        self.client = None

    def connexion_serveur(self,ip, port):
        # Création de la socket

        dic = {}
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client.connect((ip, port))
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
        client.close()

    def reception_server(self):
        while True:

            data = json.loads(self.client.recv(1024).decode())  #reception des datas
            
            if not data:
                break
            # Réception de la réponse
            print(f"Réponse du serveur : {data["pseudo"]} ta force : {data["force"]}")