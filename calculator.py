import re

messange = {"msg_0": "Enter an equation",
            "msg_1": "Do you even know what numbers are? Stay focused!",
            "msg_2": "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "msg_3": "Yeah... division by zero. Smart move...",
            "msg_4": "Do you want to store the result? (y / n):",
            "msg_5": "Do you want to continue calculations? (y / n):",
            "msg_6": " ... lazy",
            "msg_7": " ... very lazy",
            "msg_8": " ... very, very lazy",
            "msg_9": "You are",
            "msg_10": "Are you sure? It is only one digit! (y / n)",
            "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)"}
memory = 0


def main():
    global calc
    print(messange["msg_0"])
    calc = input().split()
    check_equation()


def check_equation():
    if re.match(r"\d", calc[0]) and re.match(r"\d", calc[2]) and re.match(r"[-+*/]", calc[1]):
        check(float(calc[0]), calc[1], float(calc[2]))
        equation_solution()
    elif not re.match(r"\d", calc[0]) or not re.match(r"\d", calc[2]):
        if calc[0] == "M" and calc[2] == "M":
            calc[0] = memory
            calc[2] = memory
            check(float(calc[0]), calc[1], float(calc[2]))
            equation_solution()
        elif calc[2] == "M":
            calc[2] = memory
            check(float(calc[0]), calc[1], float(calc[2]))
            equation_solution()
        elif calc[0] == "M":
            calc[0] = memory
            check(float(calc[0]), calc[1], float(calc[2]))
            equation_solution()
        else:
            print(messange["msg_1"])
            main()
    elif not re.match(r"[-+*/]", calc[1]):
        print(messange["msg_2"])
        main()


def equation_solution():
    global result
    if calc[1] == "+":
        result = float(calc[0]) + float(calc[2])
        print(result)
        save_in_memory()
    elif calc[1] == "-":
        result = float(calc[0]) - float(calc[2])
        print(result)
        save_in_memory()
    elif calc[1] == "*":
        result = float(calc[0]) * float(calc[2])
        print(result)
        save_in_memory()
    elif calc[1] == "/" and calc[2] == 0:
        print(messange["msg_3"])
        main()
    elif calc[1] == "/" and calc[2] != 0:
        result = float(calc[0]) / float(calc[2])
        print(result)
        save_in_memory()


def save_in_memory():
    global memory
    answer = input(messange["msg_4"] + "\n")
    if answer == "y":
        last_block()
        memory = result
        continue_exit()
    elif answer == "n":
        continue_exit()


def continue_exit():
    answer = input(messange["msg_5"] + "\n")
    if answer == "y":
        main()
    elif answer == "n":
        exit()


def is_one_digit(v):
    if -10 < v < 10 and (v - int(v) == 0):
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v3):
        msg += messange["msg_6"]
    if (v1 == 1 or v3 == 1) and v2 == "*":
        msg += messange["msg_7"]
    if (v1 == 0 or v3 == 0) and any([v2 == "+", v2 == "-", v2 == "*"]):
        msg += messange["msg_8"]
    if msg != "":
        msg = messange["msg_9"] + msg
        print(msg)


def last_block():
    if is_one_digit(result):
        indx = 10
        while indx <= 12:
            answer = input(messange[f"msg_{indx}"] + "\n")
            if answer == "y":
                indx += 1
            elif answer == "n":
                continue_exit()


if __name__ == '__main__':
    main()
