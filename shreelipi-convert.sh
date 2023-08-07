#!/bin/bash

# First variable
file=$1;

# Extract file name using basename command
filename=$(basename "$file")

# Append suffix to file name
suffix="_kan.txt"
new_filename="${filename%.*}$suffix"

# Second variable
new_file=$new_filename;

python3 shreelipi_convert.py $1 > ./$new_file
