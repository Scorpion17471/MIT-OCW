N = 8
negativeFlag = False

if N < 0:
    negativeFlag = True
    N = abs(N)

for i in range(N+1):
    if i ** 3 == N:
        if negativeFlag:
            i, N = -i, -N
        print(f"The cube root of {N} is {i}")
        break
    elif i ** 3 > N:
        print("error")
        break