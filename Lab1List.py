number_list = [2,4,6]
number_added_list = [n + 1 for n in number_list]
print(number_added_list)

remove_zero_list = [0,3,4,0,22,1]
removing_zeros = [n for n in remove_zero_list if n > 0]
print(removing_zeros)

classes_list = ['ITEC 2536', 'BTEC 1010', 'ITEC 2905']
filter_classes_list = [itec for itec in classes_list if 'ITEC' in itec]
print(filter_classes_list)