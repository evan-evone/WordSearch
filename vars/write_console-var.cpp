#include <iostream>
#include "args.h"
using namespace std;

int main(int argc, char** argv)
{
  setargs(&argc, argv);                                                                     // clear self-call

  int write_console = 0;
  for (int i = 0; i < argc; i++) {
    if (/*check if starts with `-` and contains `d`*/) { write_console = 1; }
  }

  printf("%d\n", write_console);                                                            // tell `master.sh` 0 or 1, depending

  return 0;
}
