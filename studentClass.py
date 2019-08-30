class Student:
    def __init__(self, name, college_id):
        self.name = name 
        self.college_id = college_id
    def _str_(self):
        return f'Name: {self.name}, id: {self.college_id}'


def main():
    josh = Student('Josh', 'nq6647xv')
    bob = Student('Bob', 'hu8892bv')

    print(josh.name)
    print(bob.college_id)

    
main()

