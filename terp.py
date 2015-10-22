import csv
import re
import stack as st
from ip import *
from getch import getch


def lp(content):
    return csv.reader(content, delimeter=' ', quotechar='"')


def execute(prog):
    stacks = [st.stack()]
    stacki = 0
    prog = lp(prog)
    ips = [IP()]

    for ip in ips:
        com = prog[ip.y][ip.x].upper()

        if ip.mode == 'main':
            com = com.split(';')
            assert com[-1] == ''
            com = com[:-1]
            for c in com:
                stack = stacks[stacki]
                if c in ['>', 'RIGHT', 'EAST']:
                    ip.delta = (1, 0)

                elif c in ['<', 'LEFT', 'WEST']:
                    ip.delta = (-1, 0)

                elif c in ['^', 'UP', 'NORTH']:
                    c.delta = (0, 1)

                elif c in ['v', 'V', 'DOWN', 'SOUTH']:
                    ip.delta = (0, -1)

                elif com in ['+', 'ADD']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b+a)

                elif c in ['-', 'SUB', 'SUBTRACT']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b-a)

                elif c in ['*', 'MUL', 'MULT', 'MULTIPLY']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b*a)

                elif c in ['/', 'DIV', 'DIVIDE']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b/a)

                elif c in ['%', 'MOD', 'MODULO']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b % a)

                elif c in ['**', 'EXP', 'EXPONENT']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b**a)

                elif c in ['==', 'EQ']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b == a)

                elif c in ['!=', 'NEQ']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b != a)

                elif c in ['GT']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b > a)

                elif c in ['LT']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b < a)

                elif c in ['>=', 'GTE']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b >= a)

                elif c in ['&', 'BAND']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b & a)

                elif c in ['|', 'BOR']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b | a)

                elif c in ['^', 'BXOR']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b ^ a)

                elif c in ['~', '1COMP']:
                    stack.push(~stack.pop())

                elif c in ['>>', 'LS']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b >> a)

                elif c in ['<<', 'RS']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b << a)

                elif c in ['AND']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b and a)

                elif c in ['OR']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(b or a)

                elif c in ['!', 'NOT']:
                    stack.push(not stack.pop())

                elif c in ['_', 'EWIF']:
                    a = stack.pop()
                    if a == 0:
                        ip.delta = (1, 0)
                    else:
                        ip.delta = (-1, 0)

                elif c in ['|', 'NSIF']:
                    a = stack.pop()
                    if a == 0:
                        ip.delta = (0, 1)
                    else:
                        ip.delta = (0, -1)

                elif c in [':', 'DUP']:
                    a = stack.pop()
                    stack.push(a)
                    stack.push(a)

                elif c in ['\\', 'SWAP']:
                    a = stack.pop()
                    b = stack.pop()
                    stack.push(a)
                    stack.push(b)

                elif c in ['$', 'DROP']:
                    stack.pop()

                elif c in ['PRINT']:
                    print(chr(stack.pop()), end='')

        ip.step()
