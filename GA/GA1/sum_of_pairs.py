import argparse


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


def merge_sort(in_arr):
    if len(in_arr) <= 1:
        return in_arr

    mid_idx = len(in_arr) // 2
    low_half = merge_sort(in_arr[0:mid_idx])
    up_half = merge_sort(in_arr[mid_idx:])
    i, j = 0, 0
    sorted = []
    while i < len(low_half) and j < len(up_half):
        if low_half[i] <= up_half[j]:
            sorted.append(low_half[i])
            i += 1
        else:
            sorted.append(up_half[j])
            j += 1
    while i < len(low_half):
        sorted.append(low_half[i])
        i += 1
    while j < len(up_half):
        sorted.append(up_half[j])
        j += 1
    return sorted


def get_invalid_bmin(tmin, vecB):
    low_idx, high_idx = 0, len(vecB) - 1
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if vecB[mid_idx] == tmin:
            num = mid_idx
            return num
        elif vecB[mid_idx] < tmin:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    mid_idx = (low_idx + high_idx) // 2
    num = mid_idx + 1
    return num


def get_valid_bmax(tmax, vecB):
    low_idx, high_idx = 0, len(vecB) - 1
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if vecB[mid_idx] == tmax:
            num = mid_idx + 1
            return num
        elif vecB[mid_idx] < tmax:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1
    mid_idx = (low_idx + high_idx) // 2
    num = mid_idx + 1
    return num


def get_sum_of_pairs(tmin, tmax, vecA, vecB):
    vecA, vecB = merge_sort(vecA), merge_sort(vecB)
    valid_num = 0
    for a in vecA:
        adjusted_tmin, adjusted_tmax = tmin - a, tmax - a
        invalid_bmin_num = get_invalid_bmin(adjusted_tmin, vecB)
        valid_bmax_num = get_valid_bmax(adjusted_tmax, vecB)
        valid_num += valid_bmax_num - invalid_bmin_num
    return valid_num


def print_to_output(val, output):
    with open(output, 'w') as file:
        file.write(str(val))
    print("Writing value to file " + output + " is completed.")


def calculate_pairs(input, output):
    n, tmin, tmax, arr1, arr2 = get_params(input)

    valid_pair_num = get_sum_of_pairs(tmin, tmax, arr1, arr2)
    print("Valid number of pairs within the range [" + str(tmin) + ", " + str(tmax) + "] is "+ str(valid_pair_num))
    print_to_output(valid_pair_num, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sum of element pairs from 2 different vectors.")
    parser.add_argument('-input', type=str, dest='input', help="Path to txt containing inputs.")
    parser.add_argument('-output', type=str, dest='output', help="Path to txt containing outputs.")
    args = parser.parse_args()

    calculate_pairs(args.input, args.output)
