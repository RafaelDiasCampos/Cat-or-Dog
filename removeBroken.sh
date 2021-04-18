# !/bin/bash

i=0
for file in data/test/cat/*; do
    identify "$file" > /dev/null
    if [ $? -eq 1 ]; then
        rm "$file";
        ((i++));
    fi
done

for file in data/test/dog/*; do
    identify "$file" > /dev/null
    if [ $? -eq 1 ]; then
        rm "$file";
        ((i++));
    fi
done

for file in data/train/cat/*; do
    identify "$file" > /dev/null
    if [ $? -eq 1 ]; then
        rm "$file";
        ((i++));
    fi
done

for file in data/train/dog/*; do
    identify "$file" > /dev/null
    if [ $? -eq 1 ]; then
        rm "$file";
        ((i++));
    fi
done

echo "Total $i files deleted"