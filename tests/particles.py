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

class water:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.density = (1,1)
        self.move = [False,False] #(left,right)
        self.color = (0,0,255)

    def update_position(self,grid,cells_h,cells_w):

        to_add = set()

        if self.y - 1 >= 0: #A opti
            to_add.add((self.x, self.y - 1))

        if self.y + 1 < cells_h and grid[self.y + 1][self.x] is None:

            # on ajoute les voisins à surveiller
            if self.y - 1 >= 0:
                to_add.add((self.x, self.y - 1))

            if self.x + 1 < cells_w:
                to_add.add((self.x + 1, self.y))

            if self.x - 1 >= 0:
                to_add.add((self.x - 1, self.y))

            self.y += 1
            to_add.add((self.x, self.y))

            return (True,( self.x,self.y),to_add) #if moved

        else:#elif random.random() < 1:  # essaie de moins unifier le sable:

            if False :
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
                
            # choisir une direction
            else :
                #print("move right")
                if self.move[0] is False and self.move[1] is False:
                    choice = random.choice([-1,1])
                    if choice == -1:
                        self.move = [True,False]
                    else:
                        self.move = [False,True]

                if self.move[0] : 
                    if self.x - 1 >= 0 and grid[self.y][self.x - 1] is None:
                        #print("move left")
                        if self.x + 1 < cells_w:
                            to_add.add((self.x + 1, self.y))
                        to_add.add((self.x , self.y-1))
                        self.x -= 1
                        to_add.add((self.x, self.y))
                        return (True,(self.x,self.y),to_add) #if moved
                    else :
                        self.move[0] = False
                        #if self.move[1] is None :
                        self.move[1] = True
                        to_add.add((self.x, self.y))
                        return (True,(None,None),to_add)
                        #else :
                            #return (False,(None,None),None) #if not moved
                
                elif self.move[1] :
                    if self.x + 1 < cells_w and grid[self.y][self.x + 1] is None:
                        if self.x - 1 >= 0:
                            to_add.add((self.x - 1, self.y))
                        to_add.add((self.x , self.y-1))
                        self.x += 1
                        to_add.add((self.x, self.y))
                        return (True,(self.x,self.y),to_add) #if moved
                    else :
                        self.move[1] = False
                        #if self.move[0] is None :
                        self.move[0] = True
                        to_add.add((self.x, self.y))
                        return (True,(None,None),to_add)
                        #else :
                         #   return (False,(None,None),None) #if not moved
    
        return (False,(None,None),None) #if not moved