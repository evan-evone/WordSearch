#include <iostream>
using namespace std;

#ifndef ARGS_H
#define ARGS_H

void setargs(int* argc, char** argv)
{
  for (int i = 0; i < *argc - 1; i++) { argv[i] = argv[i + 1]; }
  *argc = *argc - 1;
}

#endif
