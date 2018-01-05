class mergesort:

    def sort(self,data):
        sort = self._sort(data)
        print(sort)

    def _sort(self,data):
        if len(data) < 2:
            return data

        mid = len(data) //2 

        left = data[:mid]
        right = data[mid:]

        left = self._sort(left)
        right = self._sort(right)   

        return self._merge(left,right)

    def _merge(self,left,right):
        l = 0
        r = 0
        result = []
        lval = left[l]
        print("left",lval)
        rval = right[r]
        print("right", rval)


        while l < len(left) and r < len(right):
            if left[l] <  right[r]:
                result.append(left[l])
                print(result)
                l += 1
            else:
                result.append(right[r])
                r += 1
                print(result)

        while l < len(left):
            lval = left[l]
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1


        return result

ms = mergesort()
ar = [4,5,9,10,1,55,20]

ms.sort(ar)




