import codejam.utils.codejamrunner as cjr
import itertools
import networkx as nx

class Dynam(object):pass

def calc_time(distance, accel):
    return (2.0 *distance / accel)**0.5

def simplify_other_car_locations(sunday_speeds, distance):
    
    while sunday_speeds:
        if len(sunday_speeds) == 1:
            sunday_speeds[0][1] = distance
            return
    
        if sunday_speeds[-1][1] == distance:
            return
        if sunday_speeds[-2][1] < distance:
            last = sunday_speeds.pop()
            lb1 = sunday_speeds[-1]
            t = ((last[0]- lb1[0])*(distance - lb1[1])/(last[1] - lb1[1])) + lb1[0]
            new_final = [t, distance]
            sunday_speeds.append(new_final)
            #import pdb;pdb.set_trace()
            return
        else:
            sunday_speeds.pop()



def solve(data):
    
    simplify_other_car_locations(data.sunday_speeds, data.distance)
    results = ['']
    for a in data.accels:
        delay = 0
        for time, pos in data.sunday_speeds[::-1]:
            finish_time = calc_time(pos, a)
            if finish_time < time and delay < (time - finish_time):
                delay = time-finish_time
        results.append(calc_time(data.distance, a) + delay)

    return '\n'.join([str(x) for x in results])
        
                
            
   

def builder(f):
    data = Dynam()
    data.distance, data.n, data.a = f.get_floats()
    data.n = int(data.n)
    data.a = int(data.a)
    data.sunday_speeds = f.get_float_grid(data.n)
    data.accels = f.get_floats()

    return data
  
    



cjr = cjr.CodeJamRunner()
cjr.run(builder, solve, problem_name = "B", problem_size='large-practice')
