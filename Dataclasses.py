from dataclasses import dataclass

@dataclass
class Student: 
    name: str
    college_id: int 
    gpa: float

def main():

    josh = Student('Josh', 1233, 3.2)
    alice = Student('Alice', 2144, 3.3)

    print(josh)
    print(alice)

main()