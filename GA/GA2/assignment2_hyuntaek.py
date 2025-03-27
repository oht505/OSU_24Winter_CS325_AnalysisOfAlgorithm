import random

# Calculate and check the real distance between (p_m) and (q_n)
def distancePQ(pointP,pointQ):

    return ((abs(pointQ[0]-pointP[0]))**2 + (abs(pointQ[1]-pointP[1]))**2)**(1/2)

# needed to check it
def Cross1(p, q, l):

    # base case is the end of list P and list Q
    if (len(p)==0 or len(q)==0):
        return True

    # if band length is negative, frogs cannot traverse
    if l - distancePQ(p[0],q[0]) < 0:
        #print("False -", "/p:",p[0], "/q:",q[0], "/l:", l, "/distance:", distancePQ(p[0], q[0]))
        return False
    # else:
    #     print("True -", "/p:",p[0], "/q:",q[0], "/l:", l, "/distance:", distancePQ(p[0], q[0]))

    result = False

    # recursion
    # p + 1 and q + 1
    if len(p) > 0 and len(q) > 0:
        print("(P + Q) -  p:", p[0], ",  q:", q[0], ",  l:", l, ", distance:", distancePQ(p[0], q[0]))
        result = result or Cross1(p[1:], q[1:], l)

    # p + 1
    if len(p) > 0:
        print("P -  p:", p[0], ",  q:", q[0], ",  l:", l, ", distance:", distancePQ(p[0], q[0]))
        result = result or Cross1(p[1:], q, l)

    # q + 1
    if len(q) > 0:
        print("Q -  p:", p[0], ",  q:", q[0], ",  l:", l, ", distance:", distancePQ(p[0], q[0]))
        result = result or Cross1(p, q[1:], l)

    return result

# Using Memoization
def Cross2(p, q, l):
    memo = {}

    def Cross2_memo(p, q, l, memo):

        if len(p) == 0 or len(q) == 0:
            return True

        if (len(p), len(q)) in memo:
            return memo[(len(p), len(q))]

        if l - distancePQ(p[0], q[0]) < 0:
            return False

        result = Cross2_memo(p[1:], q[1:], l, memo) \
                 or Cross2_memo(p[1:], q, l, memo) \
                 or Cross2(p, q[1:], l, memo)

        memo[(len(p), len(q))] = result

        #print(memo)

        return result

    return Cross2_memo(p,q,l,memo)

if __name__ == "__main__":
    p = [(0,0), (2,0), (3,0), (4,1), (3,2), (2,2)]
    q = [(0,-1), (-1,0), (0,1), (2,1), (3,1)]
    l = [5, 0, 1, 3, 2, 5, 12, 18]

    # p = [(0, 0), (1, 1), (2, 2), (3, 3)]  # Replace with your actual input
    # q = [(0, 0), (1, 2), (2, 4), (3, 6)]  # Replace with your actual input

    p = [(0,0), (2,0)]
    q = [(0,1), (2,1)]

    m = len(p)
    n = len(q)
    t = len(l)

    #print(Cross1(p, q, l[0]))
    #print(Cross2(p, q, l[0]))





