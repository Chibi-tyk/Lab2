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
    print (f"This is your new list: {new_list}")
    return new_list


def calc_average(new_list):
    print("calc_Average")
    avg = sum(new_list) / len(new_list)
    print(f"Average value: {avg}")
    return avg

def min_max_temp(new_list):
    print("find_min_max")
    new_list.sort()
    print(f"after sorting {new_list}")
    return [new_list[0], new_list[-1]]

def sort_temperature(new_list):
    print("sorting_temperature")
    new_list.sort()
    print(f"after sorting {new_list}")


def median_temperature(new_list):
    print("calc_median_temperature")
    total = len(new_list)

    if total % 2 == 0 :
        num1 = new_list[total // 2 - 1]
        num2 = new_list[total //2]
        median_temp = (num1+num2) /2
    else:
        median_temp = new_list[total //2]
    print(f"Your median temperature is {median_temp}")
    return median_temp

def main():
    print("Lab2- Exercise 3")
    display_main_menu()
    num_list = get_user_input()
    avg = calc_average(num_list)
    min_max_values= min_max_temp(num_list)
    print(f"Minimum and maximum values: {min_max_values}")
    median_temp = median_temperature(num_list)

if __name__ == "__main__":
    main()