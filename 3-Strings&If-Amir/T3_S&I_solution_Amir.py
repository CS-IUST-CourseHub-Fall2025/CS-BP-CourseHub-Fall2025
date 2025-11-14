king_x, king_y = map(int, input().split())
piece_data = input()
piece = piece_data.split(":")[0]
piece_x, piece_y = map(int, piece_data.split(": ")[1].split())

check = 0

if not (1 <= king_x <= 8 and 1 <= king_y <= 8 and 1 <= piece_x <= 8 and 1 <= piece_y <= 8):
    print("Invalid positions")
    exit()

if piece == 'Q':
    if (abs(king_x - piece_x)) == (abs(king_y - piece_y))\
          or king_y == piece_y or king_x == piece_x:
        check = 1

elif piece == 'B':
    if (abs(king_x - piece_x)) == (abs(king_y - piece_y)):
        check = 1
    
elif piece == 'R':
    if king_y == piece_y or king_x == piece_x:
        check = 1

elif piece == 'N':
    if ((abs(king_x - piece_x)) == 2 and (abs(king_y - piece_y)) == 1)\
    or ((abs(king_x - piece_x)) == 1 and (abs(king_y - piece_y)) == 2):
        check = 1

elif piece == 'P':
    if not (2 <= piece_y <= 7):
        print("Invalid positions")
        exit()
    if king_y - piece_y == 1 and abs(king_x - piece_x) == 1:
        check = 1

else:
    print("Invalid piece")
    exit()

if check:
    print("YOU ARE IN CHECK")
else:
    print("It's Safe")