import networkx as nx
import random
from Vehicle import Auto
import numpy as np

class VehicleGenerator:
    def __init__(self, graph, sim, startpoints, endpoints, max_car, config={}):
        self.graph = graph
        self.sim = sim
        self.starts = startpoints
        self.ends = endpoints
        self.max_car = max_car

        self.set_default_config()

        # possibility to edit default config:
        for attr, val in config.items():
            setattr(self, attr, val)

        self.init_properties()

    def set_default_config(self):
        self.vehicle_rate = 20
        self.last_added_time = 0.00000000001
        self.vehicle_num = 1

    def init_properties(self):
        self.upcoming_vehicle = self.generate_vehicle()

    def generate_vehicle(self):
        # set start end end points for next vehicle:
        s = random.choice(self.starts)
        ends = [i for i in self.ends if i != s]
        e = random.choice(ends)
        path_1 = []
        v_max_1 = []

        # find path for given start and endpoints:
        pfad = nx.dijkstra_path(self.graph, s, e, weight = 'weight')
        for i in range(len(pfad) - 1):
            for k in self.graph.out_edges(nbunch = pfad[i], data = 'weight'):
                if k[1] == pfad[i + 1]:
                    path_1.append(k)

        # randomly set vehicle config:
        l = random.choice([3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 12])
        t = random.uniform(0.8, 1.2)

        if l > 6:
            a = random.uniform(2, 3)
            j = random.uniform(-0.3, 0.05)
        elif l == 6:
            a = random.uniform(2.5, 3.5)
            j = random.uniform(-0.2, 0.2)
        else:
            a = random.uniform(3, 5)
            j = random.uniform(-0.2, 0.3)

        for i in path_1:
            for k in self.sim.roads:
                if i in k.edges:
                    v_max_1.append(k.speed_lim + k.speed_lim * j)

        return Auto(self.graph, self.sim, {"path": path_1, "v_max": v_max_1, "l": l, "s0": l, "T": t, "a_max": a})


    def update(self):
        # add vehicles:
        # generate vehicle if enough time has elapsed:
        if self.sim.t - self.last_added_time + 0.000001 >= 60 / self.vehicle_rate:
            added = False
            while not added:
                for i in range(len(self.sim.roads)):
                    if self.upcoming_vehicle.path[0] in self.sim.roads[i].edges:
                        road = self.sim.roads[i].edges.index(self.upcoming_vehicle.path[0])
                        # check if there is enough space on the street to add vehicle:
                        if len(self.sim.roads[i].vehicles[road]) == 0 or self.sim.roads[i].vehicles[road][-1].x > self.upcoming_vehicle.s0 + self.upcoming_vehicle.l:
                            # if given maximum vehicle count, check if next vehicle would exceed that limit and add vehicle:
                            if self.max_car == None:
                                self.last_added_time = self.sim.t
                                self.sim.roads[i].vehicles[road].append(self.upcoming_vehicle)
                                print(self.sim.t)
                                added = True
                                self.vehicle_num += 1
                                self.upcoming_vehicle = self.generate_vehicle()
                                break
                            elif self.vehicle_num <= self.max_car:
                                self.last_added_time = self.sim.t
                                self.sim.roads[i].vehicles[road].append(self.upcoming_vehicle)
                                print(self.sim.t)
                                added = True
                                self.vehicle_num += 1
                                self.upcoming_vehicle = self.generate_vehicle()
                                break
                        # generate new vehicle if there is not enough space on road:
                        else:
                            self.upcoming_vehicle = self.generate_vehicle()
