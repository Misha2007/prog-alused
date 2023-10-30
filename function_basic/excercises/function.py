"""Function examples."""


def func():
    print("I´m inside the function")

func()


def my_name_is(name: str) -> str:
    print(f"My name is {name}")

my_name_is(Misha)


def sum_six(num: int) -> int:
    return 6 + num

sum_six(5)


def sum_numbers(a, b: int) -> int:
    return a + b

sum_numbers(10,8)


def usd_to_eur(a):
    return a * 0.8

usd_to_eur(10)