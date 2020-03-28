class Student:
    age = 18
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


    def on_honer_role(self):
        if self.gpa >=3.5:
            return True
        else:
            return False


