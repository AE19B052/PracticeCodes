'''
Print multiplication table form 1 to 10
'''
def multiplicationTable(number):
    for i in range(1 , 11):
        print(number * i, end='\t')
    print('\n')
    return 0

for number in range(1 , 11):
    multiplicationTable(number)