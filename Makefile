INPUT = exemple1 exemple2

assembleur_vers_exercutable: generation_code_nasm
	for a in $(INPUT); do echo "Assemblage: " $${a}; done;

generation_code_nasm:
	for a in $(INPUT); do echo "Generation code nasm: " $${a}; python3 generation_code.py -nasm input/$${a}.flo > output/$${a}.nasm; done;
