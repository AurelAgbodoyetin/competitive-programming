n = int(input())
capacity = float('-inf')
actual = 0
for _ in range(n):
    a, b = list(map(int, input().split()))
    actual = b - a + actual
    capacity = max(capacity, actual)
    
print(capacity)