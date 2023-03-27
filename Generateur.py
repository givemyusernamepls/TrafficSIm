import networkx as nx
import random
from Vehicle import Auto
from numpy.random import randint

class VehicleGenerator:
    def __init__(self, graph, sim, startpoints, endpoints, max_car, config={}):
        self.graph = graph
        self.sim = sim
        self.starts = startpoints
        self.ends = endpoints
        self.max_car = max_car

        self.set_default_config()

        for attr, val in config.items():
            setattr(self, attr, val)

        self.init_properties()

    def set_default_config(self):
        self.vehicle_rate = 20
        self.last_added_time = 0
        self.vehicle_num = 1

    def init_properties(self):
        self.upcoming_vehicle = self.generate_vehicle()

    def generate_vehicle(self):
        s = random.choice(self.starts)
        ends = [i for i in self.ends if i != s]
        e = random.choice(ends)
        path = []
        v_max = []
        pfad = nx.dijkstra_path(self.graph, s, e, weight = 'weight')
        for i in range(len(pfad) - 1):
            for k in self.graph.out_edges(nbunch = pfad[i], data = 'weight'):
                if k[1] == pfad[i + 1]:
                    path.append(k)
        j = random.uniform(-1, 1)
        for i in path:
            for k in self.sim.roads:
                if i in k.edges:
                    v_max.append(k.speed_lim + j)
        l = random.choice([3, 4, 4, 4, 4, 5, 5, 5, 6, 8])
        t = random.uniform(0.9, 1.1)
        if l >= 6:
            a = random.uniform(2, 3)
        else:
            a = random.uniform(3, 4)
        return Auto(self.graph, self.sim, {"path": path, "v_max": v_max, "l": l, "s0": l, "T": t, "a_max": a})


    def update(self):
        if self.sim.t - self.last_added_time >= 60 / self.vehicle_rate:
            for i in range(len(self.sim.roads)):
                if self.upcoming_vehicle.path[0] in self.sim.roads[i].edges:
                    road = self.sim.roads[i].edges.index(self.upcoming_vehicle.path[0])
                    if len(self.sim.roads[i].vehicles[road]) == 0 or self.sim.roads[i].vehicles[road][-1].x > self.upcoming_vehicle.s0 + self.upcoming_vehicle.l:
                        self.upcoming_vehicle.time_added = self.sim.t
                        if self.max_car == None:
                            self.sim.roads[i].vehicles[road].append(self.upcoming_vehicle)
                        elif self.vehicle_num <= self.max_car:
                            self.sim.roads[i].vehicles[road].append(self.upcoming_vehicle)
                            self.vehicle_num += 1
                        self.last_added_time = self.sim.t
                    self.upcoming_vehicle = self.generate_vehicle()
