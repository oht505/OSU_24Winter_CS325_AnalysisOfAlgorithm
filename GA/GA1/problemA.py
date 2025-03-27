import bisect

def solution(listA, listB, tmin, tmax):
    listA.sort()
    listB.sort()

    m,n = len(listA), len(listB)
    ans = 0
    
    for a in listA:
        low = tmin-a
        high = tmax-a

        lower_bound = bisect.bisect_left(listB, low)
        print("low:", low,", lower_bound:", lower_bound)

        upper_bound = bisect.bisect_right(listB, high)
        print("high:",high, ", upper_bound:",upper_bound)

        ans += max(0, upper_bound-lower_bound)
        
    return ans

A = [-3,-1,0,20]
B = [-4,5]
tmin, tmax = -3, 20
print(solution(A,B,tmin,tmax))