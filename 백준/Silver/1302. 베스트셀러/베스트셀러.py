import sys
input = sys.stdin.readline

N = int(input())
books = dict()
for _ in range(N):
    title = input().strip()
    books[title] = books.get(title, 0) + 1
        
sorted_books = sorted(books.items(), key = lambda x:(-x[1], x[0]))
print(sorted_books[0][0])