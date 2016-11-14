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
  input = ""
  #create a dict to store each wire's value
  circuit = {}
  #solve for a - loop until it exists
  chop = ""
  while not circuit.has_key("a"):
    input = open(filename, 'rU')
    for line in input:
      chop = line.split()
      #skip every line we did before (that is in circuit{} already)
      if circuit.has_key(chop[-1]):
        continue
      #each command has a fixed length
      elif len(chop) == 3:
        #fill out raw input, ex: "1 -> x"
        if chop[0].isdigit():
          circuit[chop[-1]] = int(chop[0])
        #do "x -> y" if x is assigned
        elif circuit.has_key(chop[0]):
          circuit[chop[-1]] = circuit[chop[0]]
        #skip line for "x -> y" when x is unassigned
        else:
          continue
          #print line + ", where "+chop[-1]+" = "+str(circuit[chop[-1]])
      #...then dig into the logic-y parts
      #needs to accomodate wire names as inputs only from here on in
      #but you need to skip any line if you don't have the values
      elif len(chop) == 4 and chop[0] == "NOT":
        if circuit.has_key(chop[1]):
          #the 0xFFFF de-signs the signed int. ex: "NOT x -> y" will be (-x - 1) unless ANDed with 0xFFFF
          circuit[chop[-1]] = ~int(circuit[chop[1]]) & 0xFFFF
        else:
          continue
          #print line + ", where " + chop[-1] + " = "+str(circuit[chop[-1]]) + " and ~" + chop[1] + " = "+str(~int(circuit[chop[1]]))
      elif len(chop) == 5:
        if chop[1] == "AND":
          if circuit.has_key(chop[0]) and circuit.has_key(chop[2]):
            circuit[chop[-1]] = (circuit[chop[0]] & circuit[chop[2]])
          elif chop[0].isdigit() and circuit.has_key(chop[2]):
            circuit[chop[-1]] = int(chop[0]) & circuit[chop[2]]
          elif chop[2].isdigit() and circuit.has_key(chop[0]):
            circuit[chop[-1]] = int(chop[2]) & circuit[chop[0]]
          else:
            continue
            #print line
        elif chop[1] == "OR":
          if circuit.has_key(chop[0]) and circuit.has_key(chop[2]):
            circuit[chop[-1]] = (circuit[chop[0]] | circuit[chop[2]])
          elif chop[0].isdigit() and circuit.has_key(chop[2]):
            circuit[chop[-1]] = int(chop[0]) | circuit[chop[2]]
          elif chop[2].isdigit() and circuit.has_key(chop[0]):
            circuit[chop[-1]] = int(chop[2]) | circuit[chop[0]]
          else:
            continue
            #print line
        elif chop[1] == "LSHIFT":
          if circuit.has_key(chop[0]):
            circuit[chop[-1]] = (circuit[chop[0]] << int(chop[2]))
          else:
            continue
            #print line
        elif chop[1] == "RSHIFT":
          if circuit.has_key(chop[0]):
            circuit[chop[-1]] = (circuit[chop[0]] >> int(chop[2]))
          else:
            continue
            #print line
          
          #clean up a little
          
      
      else:
        print "Error: "+ line +" is an invalid input!"
        break
        
  #a can only have one input - once it exists, yer done
  #for k, v in sorted(circuit.iteritems()):
  #  print k, v,
  return circuit["a"]
  
  
def bobby_logic_2(filename):
  circuit = {}
  circuit["b"] = bobby_logic(filename)
  #^ pre-set the value for b
  #v just copypaste bobby_logic
  input = ""
  #solve for a - loop until it exists
  chop = ""
  while not circuit.has_key("a"):
    input = open(filename, 'rU')
    for line in input:
      chop = line.split()
      #skip every line we did before (that is in circuit{} already)
      if circuit.has_key(chop[-1]):
        continue
      #each command has a fixed length
      elif len(chop) == 3:
        #fill out raw input, ex: "1 -> x"
        if chop[0].isdigit():
          circuit[chop[-1]] = int(chop[0])
        #do "x -> y" if x is assigned
        elif circuit.has_key(chop[0]):
          circuit[chop[-1]] = circuit[chop[0]]
        #skip line for "x -> y" when x is unassigned
        else:
          continue
          #print line + ", where "+chop[-1]+" = "+str(circuit[chop[-1]])
      #...then dig into the logic-y parts
      #needs to accomodate wire names as inputs only from here on in
      #but you need to skip any line if you don't have the values
      elif len(chop) == 4 and chop[0] == "NOT":
        if circuit.has_key(chop[1]):
          #the 0xFFFF de-signs the signed int. ex: "NOT x -> y" will be (-x - 1) unless ANDed with 0xFFFF
          circuit[chop[-1]] = ~int(circuit[chop[1]]) & 0xFFFF
        else:
          continue
          #print line + ", where " + chop[-1] + " = "+str(circuit[chop[-1]]) + " and ~" + chop[1] + " = "+str(~int(circuit[chop[1]]))
      elif len(chop) == 5:
        if chop[1] == "AND":
          if circuit.has_key(chop[0]) and circuit.has_key(chop[2]):
            circuit[chop[-1]] = (circuit[chop[0]] & circuit[chop[2]])
          elif chop[0].isdigit() and circuit.has_key(chop[2]):
            circuit[chop[-1]] = int(chop[0]) & circuit[chop[2]]
          elif chop[2].isdigit() and circuit.has_key(chop[0]):
            circuit[chop[-1]] = int(chop[2]) & circuit[chop[0]]
          else:
            continue
            #print line
        elif chop[1] == "OR":
          if circuit.has_key(chop[0]) and circuit.has_key(chop[2]):
            circuit[chop[-1]] = (circuit[chop[0]] | circuit[chop[2]])
          elif chop[0].isdigit() and circuit.has_key(chop[2]):
            circuit[chop[-1]] = int(chop[0]) | circuit[chop[2]]
          elif chop[2].isdigit() and circuit.has_key(chop[0]):
            circuit[chop[-1]] = int(chop[2]) | circuit[chop[0]]
          else:
            continue
            #print line
        elif chop[1] == "LSHIFT":
          if circuit.has_key(chop[0]):
            circuit[chop[-1]] = (circuit[chop[0]] << int(chop[2]))
          else:
            continue
            #print line
        elif chop[1] == "RSHIFT":
          if circuit.has_key(chop[0]):
            circuit[chop[-1]] = (circuit[chop[0]] >> int(chop[2]))
          else:
            continue
            #print line
          
          #clean up a little
          
      
      else:
        print "Error: "+ line +" is an invalid input!"
        break
        
  #a can only have one input - once it exists, yer done
  #for k, v in sorted(circuit.iteritems()):
  #  print k, v,
  return circuit["a"]
  

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #a_signal = bobby_logic(sys.argv[1])
  #print "Wire A receives the signal " + str(a_signal)
  
  a_signal = bobby_logic_2(sys.argv[1])
  print "Wire A receives the signal " + str(a_signal)

if __name__ == '__main__':
  main()