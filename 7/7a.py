import itertools
import math


def intcode_computer(input, intcode):

    output = []
    input_ptr = 0
    ptr = 0

    while ptr < len(intcode):

        if int(intcode[ptr][-2:]) == 1:
            instruction = intcode[ptr].zfill(5)  # zero padding

            if instruction[2] == "0":
                a = int(intcode[int(intcode[ptr + 1])])
            else:
                a = int(intcode[ptr + 1])

            if instruction[1] == "0":
                b = int(intcode[int(intcode[ptr + 2])])
            else:
                b = int(intcode[ptr + 2])

            intcode[int(intcode[ptr + 3])] = str(a + b)
            ptr += 4
            continue

        if int(intcode[ptr][-2:]) == 2:
            instruction = intcode[ptr].zfill(5)

            if instruction[2] == "0":
                a = int(intcode[int(intcode[ptr + 1])])
            else:
                a = int(intcode[ptr + 1])

            if instruction[1] == "0":
                b = int(intcode[int(intcode[ptr + 2])])
            else:
                b = int(intcode[ptr + 2])

            intcode[int(intcode[ptr + 3])] = str(a * b)

            ptr += 4
            continue

        if int(intcode[ptr][-2:]) == 3:
            intcode[int(intcode[ptr + 1])] = str(input[input_ptr])
            input_ptr += 1
            ptr += 2
            continue

        if int(intcode[ptr][-2:]) == 4:
            if int(intcode[ptr]) == 4:
                output.append(intcode[int(intcode[ptr + 1])])
                # print(output[-1])

            elif int(intcode[ptr]) == 104:
                output.append(intcode[ptr + 1])
                # print(output[-1])

            ptr += 2
            continue

        if int(intcode[ptr][-2:]) == 5:
            instruction = intcode[ptr].zfill(4)

            if instruction[1] == "0":
                a = int(intcode[int(intcode[ptr + 1])])
            else:
                a = int(intcode[ptr + 1])

            if a != 0:
                if instruction[0] == "0":
                    ptr = int(intcode[int(intcode[ptr + 2])])
                else:
                    ptr = int(intcode[ptr + 2])
            else:
                ptr += 3
                pass

            continue

        if int(intcode[ptr][-2:]) == 6:
            instruction = intcode[ptr].zfill(4)

            if instruction[1] == "0":
                a = int(intcode[int(intcode[ptr + 1])])
            else:
                a = int(intcode[ptr + 1])

            if a == 0:
                if instruction[0] == "0":
                    ptr = int(intcode[int(intcode[ptr + 2])])
                else:
                    ptr = int(intcode[ptr + 2])
            else:
                ptr += 3
                pass

            continue

        if int(intcode[ptr][-2:]) == 7:
            instruction = intcode[ptr].zfill(5)

            if instruction[2] == "0":
                a = int(intcode[int(intcode[ptr + 1])])
            else:
                a = int(intcode[ptr + 1])

            if instruction[1] == "0":
                b = int(intcode[int(intcode[ptr + 2])])
            else:
                b = int(intcode[ptr + 2])

            if a < b:
                intcode[int(intcode[ptr + 3])] = 1
            else:
                intcode[int(intcode[ptr + 3])] = 0

            ptr += 4
            continue

        if int(intcode[ptr][-2:]) == 8:
            instruction = intcode[ptr].zfill(5)

            if instruction[2] == "0":
                a = int(intcode[int(intcode[ptr + 1])])
            else:
                a = int(intcode[ptr + 1])

            if instruction[1] == "0":
                b = int(intcode[int(intcode[ptr + 2])])
            else:
                b = int(intcode[ptr + 2])

            if a == b:
                intcode[int(intcode[ptr + 3])] = 1
            else:
                intcode[int(intcode[ptr + 3])] = 0

            ptr += 4
            continue

        if int(intcode[ptr][-2:]) == 99:
            break

    return output


def read_input(file):
    with open(file) as inputfile:
        input = inputfile.readline()
    return input


def signal(phase_setting, program):
    input_signal = 0
    for phase in phase_setting:
        input_signal = int(intcode_computer([phase, input_signal], program[:])[0])
    return input_signal


def max_signal(program):
    max_output = -math.inf
    phase_settings = list(itertools.permutations(range(0, 5)))
    for phase_setting in phase_settings:
        output_signal = signal(phase_setting, program[:])
        if output_signal > max_output:
            max_output = output_signal
            max_phase_setting = phase_setting
    return max_phase_setting, max_output


if __name__ == "__main__":
    input = read_input("input.txt")
    program = input.split(",")
    max_phase_setting, max_output = max_signal(program)
    print("Max output: "+str(max_output))
    print("Max phase settings: " + str(max_phase_setting))
