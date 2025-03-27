def euclidean_distance(point1, point2):
    return (((point1[0] - point2[0]))**2 + ((point1[1] - point2[1]))**2)**0.5

def merge_sort(in_arr):
    if len(in_arr) > 1:
        mid = len(in_arr)//2
        left_half = in_arr[:mid]
        right_half = in_arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                in_arr[k] = left_half[i]
                i += 1
            else:
                in_arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            in_arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            in_arr[k] = right_half[j]
            j += 1
            k += 1

    return in_arr

def valid_band(P, Q, band_length):
    m, n = len(P), len(Q)

    dp = [[False] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = True

    for i in range(1,m + 1):
        for j in range(1,n + 1):
            if i > 0 and dp[i - 1][j] and euclidean_distance(P[i - 1], Q[j - 1]) <= band_length:
                dp[i][j] = True
            elif j > 0 and dp[i][j - 1] and euclidean_distance(P[i - 1], Q[j - 1]) <= band_length:
                dp[i][j] = True
            elif i > 0 and j > 0 and dp[i - 1][j - 1] and euclidean_distance(P[i - 1], Q[j - 1]) <= band_length:
                dp[i][j] = True

    return dp[m][n]

def min_band_length(input_file_path, output_file_path):
    # Read input from file
    with open(input_file_path, 'r') as f:
        input_lines = f.readlines()

    # Parse input
    m = int(input_lines[0].strip())
    P_raw = input_lines[1].strip().split('),(')
    P = [tuple(int(coord) for coord in point.strip('()').split(',')) for point in P_raw]
    n = int(input_lines[2].strip())
    Q_raw = input_lines[3].strip().split('),(')
    Q = [tuple(int(coord) for coord in point.strip('()').split(',')) for point in Q_raw]
    t = int(input_lines[4].strip())
    L_raw = input_lines[5].strip().split(',')
    L = [int(band_length) for band_length in L_raw]

    # Sort the band lengths : t*logt
    merge_sort(L)

    # Find the minimum valid band length
    left, right = 0, len(L)-1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if valid_band(P, Q, L[mid]):
            result = L[mid]
            right = mid-1
        else:
            left = mid+1

    # Write output to file
    with open(output_file_path, 'w') as f:
        f.write(str(result))

    return result


# Example usage:
input_file_path = "test_small_2.txt"
output_file_path = "output_file.txt"

result = min_band_length(input_file_path, output_file_path)
print(result)