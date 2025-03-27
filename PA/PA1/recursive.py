def ToBinary(n):
    if int(n)<2:
        print(int(n),end="")
    else:
        ToBinary(int(n/2))
        print(int(n)%2,end="")

ToBinary(10)