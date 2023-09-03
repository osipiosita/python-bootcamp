def min_index(mylist):
    smallest = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] < smallest:
            smallest = mylist[i]
            ind = mylist.index(smallest)
    return ind
print(min_index([40,50,10,90,100,5, 20, 2, 45]))

def max_index(mylist):
    largest = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] > largest:
            largest = mylist[i]
            ind = mylist.index(largest)
    return ind
print(max_index([40,50,10,90,100,5, 20, 2, 45]))

def smaller_indices(list1, list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            if list1[i] < list2[i]:
                list3.append(i)
        return list3
    else:
        print('lists MUST be of equal length!')
print(smaller_indices([40,50,10,90,100,70], [60,20,19,95,30,20]))


def pairwise_product(list1,list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            product = list1[i] * list2[i]
            list3.append(product)
        return list3
    else:
        print('lists MUST be of equal length!')
print(pairwise_product([40,50,10,90], [6,2,2,5]))


def pairwise_ratio(list1,list2):
    list3 = []
    if len(list1) == len(list2):
        for i in range(len(list1)):
            ratio = list1[i] / list2[i]
            list3.append(round(ratio,3))
        return list3
    else:
        print('lists MUST be of equal length!')
print(pairwise_ratio([40,50,10,90], [60,20,19,95]))