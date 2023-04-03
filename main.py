import matplotlib
matplotlib.use('TkAgg')
from Winodw import *
from Simulation import *
from Map import *

# create simulation:
sim = Simulation(I, {'stop_time': 0})

# add roads (subgraphs) to simulation:


# create traffic signals:
#sim.create_signal([2])

# create vehicle generator:
sim.create_gen(I, starts, ends, 50, {'vehicle_rate': 20})

# manually add vehicles:


# create and start visual simulation:
win = Window(sim)
win.run(steps_per_update=2)
