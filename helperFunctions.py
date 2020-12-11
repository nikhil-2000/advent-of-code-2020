
"""
def isValid(condition,password):

    limits, letter = condition.split(" ")

    lower,upper = limits.split("-")
    lower,upper = int(lower), int(upper)

    if lower <= password.count(letter) <= upper:
        return True

    return False
"""
def isValid_part_two(condition,password):
    limits, letter = condition.split(" ")

    lower, upper = limits.split("-")
    lower, upper = int(lower)-1, int(upper)-1

    count = 0
    if password[lower] == letter:
        count += 1

    if password[upper] == letter:
        count += 1

    return count == 1

def extract(password_and_condition):
    c,p =  password_and_condition.split(":")
    return c,p.strip()

def product(l):
    t = 1
    for n in l:
        t = t * n

    return t

def get_dict_from_passport(passport):
    passport = passport.replace("\n"," ")
    d = {}

    for kv in passport.split(" "):
        k,v = kv.split(":")
        d[k] = v

    return d

valid_chars = list("".join([str(i) for i in range(10)]) + "abcdef")

def valid_field(key,value):
    if key == "byr" and 1920 <= int(value) <= 2002: return True
    elif key == "iyr" and 2010 <= int(value) <= 2020: return True
    elif key == "eyr" and 2020 <= int(value) <= 2030: return True
    elif key == "hgt":
        value = value.strip()
        if value[-2:] == "cm" and 150 <= int(value[:-2]) <= 193:
            return True

        if value[-2:] == "in" and 59 <= int(value[:-2]) <= 76:
            return True

    elif key == "hcl":
        if value[0] == "#" and set(value[1:]) <= set(valid_chars) and len(value) == 7:
            return True

    elif key == "ecl":
        valid = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in valid:
            return True

    elif key == "pid" and len(value) == 9 and value.isdigit():
        return True
    elif key == "cid":
        return True

    print(key,value)
    return False

def is_passport_valid(passport):
    keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

    passport_dict = get_dict_from_passport(passport)

    for k in keys:
        if not(k in passport_dict.keys()):
            return False

    for k in passport_dict.keys():
        if not(valid_field(k,passport_dict[k])):
            return False

    return True

def convert_FB(chars):
    binary = chars.replace("F","0").replace("B","1")
    return int(binary,base = 2)

def convert_RL(chars):
    binary = chars.replace("L","0").replace("R","1")
    return int(binary,base = 2)

def calc_seat_id(chars):
    return (convert_FB(chars[:7])*8) + convert_RL(chars[-3:])

def string_to_rule(line):
    line = line.replace(".", "")
    line = line.replace("bags","bag")
    line = line.replace("bag","")

    key,other_bags = line.split("contain")
    key = key.strip()
    if other_bags.strip() == "no other":
        return (key, {"":0})

    other_bags_l = other_bags.split(",")

    inside_bag = {}

    for string_bag in other_bags_l:
        split_string = string_bag.strip().split(" ")
        v,k = (split_string[0], " ".join(split_string[1:]))
        inside_bag[k] = v

    return key,inside_bag

def string_to_rule_2(line):
    line = line.replace(".", "")
    line = line.replace("bags", "bag")
    line = line.replace("bag", "")

    key, other_bags = line.split("contain")
    if other_bags.strip() == "no other":
        return None

    other_bags_l = other_bags.split(",")

    inside_bag = []

    for string_bag in other_bags_l:
        split_string = string_bag.strip().split(" ")
        v, k = (split_string[0], " ".join(split_string[1:]))
        inside_bag.append((k,key.strip()))


    return inside_bag

def count_bags(bag,rules):
    if "" in rules[bag].keys():
        return 1

    return 1 + sum([count_bags(k,rules) * int(rules[bag][k]) for k in rules[bag].keys()])

def run_code(code):
    # code = replace_last_jump(code)
    lines_to_executed = [(line,False) for line in code]

    acc = 0
    line_number = 0
    current_line = code[line_number]
    jmp_count = 0
    nop_count = 0
    while not (lines_to_executed[line_number][1]) and line_number < len(code):
        lines_to_executed[line_number] = (current_line,True)
        opcode,operand = current_line.split(" ")
        if opcode == "acc":
            acc += int(operand)
            line_number += 1
        elif opcode == "jmp":
            line_number += int(operand)
            jmp_count += 1
        elif opcode == "nop":
            line_number += 1
            nop_count += 1

        previous_line = current_line
        if line_number < len(code):
            current_line = code[line_number]
        else:
            current_line = "Terminated"
            print(acc)
            return True

        if lines_to_executed[line_number][1]:
            print(acc)
            return False

def isValid(preamble,number):

    for n in preamble:
        if (number - n) in preamble and number - n != n:
            return True

    return False


