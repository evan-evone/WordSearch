#include <iostream>
#include <fstream>
#include "args.h"
using namespace std;

int main(int argc, char** argv)
{
  setargs(&argc, argv);

  // DEFINE INPUT SOURCES
  int read_puzzle = 1;
  int last_index = -1;
  int read_word = 0;                                                                        // 0: read from args. 1: read from file

  for (int i = 0; i < argc; i++) {
    string arg = argv[i];
    if (arg[0] == '-' && arg.find('f') < arg.length()) read_puzzle = 1;                     // if not in string, returns huge number
    if (arg[0] == '-' && arg.find('w') < arg.length()) read_word = 1;                       // if not in string, returns huge number
    if (arg == "-") read_puzzle = 0;
    if (arg[0] == '-' && arg.find('o') < arg.length()) last_index = i;                      // if not in string, returns huge number
  }

  int word_count = 0;
  for (int i = 0; i < argc; i++) {
    string arg = argv[i];
    if (arg[0] != '-' && i != last_index + 1) {
      argv[word_count] = argv[i];
      word_count = word_count + 1;                                                          // iterate after because start at 0
    }
  }

  // READ PUZZLE
  string puzzle_text;

  if (read_puzzle && word_count > 0) {
    string puzzle_name = argv[0];

    ifstream puzzle(puzzle_name);
    string current_line;

    while (puzzle >> current_line) {
      puzzle_text = puzzle_text + current_line + "\t";
    }
  }

  else {
    string current_line;
    int line_number;

    cout << "Enter Number of Lines: ";
    cin >> line_number;

    for (int i = 0; i < line_number; i++) {
      cout << "Enter Puzzle Line " << i+1 << ": ";
      cin >> current_line;
      puzzle_text = puzzle_text + current_line + "\t";
    }
  }

  // READ WORDS
  string word_text;

  if (read_word && word_count > 1) {                                                        // remember, argv[0] is now puzzle name
    string word_name = argv[1];

    ifstream words(word_name);
    string word_line;

    while (words >> word_line) {
      word_text = word_text + word_line + "\t";
    }
  }

  else {
    if (word_count > 1) {

      for (int i = 1; i < word_count; i++) {
        word_text = word_text + argv[i] + "\t";
      }
    }
    else {
      string word_line;

      cout << "Enter Number of Words: ";
      cin >> word_count;

      for (int i = 0; i < word_count; i++) {
        cout << "Enter Word " << i+1 << ": ";
        cin >> word_line;
        word_text = word_text + word_line + "\t";
      }
    }
  }

  printf("%s\t\t%s\n", puzzle_text.c_str(), word_text.c_str());

  return 0;
}
