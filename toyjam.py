import codejam.utils.codejamrunner as cjr
import itertools
import networkx as nx

class Dynam(object):pass

def solve(data):
    max_score = 0
    options = [[data.boxes, data.toys, 0]]
    count = 0
    
    while options:
        bx, t, s = options.pop()

        if (bx[0][1] == t[0][1]):
              sim = min(bx[0][0], t[0][0])
              s += sim

              bx[0] = [bx[0][0] -sim, bx[0][1]]
              t[0] = [t[0][0] -sim, t[0][1]]

              if bx[0][0] == 0:
                  bx = bx[1:]
              elif t[0][0] == 0:
                  t = t[1:]
                  
        if len(bx) == 0 or len(t) == 0:
            if s > max_score:
                #print 'replacing max_score (%s) with %s' % (max_score, s)
                max_score = s
        else:
            if len(t) > 1:
                options.append([bx[:], t[1:], s])
            else:
                if s > max_score:
                    #print 'replacing max_score (%s) with %s' % (max_score, s)
                    max_score = s
            if len(bx) >1:
                options.append([bx[1:], t[:], s])
            else:
                if s > max_score:
                    #print 'replacing max_score (%s) with %s' % (max_score, s)
                    max_score = s

        count += 1

    #print count
    #import pdb;pdb.set_trace()      
    return max_score
   

def builder(f):
    #(count, type)
    
    data = Dynam()
    data.b, data.t = f.get_ints()
    boxes = f.get_ints()
    toys = f.get_ints()
    data.boxes = []
    data.toys = []
    
    for i in range(data.b):
      data.boxes.append([boxes[2*i], boxes[2*i + 1]])  

    for i in range(data.t):
      data.toys.append([toys[2*i], toys[2*i + 1]])  
    #import pdb;pdb.set_trace()
    return data
  

cjr = cjr.CodeJamRunner()
cjr.run(builder, solve, problem_name = "C", problem_size='small-practice')
