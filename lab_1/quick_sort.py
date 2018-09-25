class Quicksort:

    list_for_sorting = []

    def __init__(self, list):
        self.list_for_sorting = list

    def quick_sort(self, low, hi):
        if low < hi:
            p = self.partition(low, hi)
            self.quick_sort(low, p-1)
            self.quick_sort(p+1, hi)
            pass

    def pivot(self, low, hi):
        mid = int((hi+low)/2)
        pivot = hi

        if self.list_for_sorting[low].price < self.list_for_sorting[mid].price:
            if self.list_for_sorting[mid].price < self.list_for_sorting[hi].price:
                pivot = mid

        elif self.list_for_sorting[low].price < self.list_for_sorting[hi].price:
            pivot = low

        return pivot

    def partition(self, low, hi):
        pivot_index = self.pivot(low, hi)
        pivot_value = self.list_for_sorting[pivot_index]
        self.list_for_sorting[pivot_index], self.list_for_sorting[low] = self.list_for_sorting[low], self.list_for_sorting[pivot_index]

        border = low

        for i in range(low, hi+1):
            if self.list_for_sorting[i].price < pivot_value.price:
                border+=1
                self.list_for_sorting[i], self.list_for_sorting[border] = self.list_for_sorting[border], self.list_for_sorting[i]

        self.list_for_sorting[low], self.list_for_sorting[border] = self.list_for_sorting[border], self.list_for_sorting[low]

        return border

