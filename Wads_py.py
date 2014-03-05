#!/usr/bin/env python2

import sys

def wadsworth(original):  

  if len(sys.argv) != 0:
    phrase = ' '.join(original[1:])
  else:
    phrase = original

  output = phrase[int(len(phrase)-len(phrase)*.70):]

  return output

if __name__ == '__main__':
  print wadsworth(sys.argv)

