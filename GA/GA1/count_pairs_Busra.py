def count_pairs_in_range(A, B, tmin, tmax):
    A.sort()
    B.sort()
    count = 0

    for a in A:
        low = tmin - a
        high = tmax - a
        i=0
        j=0

        for b in B: 
         if b>=low:
            break
         i+=1
        
        for b in B:  
         if b>high:
            break
         j+=1

        count += max(0, j-i)

    return count

# Example usage:
A = [-2, 0, -1]
B = [-3, 10]
tmin, tmax = -3, 20
result = count_pairs_in_range(A, B, tmin, tmax)
print(result)  # Expected Output: 4
