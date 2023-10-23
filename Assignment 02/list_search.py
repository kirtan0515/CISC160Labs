#  def list_search(sequence, value):
#     indices = []
#     for i, item in enumerate(sequence):
#         if item == value:
#             indices.append(i)
#     return indices
#
#
# print(list_search([1, 'A', 3, 5, 7, 'A'], 'A'))
# print(list_search([1, 'A', 3, 5, 7, 'A'], 3))
# print(list_search([1, 'A', 3, 5, 7, 'A'], 'zebra'))


# def add3D(arr1, arr2):
#     new_arr = []
#     for i in range(len(arr1)):
#         sub_arr = []
#         for j in range(len(arr1[i])):
#             inner_arr = []
#             for k in range(len(arr1[i][j])):
#                 sum_val = arr1[i][j][k] + arr2[i][j][k]
#                 inner_arr.append(sum_val)
#             sub_arr.append(inner_arr)
#         new_arr.append(sub_arr)
#     return new_arr

# array_input = [1, 2, 3, 4, 5, 6, 7]
# array1 = []
# array2 = []
#
# for i in range(len(array_input)):
#     if i % 2 == 0:
#         array1.append(array_input[i])
#     else:
#         array2.append(array_input[i])
#
# print("array1:", array1)
# print("array2:", array2)
def removeAll(array, count, value):
    newCount = 0

    for i in range(count):
        if array[i] != value:
            array[newCount] = array[i]
            newCount += 1

    while newCount < count:
        array[newCount] = None
        newCount += 1

    return newCount


data = [1, 2, 3, 2, 4, 2, 5]
newCount = removeAll(data, 7, 2)
print(data)
print(newCount)

