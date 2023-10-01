def hello(user_name):
    print(f"Hi, {user_name}, How are you today?")

def pack(arg_0, arg_1, arg_2):
    return[arg_0, arg_1, arg_2]

def eat_lunch(Lunch_items):
    if len(Lunch_items) == 0:
        print("My lunchbox is empty")
    else:
        for index in range(len(Lunch_items)):
            if index == 0:
                print(f"First I eat {Lunch_items[index]}")
            else:
                print(f"Then I eat {Lunch_items[index]}")

print(pack("apples", "bananas", "fishes"))
hello("Roberto")

eat_lunch(pack("apples", "bananas", "fishes"))