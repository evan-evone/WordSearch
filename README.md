# WordSearch with Python
### Because you either love word searches or you hate them

WordSearch is made to solve word searches. In the future, it may also be able to make word
searches and let you play them, _if_ you fancy that. Right now, all that's here is the one
file that can find a single word in a word search file. A lot of work needs to be done.

### Arguments (Implementation Incomplete)

Usage: `./master.sh -[dfosw] [INFILE OUTFILE SOLUTION] [words | WORDFILE]`

- `-d`: Debug (write to console). Does a lot of `print` statements.
- `-f`: Specify input file. Default stdin (`-`).
- `-o`: Specify output file. Default stdout (`-`).
- `-s`: Specify file to output solution. Default no output, with flag defaults to `-`.
- `-w`: Specify a file containing the words to be found. Default read as trailing arguments.
