import matplotlib
matplotlib.use('TkAgg')
from Winodw import *
from Simulation import *
from Map import *


sim = Simulation(I)

sim.create_road(ort, strecken_H, H_speed_lim, 0)
sim.create_road(ort, strecken_G, G_speed_lim, 1)
sim.create_road(ort, strecken_K, K_speed_lim, 1)

#sim.create_signal([2])

sim.create_gen(I, starts, ends)

#sim.roads[0].vehicles[0].append(
#    Auto(I, sim, {"path": [strecken_H[0], strecken_G[1]], "v_max": [H_speed_lim, G_speed_lim]})
#)

win = Window(sim)

win.run(steps_per_update=2)
