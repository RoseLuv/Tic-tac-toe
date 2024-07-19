import random

EMPTY = ' '
PLAYER_0 = 'X'
PLAYER_1 = 'O'
Tile_map = {
    1: (2,0),
    2: (2,1),
    3: (2,2),
    4: (1,0),
    5: (1,1),
    6: (1,2),
    7: (0,0),
    8: (0,1),
    9: (0,2)
}


class Game():
    def __init__(self) -> None:
        self.tiles = [
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY,EMPTY,EMPTY]
        ]
        self.main()
    def print_tiles(self) -> None:
        for i in range(3):
            print("       |       |     ")
            for j in range(3):
                print("  " + self.tiles[i][j] + "    ", end="")
                if j != 2:
                    print("|", end="")
                else:
                    print("")
            print("       |       |     ")
            if i != 2:
                print("-----------------------")
        return


        
    def turn(self, player: str) -> bool:
        tile = Tile_map.get(int(input("Select a tile! (1 - 9):")), -1)
        if tile == -1 or self.tiles[tile[0]][tile[1]] != EMPTY:
            print("Invalid number!\nEither out of range or already filled!")
            return False
        
        self.tiles[tile[0]][tile[1]] = player
        return True
    
    def check_ver(self, player: str):
        
        for i in range(3):
            in_row = 0
            for j in range(3):
                if self.tiles[j][i] == player:
                    in_row += 1
                
            if in_row == 3:
                return True
        return False
    
    def check_dig_up(self, player: str):
        in_row = 0
        for i in range(2, -1, -1):
            if self.tiles[i][i] == player:
                in_row += 1
        return in_row == 3
    
    def check_dig_down(self, player: str):
        in_row = 0
        for i in range(3):
            if self.tiles[i][i] == player:
                in_row += 1
        return in_row == 3
    
    def check_hor(self, player: str):
        for i in range(3):
            in_row = 0
            for j in range(3):
                if self.tiles[i][j] == player:
                    in_row += 1
                    
            if in_row == 3:
                return True
            
        return False
    
    def check_win(self, player:str):
        if self.check_hor(player) or\
            self.check_dig_down(player) or\
            self.check_dig_up(player) or\
            self.check_ver(player):
            print('Congrats! ' + player + " won!")
            return True
        
        
        return False
    
    
    def main(self):
        print("Welcome to Tic-Tac-Toe!\nThe first player is chosen at random!")
        print("The chosen player is:")
        cur_player = random.randint(0,1)
        if cur_player == 0:
            print('X!')
        else:
            print('O!')

        self.print_tiles()
        while True:
            if cur_player == 0:
                if self.turn(PLAYER_0):
                    self.print_tiles()
                    if self.check_win(PLAYER_0):
                        break
                    cur_player = 1
            else:
                if self.turn(PLAYER_1):
                    self.print_tiles()
                    if self.check_win(PLAYER_1):
                        break
                    cur_player = 0
                
    
game = Game()