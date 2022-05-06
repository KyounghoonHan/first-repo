print('hello')

for i in range(20):
    if (i+1) % 3 == 0 and (i+1) % 5 != 0:
        print('year')
    elif (i+1) % 5 == 0 and (i+1) % 3 != 0:
        print('dream')
    elif (i+1) % 5 == 0 and (i+1) % 3 == 0:
        print('year dream') 
    else:
        print(i+1) 
