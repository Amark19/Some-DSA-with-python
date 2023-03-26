#traditional approach

# def list_zipper(list1, list2):
#     result = []# storing the value in memory
#     for i in range(min(len(list1), len(list2))):
#         result.append((list1[i], list2[i]))
#     return result

# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c']

# for pair in list_zipper(list1, list2):
#     print(pair)

#generator approach


'''
The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested
'''
def list_zipper(list1, list2):
    for i in range(min(len(list1), len(list2))):
        yield (list1[i], list2[i])# generating value on the fly without storing the value in memory 


list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

for pair in list_zipper(list1, list2):# calling the generator function and iterating over it
    print(pair)