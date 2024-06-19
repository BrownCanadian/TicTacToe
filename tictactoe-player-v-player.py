

row1=['■','■','■']

row2=['■','■','■']

row3=['■','■','■']

turn=1
position_list=[]


for i in range(0,1000):
    if turn%2!=0:
        point='X'
    if turn%2==0:
        point='O'
    
    location=int(input('Enter a number between 1 and 9: '))
     
    
    if location>9 or location<=0 or location in position_list:
        print('Error, put a valid input!')
    else:
        if location==1:
            row1[0]=point
        if location==2:
            row1[1]=point    
        if location==3:
            row1[2]=point
        if location==4:
            row2[0]=point
        if location==5:
            row2[1]=point
        if location==6:
            row2[2]=point
        if location==7:
            row3[0]=point
        if location==8:
            row3[1]=point
        if location==9:
            row3[2]=point
        position_list.append(location)
    
        turn+=1
        
        
        
            
    

    print(row1[0:])
    print(row2[0:])
    print(row3[0:])
    if (row1[0]=='X' and row1[1]=='X' and row1[2]=='X') or (row1[0]=='O' and row1[1]=='O' and row1[2]=='O'):
        print('Won')
        break        
    if (row2[0]=='X' and row2[1]=='X' and row2[2]=='X') or (row2[0]=='O' and row2[1]=='O' and row2[2]=='O'):
        print('Won')
        break 
    if (row3[0]=='X' and row3[1]=='X' and row3[2]=='X') or (row3[0]=='O' and row3[1]=='O' and row3[2]=='O'):
        print('Won')
        break 
    if (row1[0]=='X' and row2[0]=='X' and row3[0]=='X') or (row1[0]=='O' and row2[0]=='O' and row3[0]=='O'):
        print('Won')
        break 
    if (row1[1]=='X' and row2[1]=='X' and row3[1]=='X') or (row1[1]=='O' and row2[1]=='O' and row3[1]=='O'):
        print('Won')
        break 
    if (row1[2]=='X' and row2[2]=='X' and row3[2]=='X') or (row1[2]=='O' and row2[2]=='O' and row3[2]=='O'):
        print('Won')
        break     
    if (row1[0]=='X' and row2[1]=='X' and row3[2]=='X') or (row1[0]=='O' and row2[1]=='O' and row3[2]=='O'):
        print('Won')
        break 
    if (row1[2]=='X' and row2[1]=='X' and row3[0]=='X') or (row1[2]=='O' and row2[1]=='O' and row3[0]=='O'):
        print('Won')

    elif(len(position_list))==9:
        print('TIE')
        break