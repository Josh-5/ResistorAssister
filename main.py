import sys

# Read the resistor values into an array from the input file
with open('resistors.txt') as resistorFile:
    singleResistors = []
    for line in resistorFile:
         singleResistors.append([int(x) for x in line.split()])


rCombo = ""
rTarget = sys.argv[0]
rCount = sys.argv[1]
closestR = 0


def series(r1, r2):
    return r1 + r2


def parallel(r1, r2):
    return (r1 * r2)/(r1 + r2)


# TODO: rename target or rTarget to better differentiate them
def find_closest(target, r1List, r2List):
    result = [series(r1List[0], r2List[0]), str(r1List[0]) + ' + ' + str(r2List)]
    for r1 in r1List:
        for r2 in r2List:
            if (series(r1, r2) - target) < (result[0] - target):
                result[0] = series(r1, r2)
                result[1] = str(r1) + ' + ' + str(r2)
            if (parallel(r1, r2) - target) < (result[0] - target):
                result[0] = parallel(r1, r2)
                result[1] = str(r1) + ' || ' + str(r2)
    return result


# #tracks the current combination possibilities through the recursion
# comboResistors = singleResistors
#
# # finds the closest combination of resistors using recursion
# # takes two array arguments containing the possibilities for each resistor
# def combine(r2):
#     if rCount == 2:
#         isSeries = True
#         for r1 in singleResistors:
#             if (series(r1, r2) - rTarget) < (series(r1, r2) - rTarget)
#     else:
#         for r1 in singleResistors:
#             for r2 in comboResistors:
#                 if !(series(r1, r2) in comboResistors):
#                     comboResistors.append(series(r1, r2))
#
#                 if !(parallel(r1, r2) in comboResistors):
#                     comboResistors.append(parallel(r1, r2))
