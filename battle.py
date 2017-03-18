import random #Import the "random" library to randomly generate numbers for use in populating the CPU Board and making the CPU's moves
import platform #Import the "platform" library to detect the systems OS using "platform.system()"
import os
os = platform.system() #Get Operating system at library compile

def generateBoard(w, h):
	w += 1
	h += 1
	board = [[None for x in range(w)] for y in range(h)] #Generate the 2d array using for loops
	return board #Return the generated 2d array

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
			continue #continue back into the row's FOR loop
		labels = [str(x) for x in board[row]]
		print(str(row) + "\t" + "\t".join(labels))


def clearScreen():
	#Clear the Console using the command for the current running system
	global os
	if os == "Windows":
		os.system('cls') #Clear the screen on Windows
	elif os == "Linux":
		os.system('clear') #Clear the screen on Linux
	elif os == "Mac":
		os.system('cld') #Clear the screen on Mac OS
	else:
		print('OS NOT FOUND') #Display Error Code (This needs to be changed to submit a issue on github using http library


def populateCPUBoard(cpu_board, numShips):
	#Populate the board given with ships for the CPU.
	xlim = getColumns(cpu_board)  #Get the horizontal size of the board passed to the function.
	ylim = getRows(cpu_board) #Get the verticle size of the board passed to the function.

	for ship in range(numShips): #Start a for loop that will run once for every ship that is passed to the function in the numShips variable.
		x = random.randint(0,xlim) #Generate a random interger to use as the x coordinate.
		y = random.randint(0,ylim) #Generate a random interger to use as the y coordinate.
		placing = True #define a variable to start a second while loop to check if the place on the board is already taken.
		while placing: #start the while loop.
			if cpu_board[y][x] == None: #if there is nothing on the CPU's board at the coordinates generated continue.
				cpu_board[y][x] = 'X' #place the string of "X" to indicate that there is a ship at that location on the 2d array.
				placing = False #Stop the WHILE loop and return to the first FOR loop.
			else: #if the first condition is not met continue to regenerate the x and y coordinates on which to check.
				x= random.randint(0,xlim) #Generate a random interger to use as the x coordinate.
				y= random.randint(0,ylim) #Generate a random interget to use as the y coordinate.

def populatePlayerBoard(board, numShips):
	#Populate a board using the users input, this function takes two inputs, The board to populate and the number of ships to populate it with.
	xlim = getColumns(board) #Get the horizontal size of the board passed to the function.
	ylim = getRows(board) #Get the verticle size of the board passed to the function.

	for ship in range(numShips):
			playerinput = raw_input("Enter ship coordinates (x,y): ") #Get the users input from console.
			playerinput = playerinput.split(',') #Split the users input at the "," which will split it into two list items x and y.
			playerinput = [int(x) for x in playerinput] #Turn the split string into a list.
			x,y = playerinput[0],playerinput[1] #set the variables x & y to their values.

			placing = True #Define a variable to start a second while loop to check if the place on the board is already taken.
			while placing: #Start the checking loop.
				if x <= xlim and y <= ylim:
					board[x][y] = "O"
					placing = False #Stop the WHILE loop and return to the first FOR loop.
				else:
					print("incorrect placement, this would be off the board please try again!")
					playerinput = raw_input("Enter ship coordinates (x,y): ")
					playerinput = playerinput.split(',')
					playerinput = [int(x) for x in playerinput]
					x,y = playerinput[0],playerinput[1]
