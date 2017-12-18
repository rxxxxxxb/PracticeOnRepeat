# def MergeSort(numbers):

#     values = numbers
#     count = len(numbers)
#     return numbers,count

# numbers=[1,5,76,3,5,6]

# a = MergeSort(numbers)

# print(a)

# def sort():
#     merge_sort(0, count - 1)
#     return values

def merge_sort(low,high):
    if low < high:
        mid = (low + high)//2
        
        print("low " + str(low))
        print("mid " + str(mid))
        print("high "+ str(high))
        print("\n")

        merge_sort(low, mid)
        merge_sort(mid + 1, high)
        
a= [1,5,4,3,2,5,6]
merge_sort(1,10)

# def merge_sort(self, low, high):
#     if low < high:
#         mid = (low + high) // 2
#         print(mid)

#         self.merge_sort(low, mid)
#         self.merge_sort(mid + 1, high)
#         self.merge(low, mid, high)

# def merge(self, low, mid, high):
#     b = []
#     i = low
#     j = mid + 1

#     while i <= mid and j <= high:
#         if self.values[i] <= self.values[j]:
#             b.append(self.values[i])
#             i += 1
#         else:
#             b.append(self.values[j])
#             j += 1

#     while i <= mid:
#         b.append(self.values[i])
#         i += 1

#     while j <= high:
#         b.append(self.values[j])
#         j += 1

#     for index, val in enumerate(b):
#         self.values[low + index] = val


# def main():
#     original = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
#                 597, 42, 7506, 184, 184, 2409, 45, 824,
#                 4, -2650, 9, 662, 3928, -170, 45358, 395,
#                 842, 7697, 110, 14, 99, 221]

#     num = original[:]

#     ms = MergeSort(num)

#     output = ms.sort()


#     print(output)        