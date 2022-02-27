import sys


class Resistor:
    def __init__(self, resistance: float, components: str):
        self.resistance = resistance
        self.components = components

    def __eq__(self, other):
        return self.resistance == other.resistance

    def __str__(self):
        return self.components


def series(r1: Resistor, r2: Resistor) -> Resistor:
    resistance = r1.resistance + r2.resistance
    components = '(' + r1.components + ' + ' + r2.components + ')'
    return Resistor(resistance, components)


def parallel(r1: Resistor, r2: Resistor) -> Resistor:
    resistance = (r1.resistance * r2.resistance)/(r1.resistance + r2.resistance)
    components = '(' + r1.components + ' || ' + r2.components + ')'
    return Resistor(resistance, components)


# Finds the closest resistance achievable with a combination of two resistors from the input lists
def find_closest(r1_list, r2_list):
    closest = series(r1_list[0], r2_list[0])
    global rTarget
    for r1 in r1_list:
        for r2 in r2_list:
            if abs(series(r1, r2).resistance - rTarget) < abs(closest.resistance - rTarget):
                closest = series(r1, r2)
            if abs(parallel(r1, r2).resistance - rTarget) < abs(closest.resistance - rTarget):
                closest = parallel(r1, r2)
    return closest


# Read the resistor values into an array from the input file
with open('resistors.txt') as resistorFile:
    singleResistors = []

    for line in resistorFile:
        singleResistors.append(Resistor(float(line), line.strip('\n')))


rTarget = float(sys.argv[1])
rCount = int(sys.argv[2])
rClosest = Resistor(0, '0')


# finds the closest combination of resistors using recursion
# takes two array arguments containing the possibilities for each resistor
def combine(combo_resistors=singleResistors):
    global rCount
    global rTarget
    global rClosest
    rClosest = find_closest(singleResistors, combo_resistors)

    if rCount == 2:
        return
    elif rClosest.resistance == rTarget:
        return
    else:
        new_combos = []
        for r1 in singleResistors:
            for r2 in combo_resistors:
                if series(r1, r2) not in singleResistors:
                    new_combos.append(series(r1, r2))
                if parallel(r1, r2) not in new_combos:
                    new_combos.append(parallel(r1, r2))
        rCount -= 1
        combine(new_combos)


# output
combine()
print('best combination: ' + str(rClosest))
print('total resistance: ' + str(rClosest.resistance))
