# binary search with first occurrence
def modified_binary_search(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2
        if theValues[mid] == target:
            if mid != 0 and theValues[mid - 1] == target:
                high = mid
            else:
                return mid
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low


# find negatives in a list
def negatives_finder(theValues):
    negatives = []
    for i in range(len(theValues)):
        if theValues[i] < 0:
            negatives.append(theValues[i])
    return negatives

# returns True if the first list is a subset of the second one
def is_subset_of(first_list, second_list):
    i = 0
    if len(second_list) <= len(first_list):
        for j in range(len(first_list)):
            if first_list[j] == second_list[i]:
                i += 1
            if len(second_list) == i:
                return True
        return False


# returns a list containing the intersection between the two lists
def intersect(first_list, second_list):
    i = 0
    intersection = []

    first = first_list
    second = second_list

    if len(first_list) < len(second_list):
        first = second_list
        second = first_list
        
    for j in range(len(first)):
        if first[j] > second[i]:
            i += 1
        if first[j] == second[i]:
            intersection.append(first[j])
            i += 1
        if i == len(second):
            break
    return intersection


# returns a list containing the difference between the two lists.
def difference(first_list, second_list):
    index = 0
    differences = []
    first = first_list
    second = second_list

    if len(first_list) < len(second_list):
        first = second_list
        second = first_list

    for i in range(len(first)):
        if first[i] < second[index]:
            differences.append(first[i])
        elif first[i] > second[index]:
            differences.append(second[index])
            index += 1
        if first[i] == second[index]:
            index += 1
        if index == len(second):
            return differences + first[i:]
    return differences + second[index:]