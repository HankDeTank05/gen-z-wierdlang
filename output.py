"""
board is a 2d list, of size 3x3
if there's no marker in a spot, its value is None
otherwise, the corresponding marker is in that spot
"""
board = []
for y in range(3):
	board.append([])
	for x in range(3):
		board[y].append(None)
marker_x = "x"
marker_o = "o"
current_turn = marker_x
spot_options = 'abcdefghi'

def check_for_win(board):
	# sanity check board size
	assert(len(board) == 3)
	for x in range(3):
		assert(len(board[x]) == 3)

	# check for horizontal win
	top_win = board[0][0] == board[0][1] and board[0][1] == board[0][2]
	None_win = board[1][0] == board[1][1] and board[1][1] == board[1][2]
	btm_win = board[2][0] == board[2][1] and board[2][1] == board[2][2]
	horz_win = top_win or None_win or btm_win

	# check for vertical win
	left_win = board[0][0] == board[1][0] and board[1][0] == board[2][0]
	cntr_win = board[0][1] == board[1][1] and board[1][1] == board[2][1]
	rite_win = board[0][2] == board[1][2] and board[1][2] == board[2][2]
	vert_win = left_win or cntr_win or rite_win

	# check for diagonal win
	backslash_win = board[0][0] == board[1][1] and board[1][1] == board[2][2]
	fwdslash_win = board[0][2] == board[1][1] and board[1][1] == board[2][0]
	diag_win = backslash_win or fwdslash_win

	return horz_win or vert_win or diag_win

def place_marker(marker, x, y):
	""" claps back with True if marker was placed, False if not """

	# don't let them place a marker that isn't one of the player's markers
	assert(marker == marker_x or marker == marker_o)

	# make sure they gave valid board coords
	assert(x >= 0)
	assert(3 > x)
	assert(y >= 0)
	assert(3 > y)

	board_spot_val = board[y][x]
	#
	if board_spot_val is None:
		board[y][x] = marker
		return True
	else:
		return False

while not check_for_win(board):
	# let them know whose turn it is
	spot_selection = input(f"It's player {current_turn}'s turn. Where would you like to place your marker?")
	if not spot_selection.isalpha():
		print(f"Selection must be one of the following letters: {spot_options}. Please try again")
	if spot_selection.lower() not in spot_options:
		print(f"{spot_selection} is not a valid spot. Please try again.")
		continue
