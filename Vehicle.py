import numpy as np
from Road import Road
from Simulation import *

class Vehicle:
    def __init__(self, graph, sim, config={}):

        self.graph = graph
        self.sim = sim
        self.set_default_config()

        for attr, val in config.items():
            setattr(self, attr, val)

        self.init_properties()

    def set_default_config(self):
        self.l = 4
        self.s0 = 4
        self.T = 1
        self.v_max = []
        self.a_max = 3
        self.b_max = 7

        self.path = []
        self.current_road_index = 0
        self.current_edge_index = 0

        self.x = 0
        self.a = 0
        self.stopped = False
        self.kreuzung = False

    def init_properties(self):
        self.sqrt_ab = 2*np.sqrt(self.a_max*self.b_max)
        self._v_max = self.v_max[self.current_edge_index]
        self.v = self.v_max[self.current_edge_index]

    def vorfahrt(self):
        for t in self.graph.in_edges(nbunch = self.path[self.current_edge_index][1], data = 'weight'):
            for i in range(len(self.sim.roads)):
                if self.path[self.current_edge_index] in self.sim.roads[i].edges:
                    k = i
            for i in self.sim.roads:
                if self.sim.roads[k].prio < i.prio:
                    continue
                elif t == self.path[self.current_edge_index]:
                    continue
                elif self.sim.roads[k].prio == i.prio:
                    if t in i.edges:
                        if not (t[0], t[1]) == (self.path[self.current_edge_index + 1][1], self.path[self.current_edge_index + 1][0]):
                            if i.edges.index(t) < i.edges.index(i.edges[self.current_edge_index]):
                                continue
                            else:
                                for car in i.vehicles[i.edges.index(t)]:
                                    if i.length[i.edges.index(t)] - car.x <= car.v * 2:
                                        self.a = -self.b_max * self.v / self._v_max - 0.1337
                elif t in i.edges:
                    for car in i.vehicles[i.edges.index(t)]:
                        if i.length[i.edges.index(t)] - car.x <= car.v * 2:
                            self.a = -self.b_max * self.v / self._v_max - 0.1337


    def update(self, lead, dt):
        if self.v + self.a * dt < 0:
            self.x -= 1 / 2 * self.v * self.v / self.a
            self.v = 0
        else:
            self.v += self.a * dt
            self.x += self.v * dt + self.a * dt * dt / 2

        alpha = 0
        if lead:
            delta_x = lead.x - self.x - lead.l
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T * self.v + delta_v * self.v / self.sqrt_ab)) / delta_x

        self.a = self.a_max * (1 - (self.v / self._v_max) ** 4 - alpha ** 2)

        if self.stopped:
            self.a = -self.b_max * self.v / self._v_max - 0.1337

        if self.kreuzung:
            self.vorfahrt()

    def stop(self):
        self.stopped = True
        self.kreuzung = False

    def unstop(self):
        self.stopped = False
        self.kreuzung = True

    def slow(self, v):
        self.v_max = v

    def unslow(self):
        self.v_max = self._v_max