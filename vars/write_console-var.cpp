#include <iostream>
#include "args.h"
using namespace std;

int main(int argc, char** argv)
{
  setargs(&argc, argv);                                                                     // clear self-call

  int write_console = 0;
  for (int i = 0; i < argc; i++) {
    string arg = argv[i];
    if (arg[0] == '-' && arg.find('d') < arg.length())                                      // if not in string, returns huge number
    {
      write_console = 1;
    }
  }

  printf("%d\n", write_console);                                                            // tell `master.sh` 0 or 1, depending

  return 0;
}
