a = [['4'], ['0'], ['4'], ['C'], ['T'], ['F'], ['{'], ['M'], ['3'], ['R'], ['C'], ['1'], ['_'], ['P'], ['Y'], ['7'], ['H'], ['0'], ['N'], ['3'], ['.'], ['1'], ['0'], ['_'], ['P'], ['0'], ['U'], ['R'], ['_'], ['L'], ['3'], ['_'], ['M'], ['4'], ['7'], ['C'], ['H'], ['}']]

max_height = max([len(i) for i in a])

for i in range(max_height):
    for column in a:
        if len(column) > i:
            print(column[i], end = "")
        else:
            print(" ", end = "")
    print()
