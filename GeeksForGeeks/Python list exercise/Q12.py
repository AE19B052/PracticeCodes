#defining a function to find product
def prod(a):
    p = 1
    for i in a:
        p = p * i
    return p

#initaialize list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
test_set = set(test_list)
print(prod(test_set))