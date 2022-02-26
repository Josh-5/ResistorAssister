import sys

# Read the resistor values into an array from the input file
with open('resistors.txt') as resistorFile:
    singleResistors = []
    for line in resistorFile:
        singleResistors.append([int(line), line])


rTarget = sys.argv[0]
rCount = sys.argv[1]
rClosest = []


def series(r1, r2):
    return r1 + r2


def parallel(r1, r2):
    return (r1 * r2)/(r1 + r2)


def find_closest(r1_list, r2_list):
    closest = [series(r1_list[0], r2_list[0]), str(r1_list[0]) + ' + ' + str(r2_list)]
    global rTarget
    for r1 in range(len(r1_list)):
        for r2 in range(len(r2_list)):
            r1Val = r1[1]
            r2Val = r2[1]
            if (series(r1Val, r2Val) - rTarget) < (closest[0] - rTarget):
                closest[0] = series(r1Val, r2Val)
                closest[1] = '(' + str(r1Val) + ' + ' + str(r2Val) + ')'
            if (parallel(r1, r2) - rTarget) < (closest[0] - rTarget):
                closest[0] = parallel(r1, r2)
                closest[1] = '(' + str(r1) + ' || ' + str(r2) + ')'
    return result


# finds the closest combination of resistors using recursion
# takes two array arguments containing the possibilities for each resistor
def combine(combo_resistors = singleResistors):
    global rCount
    global rTarget
    if rCount == 2:
        return find_closest(singleResistors, combo_resistors)
    else:
        new_combos = []
        for r1 in range(len(singleResistors)):
            for r2 in range(len(combo_resistors)):
                r1Val = r1[1]
                r2Val = r2[1]
                if series(r1Val, r2Val) not in singleResistors:
                    new_combos.append([series(r1, r2), '(' + str(r1) + ' + ' + str(r2) + ')'])
                if parallel(r1Val, r2Val) not in new_combos:
                    new_combos.append([parallel(r1, r2), '(' + str(r1) + ' || ' + str(r2) + ')'])
        rCount -= 1
        combine(new_combos)


# output
result = combine()
print('best combination: ' + str(result[1]))
print('total resistance: ' + str(result[0]))
