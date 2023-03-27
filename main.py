import matplotlib
matplotlib.use('TkAgg')
from Winodw import *
from Simulation import *
from Map import *


sim = Simulation(I)

sim.create_road(ort, strecken_H, H_speed_lim, 0)
sim.create_road(ort, strecken_G, G_speed_lim, 1)
sim.create_road(ort, strecken_K, K_speed_lim, 1)

sim.create_signal([2])

sim.create_gen(I, starts, ends, 50, {'vehicle_rate': 20})


#sim.roads[1].vehicles[0].append(
#    Auto(I, sim, {"path": [strecken_G[0], strecken_K[1]], "v_max": [G_speed_lim, K_speed_lim]})
#)
#sim.roads[2].vehicles[0].append(
#    Auto(I, sim, {"path": [strecken_K[0], strecken_G[1]], "v_max": [G_speed_lim, K_speed_lim]})
#)



win = Window(sim)

win.run(steps_per_update=5)
