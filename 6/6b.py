import csv


def generate_paths(parent_node, map):
    # Probably could have handled this recursion more neatly
    child_nodes = []
    i = 0
    while i < len(map):
        if map[i][0] == parent_node:
            child_nodes.append(map.pop(i)[1])
        else:
            i += 1
    if len(child_nodes) == 0:
        return [[parent_node]]
    else:
        paths = []
        for child_node in child_nodes:
            sub_paths = generate_paths(child_node, map)
            for sub_path in sub_paths:
                sub_path.insert(0, parent_node)
            paths.extend(sub_paths)
        return paths


def indirect_orbits(paths):
    depth = {}
    for path in paths:
        for i, point in enumerate(path):
            depth[point] = i - 1
    del depth["COM"]
    indirect_orbits = 0
    for value in depth.values():
        indirect_orbits += value
    return indirect_orbits


def read_map(file):
    map = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            orbit = [row[0][: row[0].index(")")], row[0][row[0].index(")") + 1 :]]
            map.append(orbit)
    return map

def min_transfers(paths):
    path_you = [path for path in paths if "YOU" in path][0] # luckily only one path leads to you/san respectively
    path_san = [path for path in paths if "SAN" in path][0]

    min_transfer = len(path_san)+len(path_you)

    for i,planet_1 in enumerate(path_you):
        for j,planet_2 in enumerate(path_san):
            if planet_1 == planet_2:
                tmp = (len(path_you)-i -2)+(len(path_san)-j-2)
                if tmp < min_transfer:
                    min_transfer = tmp

    return min_transfer

if __name__ == "__main__":
    map = read_map("map.csv")
    paths = generate_paths("COM", map[:])
    print(min_transfers(paths))
