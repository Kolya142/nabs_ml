# documentation


## how to use
1. change `test.nml`
2. run `python3 interpreter.py`


## how to make
1. split every line to word
2. detect command
3. compile commands to bytecode
4. interpret


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

1 byte - function body size (1) # todo: change to 3 bytes 
n byte - function body name (b)
```

## std
```
stack:
load
pop
push

io:
out
in
fread
fwrite

functions:
lz
call
bz
ez

math:
inc
dec
add
sub
mul
div
pow
sqrt
rnd

utils:
str
exec
```