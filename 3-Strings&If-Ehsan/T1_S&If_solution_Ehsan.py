before = input()
after = input()

if (len(after) != len(before)):
    print("IMPOSSIBLE")
    exit()

forward_first_position = None
backward_first_position = None
forward_second_position = None
backward_second_position = None

if (before.count('>') != 0):
    forward_first_position = before.find('>')
if (before.count('<') != 0):
    backward_first_position = before.find('<')

if (forward_first_position != None):
    forward_second_position = after.find('>')
    if (forward_second_position < forward_first_position):
        print("IMPOSSIBLE")
        exit()
if (backward_first_position != None):
    backward_second_position = after.find('<')
    if (backward_second_position > backward_first_position):
        print("IMPOSSIBLE")
        exit()
        

if ((forward_first_position != None) and (backward_first_position != None)):
    if ((forward_first_position < backward_first_position) and (forward_second_position > backward_second_position)):
        print("IMPOSSIBLE")
        exit()

print("POSSIBLE")
    
