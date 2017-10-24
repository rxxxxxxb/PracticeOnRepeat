class MergeSort():
    def __init__(self,numbers):
        self.value = numbers
        self.count = len(numbers) 


    def sort(self):
        self.merge_sort(0, self.count - 1)
        return self.value

    def merge_sort(self,low,high):
        if low < high:
            mid = (low + high)//2

            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self,low,mid,high):
        m = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.value[i] <= self.value[j]:
                m.append(self.value[i])
                i += 1
            else:
                m.append(self.value[j])
                j += 1

        while i<= mid:
            m.append(self.value[i])
            i += 1

        while j<= high:
            m.append(self.value[j])
            j += 1

        for index,val in enumerate(m):
            self.value[low + index] = val                   




