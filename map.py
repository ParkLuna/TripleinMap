def triple_number(num):
    return num * 3
sample_list = [1, 2, 3, 4, 5, 6, 7]
result_list = list(map(triple_number, sample_list))
print("Triple of list numbers:")
print(result_list)
