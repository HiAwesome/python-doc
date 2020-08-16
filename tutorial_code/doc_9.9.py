def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


for char in reverse('Hello world'):
    print(char)

"""
d
l
r
o
w
 
o
l
l
e
H
"""
