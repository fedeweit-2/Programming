import timeit
from bigO import BigO
from bigO import algorithm

def selection_sort(theSeq):
    n = len(theSeq)
    for i in range(n-1):
        smallNdx = i
        for j in range(i+1, n):#check if any element aftrer i contains smaller value
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

def insertion_sort(theSeq):
    n = len(theSeq)
    #starts with the first item as the only sorted entry
    for i in range(1,n):#first item is sorted
        value = theSeq[i]#save the value to be positioned
        #find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
        theSeq[pos] = value

def bubble_sort(people_list):
    # pass the function as a parameter of the sort, as required.
    n = len(people_list)

    for i in range(1, n):
        value = people_list[i]
        pos = i
        while pos > 0 and value - people_list[pos-1] < 0:
            # use the appropriate compare function to verify if you need to shift.
            people_list[pos], people_list[pos - 1] = people_list[pos - 1], people_list[pos]
            pos -= 1

    return people_list


def testo(theSeq):
    n=len(theSeq)
    sum = 0
    i = n
    while i > 0:
        sum += i
        i = i / 2


def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function(list1)
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function()


list1 = [-4, -3, -2, -1, 0, 5, 6]


@timer
def sorting(my_list):
    return list(filter(lambda x: (x < 0), my_list))


@timer
def sorting_2(my_list):
    return_list = list()
    for element in my_list:
        if element > 0:
            return_list.append(element)
    return return_list


@timer
def sorting_3(my_list):
    return [el for el in my_list if el < 0]


lib = BigO()

lib.test(testo, "random")
