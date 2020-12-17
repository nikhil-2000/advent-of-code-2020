
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

def find_permutations_of_adaptors(adaptors,current_perm = [0]):
    if max(current_perm) == max(adaptors):
        return (current_perm)

    next_perm_1,next_perm_2,next_perm_3= [],[],[]
    if current_perm[-1] + 1 in adaptors:
        next_perm = current_perm +  [current_perm[-1] + 1]
        next_perm_1 = find_permutations_of_adaptors(adaptors,next_perm)

    if current_perm[-1] + 2 in adaptors:
        next_perm = current_perm +  [current_perm[-1] + 2]
        next_perm_2 = find_permutations_of_adaptors(adaptors,next_perm)

    if current_perm[-1] + 3 in adaptors:
        next_perm = current_perm +  [current_perm[-1] + 3]
        next_perm_3 = find_permutations_of_adaptors(adaptors,next_perm)

    return next_perm_1 + next_perm_2 + next_perm_3

#W(N) = I(N-1 in A)W(N-1) + I(N-2 in A)W(N-2) + I(N-3 in A)W(N-3)
#W(1) = 1
def dynamic_find_permutations(adaptors,n,memory = {}):

    if n < 0:
        return 0
    if 0 <= n <= 1:
        return 1

    if n not in memory.keys():
        total = 0
        for i in range(1,4):
            indicator,ways = int(n-i in adaptors), dynamic_find_permutations(adaptors,n-i)
            total += indicator * ways

        memory[n] = total

    print(memory)


    return memory[n]

def is_seat_occupied(chosen_row, chosen_seat_on_row, seating_arrangement):
    if seating_arrangement[chosen_row][chosen_seat_on_row] == ".": return None

    w,h = len(seating_arrangement[0]),len(seating_arrangement)
    occupied_count = 0

    for x in range(-1,2):
        for y in range(-1,2):

            if 0 <= chosen_seat_on_row +x < w and 0 <= chosen_row +y < h and not (x == 0 and y == 0):
                seat = seating_arrangement[chosen_row + y][chosen_seat_on_row + x]
                occupied_count += int(seat == "#")

    if occupied_count >= 4 and seating_arrangement[chosen_row][chosen_seat_on_row] == "#":
        return False
    elif occupied_count == 0 and seating_arrangement[chosen_row][chosen_seat_on_row] == "L":
        return True
    else:
        return None

def valid_coord(coords, array_2d):
    x,y = coords
    return 0 <= x < len(array_2d) and 0 <= y < len(array_2d[0])

def get_closest_seat(row,col,seating_arrangement,y_dir,x_dir):
    current_coord = [row + x_dir, col + y_dir]
    if valid_coord(current_coord,seating_arrangement):
        seat = seating_arrangement[current_coord[0]][current_coord[1]]
        while seat == ".":
            x,y = current_coord
            current_coord = [x + x_dir, y + y_dir]
            if not valid_coord(current_coord,seating_arrangement):
                return "."
            else:
                seat = seating_arrangement[current_coord[0]][current_coord[1]]
        return seat

    return ""


def is_seat_occupied_part_2(chosen_row,chosen_seat_on_row, seating_arrangment):
    left_seat = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, -1, 0)
    right_seat = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, 1, 0)
    down_seat = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, 0, 1)
    up_seat = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, 0, -1)

    l_b_diag = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, -1, 1)
    r_b_diag = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, 1, 1)
    l_u_diag = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, 1, -1)
    r_u_diag = get_closest_seat(chosen_row, chosen_seat_on_row, seating_arrangment, -1, -1)

    visible_seats = [left_seat,right_seat,down_seat,up_seat,l_b_diag,r_b_diag,l_u_diag,r_u_diag]
    seat = seating_arrangment[chosen_row][chosen_seat_on_row]
    occupied_count = visible_seats.count("#")


    if occupied_count >= 5 and seat == "#":
        return False
    elif occupied_count == 0 and seat == "L":
        return True
    else:
        return None


def update_seats(seating):
    before_seating = seating
    after_seating = [[0 for i in range(len(seating[0]))] for i in range(len(seating))]
    for y, row in enumerate(seating):
        for x, col in enumerate(row):

            is_occupied = is_seat_occupied(y, x, before_seating)
            if is_occupied is None:
                after_seating[y][x] = before_seating[y][x]
            elif is_occupied:
                after_seating[y][x] = "#"
            elif not is_occupied:
                after_seating[y][x] = "L"

    return after_seating

def update_seats_p2(seating):
    before_seating = seating
    after_seating = [[0 for i in range(len(seating[0]))] for i in range(len(seating))]
    for y, row in enumerate(seating):
        for x, col in enumerate(row):

            is_occupied = is_seat_occupied_part_2(y, x, before_seating)
            if is_occupied is None:
                after_seating[y][x] = before_seating[y][x]
            elif is_occupied:
                after_seating[y][x] = "#"
            elif not is_occupied:
                after_seating[y][x] = "L"

    return after_seating


def apply_mask(mask,value):
    value = str(bin(value))[2:]
    while len(value) < len(mask):
        value = "0" + value

    value = list(value)
    for i,bit in enumerate(mask):
        if bit == "X":
            pass
        elif bit == "1":
            value[i] = "1"
        elif bit == "0":
            value[i] = "0"

    final = "".join(value)
    return int(final,base=2)

def apply_mask_2(mask,key):
    key = str(bin(key))[2:]

    key = pad(key,len(mask))

    key = list(key)
    for i, bit in enumerate(mask):
        if bit == "X":
            key[i] = "X"
        elif bit == "1":
            key[i] = "1"
        elif bit == "0":
            pass

    potential_keys = gen_perms(key)
    return [int(k,base=2) for k in potential_keys]

    # final = "".join(value)
    # return int(final, base=2)

def pad(s,digits):
    while len(s) < digits:
        s = "0" + s

    return s

def insert_bits(key,bits):
    i = 0
    new_key = ""
    for idx,b in enumerate(key):
        if i < len(bits): current_bit = bits[i]
        if b == "X":
            new_key += current_bit
            i += 1
        else:
            new_key += b
    return new_key

def gen_perms(key):
    p = key.count("X")
    n_of_perms = 2**p

    all_bits = [pad(str(bin(n))[2:],p) for n in range(n_of_perms)]
    perms = [insert_bits(key,bits) for bits in all_bits]
    return perms

def find_previous_occurence(n, array):
    i = len(array) - 1
    while i >= 0:
        if array[i] == n:
            return i

        i = i -1

    return i

def print_seating(seating):
    for r in seating:
        print(" ".join(r))

def convert_to_compass(opcode,current_direction):
    if opcode == "F":
        idx = current_direction/90

def remove_empty(l):
    return [e for e in l if e.strip() != ""]

def rules_dict(string_rules):
    rules = {}
    for str_rule in string_rules:
        key,values = str_rule.split(":")
        values = values.split(" or ")
        bounds = []
        for bound in values:
            bound = list(map(int,bound.strip().split("-")))
            bounds.append(bound)

        rules[key] = bounds

    return rules

def convert_to_ticket(line):
    return list(map(int,line.replace("\n","").split(",")))

def within_bounds(value,bounds):

    for bound in bounds:
        l,h = bound
        if l <= value <= h:
            return True

    return False

