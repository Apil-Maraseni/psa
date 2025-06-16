# This function takes keyword arguments and returns them as a dictionary.
# create the function
def full_name(**kwargs):
    # print the argument
    for key, value in kwargs.items():
        return kwargs

first = input()
last = input()

print(full_name(first = first, last = last))