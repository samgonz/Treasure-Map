row1 = ['⬜️','⬜️','⬜️']
row2 = ['⬜️','⬜️','⬜️']
row3 = ['⬜️','⬜️','⬜️']

userGuess = input('Where do you think the treasure is?\nChoose the row then location.\nExample 12 would mean row 1 2nd item.')

i = userGuess[0]   
j = userGuess[1] 

if i == '1':
    row1.pop(int(j))
    row1.insert(int(j)-1,'X')
if i == '2':
    row2.pop(int(j))
    row2.insert(int(j)-1,'X')
if i == '3':
    row3.pop(int(j))
    row3.insert(int(j)-1,'X')