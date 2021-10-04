def init():
    pairs = dict()
    for i in range(1, 90):
        key =  i*i
        pairs[key] = i
    return pairs


p = init()
x = 35

left = min(p.keys())
right = max(p.keys())
result = 0
ct=0
while True:

    ct +=1

    middle = (left + right) // 2

    if middle in p.keys():
        result = p[middle]  
        break
    else:
        if x < middle:
            right = middle
        if x > middle:
            left = middle

    print("==")
    print(middle)
    print("--")
    print(left)
    print(right)
    print("==")

    if ct>30:
        break




