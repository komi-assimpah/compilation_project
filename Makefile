INPUT = $(shell ls input | sed 's/.flo//g')

.DEFAULT_GOAL := all

assembleur_vers_executable: generation_code_nasm
    for a in $(INPUT); do [ -f output/$${a}.nasm ] && (echo "Assemblage: " $${a}; nasm -f elf -g -F dwarf output/$${a}.nasm; ld -m elf_i386 -o output/$${a} output/$${a}.o && rm output/$${a}.o);  done;

generation_code_nasm:
    for a in $(INPUT); do echo "Generation code nasm: " $${a}; python3 generation_code.py -nasm input/$${a}.flo > output/$${a}.nasm || (rm output/$${a}.nasm; exit 0); done;

clean:
    rm output/*

all: assembleur_vers_executable
    exit 0