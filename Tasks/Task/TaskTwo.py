def decorate(fn):
    print("*****************")
    print(fn())
    print("*****************")

@decorate
def show_name():
    return "chichi"
#if u want to decorate the function

show_name("chichi")