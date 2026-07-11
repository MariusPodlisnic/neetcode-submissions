def add_two_numbers() -> int:
    line = input()
    line_list = [int(i) for i in line.split(",")]
    sum = 0
    for x in line_list:
        sum += x
    return sum

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
