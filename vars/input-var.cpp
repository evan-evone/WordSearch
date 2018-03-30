#include <iostream>
#include "args.h"
using namespace std;

int main()
{
  /*
  puzzle:
    if nothing, `-f`,`-` followed by `-f`---read from first file except for -o
    if `-`---read from stdin
    program should write puzzle to stdout, lines separated by single tab. will be detected by master.sh
  words:
    if nothing---read from args
    if `-w`---read from file after output, ws file (either/both may be skipped)
    program should write words to stdout, words separated by single tab. will be detected by master.sh
  SEPARATE WITH `\t\t`

  example output: "LINE1\tLINE2\tLINE3\tLINE4\tLINE5\t\tWORD1\tWORD2\tWORD3"
  */

  return 0;
}
