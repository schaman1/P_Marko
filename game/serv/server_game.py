from serv.in_game.read_map import Read_map
import var

class Server_game :
    def __init__(self):
        self.canva_size = var.serv_size
        self.map = Read_map("assets/bgWater.png",var.cell_size,self.canva_size)
        self.canva_map = self.map.canva

    def return_chg(self):
        return self.map.return_map()

    def init_canva(self):
        l = []
        for e in self.map.grid:
            for el in e :
                if el != None :
                    l.append((el.x,el.y,el.color))
        return l