import csv
import re

import lib.stack as st
from lib.ip import *
from lib.getch import getch


def lp(content):
    r = [row for row in csv.reader(content, delimiter=' ', quotechar='"')]
    return r


def execute(program):
    stacks = [st.stack()]
    stack_i = 0
    program = lp(program)
    ips = [IP(0, 0, (1, 0))]

    while len(ips) > 0:
        for ipi in range(len(ips)):
            ip = ips[ipi]
            com = program[::-1][ip.y][ip.x]

            if ip.mode == 'main':
                com = [x for x in com.split(';') if x]
                for c in com:
                    cu = c.upper()
                    stack = stacks[stack_i]
                    if cu in ['>', 'RIGHT', 'EAST']:
                        ip.delta = (1, 0)

                    elif cu in ['<', 'LEFT', 'WEST']:
                        ip.delta = (-1, 0)

                    elif cu in ['^', 'UP', 'NORTH']:
                        ip.delta = (0, 1)

                    elif cu in ['v', 'V', 'DOWN', 'SOUTH']:
                        ip.delta = (0, -1)

                    elif cu in ['+', 'ADD']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b+a)

                    elif cu in ['-', 'SUB', 'SUBTRACT']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b-a)

                    elif cu in ['*', 'MUL', 'MULT', 'MULTIPLY']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b*a)

                    elif cu in ['/', 'DIV', 'DIVIDE']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b/a)

                    elif cu in ['%', 'MOD', 'MODULO']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b % a)

                    elif cu in ['**', 'EXP', 'EXPONENT']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b**a)

                    elif cu in ['==', 'EQ']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b == a)

                    elif cu in ['!=', 'NEQ']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b != a)

                    elif cu in ['GT']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b > a)

                    elif cu in ['LT']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b < a)

                    elif cu in ['>=', 'GTE']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b >= a)

                    elif cu in ['&', 'BAND']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b & a)

                    elif cu in ['|', 'BOR']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b | a)

                    elif cu in ['BXOR']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b ^ a)

                    elif cu in ['~', '1COMP']:
                        stack.push(~stack.pop())

                    elif cu in ['>>', 'LS']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b >> a)

                    elif cu in ['<<', 'RS']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b << a)

                    elif cu in ['AND']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b and a)

                    elif cu in ['OR']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(b or a)

                    elif cu in ['!', 'NOT']:
                        stack.push(not stack.pop())

                    elif cu in ['_', 'EWIF']:
                        a = stack.pop()
                        if a == 0:
                            ip.delta = (1, 0)
                        else:
                            ip.delta = (-1, 0)

                    elif cu in ['|', 'NSIF']:
                        a = stack.pop()
                        if a == 0:
                            ip.delta = (0, 1)
                        else:
                            ip.delta = (0, -1)

                    elif cu in [':', 'DUP']:
                        a = stack.pop()
                        stack.push(a)
                        stack.push(a)

                    elif cu in ['\\', 'SWAP']:
                        a = stack.pop()
                        b = stack.pop()
                        stack.push(a)
                        stack.push(b)

                    elif cu in ['$', 'DROP']:
                        stack.pop()

                    elif cu in ['PRINT']:
                        toprint = stack.pop()
                        if type(toprint) == str:
                            print(toprint)
                        elif type(toprint) == int:
                            print(chr(toprint), end='')

                    elif cu in ['GETCH']:
                        stack.push(getch())

                    elif cu in ['EXIT']:
                        del ips[ipi]

                    elif cu in ['']:
                        print('Invalid command!')

                    elif cu[0] == '\'' and c[-1] == '\'':
                        stack.push(c[1:-1])

                    elif re.compile(r'-?[0-9]+').match(c):
                        stack.push(int(c))

                    elif re.compile(r'-?[0-9]+(\.[0-9]+)?').match(c):
                        stack.push(float(c))

                    elif re.compile(r'-?0x[0-9a-fA-F]+').match(c):
                        stack.push(int(c, 16))

                    elif re.compile(r'-?0o[0-7]+').match(c):
                        stack.push(int(c, 8))

                    elif re.compile(r'0?0b[0-1]+').match(c):
                        stack.push(int(c, 2))
            ip.step()


def execf(f):
    execute(open(f, newline=''))

execf('test.pf')
