__author__ = 'William Kvaale'
# D E C O R A T O R S III


class Student:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property 
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    
    @fullname.setter
    def fullname(self, fullname):
        first, last = fullname.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Deleted name for", self.fullname)
        self.first, self.last = None, None

    @property
    def email(self): 
        return '{}.{}@ntnu.no'.format(self.first, self.last)

   

def main():
    # Init student
    stud1 = Student('William', 'Kvaale')
    stud1.first = 'Kissa'
    print(stud1.last)
    print(stud1.fullname)
    print(stud1.email)
    stud1.fullname = 'William Kvaale'
    print(stud1.fullname)
    del stud1.fullname


if __name__ == '__main__':
    main()