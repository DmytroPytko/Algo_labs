def read_graph(txt_in):
    pup = []
    matrix = []
    with open(txt_in) as f:
        pup.extend(f.readline().split())
    for char in pup:
        matrix.append([ch for ch in char])

    length = len(matrix)
    num_of_mates = []

    for i in range(0, length):
        double_mates = set()
        for j in range(0, length):
            if matrix[i][j] == 'Y':
                double_mates.add(j)
                for row in range(0, length):
                    if matrix[row][j] == 'Y':
                        double_mates.add(row)
                double_mates.remove(i)
        num_of_mates.append(double_mates.__len__())
    print(num_of_mates)
    return max(num_of_mates)


if __name__ == '__main__':
    print(read_graph('txt.in'))
