import math


def read_from_file():
    values = open('electr.in', 'r')
    readable_values = values.readlines()
    width = int(readable_values[0])
    heights = list(map(int, readable_values[1].split()))
    return width, heights


def calculate_length(width, start, end):
    return math.sqrt(pow(width, 2) + pow((end - start), 2))


def find_solution(width, heights):
    solutions = []
    last_on_top = [calculate_length(width, 1, heights[1])]
    last_on_bot = [calculate_length(width, heights[0], 1)]

    for i in range(2, len(heights)):
        x1_to_x2 = last_on_bot[last_on_bot.__len__() - 1] + calculate_length(width, 1, 1)
        x1_to_y2 = last_on_bot[last_on_bot.__len__() - 1] + calculate_length(width, 1, heights[i])
        y1_to_x2 = last_on_top[last_on_top.__len__() - 1] + calculate_length(width, heights[i - 1], 1)
        y1_to_y2 = last_on_top[last_on_top.__len__() - 1] + calculate_length(width, heights[i - 1], heights[i])

        last_on_bot.append(max(y1_to_x2, x1_to_x2))
        last_on_top.append(max(x1_to_y2, y1_to_y2))

        solutions.insert(i - 2, max(last_on_bot[last_on_bot.__len__() - 1], last_on_top[last_on_top.__len__() - 1]))
    return solutions


if __name__ == "__main__":
    width, heights = read_from_file()
    print(find_solution(width, heights).pop())
