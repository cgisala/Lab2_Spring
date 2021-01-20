# This program deal with dataclasses

from dataclasses import dataclass

# no boiler plate like self.name, self.school, or self.gpa
# no __init__ or __str__
# much easier to create a class it is just going to be used to store data
@dataclass
class Student: 
    name: str
    school_id: str
    gpa: float

def main():
    print()
    alex = Student('Alex', '12345', 4.0)  # must be entered in the same order as the arangement of the variables in the class.
    print(alex.name)
    print(alex.school_id)
    print(alex.gpa)
    print(alex)
    print()

    sam = Student('Sam', 'qwerty', 3.7)
    print(sam.name)
    print(sam.school_id)
    print(sam.gpa)
    print(sam)

if __name__=="__main__": 
    main() 