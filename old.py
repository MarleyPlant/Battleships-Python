import platform
import time
numberofcpuships = 4
numberofplayerships = 4
is_python_2 = platform.python_version().split(".")[0] == "2" #Check Python Version
def Startscreen():
	print("Instructions:")
	print("1. 0 is the location of your ship")
	print("2. ! Meens A hit there")
	print("3. # Meens a miss there")
	print("")
	print("All Credit: @MarleyJPlant - http://marleyplant.com")
	import time
	time.sleep(5)

if is_python_2:
    input = raw_input

os = platform.system() #Get Operating System

if os == "Windows": #Set Clear Commads to the operating systems
    clear = "cls"
elif os == "Linux":
    clear = "clear"
elif os == "Mac":
    clear = "clf"
else:
	print("Error code 01")
	print("Unknown OS!!")
    
def clearscreen():
	import os
	os.system(clear)
clearscreen()
Startscreen()


cpu_board = [ #Generate The Computers Board
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]

bottom_board = [ #Generate Your Bottom Board
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]

top_board = [ #Generate Top Bottom Board
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None]
]


#Game Logic
import random

def count_O(l,letter):
    count = 0
    for sublist in l:
        count += sublist.count(letter)
    return count
def checkifwon():
	playerships = count_O(bottom_board,"O")
	computerships = count_O(cpu_board,"X")
	if playerships == 0:
		print("Computer wins!!!")
		import sys
		import time
		time.sleep(5)
		sys.exit()
	elif computerships == 0:
		print("Player Wins!!")
		import sys
		import time
		time.sleep(5)
		sys.exit()
def cpu_attack():
	import random
	x = random.randint(0,8)
	y = random.randint(0,8)
	if bottom_board[y][x] == "O":
		print("Computer Hit You at " + str(x) + "," + str(y))
		bottom_board[y][x] = "!"
		time.sleep(2)
	else:
		print("Computer Missed")
		bottom_board[y][x] = "#"

def place_a_ship(xpos,ypos):
    if cpu_board[ypos][xpos] == "X" or bottom_board == "O":
        print("Cannot place board taken!")
    else:
        bottom_board[ypos][xpos] = "O"
def draw_board(board):
    if board == "top":
        global top_board

        print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\n")

        for row in range(9):
            for column in range(9):
                continue

            labels = [str(x) for x in top_board[row]]
            print(str(row) + "\t" + "\t".join(labels))

    elif board == "bottom":
        global bottom_board
        print("\t0\t1\t2\t3\t4\t5\t6\t7\t8\n")

        for row in range(9):
            for column in range(9):
                continue

            labels = [str(x) for x in bottom_board[row]]
            print(str(row) + "\t" + "\t".join(labels))

def getplayerinput(typeofinput):
    if typeofinput == "place":
        playerinput = input("Enter ship coordinates (x,y): ")
        playerinput = playerinput.split(',')
        playerinput = [int(x) for x in playerinput]
        return playerinput
    elif typeofinput == "attack":
        playerinput = input("Enter Attack coordinates (x,y): ")
        playerinput = playerinput.split(',')
        playerinput = [int(x) for x in playerinput]
        return playerinput
    else:
        print("Error code 02")
        print("Unknown input type")
    
def attack(x,y):
    if cpu_board[y][x] == "X":
        print("HIT!")
        top_board[y][x] = "!"
    else:
        print("MISS!!")
        top_board[y][x] = "#"

for i in range(numberofcpuships):
    cpu_x = random.randint(0,8)
    cpu_y = random.randint(0,8)
    
    loop = True
    while loop:
        if cpu_board[cpu_y][cpu_x] == None:
            cpu_board[cpu_y][cpu_x] = 'X'
            loop = False
        else:
            cpu_x = random.randint(0,8)
            cpu_y = random.randint(0,8)

clearscreen()
draw_board("top")
draw_board("bottom")
for i in range(numberofplayerships):
        coords = getplayerinput("place")
        place_a_ship(coords[0],coords[1])
        clearscreen()
        draw_board("top")
        draw_board("bottom")
clearscreen()
clearscreen()
draw_board("top")
draw_board("bottom")

while True:
    clearscreen()
    draw_board("top")
    draw_board("bottom")
    coords = getplayerinput("attack")
    attack(coords[0],coords[1])
    checkifwon()
    clearscreen()
    draw_board("top")
    draw_board("bottom")
    print("computer guessing...")
    time.sleep(1)
    clearscreen()
    draw_board("top")
    draw_board("bottom")
    cpu_attack()
    checkifwon()
    time.sleep(2)
