board=[]
for i in range(9):
	board.append('_')

player='X'
comp='O'

def checkWinner(guy, board):
	if board[0]==guy and board[1]==guy and board[2]==guy or board[3]==guy and board[4]==guy and board[5]==guy or board[6]==guy and board[7]==guy and board[8]==guy or board[0]==guy and board[3]==guy and board[6]==guy or board[1]==guy and board[4]==guy and board[7]==guy or board[2]==guy and board[5]==guy and board[8]==guy or board[0]==guy and board[4]==guy and board[8]==guy or board[2]==guy and board[4]==guy and board[6]==guy:
		return True
	return False		

def playmove(move):
	if board[move]=='_':
		board[move]='X'
	else:
		print("invalid u fucker")

def guesscompmove(board):
	playables=[i for i in range(9) if board[i]=='_']
	score=0
	for i in playables:
		fakeboard=board[:]
		fakeboard[i]='O'
		if checkWinner('O', fakeboard)==True:
			score+=1
		else:
			score+=0.3*guessplaymove(fakeboard)
	return score

def guessplaymove(board):
	playables=[i for i in range(9) if board[i]=='_']
	score=0
	for i in playables:
		fakeboard=board[:]
		fakeboard[i]='X'
		if checkWinner('X', fakeboard):
			score-=1
		else:
			score+=0.3*guesscompmove(fakeboard)
	return score

def compmove(board):
	score=[]
	lol=[-100, 0]
	print("comp move entered: ")
	playables=[i for i in range(9) if board[i]=='_']
	fin=[playables[0], 0]
	for i in playables:
		fakeboard=board[:]
		fakeboard[i]='O'
		if checkWinner('O', fakeboard)==True:
			board[i]='O'
			print("won at ", i)
			return
		else:
			score.append(guessplaymove(fakeboard))
	
	lol=sorted(score, key=lambda x:float(x))[-1]
	for i in enumerate(score):
		if i[1]==lol:
			lol=playables[i[0]]
			break
	board[lol]='O'

def dikhao(board):
	for i in range(3):
		for j in range(3):
			print(board[i*3+j], end=" ")
		print()

def khatam():
	if '_' not in board:
		return True
	return False

def play():
	dikhao(board)
	while(khatam()==False):
		move=int(input("de na be: "))
		playmove(move)
		if checkWinner('X', board) == True:
			print("Winner winner chicken dinner")
			break
		if khatam():
			print("draw")
			break
		compmove(board)
		dikhao(board)
		if checkWinner('O', board) == True:
			print("Fuck off loser")
			break
play()
