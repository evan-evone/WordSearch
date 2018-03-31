#!/usr/bin/env bash

#please note that this is temporary
#still working out argument parsing, but the plan is parsed in c++ then given to python in two parts
#puzzle separated by tabs and words separated by tabs

declare argv
for (( i=0; i<BASH_ARGC; i++ ))
  do argv[$i]=${BASH_ARGV[$BASH_ARGC - $i - 1]}
done

write_console=$(./vars/write_console-var.o ${argv[*]})

#: debug `write_console` variable process
# if [ $write_console == "1" ]; then
#   echo "Writing to Console."
# else
#   echo "Not writing to Console."
# fi

output=$(./vars/output-var.o ${argv[*]})

#: debug `output` variable process
# echo $output
# if [ "$output" == "&1" ]; then echo "this is sample output"; else echo "this is sample output" > $output; fi

input=$(./vars/input-var.o ${argv[*]})
    #PUZZLE - $(echo input | awk -F"\t\t" '{print $1}'). Puzzle printed first, separated by tabs.
    #WORDS - $(echo input | awk -F"\t\t" '{print $2}'). Words printed second, separated by tabs.

#writing: [output]`>$output`. May be &1 for stdout or may be path.
# output=$(python/solve.py $1 < $2)                                                                             #$1 = string of args, separated by spaces. `sys.argv`
# python/display.py "$output" < $2                                                                              #$2 = string/file of wordsearch. `sys.stdin`
