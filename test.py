class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self._score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student("Zero", 32)
print(bart)
