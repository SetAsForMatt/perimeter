land_array = ['XOOO',
'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']

def get_block_per(land, x, y, right=True, top=True, left=True, bottom=True):
    temp_perimeter = 4;
    if right:
        if land[y][x+1] == 'X':
            temp_perimeter-=1

    if top:
        if land[y-1][x] == 'X':
            temp_perimeter-=1

    if left:
        if land[y][x-1] == 'X':
            temp_perimeter-=1

    if bottom:
        if land[y+1][x] == 'X':
            temp_perimeter-=1

    return temp_perimeter



def landPerimeter(land):
    perimeter = 0
    width = len(land[0])
    height = len(land)
    for y in range(0,height):
        for x in range(0,width):
            if land[y][x]=='X':
                if y == 0:
                    if x ==0:
                        perimeter+=get_block_per(land, x,y,True,False,False,True)
                    elif x==len(land[0])-1:
                        perimeter += get_block_per(land, x, y, False, False, True, True)
                    else:
                        perimeter += get_block_per(land, x, y, True, False, True, True)
                elif y == len(land)-1:
                    if x ==0:
                        perimeter+=get_block_per(land, x,y,True,True,False,False)
                    elif x==len(land[0])-1:
                        perimeter += get_block_per(land, x, y, False, True, True, False)
                    else:
                        perimeter += get_block_per(land, x, y, True, True, True, False)
                else:
                    if x ==0:
                        perimeter+=get_block_per(land, x,y,True,True,False,True)
                    elif x==len(land[0])-1:
                        perimeter += get_block_per(land, x, y, False, True, True, True)
                    else:
                        perimeter += get_block_per(land, x, y, True, True, True, True)

    return perimeter

print(landPerimeter(land_array))