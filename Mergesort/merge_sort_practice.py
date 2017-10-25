class MergeSort():
    def __init__(self,numbers):
        self.values = numbers
        self.count = len(numbers)


    def sort(self):
        self.merge_sort(0, self.count -1)
        return self.values

    def merge_sort(self,low,high):
       if low < high:
           mid = (low +high)//2

           self.merge_sort(low,mid)
           self.merge_sort(mid +1 ,high)
           self.merge(low,mid,high)

    def merge(self,low,mid,high):
        b = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.values[i] <= self.values[j]:
