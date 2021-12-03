import math

seed = 1
def randoPlus():
    global seed
    seed = (seed * 31 + 111119) % 10
    return seed

numbers = {
    0: ('XXX', 'X X', 'X X', 'X X', 'XXX'),
    1: ('  X', ' XX', '  X', '  X', '  X'),
    2: ('XXX', 'X  ', 'XXX', '  X', 'XXX'),
    3: ('XXX', '  X', ' XX', '  X', 'XXX'),
    4: ('  X', ' XX', 'XXX', '   ', '  X'),
    5: ('XXX', 'X  ', 'XXX', '  X', 'XXX'),
    6: ('XXX', 'X  ', 'XXX', 'X X', 'XXX'),
    7: ('XXX', '  X', ' X ', ' X ', 'X  '),
    8: ('XXX', 'X X', 'XXX', 'X X', 'XXX'),
    9: ('XXX', 'X X', 'XXX', '  X', 'XXX')
}

class task1(object):
    def __init__(self):
        pass
    def run(self):
        strings = set()
        while len(strings) < 4:
            strings.add(randoPlus())
        print(strings)

class task2(object):
    def __init__(self):
        pass
    def run(self):
        global numbers
        for i in range(len(numbers)):
            for v in numbers[i]:
                print(v)

class task3(object):
    def __init__(self):
        pass
    def run(self):

        global numbers
        strings = [""] * len(numbers[0])
        s = input()

        for v in s:
            t = numbers[int(v)]
            index = 0
            for v2 in t:
                strings[index] += v2 + " | "
                index+=1

        for v3 in strings:
            print(v3)

def main():
    key = 3 #int(input())
    tas1 = task1()
    if key == 1:
        tas1 = task1()
    elif key == 2:
        tas1 = task2()
    elif key == 3:
        tas1 = task3()
    tas1.run()

if __name__ == "__main__":
    main()
