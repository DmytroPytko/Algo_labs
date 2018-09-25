def insertion_sort(putivkas):

    for i in range(len(putivkas)):

        min_index = i

        for j in range(i + 1, len(putivkas)):
            if putivkas[min_index].duration < putivkas[j].duration:
                min_index = j

        putivkas[min_index], putivkas[i] = putivkas[i], putivkas[min_index]

