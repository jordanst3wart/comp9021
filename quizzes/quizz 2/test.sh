#!/bin/sh


# should make into for loop
printf "Inputting 1 into python quiz 2:\n"
echo 3 | python3 quiz_2.py
echo "answer: In base 2, [1] is: [1]"
echo "---------------------------------------"

printf "Inputting 51315663 into python quiz 2:\n"
echo 51315663 | python3 quiz_2.py
echo "answer: In base 2, [4891] is: [1001100011011]"
echo "---------------------------------------"

printf "Inputting 424896 into python quiz 2:\n"
echo 424896 | python3 quiz_2.py
echo "answer: In base 2, [11, 24] is: [1011, 11000]"
echo "---------------------------------------"

printf "Inputting 857310204 into python quiz 2:\n"
echo 857310204 | python3 quiz_2.py
echo "answer: In base 2, [10, 20, 30] is: [1010, 10100, 11110]"
echo "---------------------------------------"

printf "Inputting 13609683913728 into python quiz 2:\n"
echo 13609683913728 | python3 quiz_2.py
echo "answer: In base 2, [2, 4, 8, 16, 32] is: [10, 100, 1000, 10000, 100000]"
echo "---------------------------------------"

printf "Inputting 11 into python quiz 2:\n"
echo 11 | python3 quiz_2.py
echo "answer: Incorrect encoding!"
echo "---------------------------------------"

printf "Inputting 12345 into python quiz 2:\n"
echo 12345 | python3 quiz_2.py
echo "answer: Incorrect encoding!"
echo "---------------------------------------"