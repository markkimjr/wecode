def even_num():
    my_list = []
    for i in range(1,51):
        if i % 2 == 0:
            my_list.append(i)
    return set(my_list)

