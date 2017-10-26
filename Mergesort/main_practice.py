from merge_sort_practice import MergeSort



def main():
    num = [325432, 989, 547510, 3, -93, 189019, 5042, 123,
                597, 42, 7506, 184, 184, 2409, 45, 824]

    #num = original[:]

    ms = MergeSort(num)

    out = ms.sort()

    print(out)


if __name__ == "__main__":
    main()
