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


def mutateTheArray(n, a):
    b=list()
    the_sum=0
    for i in range(0,n):

        if (i+1) > len(a)-1:
            the_sum=a[i-1]+a[i]+0
        elif (i-1) < 0:
            the_sum=0+a[i]+a[i+1]
        else:
            the_sum=a[i-1]+a[i]+a[i+1]
        b.append(the_sum)
        print(str(i)+","+str(the_sum))
    return b


def alternatingSort(a):
    b=list()
    counter=0
    counter2=0
    check_list=list()
    for i in range(0,len(a)):
        if i%2==0:
            b.append(a[counter2])
            counter2+=1
        else:
            b.append(a[len(a)-counter-1])
            counter += 1
    check_list=b.copy()
    check_list.sort()
    print(check_list)
    print(b)
    return check_list==b

def countPairsSum(k, a):
    counter=0
    pairs=list()
    if len(a)>1:
        for i in range(0,len(a)-1):
            for j in range(i,len(a)):
                if a[i]+a[j]==k:
                    print(str(a[i])+","+str(a[j]))
                    if str(a[i])+","+str(a[j]) not in pairs:
                        pairs.append(str(a[i])+","+str(a[j]))
                        pairs.append(str(a[j])+","+str(a[i]))
                        counter+=1
    return counter


def main():
    p= [10, 9, 4, 0, 8, 1, 7, 6, 10, 5]
    k=11
    print(countPairsSum(k,p))

    x = [2, 1, 3, 5, 3, 2]
    s = "abacabad"
    print(firstDuplicate(x))
    print(firstNotRepeatingCharacter(s))

    n= 5
    a= [4, 0, 1, -2, 3]

    print(mutateTheArray(n,a))



if __name__ == "__main__":
    main()



