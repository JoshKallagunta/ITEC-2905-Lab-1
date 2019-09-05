


classes = []
what_classes = int(input('How many classes are you taking this semester? '))

for number_of_classes in range(what_classes):
    each_class = input('What is the class name? ')
    classes.append(each_class)

print('\nHere are the classes you are taking this semester: ')

for each_class in classes:
    print(each_class)



