from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

def main():
    print()
    alex = Student('Alex', '12345', 4.0)
    print(alex.name)
    print(alex.school_id)
    print(alex.gpa)
    print(alex)
    print()

if __name__=="__main__": 
    main() 