def binary_search(my_list: list, k: float, head_index: int, tail_index: int):
    if head_index >= tail_index:
        return "not found"
    index = head_index+(tail_index-head_index)//2
    if(k < my_list[index]):
        index -= 1
        index = binary_search(my_list, k, head_index, index)
        return index
    elif(k > my_list[index]):
        index += 1
        index = binary_search(my_list, k, index, tail_index)
        return index
    elif(k == my_list[index]):
        return index


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
index = binary_search(my_list, k, 0, len(my_list)-1)
print(index)
