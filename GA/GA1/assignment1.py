import argparse


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

def get_params(input):
    with open(input, 'r') as file:
        lines = file.readlines()

    first_line = lines[0].split(',')
    second_line = lines[1].split(',')
    third_line = ''
    if len(lines) == 3:
        third_line = lines[2].split(',')

    n, tmin, tmax = int(first_line[0]), int(first_line[1]), int(first_line[2])
    arr1, arr2 = [], []
    for i in range(n):
        arr1.append(int(second_line[i]))
    if len(lines) == 3:
        for j in range(len(third_line)):
            arr2.append(int(third_line[j]))

    return n, tmin, tmax, arr1, arr2


def print_to_output(val, output):
    with open(output, 'w') as file:
        file.write(str(val))
    print("Writing value to file " + output + " is completed.")


def bin_search_large(thres, keys):
    # len() has time complexity O(1)
    low_idx, high_idx = 0, len(keys) - 1
    # Decrease threshold by delta amount to eliminate equalities (there might be many 'a' values.)
    thres = thres + 0.01
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if keys[mid_idx] == thres:
            num = len(keys) - (mid_idx + 1)
            return num
        elif keys[mid_idx] < thres:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    mid_idx = (low_idx + high_idx) // 2
    num = len(keys) - (mid_idx + 1)
    return num


def bin_search_large_eq(thres, keys):
    # len() has time complexity O(1)
    low_idx, high_idx = 0, len(keys) - 1
    # Increase threshold by delta amount to include equalities (there might be many 'a' values.)
    thres = thres - 0.01
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if keys[mid_idx] == thres:
            num = len(keys) - mid_idx
            return num
        elif keys[mid_idx] < thres:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    mid_idx = (low_idx + high_idx) // 2
    num = len(keys) - (mid_idx + 1)
    return num


class SortedArray:
    def __init__(self):
        self.array = []
        self.length = 0

    def add(self, x, lo=0, hi=None):
        if hi is None:
            hi = len(self.array)
        pos = bisect_left(self.array, x, lo, hi)
        self.array.insert(pos, x)
        self.length += 1

    def __getitem__(self, idx):
        return self.array[idx]

    def __len__(self):
        return self.length


def bisect_left(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def number_of_allowable_intervals(input_file_path, output_file_path):
    n, tmin, tmax, arr, _ = get_params("C:\\Users\\dh-gu\\Desktop\\est_06.txt")

    # Sorted list ise used to keep track of previous values encountered. The values
    # will represent how many of a particular sum is encountered before.
    prev_sum = SortedArray()
    # Number of valid subsets that are less than tmin and/or tmax.
    num_min, num_max = 0, 0
    # Current summation value.
    sum_val = 0
    # Loop over every element of list A.
    for i in range(n):
        # Add current element of A onto sum.
        sum_val += arr[i]
        # Increase the number of subsets that add up to a value less than tmin.
        if sum_val < tmin:
            num_min += 1
        # Increase the number of subsets that add up to a value less than tmax.
        if sum_val <= tmax:
            num_max += 1
        # It might be possible that there exists sum_val - sum(A[i:k]) < tmin
        maxmin_num = bin_search_large(sum_val - tmin, prev_sum)
        num_min += maxmin_num
        # It might be possible that there exists sum_val - sum(A[i:k]) <= tmax
        maxmax_num = bin_search_large_eq(sum_val - tmax, prev_sum)
        num_max += maxmax_num
        # Add current sum value into the sortedlist so that it can be used to check future possible valid subsets.
        prev_sum.add(sum_val)
    num = num_max - num_min
    print("Valid number of pairs within the range [" + str(tmin) + ", " + str(tmax) + "] is " + str(num))
    print_to_output(num, output_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sum of element pairs from 2 different vectors.")
    parser.add_argument('-input', type=str, dest='input', help="Path to txt containing inputs.")
    parser.add_argument('-output1', type=str, dest='output1', help="Path to txt containing outputs.")
    parser.add_argument('-output2', type=str, dest='output2', help="Path to txt containing outputs.")
    args = parser.parse_args()

    print(solution2([-1, -1, -1, -1, 40, 20, -1, -1, -1, -1], -1000,0))
    number_of_allowable_intervals(args.input, args.output2)
