import copy

from Road import *
from Ampel import *
from Generateur import *
from operator import attrgetter
from copy import deepcopy

class Simulation:
    def __init__(self,graph, config={}):
        self.graph = graph
        self.set_default_config()

        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0
        self.frame_count = 0
        self.dt = 1/60
        self.roads = []
        self.generators = []
        self.traffic_signals = []

    def create_road(self, nodes, edges, speed_lim, prio):
        road = Road(nodes, edges, speed_lim, prio)
        self.roads.append(road)

    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_signal(self, nodes, config={}):
        for i in nodes:
            roads = [e for e in self.graph.in_edges(nbunch = i, data = 'weight')]
            num = []
            prio = []
            for j in range(len(roads)):
                for k in range(len(self.roads)):
                    if roads[j] in self.roads[k].edges:
                        prio.append(self.roads[k].prio)
            for j in range(len(roads)):
                for k in range(len(self.roads)):
                    if roads[j] in self.roads[k].edges:
                        if prio[j] == min(prio):
                            num.append(1)
                        else:
                            num.append(0)
            sig = TrafficSignal(num, self, roads, config)
            self.traffic_signals.append(sig)

    def create_gen(self, graph, startpoints, endpoints, config={}):
        gen = VehicleGenerator(graph, self, startpoints, endpoints, config)
        self.generators.append(gen)

    def update(self):
        for road in self.roads:
            road.update(self.dt)

        for signal in self.traffic_signals:
            signal.update(self)

        for gen in self.generators:
            gen.update()

        for i in range(len(self.roads)):
            for j in range(len(self.roads[i].edges)):
                if len(self.roads[i].vehicles[j]) == 0: continue
                vehicle = self.roads[i].vehicles[j][0]
                if self.roads[i].length[j] - vehicle.x <= vehicle.v * 2:
                    vehicle.kreuzung = True
                if vehicle.x >= self.roads[i].length[j]:
                    vehicle.current_road_index += i
                    vehicle.current_edge_index = vehicle.path.index(self.roads[i].edges[j]) + 1
                    new_vehicle = copy.copy(vehicle)
                    new_vehicle.x = 0
                    if vehicle.current_edge_index == len(vehicle.path):
                        self.roads[i].vehicles[self.roads[i].edges.index(vehicle.path[vehicle.current_edge_index - 1])].popleft()
                        continue
                    elif vehicle.path[vehicle.current_edge_index] in self.roads[i].edges:
                        self.roads[vehicle.current_road_index].vehicles[self.roads[i].edges.index(vehicle.path[vehicle.current_edge_index])].append(new_vehicle)
                        new_vehicle.unstop()
                        new_vehicle.unslow()
                    else:
                        for k in range(len(self.roads)):
                            if vehicle.path[vehicle.current_edge_index] in self.roads[k].edges:
                                vehicle.current_road_index = k
                                self.roads[vehicle.current_road_index].vehicles[self.roads[k].edges.index(vehicle.path[vehicle.current_edge_index])].append(new_vehicle)
                                new_vehicle.unstop()
                                new_vehicle.unslow()
                    self.roads[i].vehicles[j].popleft()

        self.t += self.dt
        self.frame_count += 1

    def run(self, steps):
        for _ in range(steps):
            self.update()