i = 10
while i < 100:
    one = i // 10
    two = i % 10
    if one * two * 3 == i:
        print(i)
    i += 1