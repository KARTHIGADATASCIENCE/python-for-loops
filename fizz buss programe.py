for i in range(1,50):
    if i%3==0 and i%5==0:
        i="fizz buzz"
    elif i%5==0:
            i="buzz"
    elif i%3==0:
        i="fizz"
    else:
        i=i
    print(i)     
