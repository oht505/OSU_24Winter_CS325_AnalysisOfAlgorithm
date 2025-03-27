from collections import deque

# def CountBinaryStrings(n):
#     if n == 1:
#         return 2  # 0 또는 1을 가질 수 있으므로 2를 반환
#     if n == 2:
#         return 3
#     else:
#         # n 번째 비트가 0이라면, n-1 길이의 문자열에 대해 이진 문자열을 만들 수 있음
#         # n 번째 비트가 1이라면, n-2 길이의 문자열에 대해 이진 문자열을 만들 수 있음 (연속된 1을 피하기 위해)
#         return CountBinaryStrings(n-1) + CountBinaryStrings(n-2)


# #print(CountBinaryStrings(2))


# def collatz_sequence(n):
#     print(n)  # Print the current number in the sequence
#     if n == 1:  # Base case: If n reaches 1, stop the recursion
#         return None
#     elif n % 2 == 0:  # If n is even
#         collatz_sequence(n // 2)  # Recursively call collatz_sequence with n/2
#     else:  # If n is odd
#         collatz_sequence(3 * n + 1)  # Recursively call collatz_sequence with 3n + 1

# # Example usage:
# collatz_sequence(10)

# v = 5
# graph = [[0 for col in range(v)] for row in range(v)]
# print(graph)

def GreedySchedule(s,f):
    n = len(s)
    sf = [[s[i],f[i]] for i in range(n)]
    x = [0] * n

    sf.sort(key=lambda x:x[1])

    print(sf)

    count = 0
    x[count] = 0

    for i in range(0,n):
        #print(sf[i][0], sf[x[count]][1])
        if sf[i][0] > sf[x[count]][1]:
            count = count+1
            x[count] = i

    for i in range(len(x)):
        if i < 5:
            print(sf[x[i]])

    return x

#s = [1,2,3,3,4,7,7,9,10,12,16,18]
#f = [7,4,10,5,6,8,20,14,13,19,17,19]
#print(GreedySchedule(s,f))