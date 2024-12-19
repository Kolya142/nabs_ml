# documentation


## how to use
Run base64: `echo -e '<base64 encoded bytecode>' | python3 interpreter.py b64 _` \
Run bytecode: `python3 interpreter.py byte <filename.nmlx>` \
Run sourcecode: `python3 interpreter.py code <filename.nml>` \
Build to bytecode: `python3 interpreter.py build <filename.nml>`

## how to make
### full version
1. split every line to word
2. detect command
3. compile commands to bytecode
4. decode bytecode
5. interpret
### only-interpret version
1. read bytecode
2. decode bytecode
3. interpret


## syntax
```
# comments
# function def:
def add
    push b
    add a
ret
# function call:
load 5
    pop a
load 4
    pop b
call add
str a
out a
```
## bytecode
#### loop:
```
1 byte - instruction type (0x01)

1 byte - first variable size (1) 
n byte - first variable name (a)

1 byte - second variable size (1) 
n byte - second variable name (b)

1 byte - check type (< - 0, > - 1, <= - 2, >= - 3, = - 4, != - 5)

1 byte - function name size (4) 
n byte - function name (lop1)
```
#### function call:
```
1 byte - instruction type (0x03)

1 byte - function name size (1) 
n byte - function name (a)

1 byte - argument size (1) 
n byte - argument name (b)
```

#### function:
```
1 byte - instruction type (0x02)

1 byte - function name size (1) 
n byte - function name (a) 

3 byte - function body size (1)
n byte - function body code (b)
```

## std
```
stack:
load - push(imm)
pop - variable = pop()
push - push(variable)

io:
out - print variable
in - write user input to variable
fread - save file with name variable data to variable
fwrite - save pop() to file with name variable

functions:
lz - call function with name in variable, if pop() < pop()
call - call function with name in variable
bz - call function with name in variable, if pop() > pop()
ez - call function with name in variable, if pop() == pop()

math:
inc - variable ++
dec - variable --
add - variable = variable add pop()
sub - variable = variable sub pop()
mul - variable = variable mul pop()
div - variable = variable div pop()
pow - variable = variable pow pop()
sqrt - variable = square root of variable
rnd - variable = random from 0 to 100 included

utils:
str - variable = str(variable)
exec - build & interpret code from variable
```