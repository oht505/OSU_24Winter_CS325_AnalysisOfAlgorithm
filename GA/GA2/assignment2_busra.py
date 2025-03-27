# import argparse


def get_params(in_file):
    with open(in_file, 'r') as file:
        lines = file.readlines()

    p_num = int(lines[0])
    p_strings = lines[1].split(')')
    p_coors = []
    for p_string in p_strings:
        if p_string == '\n':
            continue
        p_num_strs = p_string.split('(')
        p_coor_strs = p_num_strs[1].split(',')
        p_coor = [int(p_coor_strs[0]), int(p_coor_strs[1])]
        p_coors.append(p_coor)

    q_num = int(lines[2])
    q_strings = lines[3].split(')')
    q_coors = []
    for q_string in q_strings:
        if q_string == '\n':
            continue
        q_num_strs = q_string.split('(')
        q_coor_strs = q_num_strs[1].split(',')
        q_coor = [int(q_coor_strs[0]), int(q_coor_strs[1])]
        q_coors.append(q_coor)

    l_num = int(lines[4])
    l_strings = lines[5].split(',')
    l_vals = []
    for l_string in l_strings:
        if l_string == '\n':
            continue
        l_vals.append(int(l_string))

    return p_num, q_num, l_num, p_coors, q_coors, l_vals


def print_to_output(val, output):
    with open(output, 'w') as file:
        file.write(str(val))
    print("Writing output value to file " + output + " is completed.")


def search(arr, val):
    shortest_valid_band = arr[0]
    for i in arr:
        if val <= i < shortest_valid_band:
            shortest_valid_band = i
    if shortest_valid_band >= val:
        return shortest_valid_band
    return None


def compute_band_length(p_point, q_point):
    return ((p_point[0] - q_point[0])**2 + (p_point[1] - q_point[1])**2)**.5


def compute_row(last_row, q_num, p_coor, q_coors):
    row = []
    for j in range(q_num):
        prev_cost_tuple = []
        node_cost = compute_band_length(p_coor, q_coors[j])
        if len(last_row) > 0:
            prev_cost_tuple.append(last_row[j])
            if j > 0:
                prev_cost_tuple.append(last_row[j - 1])
        if j > 0:
            prev_cost_tuple.append(row[j - 1])
        if not prev_cost_tuple:
            prev_cost_tuple = [0]
        row.append(max(node_cost, min(prev_cost_tuple)))
    return row


def compute_node_costs(p_num, q_num, p_coors, q_coors):
    row = []
    for i in range(p_num):
        row = compute_row(row, q_num, p_coors[i], q_coors)
    return row[-1]


def q3(input_file_path, output_file_path):
    # Read Inputs
    p_num, q_num, l_num, p_coors, q_coors, l_vals = get_params(input_file_path)

    # For dynamic programming start with the terminal state. Terminal state (P_M, Q_N) can be achieved by 3 actions:
    # (P_M, Q_N) <= (P_{M-1}, Q_N) or (P_M, Q_{N-1}) or (P_{M-1}, Q_{N-1}). Let C_{M}{N} denote the cost of (P_M, Q_N)
    # and A_{M-1,M}{N,N} denote the cost of arrival to (P_M, Q_N) from (P_{M-1}, Q_N) and J_{M-1,M}{N,N} denote
    # the cost of path to (P_M, Q_N) from (P_{M-1}, Q_N).
    # Then the cost C_{M}{N} can be recursively computed as:
    # C_{M}{N} = max(C_{M-1}{N}, J_{M-1,M}{N,N}) where
    # J_{M-1,M}{N,N} = min(A_{M-1,M}{N,N}, A_{M,M}{N-1,N}, A_{M-1,M}{N-1,N}).
    val = compute_node_costs(p_num, q_num, p_coors, q_coors)

    # Print result to output file.
    print_to_output(val, output_file_path)


def min_band_length(input_file_path, output_file_path):
    # Read Inputs
    p_num, q_num, l_num, p_coors, q_coors, l_vals = get_params(input_file_path)

    # For dynamic programming start with the terminal state. Terminal state (P_M, Q_N) can be achieved by 3 actions:
    # (P_M, Q_N) <= (P_{M-1}, Q_N) or (P_M, Q_{N-1}) or (P_{M-1}, Q_{N-1}). Let C_{M}{N} denote the cost of (P_M, Q_N)
    # and A_{M-1,M}{N,N} denote the cost of arrival to (P_M, Q_N) from (P_{M-1}, Q_N) and J_{M-1,M}{N,N} denote
    # the cost of path to (P_M, Q_N) from (P_{M-1}, Q_N).
    # Then the cost C_{M}{N} can be recursively computed as:
    # C_{M}{N} = max(C_{M-1}{N}, J_{M-1,M}{N,N}) where
    # J_{M-1,M}{N,N} = min(A_{M-1,M}{N,N}, A_{M,M}{N-1,N}, A_{M-1,M}{N-1,N}).
    val = compute_node_costs(p_num, q_num, p_coors, q_coors)

    # Search for the valid min length band width in the input l vector.
    val = search(l_vals, val)

    # Print result to output file.
    print_to_output(val, output_file_path)


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Sum of element pairs from 2 different vectors.")
#     parser.add_argument('-input', type=str, dest='input', help="Path to txt containing inputs.")
#     parser.add_argument('-output3', type=str, dest='output3', help="Path to txt containing outputs.")
#     parser.add_argument('-output4', type=str, dest='output4', help="Path to txt containing outputs.")
#     args = parser.parse_args()
#
#     q3(args.input, args.output3)
#     min_band_length(args.input, args.output4)
