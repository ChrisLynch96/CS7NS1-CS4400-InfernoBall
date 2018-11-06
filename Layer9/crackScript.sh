

wget https://crackstation.net/files/crackstation.txt.gz
gunzip crackstation.txt.gz crackstation.txt

LC_ALL=C egrep -a "^[[:alnum:]]{5,8}$" crackstation.txt > layer9.txt

fspec=layer9.txt
num_files=4

# Work out lines per file.

total_lines=$(wc -l <${fspec})
((lines_per_file = (total_lines + num_files - 1) / num_files))

# Split the actual file, maintaining lines.

split --lines=${lines_per_file} ${fspec} xyzzy.

# Debug information

echo "Total lines     = ${total_lines}"
echo "Lines  per file = ${lines_per_file}"    
wc -l xyzzy.*