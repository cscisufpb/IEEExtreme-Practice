# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
# import numpy
# import scipy
from collections import namedtuple

size = get_number()
Member = namedtuple('Member', 'name height')
members = [Member(get_word(), get_number()) for i in range(size)]
members.sort(key=lambda m: m.height)

heights = {}

for member in members:
    if member.height not in heights:
        heights[member.height] = []
    
    heights[member.height].append(member.name)

curr_index = 1
for i in heights:
    members_with_curr_height = heights[i]
    members_with_curr_height.sort()

    for member_name in members_with_curr_height:
        print(member_name, end=" ")

    print(curr_index, curr_index + len(members_with_curr_height) - 1)

    curr_index += len(members_with_curr_height)
