#include <iostream>
#include "args.h"
using namespace std;

int main(int argc, char** argv)
{
  setargs(&argc, argv);                                                                     // clear self-call

  int last_index = -1;                                                                      // note to self: look up how to check if given value
  for (int i = 0; i < argc; i++) {
    if (/*check if starts with `-` and contains `o`*/) { last_index = i; }
  }

  if ( last_index == -1 ||  last_index + 1 == argc )                                        // if nonexistant or last argument
  {
    printf("%s\n", "&1");                                                                   // then write to path to stdout
  }
  else                                                                                      // else there is both `-o` and matching str
  {
    printf("%s\n", argv[last_index + 1]);                                                   // then write to path specified in next index
  }

  return 0;
}
