n = int(input())

horizontal_cuts = n // 2

vertical_cuts = n - horizontal_cuts

max_pieces = (horizontal_cuts + 1) * (vertical_cuts + 1)

print(max_pieces)
