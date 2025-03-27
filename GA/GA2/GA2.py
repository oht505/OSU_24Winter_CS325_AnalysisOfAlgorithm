def distance(point1, point2): #Defines a function distance to calculate the Manhattan distance between two points.
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def Cross(P, Q, band_length):  #Defines a recursive function Cross to check if the frogs can traverse P and Q with
    # a given band length. The base cases check if either sequence is empty or if the band length is negative.
    if band_length < 0:
        return False
    if len(P) == 0 or len(Q) == 0:
        return True
    #Defines three recursive options (A, B, C) where the frogs either move forward in P, move forward in Q, or move forward
    # in both simultaneously.
    option_A = Cross(P[1:], Q, band_length - distance(P[0], Q[0]))
    option_B = Cross(P, Q[1:], band_length - distance(P[0], Q[0]))
    option_C = Cross(P[1:], Q[1:], band_length - distance(P[0], Q[0]))

    return option_A or option_B or option_C  #Returns True if any of the options result in a successful traversal, otherwise False.

def CrossDP(P, Q, band_lengths):  #Defines an iterative dynamic programming function CrossDP using a 3D array dp to
    # store computed results. The array has dimensions len(P) + 1 x len(Q) + 1 x (max(band_lengths) + 1).
    dp = [[[False] * (max(band_lengths) + 1) for _ in range(len(Q) + 1)] for _ in range(len(P) + 1)]

    for i in range(len(P) + 1):
        dp[i][-1][0] = True

    for j in range(len(Q) + 1):
        dp[-1][j][0] = True

    for i in range(len(P) - 1, -1, -1):
        for j in range(len(Q) - 1, -1, -1):
            for band_length in band_lengths:
                if band_length >= distance(P[i], Q[j]):
                    dp[i][j][band_length] = dp[i + 1][j][band_length - distance(P[i], Q[j])] \
                                            or dp[i][j + 1][band_length - distance(P[i], Q[j])] \
                                            or dp[i + 1][j + 1][band_length - distance(P[i], Q[j])]
#Fills in the dynamic programming array using the recursive relation, considering three possible options at each step.
    return dp[0][0]
#Returns the result indicating whether there exists a valid band for the frogs to traverse P and Q.

#Defines a function ShortestUsefulBand to find the shortest useful band using binary search. Sorts the band lengths
# and iteratively searches for the minimum useful band length.

def ShortestUsefulBand(P, Q, band_lengths):
    band_lengths.sort()

    left, right = 0, len(band_lengths) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2

        if CrossDP(P, Q, band_lengths[:mid + 1]):
            result = band_lengths[mid]
            right = mid - 1
        else:
            left = mid + 1

    return result #Returns the final result, which is the length of the shortest useful band.

# Example usage
P = [(0, 0), (2, 0)]
Q = [(0, 1), (2, 1)]
band_lengths = [5,0,1,3,12,5]

# result = ShortestUsefulBand(P, Q, band_lengths)
# print("Shortest Useful Band:", result)
print(Cross(P,Q,band_lengths[5]))