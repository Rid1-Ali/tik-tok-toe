import itertools

print('a  b  c')

def win(current_game):
	#Diagonal
	def all_same(l):
		if (l.count(l[0]) == len(l) and l[0] != 0):
			print("Hits here")
			return True
		else:
			return False

	diags=[]
	for col, row in enumerate(reversed(range(len(current_game)))):
		diags.append(current_game[row][col])
	dig1 = all_same(diags)
	diags2 = []
	for ix in range(len(current_game)):
		diags2.append(current_game[ix][ix])

	dig2 = all_same(diags2)
	if dig1 or dig2:
		return True

	#Vertical
	for index,column in enumerate(game):
		check = []
		for x in game:
			check.append(x[index])
		if(all_same(check)):
			return True

	#Horizontal
	for row in game:
		print(row)
		if(all_same(row)):
			return True


def game_board(game_map, player=1, row=0, column=0, just_display=False):


	try:
		if game_map[row][column] != 0:
			print("Place is occupied, try again!")
			return False
		"   "+"  ".join([str(i) for i in range(len(game_map))])
		if not just_display:
			game_map[int(row)][int(column)] = player
		for count, x in enumerate(game_map):
			print(count, x)
		return game_map
	except IndexError as e:
		print(e)
		return False
	except ValueError as v:
		return False

#game_board()

play = True
player_choice = itertools.cycle([1, 2])
game_size = int(input("Please specify game size: "))
while play:
	game = [[0 for col in range(game_size)] for row in range(game_size)]
	game_won = False
	while not game_won:
		current_player = next(player_choice)

		played = False

		while not played:
			print("")
			print("Player number ",current_player," which one do you want to play")
			column_choice = int(input("What column do you want to play? "))
			row_choice = int(input("What row do you want to play? "))
			print(" ")
			played = game_board(game, current_player, row_choice, column_choice)
		if win(game):
			game_won = True
			print("Player number ",current_player, " WON!")
			again = input("Want to play again? (y)")
			if again.lower() == "y":
				print("restarting...")
			else:
				print("Byeeeeeee")
				play = False