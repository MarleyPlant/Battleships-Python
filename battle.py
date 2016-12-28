import random
import platform
import os
os = platform.system()

def generateBoard(w, h):
	w += 1
	h += 1
	board = [[None for x in range(w)] for y in range(h)]
	return board

def getRows(board):
	#Get The Number of rows on the board given. Use to get maximum ylim
	return len(board)-1

def getColumns(board):
	#Get The Number of columns on the board given. Use to get the maximum xlim
	return len(board[0])-1

def drawBoard(board):
	#Draw the board given using text in the console
	ylim = getRows(board) 
	xlim = getColumns(board)
	top_labels = ""

	for i in range(xlim):
		top_labels = top_labels + "\t" + str(i)
	print(top_labels + "\n")
	
	for row in range(ylim):
		for column in range(xlim):
			continue #continue back into the row for loop
		labels = [str(x) for x in board[row]]
		print(str(row) + "\t" + "\t".join(labels))


def clearScreen():
	global os
	if os == "Windows":
		os.system('cls')
	elif os == "Linux":
		os.system('clear')
	elif os == "Mac":
		os.system('cld')
	else:
		print('OS NOT FOUND PLEASE CONTACT MARLEY@MARLEYPLANT.COM')


def populateCPUBoard(cpu_board, numShips):
	#Populate the board given with ships for the CPU
	xlim = getColumns(cpu_board)
	ylim = getRows(cpu_board)

	for ship in range(numShips):
		x = random.randint(0,xlim)
		y = random.randint(0,ylim)
		loop = True
		while loop:
			if cpu_board[y][x] == None:
				cpu_board[y][x] = 'X'
				loop = False
			else:
				x= random.randint(0,xlim)
				y= random.randint(0,ylim)

def populatePlayerBoard(board, numShips):
	xlim = getColumns(board)
	ylim = getRows(board)

	for ship in range(numShips):
			playerinput = raw_input("Enter ship coordinates (x,y): ")
			playerinput = playerinput.split(',')
			playerinput = [int(x) for x in playerinput]
			x,y = playerinput[0],playerinput[1]
			
			placing = True
			while placing:
				if x <= xlim and y <= ylim:
					board[x][y] = "O"
					placing = False
				else:
					print("incorrect placement, this would be off the board please try again!")
					playerinput = raw_input("Enter ship coordinates (x,y): ")
					playerinput = playerinput.split(',')
					playerinput = [int(x) for x in playerinput]
					x,y = playerinput[0],playerinput[1]
