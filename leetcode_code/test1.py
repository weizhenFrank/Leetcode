with open("/Users/weizhenliu/Desktop/test.txt", "r") as f:
    count = 0
    for x in f:
        if x[0] == '-':
            count += 1
            print(x)
print(count)