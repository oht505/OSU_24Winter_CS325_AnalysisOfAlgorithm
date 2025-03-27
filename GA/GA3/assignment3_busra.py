import argparse


def print_to_output(val, output):
    with open(output, 'w') as file:
        file.write(str(val))
    print("Writing output value to file " + output + " is completed.")


def get_params(in_file):
    with open(in_file, 'r') as file:
        lines = file.readlines()

    p_strings = lines[0].split(')')
    p_coors = []
    for p_string in p_strings:
        if p_string == '\n':
            continue
        p_num_strs = p_string.split('(')
        p_coor_strs = p_num_strs[1].split(',')
        p_coor = [int(p_coor_strs[0]), int(p_coor_strs[1])]
        p_coors.append(p_coor)

    q_strings = lines[1].split(')')
    q_coors = []
    for q_string in q_strings:
        if q_string == '\n' or q_string == '':
            continue
        if 'none' in q_string:
            break
        q_num_strs = q_string.split('(')
        q_coor_strs = q_num_strs[1].split(',')
        q_coor = [int(q_coor_strs[0]), int(q_coor_strs[1])]
        q_coors.append(q_coor)

    return p_coors, q_coors


def compute_distance(v1, v2):
    # Compute manhattan distance
    dist = abs(v2[0] - v1[0]) + abs(v2[1] - v1[1])
    return dist


def create_graph(vertices, selected_edges):
    adj_matrix = [[] for _ in range(len(vertices))]

    for i, vertex in enumerate(vertices):
        print("ori:",adj_matrix)
        for j in range(i):
            man_distance = compute_distance(vertex, vertices[j])
            adj_matrix[i].append(man_distance)
            adj_matrix[j].append(man_distance)
            print("j:",adj_matrix)
        adj_matrix[i].append(0)
        print("i:",adj_matrix)

    for edge in selected_edges:
        print(edge)
        print("0:",adj_matrix)
        adj_matrix[edge[0] - 1][edge[1] - 1] = 0
        print("1:",adj_matrix)
        adj_matrix[edge[1] - 1][edge[0] - 1] = 0
        print("2:",adj_matrix)

    return adj_matrix


def binary_search(pq, val):
    # len() has time complexity O(1)
    low_idx, high_idx = 0, len(pq) - 1
    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        if pq[mid_idx][1] == val:
            return mid_idx + 1
        elif pq[mid_idx][1] < val:
            high_idx = mid_idx - 1
        else:
            low_idx = mid_idx + 1
    mid_idx = (low_idx + high_idx) // 2
    return mid_idx + 1


def push_pq(pq, val, priority):
    # Lower priority value is higher priority.
    index = binary_search(pq, priority)
    pq.insert(index, [val, priority])
    return pq


def pop_pq(pq):
    val, priority = pq.pop(-1)
    return pq, val, priority


def find_min_spanning_tree(adj_matrix):
    pq = [[[-1, 0], 0]]
    tree = [-1] * len(adj_matrix)
    marked = [0] * len(adj_matrix)
    costs = [float('inf')] * len(adj_matrix)
    costs[0] = 0
    while pq:
        pq, edge, priority = pop_pq(pq)
        curr_vertex = edge[1]
        if marked[curr_vertex]:
            continue
        marked[curr_vertex] = 1
        for vertex, weight in enumerate(adj_matrix[curr_vertex]):
            if not marked[vertex] and costs[vertex] > weight:
                costs[vertex] = weight
                pq = push_pq(pq, [curr_vertex, vertex], weight)
                tree[vertex] = curr_vertex
    return sum(costs)


def minimum_cost_connecting_edges(input_file_path, output_file_path):
    # Read Inputs
    vertices, selected_edges = get_params(input_file_path)

    # Create an adjacency matrix to store graph information.
    adj_matrix = create_graph(vertices, selected_edges)

    cost = find_min_spanning_tree(adj_matrix)

    # Print result to output file.
    print_to_output(cost, output_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Minimum cost connecting edges algorithm.")
    parser.add_argument('-input', type=str, dest='input', help="Path to txt containing inputs.")
    parser.add_argument('-output', type=str, dest='output', help="Path to txt containing outputs.")
    args = parser.parse_args()

    minimum_cost_connecting_edges(args.input, args.output)
