#Exercise2

def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas:(e.g. 5, 67, 32)")

def get_user_input():
    print("get_user_input")
    user_input =input("Enter a list of numbers: ")
    num_list = user_input.split(",")
    new_list = []
    for i in num_list:
        new_list.append(float(i))
    return new_list


def calc_average(list_input):
    print("calc_Average")

def find_min_max(list_input):
    print("find_min_max")

def sort_temperature(list_input):
    print("sorting_temperature")

def calc_median_temperature(list_input):
    print("calc_median_temperature")