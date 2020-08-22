#Given an array a that contains only numbers in the range from 1 to a.length,
#find the first duplicate number for which the second occurrence has the minimal
#index. In other words, if there are more than 1 duplicated numbers, return the
#number for which the second occurrence has a smaller index than the second
#occurrence of the other number does. If there are no such elements, return -1

def firstDuplicate(a):
    winner =-1
    if len(a) > 2:
        duplicates=set()
        for i in a:
            if i in duplicates:
                winner=i
                break
            else:
                duplicates.add(i)
    return winner



x= [2, 1, 3, 5, 3, 2]

print(firstDuplicate(x))