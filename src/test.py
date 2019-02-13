class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self._score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student("Zero", 32)
print(bart)

if __name__ == "__main__":
    jump = True
    number = 1
    while jump:
        if number < 4:
            number += 1
        else:
            pass
    print("结束")