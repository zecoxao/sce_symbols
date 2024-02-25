# sce_symbols
General repository of names and symbols from SCE

Easy shortcuts:

get symbols list:

nm name of elf > list.txt

cut first N characters of list (useful for trimming the addresses):

cut -cN- list.txt

sort automatically and only include unique words:

sort -u list.txt > final_list.txt

find and grep for symtab on files without extension (useful for linux files with syms) :

find . -type f \( ! -name  '*.*' \) -exec grep -r 'symtab' {} \;

grep for stabs in files with exe extension (useful for windows files with stabs syms) :

grep -r stabs --include \*.exe

# CREDITS

* flatz, SocraticBliss, Proxima, Jevinskie

for the shortcuts
