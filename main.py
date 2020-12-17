
from helperFunctions import *

def day_1():
    numbers = open("data/numbers.txt", "r").read()

    all_numbers = set([int(n) for n in numbers.split("\n")])

    def sum_to_target(target,set_of_nums):
        for n in set_of_nums:
            if (target - n) in set_of_nums:
                return (n, target - n)

        return (0,0)


    print(sum_to_target(2020,all_numbers))

    for n in all_numbers:

        m,o = sum_to_target(2020-n, all_numbers)
        if m + o > 0:
            print(n,m,o)

def day_2():
    file_content = open("data/day2_input.txt", "r").read()

    passwords_with_conditions = file_content.split("\n")
    valid_passwords = 0

    for password_condition in passwords_with_conditions:
        condition,password = extract(password_condition)

        if isValid_part_two(condition,password):
            valid_passwords += 1

    print(valid_passwords)

def day_3(x_change,y_change):
    file_content = open("data/trees.txt", "r").read()

    trees = file_content.split("\n")
    w,h = len(trees[0]),len(trees)
    x,y = 0,0
    trees_hit = 0

    while y < h:
        x = (x + x_change) % w
        y += y_change

        if y >= h:
            return trees_hit

        if trees[y][x] == "#":
            trees_hit += 1

def day_3_part_2():
    paths = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    trees_hit = []
    for p in paths:
        trees_hit.append(day_3(p[0],p[1]))

    print(trees_hit)
    return product(trees_hit)

def day_4():
    f = open("data/passport.txt", "r")
    file_content = f.read()
    f.close()

    all_passports = file_content.split("\n\n")
    c = 0

    for passport in all_passports:
        if is_passport_valid(passport):
            c += 1

    print(c)

def day_5():
    f = open("data/boarding_passes.txt", "r")
    passes = f.read().split("\n")
    f.close()
    max_id = 0
    for boarding_pass in passes:
        current_id = calc_seat_id(boarding_pass)
        if current_id >= max_id:
            max_id = current_id

    print(max_id)

def day_5_part_two():
    f = open("data/boarding_passes.txt", "r")
    passes = f.read().split("\n")
    f.close()

    unused_ids = [i for i in range(817)]

    for boarding_pass in passes:
        current_id = calc_seat_id(boarding_pass)
        unused_ids.remove(current_id)

    print(unused_ids)

def day_6():
    f = open("data/day_6_data.txt", "r")
    answers = f.read().split("\n\n")
    f.close()

    groups = []
    print(answers)
    for answer in answers:

        chars = set(answer)
        questions_answered = len(chars)
        if "\n" in chars:
            questions_answered -= 1

        groups.append(questions_answered)

    print(sum(groups))

def day_6_part_two():
    f = open("data/day_6_data.txt", "r")
    answers = f.read().split("\n\n")
    f.close()

    groups = []


    for answer_group in answers:
        individual_answers = answer_group.split("\n")
        count = 0
        print(individual_answers)
        print()
        for response in individual_answers[0]:
            in_other_answers = all([response in a for a in individual_answers[1:]])
            if in_other_answers:
                count += 1

        groups.append(count)

    print(groups)
    print(sum(groups))

def day_7():
    """
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
    :return:
    """

    f = open("data/rules.txt", "r")
    string_rules = f.read().split("\n")
    f.close()
    rules = {}

    count = 0

    for line in string_rules:
        k_to_v = string_to_rule_2(line)
        if k_to_v != None:
            for k,v in k_to_v:
                if k in rules.keys():
                    rules[k].append(v)
                else:
                    rules[k] = [v]


    target_bag = "shiny gold"

    parent_bags = rules[target_bag]
    colours = set(parent_bags)
    count = len(parent_bags)
    while len(parent_bags) > 0:
        print(parent_bags)
        current_colour = parent_bags.pop()
        if current_colour in rules.keys():
            parent_bags.extend(rules[current_colour])
            colours = colours.union(rules[current_colour])



    print(len(colours))
    print(colours)

def day_7_part_two():
    f = open("data/rules.txt", "r")
    string_rules = f.read().split("\n")
    f.close()
    rules = {}

    for line in string_rules:
        k,v = string_to_rule(line)
        rules[k] = v

    print(rules)
    target_bag = "shiny gold"
    child_bags = count_bags(target_bag,rules) - 1

    print(child_bags)

def day_8():
    f = open("data\programs.txt", "r")
    code = f.read().split("\n")
    f.close()
    i = 0
    terminated = False
    while not terminated:
        changed_code = [c for c in code]
        if "jmp" in code[i]:
            changed_code[i] = changed_code[i].replace("jmp","nop")
            terminated = run_code(changed_code)

        elif "nop" in code[i]:
            changed_code[i] = changed_code[i].replace("nop","jmp")
            terminated = run_code(changed_code)

        i += 1

    print(terminated)

def day_9():
    f = open("data/xmas_error.txt","r")
    numbers = f.read().split("\n")
    numbers = list(map(int,numbers))
    f.close()
    preamble_size = 25
    i = 0
    number_valid = True
    while number_valid:
        preamble = numbers[i: i+preamble_size]
        number_to_check = numbers[i+preamble_size]
        number_valid = isValid(preamble,number_to_check)
        i+=1

    invalid_num = number_to_check
    start,end = 0,1
    contig_set = numbers[start:end]
    while sum(contig_set) != invalid_num or len(contig_set) < 2:
        print(contig_set,start,end)
        sum_of_set = sum(contig_set)
        if  sum_of_set < number_to_check:
            end += 1
        elif sum_of_set > number_to_check:
            start += 1

        contig_set = numbers[start:end]

    print(min(contig_set) + max(contig_set))

def day_10():
    f = open("data/joltage_adaptors","r")
    adaptors = f.read().split("\n")
    f.close()

    adaptors = list(map(int,adaptors))
    sorted_adaptors = sorted(adaptors)
    sorted_adaptors.insert(0,0)
    sorted_adaptors.append(max(sorted_adaptors) + 3)
    print(sorted_adaptors)
    differences = {1:0,2:0,3:0}

    for i,adaptor in enumerate(sorted_adaptors[:-1]):
        next_adaptor = sorted_adaptors[i+1]
        differences[next_adaptor - adaptor] += 1

    print(differences[1] * differences[3])

    """
    Part 2
    Create a tree picking 1,2 or 3 each time if available, some type of recursive call I think
    """

def day_10_part_2():
    f = open("data/joltage_adaptors", "r")
    adaptors = f.read().split("\n")
    f.close()

    adaptors = list(map(int, adaptors))
    sorted_adaptors = sorted(adaptors)
    sorted_adaptors.insert(0, 0)
    sorted_adaptors.append(max(adaptors)+3)
    print(sorted_adaptors)

    all_perms = dynamic_find_permutations(sorted_adaptors,max(sorted_adaptors))
    print(all_perms)

def day_11():
    f = open("data/seating_plan.txt","r")
    seating = f.read().split("\n")
    seating = [list(row) for row in seating]
    f.close()

    stable = False
    before_seating = seating
    while not stable:
        new_seating = update_seats(before_seating)
        stable = before_seating == new_seating
        before_seating = new_seating

    print(sum(row.count("#") for row in new_seating))

def day_11_p2():
    f = open("data/seating_plan.txt", "r")
    seating = f.read().split("\n")
    seating = [list(row) for row in seating]
    f.close()

    stable = False
    before_seating = seating
    while not stable:
        new_seating = update_seats_p2(before_seating)
        stable = before_seating == new_seating
        before_seating = new_seating

    print(sum(row.count("#") for row in new_seating))
    print_seating(new_seating)

def day_12():
    f = open("data/ship_directions.txt")
    instructions = f.read().split("\n")
    f.close()

    position = [0,0]
    direction = 90

    directions = ["N","E","S","W"]

    for instruction in instructions:
        opcode,operand = instruction[0],int(instruction[1:])
        if opcode == "F":
            idx = int(direction/90)
            opcode = directions[idx]



        if opcode == "N": position[1] += operand
        if opcode == "E": position[0] += operand
        if opcode == "S": position[1] -= operand
        if opcode == "W": position[0] -= operand

        if opcode == "L": direction -= operand
        if opcode == "R": direction += operand

        direction = direction % 360

    print(sum([abs(p) for p in position]))

def day_13():
    import math
    f = open("data/bus_schedule.txt")
    f.close()
    min_departure_time, buses = f.read().split("\n")
    min_departure_time = int(min_departure_time)
    buses = [int(id) for id in buses.split(",") if id.isdigit()]
    best_times = []

    for bus in buses:
        best_time = math.ceil(min_departure_time/bus) * bus
        best_times.append(best_time)

    idx = best_times.index(min(best_times))
    diff = best_times[idx] - min_departure_time
    print(buses[idx] * diff)

def day_14():
    f = open("data/day_14.txt")
    data = f.read().split("\n")
    f.close()

    mem = {}

    for line in data:
        lhs,rhs = line.split("=")
        if "mask" in lhs:
            mask = rhs.strip()

        if "mem" in lhs:
            key = lhs.split("[")[1]
            value = apply_mask(mask, int(rhs))
            mem[key] = value

    print(mem)
    print(sum(mem.values()))

def day_14_part_two():
    f = open("data/day_14.txt")
    data = f.read().split("\n")
    f.close()

    mem = {}

    for line in data:
        lhs, rhs = line.split("=")
        if "mask" in lhs:
            mask = rhs.strip()

        if "mem" in lhs:
            lhs = lhs.replace("[", " ").replace("]", " ")
            key = lhs.split(" ")[1]
            keys = apply_mask_2(mask, int(key))
            value = int(rhs)
            for k in keys:
                mem[k] = value

    print(mem)
    print(sum(mem.values()))

def day_15():
    import time
    f = open("data/elves_game.txt")
    numbers = f.read().split(",")
    f.close()
    rounds = list(map(int,numbers))
    mem = {}
    for i,k in enumerate(rounds[:-1]): mem[k] = i
    n_of_rounds = len(rounds)
    while n_of_rounds < 30000000:
        last_number = rounds[-1]
        idx = mem.get(last_number,-1)#find_previous_occurence(last_number,rounds[:-1])
        if idx == -1:
            rounds.append(0)
        else:
            rounds.append(n_of_rounds - (idx+1))

        mem[last_number] = n_of_rounds - 1

        n_of_rounds = n_of_rounds + 1
        # print(n_of_rounds,last_number,n_of_rounds-idx-1,mem)


    print(rounds[-1])

def day_16():
    f = open("data/train_tickets.txt")
    data = f.read()

    rules,rest = data.split("your ticket:")
    your_ticket,other_tickets = rest.split("nearby tickets:")


    rules = rules_dict(remove_empty(rules.split("\n")))
    all_bounds = []
    for bounds in rules.values():
        all_bounds = all_bounds + bounds


    your_ticket = convert_to_ticket(your_ticket)
    other_tickets = remove_empty(other_tickets.split("\n"))
    other_tickets = list(map(convert_to_ticket,other_tickets))

    invalid_values = []
    valid_tickets = other_tickets.copy()
    for ticket in other_tickets:
        for value in ticket:
            if not within_bounds(value,all_bounds):
                invalid_values.append(value)
                valid_tickets.remove(ticket)

    print(valid_tickets)

day_16()