# the dis module is a disassembler of Python byte code
# for example, the dis.dis() function disassembles whichever
# function you pass as a parameter and prints the list of bytecode instructions that
# are run by the function

import dis


def x():
    return 42


dis.dis(x)


abc = ('a', 'b', 'c')


def concat_a_1():
    for letter in abc:
        abc[0] + letter


def concat_a_2():
    a = abc[0]
    for letter in abc:
        a + letter


dis.dis(concat_a_1)
