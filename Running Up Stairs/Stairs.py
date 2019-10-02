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

def number_ways(t):
    previous_number_ways = current_number_ways = 1
    for _ in range(t - 1):
        previous_number_ways, current_number_ways = current_number_ways, previous_number_ways + current_number_ways

    return current_number_ways

n = get_number()
for _ in range(n):
    t = get_number()
    print(number_ways(t))