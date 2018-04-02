# WordSearch with Python
### Because you either love word searches or you hate them

WordSearch is made to solve word searches. In the future, it may also be able to make word
searches and let you play them, _if_ you fancy that. Right now, all that's here is the one
file that can find a single word in a word search file. A lot of work needs to be done.

### Arguments (Implementation Incomplete)

Usage: `./master.sh -[dofw] [output_file] [input_file] [words | word_file]`

- `-d`: Debug (write to console) feature. Does a lot of print statements.
- `-o`: Specify output file. Assumed to be argument following `-o`. Default stdout.
- `-f`: Specify input file. Assumed to be first argument that is not a flag (`-dofw`) or the
  output file name. This is a default and will counteract `-`.
- `-w`: Specify a file containing the words to be found. Assumed to be second argument that
  is not a flag (`-dofw`) or the output name. Otherwise words will be treated as arguments
  or stdin.
- `-`: Specify stdin reading puzzle from stdin. This will counteract `-f`.
