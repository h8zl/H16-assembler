# H16-assembler
Custom assembler for a CPU design I'm working on, written in Python.
**Opcodes included here are not final.**
## Overview
Python script to translate a semi-custom assembly language into machine code for my CPU H-16 (WIP), made to be interpreted by [logisim](https://github.com/logisim-evolution/logisim-evolution). Opcodes are in a seperate file and more can be added by the user, following the same style as the ones already in there.
## Usage
to use the script, go to your terminal in the same folder as the script and type: 

`python H16-assembler.py [inputfile] [outputfile]`.

Replace `[inputfile]` with the filename of your code, and `outputfile` with the desired name of your machine code file. **If the output filename is already used, that file will be overwritten!**
Make sure your inputfile and your opcodes file are also in the same folder!

![scriptran](https://github.com/user-attachments/assets/03dddfb4-5e9f-4706-8769-d2bed1cb1080)

example code included is to compute the 10th fibonacci number. I can't verify it works as the CPU is only theoretical right now, but the main point is to show that the assembler works ;)
## Language guidelines
Any non-indented characters (except for "/ ") will be used as a tag, tags store the line number of the next code after it. Tags may be referred to as operands, such as for a jump instruction. All indented code will be treated as an instruction. Comments must be preceded by "/ ", no in-line comments. Numbers must be preceded by either "#" or "$", for decimal and hexadecimal respectively. Decimal numbers can be any length, but hex numbers must be 4 digits long.

## Limitations
The biggest limitation is that the script won't check if what you wrote actually makes sense, so if you write something incorrect it'll either, 1. crash, or 2. assemble like normal, leaving you to figure out the issue yourself.

The reason I'm not going to put much (if any) effort into implementing error correction is that any user of this software likely has some idea of what they're doing, and can most likely figure it out.
