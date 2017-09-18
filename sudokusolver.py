"""
while (x != 9) and (y != 9)
if pos not mutable:
    add x
else:
    first, check line
    then check column
    then check chunk
    if valid:
        move forward
    else:
        add x
    if number more than 9:
        reset
        move back

if x pos > 9:
    add y
    x = 0
"""
map =  [ 

           [ [True, 2 ], [False, 0 ], [False, 0 ] ], 
           [ [False, 0 ], [True , 1 ], [False, 0 ] ], 
           [ [False, 0 ], [False, 0 ], [False, 0 ] ] 

        ] 


class Map(object): 

    def __init__(self, map): 
        self.map = map 
        self.chunk_standard = 3 

    def get_row(self, y): 
        return self.map[y] 

    def get_collum(self, x): 
        array = [] 
        for row in self.map: 
            array.append(row[x]) 
        return array 

    def get_chunk(self, x, y): 
        chunk_x = (x // self.chunk_standard) 
        chunk_y = (y // self.chunk_standard) 

        array = [] 
        for row in range(chunk_y, (chunk_y + self.chunk_standard)): 
            for data in range(chunk_x, (chunk_x + self.chunk_standard)): 
                array.append(self.map[row][data]) 
        return array 

class Game(object): 
    def __init__(self, map): 
        # 0 is x, 1 is y 
        self.cursor = [[0, 0], 1] 
        self.map = Map(map) 
        self.map_border = [9, 9] 
        self.is_running = True
    def algorithm(self):
        
        pos = self.map.map[self.cursor[0][1]][self.cursor[0][0]]

        if pos[0]: 
            self.cursor[0][0] += 1 
        else: 

            pos_valid = True
            if pos_valid:
                for data in self.map.get_row(self.cursor[0][1]): 
                    if data[1] == self.cursor[1]:  
                        pos_valid = False 
                        break 
            if pos_valid: 
                for data in self.map.get_collum(self.cursor[0][0]): 
                    if data[1] == self.cursor[1]: 
                        pos_valid = False 
                        break

            if pos_valid: 
                for data in self.map.get_chunk(self.cursor[0][0],self.cursor[0][1]): 
                    if data[1] == self.cursor[1]: 
                        pos_valid = False 
                        break
            return pos_valid
   
    def event_loop(self):
        
        valid = self.algorithm()
        if valid:
            self.map.map[self.cursor[0][1]][self.cursor[0][0]][1] = self.cursor[1]
            self.cursor[0][0] += 1 
            self.cursor[1] = 1
        else:
            #change cursor val 
            self.cursor[1] += 1 
            if self.cursor[1] > 9: 
                 self.cursor[1] = 1 
                 self.cursor[0][0] -= 1
         
        if self.cursor[0][0] < 0:
            self.cursor[0][0] = 0
            self.cursor[0][1] -= 1
        if self.cursor[0][0] > 2:
            self.cursor[0][0] = 0
            self.cursor[0][1] += 1

        if self.cursor[0][1] > 2:
            self.is_running = False

apple = Game(map)
while apple.is_running:
    apple.event_loop()

    print apple.map.map


