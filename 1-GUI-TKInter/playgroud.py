def add(*args):
    total=0
    temp = args[0]
    for num in args:
        total +=num
    return total


print(add(1,2,3,4,5,6,7,8,1234))


def student_marks(** kwargs):

    for (key, value) in kwargs.items():
        print(key, value)

    print(kwargs["Nithin"])


student_marks(Nithin=99, Newman=80)


def print_name(name, age):
    print(f"Name: {name} and Age: {age}")

names={"name":"Newman", "age": 52}

print_name(**names)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        ##If user doesn't pass the argument then get return none so it will throw error
        self.make = kw.get["make"]
        self.model = kw.get["model"]

car =Car(make="Honda", model="Oddesy")
