def print_board():
	for i in range(0, 3):
		for j in range(0, 3):
			print Map[2-i][j],
			if j != 2:
				print "|",
		print ""

def check_done():
	for i in range(0, 3):
		if Map[i][0] == Map[i][1] == Map[i][2] != " " \
		or Map[0][i] == Map[1][i] == Map[2][i] != " ":
			print turn, "won!!!"
			return True

	if Map[0][0] == Map[1][1] == Map[2][2] != " " \
	or Map[0][2] == Map[1][1] == Map[2][0] != " ":
		print turn, "won!!!"
		return True

	if " " not in Map[0] and " " not in Map[1] and " " not in Map[2]:
		print "Draw"
		return True

	return False

turn = "X"
Map = [[" "," "," "],
		[" "," "," "],
		[" "," "," "]]
done = False

while done != True:
	print_board()

	print turn, "'s turn"
	print

	moved = False 
	while moved != True:
		print "Please select position by typing in a number between 1 and 9,see below for which number that is which positon..."
		print "7|8|9"
		print "4|5|6"
		print "1|2|3"
		print

		try:
			pos = input("Select: ")
			if pos <= 9 and pos >= 1:
				Y = pos / 3
				X = pos % 3
				if X != 0:
					X -= 1
				else:
					X = 2
					Y -= 1

				if Map[Y][X] == " ":
					Map[Y][X] = turn
					moved = True
					done = check_done()

					if done == False:
						if turn == "X":
							turn = "O"
						else:
							turn = "X"


		except:
			print "You need to add a numeric value"
