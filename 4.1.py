lst=[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
non_zeros = [x for x in lst if x != 0]
zeros = [0] * (len(lst) - len(non_zeros))
print(non_zeros + zeros)
