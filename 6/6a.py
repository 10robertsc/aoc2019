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


if __name__ == "__main__":
    map = read_map("map.csv")
    paths = generate_paths("COM", map[:])
    direct_orbits = len(map)
    indirect_orbits = indirect_orbits(paths)
    print(
        "Direct orbits: %i \nIndirect orbits: %i \nSum: %i"
        % (direct_orbits, indirect_orbits, direct_orbits + indirect_orbits)
    )
