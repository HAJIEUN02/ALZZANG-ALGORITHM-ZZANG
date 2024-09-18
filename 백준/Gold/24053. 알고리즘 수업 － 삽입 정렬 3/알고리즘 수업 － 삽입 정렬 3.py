import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def insertion_sort(array_size, array_a, array_b):
    if array_a == array_b:
        print(1)
        sys.exit(0)

    for i in range(1, array_size):
        new_item = array_a[i]
        location = i-1

        while(location >= 0 and new_item < array_a[location]):
            array_a[location+1] = array_a[location]
            location -= 1
            if array_a == array_b:
                print(1)
                sys.exit(0)

        if location != i-1:
            array_a[location+1] = new_item
            if array_a == array_b:
                print(1)
                sys.exit(0)
    
    print(0)

insertion_sort(n, a, b)