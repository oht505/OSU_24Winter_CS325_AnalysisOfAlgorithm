import argparse

# def get_params(input):
#     with open(input, 'r') as file:
#         lines = file.readlines()
#
#     first_line = lines[0].split(',')
#     second_line = lines[1].split(',')
#     third_line = ''
#     if len(lines) == 3:
#         third_line = lines[2].split(',')
#
#     n, tmin, tmax = int(first_line[0]), int(first_line[1]), int(first_line[2])
#     arr1 = []
#     for i in range(n):
#         arr1.append(int(second_line[i]))
#     if len(lines) == 3:
#         for j in range(len(third_line)):
#             arr2.append(int(third_line[j]))
#
#     return n, tmin, tmax, arr1, arr2

# n^3 time complexity
def solution1(A, tmin, tmax):
    sub_sum = 0
    count = 0
 
    for start in range(len(A)):
        for end in range(start, len(A)):
            for i in range(start, end+1):
                sub_sum += A[i]
    
            if tmin <= sub_sum <= tmax:
                count += 1

            sub_sum = 0
    
    return count

# n^2 time complexity
def solution2(A, tmin, tmax):
    sub_sum = 0
    count = 0

    for start in range(len(A)):
        for end in range(start, len(A)):
            sub_sum += A[end]
            if tmin <= sub_sum <= tmax:
                count += 1
        sub_sum = 0

    return count

# n*polylogn time complexity
def dac(A, tmin, tmax):
    n = len(A)
    
    if n < 2:
        return 1 if tmin <= A[0] <= tmax else 0

    mid = n//2
    left_list = A[:mid]
    right_list = A[mid:]
    
    count_left = dac(left_list, tmin, tmax)
    count_right = dac(right_list, tmin, tmax)

    count_mid = dac_mid(A, tmin, tmax)

    return count_left + count_right + count_mid

def dac_mid(A, tmin, tmax):

    count = 0
    n = len(A)
    mid = n//2

    idx_left, idx_right = mid-1, mid
    right_prefix_sum = A[idx_right]
    mid_sum = right_prefix_sum

    while idx_left >= 0 and idx_right < n:
        
        mid_sum += A[idx_left]

        if tmin <= mid_sum <= tmax:
            count += 1

        idx_left -= 1

        if idx_left < 0:
            idx_left = mid-1
            idx_right += 1
            if idx_right >= n:
                break
            right_prefix_sum += A[idx_right]
            mid_sum = right_prefix_sum
        
    return count

# def calculate_pairs(input, output):
#     n, tmin, tmax, arr1, arr2 = get_params(input)
#
#     valid_pair_num = get_sum_of_pairs(tmin, tmax, arr1, arr2)
#     print("Valid number of pairs within the range [" + str(tmin) + ", " + str(tmax) + "] is "+ str(valid_pair_num))
#     print_to_output(valid_pair_num, output)
# def count_subsum(input, output):
#     n, t_min, t_max, arr = get_params(input)
#
#
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Sum of element pairs from 2 different vectors.")
#     parser.add_argument('-input', type=str, dest='input', help="Path to txt containing inputs.")
#     parser.add_argument('-output', type=str, dest='output', help="Path to txt containing outputs.")
#     args = parser.parse_args()
#
#     count_subsum(args.input, args.output)

if __name__=="__main__":
    #listA = [-3,-4,2,0]
    listA = [-3, -4, 2, 0, 7, -5]
    t_min = -4
    t_max = 3

    print(dac(listA, t_min, t_max))


    
