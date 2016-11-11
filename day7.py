#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/7

import sys



def l_shift(x, y, a):
  a = x << y
  return a

def r_shift(x, y, a):
  a = x >> y
  return a

def bobby_logic(filename):
  input = open(filename, 'rU')
  #create a dict to store each wire's value
  circuit = {}
  #solve for a - loop until it exists
  chop = ""
  while not circuit.has_key("a"):
    for line in input:
      chop = line.split()
      #skip every line we did before (that is in circuit{} already)
      if circuit.has_key(chop[-1]):
        continue
      #fill out all the raw input...
      elif chop[0] is int:
        circuit[chop[-1]] = int(chop[0])
      #...then dig into the logic-y parts
      #needs to accomodate wire names as inputs only from here on in
      #but you need to skip any line if you don't have the values
      elif len(chop) == 5 and chop[1] == "AND":
        if not circuit.has_key([chop[0]) and not circuit.has_key([chop[2]):
          continue
        else:
          circuit[chop[-1]] = int(chop[0]) & int(chop[2])
      elif len(chop) == 5 and chop[1] == "OR":
        if not circuit.has_key([chop[0]) and not circuit.has_key([chop[2]):
          continue
        else:
          circuit[chop[-1]] = int(chop[0]) | int(chop[2])
      elif len(chop) == 5 and chop[1] == "LSHIFT":
        if not circuit.has_key([chop[0]):
          continue
        else:
        circuit[chop[-1]] = int(chop[0]) << int(chop[2])
      elif len(chop) == 5 and chop[1] == "RSHIFT":
        if circuit.has_key([chop[0]):
          continue
        else:
          circuit[chop[-1]] = int(chop[0]) >> int(chop[2])
      elif len(chop) == 4 and chop[0] == "NOT":
        if circuit.has_key([chop[1]):
          continue
        else:
          circuit[chop[-1]] = ~chop[1]
  #a can only have one input - once it exists, yer done
  return circuit["a"]

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a_signal = bobby_logic(sys.argv[1])
  print "Wire A receives the signal " + a_signal

if __name__ == '__main__':
  main()