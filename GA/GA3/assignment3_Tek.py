import argparse
# Design and analyze an algorithm to compute E* with minimum total weight.
# The running time of your algorithm should be similar to the minimum spanning tree's running time.
# You may use Priority Queue to solve problem.

def manhatan_distance(v1,v2):
    #print(v1[0],v1[1], v2[0], v2[1])
    return abs(v2[0]-v1[0]) + abs(v2[1]-v1[1])

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

def create_graph(vertices, selected_edges):
    adj_matrix = [[] for _ in range(len(vertices))]

    for i, vertex in enumerate(vertices):
        #print("ori:",adj_matrix)
        for j in range(i):
            weight = manhatan_distance(vertex, vertices[j])
            adj_matrix[i].append(weight)
            adj_matrix[j].append(weight)
            #print("j:",adj_matrix)
        adj_matrix[i].append(0)
        #print("i:",adj_matrix)

    for edge in selected_edges:
        #print(edge)
        #print("0:",adj_matrix)
        adj_matrix[edge[0] - 1][edge[1] - 1] = 0
        #print("1:",adj_matrix)
        adj_matrix[edge[1] - 1][edge[0] - 1] = 0
        #print("2:",adj_matrix)

    return adj_matrix

def merge_sort(in_arr):
    if len(in_arr) <= 1:
        return in_arr

    mid_idx = len(in_arr) // 2
    low_half = merge_sort(in_arr[:mid_idx])
    up_half = merge_sort(in_arr[mid_idx:])
    i, j = 0, 0
    sorted = []
    while i < len(low_half) and j < len(up_half):
        if low_half[i][2] <= up_half[j][2]:
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

def kruskal(graph):

    pq = []
    visited = set()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != 0 and (i,j) not in visited:
                visited.add((i,j))
                visited.add((j,i))
                pq.append([i,j,graph[i][j]])

    sorted_pq = merge_sort(pq)
    #print(sorted_pq)

    T = []

    while sorted_pq:
                


    return 0
def solution(input_file_path, output_file_path):
    # Get points and selected edges
    vertices, selected_edges = get_params(input_file_path)

    # Create graph
    adj_matrix = create_graph(vertices, selected_edges)

    cost = kruskal(adj_matrix)

    print_to_output(0, output_file_path)

    return 0

# Example Usage
if __name__ == "__main__":
    # num_nodes = 4
    # edges = [(0, 1, 2), (1, 2, 3), (2, 3, 1), (3, 0, 4)]
    # selected_edges = [(0, 1), (2, 3)]
    # min_spanning_tree = kruskal(edges, selected_edges)
    # print("Minimum spanning tree edges:", min_spanning_tree)
    parser = argparse.ArgumentParser(description="Minimum cost connecting edges algorithm.")
    parser.add_argument('-input', type=str, dest='input', help="Path to txt containing inputs.")
    parser.add_argument('-output', type=str, dest='output', help="Path to txt containing outputs.")

    args = parser.parse_args()

    solution(args.input, args.output)


#print(Manhatan_distance(inputData[0], inputData[3]))
#print(len(Edot))