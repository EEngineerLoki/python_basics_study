char = '*'
row = 5
column = 5

for i in range(0, row + 1):
    for j in range(0, column + 1):
        if(i == 0 or i == row or j == 0 or j == column):
            print(char, end=' ')
        else:
            print(' ', end=' ')