# 수 정렬하기
# 삽입 정렬
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(1,n): # 두번째 원소부터 시작한다.
    key = arr[i] # key는 두번째 원소다.
    j = i-1 # j 는 key 바로 앞전 원소다.
    while j>=0 and arr[j] > key: #j가 0보다 크고 j번째 원소가 key 보다 클때까지 반복한다.
        arr[j+1] = arr[j] # j번째 원소가 key보다 크므로 위치를 바꿔준다.
        j = j - 1 # j를 하나 줄인다.
    arr[j+1] = key # 반복문이 끝나면 현재 위치의 원소를 다음 위치에 삽입한다.

for num in arr:
    print(num)

# 선택정렬
# 선택정렬은 비교 연산의 횟수가 적어서 교환 연산의 횟수가 적은 경우에 유리하다. 성능 안좋음.
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

for num in arr:
    print(num)

# 버블정렬
# 큰 값을 오른쪽으로 이동시키는 방법
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for num in arr:
    print(num)

# 퀵 정렬
# 다른 정렬보다 빠른 속도를 보여줌.
def quick_sort(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= pivot:
            left += 1
        while right >= start and arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

quick_sort(arr, 0, n-1)

for num in arr:
    print(num)

