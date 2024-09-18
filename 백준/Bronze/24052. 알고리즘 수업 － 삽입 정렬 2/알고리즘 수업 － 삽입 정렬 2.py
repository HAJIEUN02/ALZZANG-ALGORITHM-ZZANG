import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

def insertion_sort(array_size, change, array):
    change_count = 0

    for i in range(1, array_size):
        new_item = array[i]
        location = i-1

        while(location >= 0 and array[location] > new_item):
            array[location+1] = array[location]
            location -= 1
            change_count += 1
            if change_count == change:
                print(*array)
                sys.exit(0)

        if location != i-1:
            array[location+1] = new_item
            change_count += 1
            if change_count == change:
                print(*array)
                sys.exit(0)

    if change_count < change:
        print(-1)

insertion_sort(n, k, a)