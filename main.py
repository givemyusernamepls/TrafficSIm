import matplotlib
matplotlib.use('TkAgg')
from Winodw import *
from Simulation import *
from Map import *

# create simulation:
sim = Simulation(I, {'stop_time': 0})

# add roads (subgraphs) to simulation:
sim.create_road(ort, strecken_R_50, lim_50, 0)
sim.create_road(ort, strecken_R_70, lim_70, 0)
sim.create_road(ort, strecken_O_50, lim_50, 1)
sim.create_road(ort, strecken_O_30, lim_30, 1)
sim.create_road(ort, strecken_Y_50, lim_50, 2)
sim.create_road(ort, strecken_Y_30, lim_30, 2)
sim.create_road(ort, strecken_G_50, lim_50, 3)
sim.create_road(ort, strecken_G_30, lim_30, 3)
sim.create_road(ort, strecken_B, lim_30, 4)
sim.create_road(ort, strecken_P, lim_30, 5)


# create traffic signals:
sim.create_signal(['Y2', 'O2', 'O3', 'O5', 'G10', 'O6', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'O9', 'Y14', 'Y16', 'O19', 'O21', 'O22', 'O11', 'O15',
                   'G46', 'Y24', 'G36', 'Y32', 'Y30', 'Y28', 'Y26', 'G49', 'R9', 'O25'])

# create vehicle generator:
sim.create_gen(I, starts, ends, 5, {'vehicle_rate': 200})

# manually add vehicles:


# create and start visual simulation:
win = Window(sim, {'zoom': 0.35, 'offset': (-1700, 1270)})
win.run(steps_per_update=60)
