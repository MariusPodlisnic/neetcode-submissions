from typing import List

def read_integers() -> List[int]:
    line = input()
    line_list = [int(i) for i in line.split(",")]
    return line_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())