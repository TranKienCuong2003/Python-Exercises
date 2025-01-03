def average_of_list(lst):
    return sum(lst) / len(lst)
lst = list(map(int, input().split()))
print(average_of_list(lst))
