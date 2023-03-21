"""

"""

# ---------- Question 7 ----------
print("Question 7:")


def check_zero(func):

    def wrap(num1, num2):
        if num2 == 0:
            return "Undefined"

        return func(num1, num2)

    return wrap


def div(a, b):
    return a/b


div = check_zero(div)

print(div(div(4, 2), div(0, 10)))

# ---------- Question 8 ----------
print("Question 8")


def func1(func):

        def inner_func(*args, **kwargs):
            li = [pow(x, 2) for x in args]
            return func(li, **kwargs)

        return inner_func


@func1
def func2(li):
    return li


@func1
def func3(li):
    return [pow(x, 0.5) for x in li]


def func4():
    print(func2(1, 2, 3, 4), func3(1, 2), func2(1, 2), func3(1, 2, 3, 4))


func4()


# ---------- Question 10 ----------
print("Question 10")


def ordi():
    print("Ordinary")


print(ordi)

ordi()




