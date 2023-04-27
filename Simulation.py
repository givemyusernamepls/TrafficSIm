import copy
from Road import *
from Ampel import *
from Generateur import *
import matplotlib.pyplot as plt
from operator import attrgetter
from copy import deepcopy
import time

class Simulation:
    def __init__(self, graph, nodes_dict, config={}):
        self.graph = graph
        self.nodes_dict = nodes_dict
        self.set_default_config()

        # possibility to edit default config:
        for attr, val in config.items():
            setattr(self, attr, val)

    def set_default_config(self):
        self.t = 0.0
        self.frame_count = 0
        self.dt = 1/10
        self.roads = []
        self.generators = []
        self.traffic_signals = []
        self.stop_per_sec = []
        self.stop_time = 0
        self.vehicle_count = 0
        self.which_node = {}
        for key in self.nodes_dict:
            self.which_node[key] = 0
        print(self.which_node)

    def create_road(self, nodes, edges, speed_lim, prio):
        road = Road(nodes, edges, speed_lim, prio)
        self.roads.append(road)

    def create_roads(self, road_list):
        for road in road_list:
            self.create_road(*road)

    def create_signal(self, nodes, config={}):
        for i in nodes:
            # list streets for each traffic signal:
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
            # create traffic signal with above set properties:
            sig = TrafficSignal(num, self, roads, config)
            self.traffic_signals.append(sig)

    def create_gen(self, graph, startpoints, endpoints, max_car, config={}):
        gen = VehicleGenerator(graph, self, startpoints, endpoints, max_car, config)
        self.generators.append(gen)

    def time(self, stopped):
        if self.t >= self.stop_time and self.stop_time != 0:
            liste_stoped = []
            c = 0
            d = 0
            for i in self.stop_per_sec:
                c += i
                d += 1
                if d == 10:
                    c /= d
                    liste_stoped.append(c)
                    d = 0
                    c = 0
            l = liste_stoped
            p = len(l)
            T = np.arange(0, int(self.t), int(self.t) / p)
            plt.ylabel('Durchschnittswert der pro Sekunde stehenden Autos')
            plt.xlabel('Zeit in Sekunden')
            plt.plot(T, l, '-', color='k')
            plt.suptitle('Mittelwert der pro Sekunde stehenden Autos über die Zeit')
            plt.title(f'Straßennetz mit r= 100 und insgesamt {self.vehicle_count} passierten Autos')
            plt.ylim(-0.25, max(liste_stoped) + 10)
            plt.show()
            print(self.which_node)
            ABBRUCH()

        else:
            self.stop_per_sec.append(stopped)
            self.stopped = 0
            self.t += self.dt
            self.frame_count += 1

    def num(self, stopped):
        if self.t >= 10:
            if vehicles == 0:
                liste_stoped = []
                c = 0
                d = 0
                for i in self.stop_per_sec:
                    c += i
                    d += 1
                    if d == 10:
                        c /= d
                        liste_stoped.append(c)
                        d = 0
                        c = 0
                print(self.t)
                print(self.which_node)
                print(liste_stoped)
                ABBRUCH()

            else:
                self.stop_per_sec.append(stopped)
                self.stopped = 0
                self.t += self.dt
                self.frame_count += 1

    def update(self):
        stopped = 0
        for road in self.roads:
            road.update(self.dt)

        for signal in self.traffic_signals:
            signal.update(self)

        for gen in self.generators:
            gen.update()

        vehicles = 0
        for i in range(len(self.roads)):
            for j in range(len(self.roads[i].edges)):
                # count topped vehicles:
                for auto in self.roads[i].vehicles[j]:
                    if auto.v == 0:
                        stopped += 1
                        self.which_node[self.roads[i].edges[j][1]] += 1/10

                # update and count first vehicle on each street:
                if len(self.roads[i].vehicles[j]) == 0:
                    continue
                vehicle = self.roads[i].vehicles[j][0]
                vehicles += 1
                # if vehicle is in close proximity of intersect set lead to first car on next street and activate giving way:
                if self.roads[i].length[j] - vehicle.x <= vehicle.v * 3:
                    vehicle.kreuzung = True
                    if not vehicle.current_edge_index + 1 == len(vehicle.path):
                        r = 0
                        e = 0
                        for road in self.roads:
                            if vehicle.path[vehicle.current_edge_index + 1] in road.edges:
                                r = self.roads.index(road)
                                e = self.roads[r].edges.index(vehicle.path[vehicle.current_edge_index + 1])
                        if not len(self.roads[r].vehicles[e]) == 0:
                            v = len(self.roads[r].vehicles[e])
                            if self.roads[r].vehicles[e][v - 1].x <= vehicle.v * 0.5:
                                vehicle.update(None, self.roads[r].vehicles[e][v - 1], self.roads[i].length[j], self.dt)
                # check if vehicle has exceeded street length and if so, add to next street and remove from current one:
                if vehicle.x >= self.roads[i].length[j]:
                    vehicle.current_road_index += i
                    vehicle.current_edge_index = vehicle.path.index(self.roads[i].edges[j]) + 1
                    new_vehicle = copy.copy(vehicle)
                    new_vehicle.x = 0
                    if vehicle.current_edge_index == len(vehicle.path):
                        self.roads[i].vehicles[self.roads[i].edges.index(vehicle.path[vehicle.current_edge_index - 1])].popleft()
                        self.vehicle_count += 1
                        continue
                    elif vehicle.path[vehicle.current_edge_index] in self.roads[i].edges:
                        self.roads[i].vehicles[self.roads[i].edges.index(vehicle.path[vehicle.current_edge_index])].append(new_vehicle)
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
        # stopping simulation after time/vehicle count parameter and print list with amount of stopped vehicles per time step:
        self.time(stopped)

        # self.num(stopped)

    def run(self, steps):
        for _ in range(steps):
            self.update()