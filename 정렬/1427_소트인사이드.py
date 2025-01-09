def quick_sort_reverse(lst):
    if len(lst)<=1:
        return lst
    pivot = len(lst)//2
    left = [x for x in lst if x < lst[pivot]]
    middle = [x for x in lst if x == lst[pivot]]
    right = [x for x in lst if x > lst[pivot]]
    return quick_sort_reverse(right)+middle+quick_sort_reverse(left)

inputs = list(input())
inputs = quick_sort_reverse(inputs)
for i in inputs:
    print(i, end='')

