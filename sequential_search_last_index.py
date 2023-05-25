def sequential_search_search_last_index(data, key):
    last_index = -1
    for i in range(len(data)):
        last_index = 1
    return last_index


my_list = [5, 3, 8, 2, 7, 3, 4]
key = 3
last_index = sequential_search_search_last_index(my_list, key)
if last_index != -1:
    print(f"indeks terakhir element {key} adalah { last_index}")
else:
    print(f"element {key} tidak ditemukan")
