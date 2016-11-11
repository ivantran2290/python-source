
from utils import common

def print_hello_world():
    """
    Return hello world string
    """
    print("hello wolrd!!!")

def indentation():
    """
    Return "var is 1" if var is set 1
    """
    var = 1
    if var == 1:
        print("var is 1")

def variables_and_type():
    """
    Return some value for testing variables and type in python
    """
    # Number
    myint = 7
    myloat = 7.0
    myloat = float(7)

    # String
    mystring = 'hello'
    mystring = "hello"
    mystring = "Don't worry about apostrophes"

    one = 1
    two = 2
    three = one + two

    hello = "hello"
    world = "world"
    helloworld = hello + common.space + world

    print(myint)
    print(myloat)
    print(mystring + common.space + str(myloat))
    print(three)
    print(helloworld)
    print(str(one) + str(two) + hello)

    mystring = "hello"
    myfloat = 10.0
    myint = 20

    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %d" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)

def lists():
    """
    Return some value for testing list in python
    """
    mylist = []
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    print(mylist[0]) # prints 1
    print(mylist[1]) # prints 2
    print(mylist[2]) # prints 3

    # prints out 1,2,3
    for item in mylist:
        print(item)

    mylist = [1, 2, 3]
    print(mylist[2])

    numbers = [1, 2, 3]
    strings = ['1', '2', '3']
    names = ["John", "Eric", "Jessica"]

    # write your code here
    second_name = names[1]


    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)

def basic_operators():
    """
    Return some value for testing arithmetic operators in python
    """

    # cong tru nhan chia
    number = 1 + 2 * 3 / 4.0
    print(number)

    # chia lay du
    remainder = 12 % 3
    print(remainder)

    # binh phuong
    squared = 7 ** 2
    print(squared)

    # lap phuong
    cubed = 2 ** 3
    print(cubed)

    # 10 lan hello
    lotsofhellos = "hello" * 10
    print(lotsofhellos)

    # thuc hien toan tu voi list
    even_numbers = [2, 4, 6, 8]
    odd_numbers = [1, 3, 5, 7]
    all_numbers = odd_numbers + even_numbers
    print(all_numbers)

    # cap so nhan mang hien tai
    print([1, 2, 3] * 3)

    x_obj = object()
    y_obj = object()

    x_list = [x_obj, x_obj, x_obj, x_obj, y_obj, x_obj, x_obj, x_obj, x_obj, x_obj]
    y_list = [y_obj, y_obj, y_obj, y_obj, x_obj, y_obj, y_obj, y_obj, y_obj, y_obj]
    big_list = x_list + y_list

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    # testing code
    if x_list.count(x_obj) == 10 and y_list.count(y_obj) == 10:
        print("Almost there...")
    if big_list.count(x_obj) == 10 and big_list.count(y_obj) == 10:
        print("Great!")

print_hello_world()
indentation()
variables_and_type()
lists()
basic_operators()
