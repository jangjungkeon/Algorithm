import sys


def greedy(String):
    sum_string = 0
    idx = String.find('-')
    check = False
    val = ""
    for i in range(len(String)):
        if String[i] == '+' or String[i] == '-':
            check = True
        else:
            if check:
                if i <= idx+1:
                    sum_string += int(val)
                else:
                    sum_string -= int(val)
                val = ""
                check = False
            val += String[i]
    return sum_string


if __name__ == "__main__":
    String = sys.stdin.readline().strip()
    String += "-0"
    print(greedy(String))


