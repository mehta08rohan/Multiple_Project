
import sys
class TicTacToe:

    def __init__(self):
        self.board=[" "," "," "," "," "," "," "," "," "]
        self.counter = 0

    def display(self):
        print("{} | {} | {}".format(self.board[0],self.board[1],self.board[2]))
        print("__________")
        print("{} | {} | {}".format(self.board[3], self.board[4], self.board[5]))
        print("__________")
        print("{} | {} | {}".format(self.board[6], self.board[7], self.board[8]))



    def User1(self):
        self.counter += 1
        moves = int(input("Enter your move Player 1.{1-9}"))
        print()
        if self.board[moves-1] == " ":
            self.board[moves-1]='X'
        else:
            print("INVALID MOVE !!. . .Cell Already Taken")
            print()
            self.counter -= 1
            self.User1()


        self.display()
        self.CheckWin()
        self.User2()


    def User2(self):
        self.counter += 1
        moves = int(input("Enter your move Player 2.{0-8}"))
        print()
        if self.board[moves-1] == " ":
            self.board[moves-1]='0'

        else:
            print("INVALID MOVE !!. . .Cell Already Taken")
            print()
            self.counter -= 1
            self.User2()
        self.display()
        self.CheckWin()
        self.User1()

    def CheckWin(self):
        if self.board[0]=='X'and self.board[1]=='X' and self.board[2]=='X':
            print("Player 1 Wins")
            sys.exit()

        elif self.board[3]=='X'and self.board[4]=='X' and self.board[5]=='X':
            print("Player 1 Wins")
            sys.exit()
        elif self.board[6]=='X'and self.board[7]=='X' and self.board[8]=='X':
            print("Player 1 Wins")
            sys.exit()
        elif self.board[0]=='X'and self.board[3]=='X' and self.board[6]=='X':
            print("Player 1 Wins")
            sys.exit()
        elif self.board[1]=='X'and self.board[4]=='X' and self.board[7]=='X':
            print("Player 1 Wins")
            sys.exit()
        elif self.board[2]=='X'and self.board[5]=='X' and self.board[8]=='X':
            print("Player 1 Wins")
            sys.exit()
        elif self.board[0]=='X'and self.board[4]=='X' and self.board[8]=='X':
            print("Player 1 Wins")
            sys.exit()
        elif self.board[2]=='X'and self.board[4]=='X' and self.board[6]=='X':
            print("Player 1 Wins")
            sys.exit()


        elif self.board[0]=='0'and self.board[1]=='0' and self.board[2]=='0':
            print("Player 2 Wins")
            sys.exit()

        elif self.board[3]=='0'and self.board[4]=='0' and self.board[5]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.board[6]=='0'and self.board[7]=='0' and self.board[8]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.board[0]=='0'and self.board[3]=='0' and self.board[6]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.board[1]=='0'and self.board[4]=='0' and self.board[7]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.board[2]=='0'and self.board[5]=='0' and self.board[8]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.board[0]=='0'and self.board[4]=='0' and self.board[8]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.board[2]=='0'and self.board[4]=='0' and self.board[6]=='0':
            print("Player 2 Wins")
            sys.exit()
        elif self.counter ==9:
            print('Match Draw')
            sys.exit()



a= TicTacToe()

a.display()
a.User1()

