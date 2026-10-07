def my_join(sep, lst):
    line = ""
    for elem in lst:
        line += elem + sep
    return line[:-len(sep)]
    


def test_1():
    assert my_join("-", ["a", "b", "c"]) == "a-b-c", "Программ неверно обработывает сепаратор"

def test_2():
    assert my_join("---", ["a", "b", "c"]) == "a---b--c", "Программа неверно работает с сепаратором из нескольких символов"