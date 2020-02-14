class Student:
    def __init__(self, name, id,dept, gpa, is_graduated):
        self.name = name
        self.id = id
        self.dept = dept
        self.gpa = gpa
        self.is_graduated = is_graduated

    def is_good_student(self):
        if self.gpa >=3.5:
            return True
        else:
            return False