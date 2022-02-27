import sys


class Resistor:
    def __init__(self, resistance: float, components: str):
        self.resistance = resistance
        self.components = components


# Read the resistor values into an array from the input file
with open('resistors.txt') as resistorFile:
    singleResistors = []

    for line in resistorFile:
        singleResistors.append(Resistor(float(line), line.strip('\n')))
# print(singleResistors)
#
#
# # rTarget = sys.argv[0]
# rTarget = 50
# # rCount = sys.argv[1]
# rCount = 2
# rClosest = []
#
#
# def series(r1: float, r2: float) -> float:
#     return r1 + r2
#
#
# def parallel(r1: float, r2: float) -> float:
#     return (r1 * r2)/(r1 + r2)
#
#
# def find_closest(r1_list, r2_list):
#     closest = [series(r1_list[0], r2_list[0]), str(r1_list[0]) + ' + ' + str(r2_list)]
#     global rTarget
#     for i in range(len(r1_list)):
#         for j in range(len(r2_list)):
#             r1 = r1_list[1][i]
#             r2 = r2_list[1][j]
#             if (series(r1, r2) - rTarget) < (int(closest[0]) - rTarget):
#                 closest[0] = series(r1, r2)
#                 closest[1] = '(' + str(r1) + ' + ' + str(r2) + ')'
#             if (parallel(r1, r2) - rTarget) < (closest[0] - rTarget):
#                 closest[0] = parallel(r1, r2)
#                 closest[1] = '(' + str(r1) + ' || ' + str(r2) + ')'
#     return result
#
#
# # finds the closest combination of resistors using recursion
# # takes two array arguments containing the possibilities for each resistor
# def combine(combo_resistors = singleResistors) :
#     global rCount
#     global rTarget
#     if rCount == 2:
#         return find_closest(singleResistors, combo_resistors)
#     else:
#         new_combos = []
#         for i in range(len(singleResistors)):
#             for j in range(len(combo_resistors)):
#                 r1 = singleResistors[i][1]
#                 r2 = combo_resistors[j][1]
#                 if series(r1, r2) not in singleResistors:
#                     new_combos.append([series(r1, r2), '(' + str(r1) + ' + ' + str(r2) + ')'])
#                 if parallel(r1, r2) not in new_combos:
#                     new_combos.append([parallel(r1, r2), '(' + str(r1) + ' || ' + str(r2) + ')'])
#         rCount -= 1
#         combine(new_combos)
#
#
# # output
# result = combine()
# print('best combination: ' + str(result[1]))
# print('total resistance: ' + str(result[0]))
