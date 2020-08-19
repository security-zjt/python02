count = int(input('Please input the count: \n'))
a = 1
while a <= count:
    num = int(input('Please input {} number:'.format(a)))
    if a == 1:
        max = min = num
    else:
        if num < min:
            min = num
        elif num > max:
            max = num
    a += 1

print('The max_num is: ',max)
print('The min_num is: ',min)




