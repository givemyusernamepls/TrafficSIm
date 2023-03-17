import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from scipy.spatial import distance
from Road import *
from Vehicle import *
from Winodw import *
from Simulation import *
from Map import *


sim = Simulation()
sim.create_road(ort, strecken_G, G_speed_lim, 0)
sim.create_road(ort, strecken_H, H_speed_lim, 2)
sim.create_road(ort, strecken_K, K_speed_lim, 1)
sim.roads[0].vehicles[0].append(
  Vehicle(I, sim, {"path": [strecken_G[0]] + [strecken_H[1]], "v_max": [G_speed_lim, H_speed_lim]})
 )
sim.roads[1].vehicles[0].append(
 Vehicle(I, sim, {"path": strecken_H[:2], "v_max": [H_speed_lim, H_speed_lim]})
)
sim.roads[2].vehicles[0].append(
 Vehicle(I, sim, {"path": strecken_K + [strecken_H[2]], "v_max": [K_speed_lim, H_speed_lim]})
)
sim.roads[1].vehicles[3].append(
 Vehicle(I, sim, {"path": [strecken_H[3], strecken_H[2]], "v_max": [H_speed_lim, H_speed_lim]})
)
win = Window(sim)

win.run(steps_per_update = 3)
