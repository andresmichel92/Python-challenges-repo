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



def firstNotRepeatingCharacter(s):
    char_set=list()
    char_counter=list()
    output='_'
    for char in s:
        if char not in char_set:
            char_set.append(char)
            char_counter.append(1)
        else:
            char_counter[char_set.index(char)]+=1
    if 1 in char_counter:
        output=char_set[char_counter.index(1)]
    return output


def main():
    x = [2, 1, 3, 5, 3, 2]
    s = "abacabad"
    print(firstDuplicate(x))
    print(firstNotRepeatingCharacter(s))


if __name__ == "__main__":
    main()



