# BETPL: better programming language
BETPL is a lisp dialect that can run on everywhere from an Arduino nano 33 to a supercomputer

BETPL has a file extinsion of BPL. BETPL is targeted at FAT-12 and more complex filesystems

BETPL is simple to parse

BETPL uses visible arrays and ratios

to sum this up, here are the good things about BEPL:
- nothing more then parens
- almost everything is a builtin
- runs embeded but not designed to only be

see [PARSER.PY](PARSER.PY) (does not run on most FAT filesystem-based OSes) for a sample parser with [sly](https://sly.readthedocs.io/en/latest/sly.html)

## STANDARD METHODS
- `(ignore ...)`: ignores every parameter, useful as a comment or a no-op
- `(list ...)`: makes a list (not (visibly, can be internaly) cons-based)
- `(setindex list index value)`: sets the `index`-th item of `list` to `value`
- `(index list index)`: returns the 1-based `index`-th item of `list`. number that are fractional, bigger than the number of items in `list`, or equal to or below 0 will stop execution
- `(len list)`: returns the length of the list `list`
- `(+ ...)`: adds all numbers, or if arguments are strings concatinates them
- `(- ...)`: subtracts all numbers
- `(* ...)`: multiplies all numbers
- `(/ ...)`: divides all numbers
- `(getpermissionlevel)`: returns a number from 0-2, where 0 is guest, 1 is trusted, and 2 is system
- `(async eventfun statelist)`: creates an async where `eventfun` is called every event where the first argument is the event and the second parameter is the `statelist`, and `datalist` must be a list
- `(msg async event)`: `async` is the async which `event` will be put on 
- `(createsandbox permissionlevel)`: creates a async sandbox with permission level `permissionlevel` and `permissionlevel` must be current `permissionlevel` or smaler. it takes an event which is a string saying the code to execute in the sandbox
- `(lambda code)`: a lambda
- `(set varname value)`: sets the variable `varname` to the value `value`
- `(get varname)`: returns the value of the variable `varname`