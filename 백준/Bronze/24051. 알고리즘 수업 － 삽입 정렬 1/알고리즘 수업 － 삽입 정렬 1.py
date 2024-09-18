""" 삽입 정렬
insertion_sort(A[1..N]) { # A[1..N]을 오름차순 정렬한다.
    for i <- 2 to N {
        loc = i - 1;
        newItem = A[i];

        # 이 지점에서 A[1..i-1]은 이미 정렬되어 있는 상태
        while (1 <= loc and newItem < A[loc]) {
            A[loc + 1] <- A[loc];
            loc--;
        }
        if (loc + 1 != i) then A[loc + 1] = newItem;
    }
}
"""
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))

def check_save_count(save_count, save, number):
    if save_count == save:
        print(number)
        sys.exit(0)

def insertion_sort(array_size, save, array):
    save_count = 0

    for i in range(1, array_size):
        location = i-1
        new_item = array[i]

        # 이 시점에서 0부터 i-1까지는 정렬되어 있는 상태
        while(location >= 0 and array[location] > new_item):
            array[location + 1] = array[location]
            location -= 1
            save_count += 1
            check_save_count(save_count, save, array[location+1])

        if location + 1 != i:
            array[location+1] = new_item
            save_count += 1
            check_save_count(save_count, save, new_item)

    if save_count < save:
        print(-1)

insertion_sort(n, k, a)