from putivka import Putivka
from quick_sort import Quicksort
from selection_sort import insertion_sort
import time


if __name__ == "__main__":
    putivkas_list = []

    country_pos = 0
    duration_pos = 1
    price_pos = 2
    file = open('putivka.csv')
    for line in file:
        values = line.split(',')
        putivka = Putivka(values[country_pos], int(values[duration_pos]), int(values[price_pos][:-1]))
        putivkas_list.append(putivka)

    print("Initial array")
    for putivka in putivkas_list:
        print(putivka)
    print()

    print("Insertion sort")
    start_time = time.clock()
    insertion_sort(putivkas_list)

    print("Time: " + str(time.clock() - start_time))

    for putivka in putivkas_list:
        print(putivka)
    print()

    print("Quicksort")
    quicksort = Quicksort(putivkas_list)
    start_time = time.clock()
    quicksort.quick_sort(0, len(putivkas_list) - 1)

    print("Time: " + str(time.clock() - start_time))

    for putivka in putivkas_list:
        print(putivka)

