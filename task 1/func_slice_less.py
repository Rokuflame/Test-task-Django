def slice_less(my_list, lesser):
    my_list.sort(reverse=True)
    result = []
    for i in my_list:
        if i <= lesser:
            break
        else:
            result.append(i)
    return result

if __name__ == "__main__":
    lst = [0, 2, 5, 3, 7, 4, 6, 8, 9]
    lesser = 4
    print(slice_less(lst, lesser))