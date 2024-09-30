def is_triangle(a, b, c):
    '''Returns True if a triangle can be formed from sides a, b, and c'''
    lst = [a, b, c]
    lst.sort()
    if lst[0] + lst[1] >= lst[2]:
        return True
    else:
        return False

def func():
    pass
    



print('This program tells you if a triangle can be formed from three sticks.')
# getting input from user
side_a = int(input('Enter first stick length: '))
side_b = int(input('Enter second stick length: '))
side_c = int(input('Enter third stick length: '))

print('Your sticks are:', side_a, side_b, side_c)
if is_triangle(side_a, side_b, side_c):
    print('A triangle can be formed')
else:
    print('NO triangle can be formed')
