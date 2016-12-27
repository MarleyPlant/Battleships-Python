def generateBoard(w, h):
	w += 1
	h += 1
	board = [[0 for x in range(w)] for y in range(h)]
	return board

def getRows(board):
	#Get The Number of rows on the board given. Use to get maximum ylim
	return len(board)

def getColumns(board):
	#Get The Number of columns on the board given. Use to get the maximum xlim
	return len(board[0])

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
			continue

	labels = [str(x) for x in board[row]]
	print(str(row) + "\t" + "\t".join(labels))
