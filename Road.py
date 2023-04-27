from collections import deque
import numpy as np

class Road:
    def __init__(self, nodes, edges, speed_lim, prio):

        self.prio = prio
        self.nodes = nodes
        self.edges = edges
        self.speed_lim = speed_lim
        self.length = [t[2] * speed_lim for t in edges]

        self.vehicles = [deque() for i in range(len(self.edges))]

        self.init_properties()

    def init_properties(self):
        self.nodes_x = {}
        self.nodes_y = {}

        for key in self.nodes:
            value = self.nodes[key]
            self.nodes_x[key] = value[0]
            self.nodes_y[key] = value[1]

        self.angle_sin = [((self.nodes_y[t[1]] - self.nodes_y[t[0]]) / (t[2] * self.speed_lim)) for t in self.edges]
        self.angle_cos = [((self.nodes_x[t[1]] - self.nodes_x[t[0]]) / (t[2] * self.speed_lim)) for t in self.edges]

        self.traffic_signal_group = [None for i in range(len(self.edges))]
        self.has_traffic_signal = [False for i in range(len(self.edges))]
        self.traffic_signal = [None for i in range(len(self.edges))]

    def set_traffic_signal(self, signal, edge, group):
        self.edge = edge
        for i in self.edges:
            if self.edge == i:
                self.traffic_signal[self.edges.index(i)] = signal
                self.has_traffic_signal[self.edges.index(i)] = True
                self.traffic_signal_group[self.edges.index(i)] = group

    def traffic_signal_state(self, num):
        if self.has_traffic_signal[num]:
            if self.traffic_signal_group[num] is not None:
                j = self.traffic_signal_group[num]
                return self.traffic_signal[num].current_cycle[j]
        return True

    def update(self, dt):
        for i in range(len(self.edges)):
            # check if vehicle has leading vehicle on same street:
            n = len(self.vehicles[i])
            if n > 0:
                self.vehicles[i][0].update(None, None, None, dt)
                for j in range(1, n):
                    lead = self.vehicles[i][j - 1]
                    self.vehicles[i][j].update(lead, None, None, dt)

                if not self.traffic_signal[i] == None:

                    # unslow vehicle if traffic signal is green:
                    if self.traffic_signal_state(i):
                        self.vehicles[i][0].unstop()
                        for vehicle in self.vehicles[i]:
                            vehicle.unslow()

                    # slow/stop vehicle if traffic signal is red:
                    else:
                        for k in range(len(self.traffic_signal[i].roads)):
                            if self.traffic_signal[i].roads[k] == self.edges[i]:
                                if self.vehicles[i][0].x >= self.length[i] - self.traffic_signal[i].slow_distance[k]:
                                    self.vehicles[i][0].slow(self.traffic_signal[i].slow_factor * self.vehicles[i][0].v_max[self.vehicles[i][0].current_edge_index])
                                if self.vehicles[i][0].x >= self.length[i] - self.traffic_signal[i].stop_distance[k] and self.vehicles[i][0].x <= self.length[i] - self.traffic_signal[i].stop_distance[k] / 2:
                                    self.vehicles[i][0].stop()

