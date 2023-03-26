def hello_name(user_name):
    print("Hello, " + user_name.title() + "!")

    print("Jason")


def first_odds():
    for number in range (1, 101):
        if number % 2 == 0:
            continue
        else:
            print(number)



def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
            return max
        print(max_num_in_list)



def is_leap_year(a_year): 
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 ==0):
        return True
    else:
        return False
    

 def is_consecutive(a_list):