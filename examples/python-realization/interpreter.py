import os
import random
import time
from utils import *
from compiler import compiler, parser, parse_int
import compiler as _compiler

@dataclasses.dataclass
class State:
    variables: Dict[str, int]
    functions: Dict[str, bytes]
    stack: List[int]

def interpreter(bytecode: bytes, state: State) -> None:
    i = 0
    l = len(bytecode)
    while True:
        if i >= l:
            break
        # print(bytecode[i:])
        if bytecode[i] == 0x02:
            fl = bytecode[i+1]
            f = bytecode[i+2:][:fl].decode()
            al = bytecode[i+2+fl]
            a = bytecode[i+3+fl:][:al]
            state.functions[f] = a
            i += fl+al+3
            # print(fl, al)
            # print(f, '->', a)
        elif bytecode[i] == 0x03:
            fnl = bytecode[i+1]
            fn = bytecode[i+2:][:fnl].decode()
            al = bytecode[i+2+fnl]
            a = bytecode[i+3+fnl:][:al].decode()
            match fn:
                case 'load':
                    state.stack.append(parse_int(a))
                case 'pop':
                    state.variables[a] = state.stack.pop()
                case 'push':
                    state.stack.append(state.variables[a])
                case 'out':
                    print(int_to_str(state.variables[a]), end='')
                case 'lz':
                    if state.stack.pop() < state.stack.pop():
                        print(state.functions)
                        interpreter(state.functions[a], state)
                case 'call':
                    interpreter(state.functions[a], state)
                case 'bz':
                    if state.stack.pop() > state.stack.pop():
                        print(state.functions)
                        interpreter(state.functions[a], state)
                case 'ez':
                    if state.stack.pop() == state.stack.pop():
                        interpreter(state.functions[a], state)
                case 'in':
                    state.variables[a] = parse_int(f"'{input()}'")
                case 'inc':
                    state.variables[a] += 1
                case 'dec':
                    state.variables[a] += 1
                case 'add':
                    state.variables[a] += state.stack.pop()
                case 'sub':
                    state.variables[a] -= state.stack.pop()
                case 'mul':
                    state.variables[a] *= state.stack.pop()
                case 'div':
                    state.variables[a] /= state.stack.pop()
                case 'pow':
                    state.variables[a] **= state.stack.pop()
                case 'sqrt':
                    state.variables[a] = state.variables[a] ** 0.5
                case 'rnd':
                    state.variables[a] = random.randint(0, 100)
                case 'str':
                    state.variables[a] = parse_int(f"'{state.variables[a]}'")
                # case 'sys':
                #     print(int_to_str(state.variables[a]))
                #     state.variables[a] = os.system(int_to_str(state.variables[a]))
                case 'fread':
                    state.variables[a] = open(int_to_str(state.variables[a]), 'r').read()
                case 'fwrite':
                    open(int_to_str(state.variables[a]), 'w').write(state.stack.pop())
                case 'exec':
                    interpreter(compiler(parser(int_to_str(state.variables[a])), _compiler.State({}, {})), state)
            i += fnl+al+3
        elif bytecode[i] == 0x01:
            fl = bytecode[i+1]
            f = bytecode[i+2:][:fl].decode()

            tl = bytecode[i+2+fl]
            t = bytecode[i+3+fl:][:tl].decode()

            op = bytecode[i+3+fl+tl]

            fnl = bytecode[i+3+fl+tl+1]
            fn = bytecode[i+3+fl+tl+2:][:fnl].decode()

            while True:
                interpreter(state.functions[fn], state)

                if op == 0x1 and state.variables[f] >= state.variables[t]:
                    break
                if op == 0x2 and state.variables[f] <= state.variables[t]:
                    break
                if op == 0x3 and state.variables[f] > state.variables[t]:
                    break
                if op == 0x4 and state.variables[f] < state.variables[t]:
                    break
                if op == 0x5 and state.variables[f] != state.variables[t]:
                    break
                if op == 0x6 and state.variables[f] == state.variables[t]:
                    break
            i += fl+tl+3+tl+2+fnl
        # time.sleep(0.1)
                    
if __name__ == '__main__':
    tkns = parser(open('../test.nml').read())
    print(tkns)
    cmds = compiler(tkns, _compiler.State({}, {}))
    print(cmds)
    interpreter(cmds, State({}, {}, []))