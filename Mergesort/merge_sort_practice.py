class MergeSort():
    def __init__(self,number):
        self.values = number
        self.count = len(number)

    def sort(self):
        self.merge_sort(0 ,self.count - 1)
        return self.values

    def merge_sort(self,low,high):
        if low < high:
            mid = (low+high)//2

            self.merge_sort(low,high)
            self.merge_sort(mid +1,high)
            self.merge(low,mid,high)

    def merge(self,low,mid,high):
        a = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.values[i] <= self.values[j]:
                a.append(self.values[i])
                i += 1
            else:
                a.append(self.values[j])
                j += 1

        while i<=mid:
            a.append(self.values[i])
            i += 1

        while j<= high:
            a.append(self.values[j])
            j += 1     

        for index, v in enumerate(a):
            self.values[low+index] = v            


        

          

