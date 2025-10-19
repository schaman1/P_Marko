import random


class sand:
    def __init__(self,x,y,density = (1,1)):
        self.x = x
        self.y = y
        self.density = density
        self.color = (random.randint(150,200),random.randint(75,140),0)

    def update_position(self,grid,cells_h,cells_w):

        to_add = set()

        if self.y - 1 >= 0: #A opti
            to_add.add((self.x, self.y - 1))

        if self.y + 1 < cells_h and grid[self.y + 1][self.x] is None:

            # on ajoute les voisins à surveiller
            if self.y - 1 >= 0:
                to_add.add((self.x, self.y - 1))

            if self.x + self.density[0] < cells_w:
                to_add.add((self.x + self.density[0], self.y - 1))

            if self.x - self.density[0] >= 0:
                to_add.add((self.x - self.density[0], self.y - 1))

            to_add.add((self.x, self.y + 1))
            self.y += 1

            return (True,( self.x,self.y),to_add) #if moved

        else:#elif random.random() < 1:  # essaie de moins unifier le sable:

            for i in range(1,self.density[0]+1):

                if self.y + 1 < cells_h and self.x - i >= 0 and grid[self.y + 1][self.x - i] is None:
                    # on ajoute les voisins à surveiller
                    if self.y - 1 >= 0:
                        to_add.add((self.x, self.y - 1))


                    for j in range(1,self.density[0]+1):
                        if self.x + j < cells_w:
                            to_add.add((self.x + j, self.y - 1))
                        
                        to_add.add((self.x - i, self.y + 1))

                    self.x -= i
                    self.y += 1
                    
                    return (True,(self.x,self.y),to_add) #if moved

                elif self.y + 1 < cells_h and self.x + i < cells_w and grid[self.y + 1][self.x + i] is None:
                    # on ajoute les voisins à surveiller
                    if self.y - 1 >= 0:
                        to_add.add((self.x, self.y - 1))

                    for j in range(1,self.density[0]+1):
                        if self.x - j >= 0:
                            to_add.add((self.x - j, self.y - 1))
                        
                        to_add.add((self.x + j, self.y + 1))

                    self.x += i
                    self.y += 1

                    return (True,(self.x,self.y),to_add) #if moved
        
        return (False,(None,None),None) #if not moved
    
class wood:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = (0,0,0)