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

        self.has_traffic_signal = [False for i in range(len(self.edges))]

    def set_traffic_signal(self, signal, group):
        self.traffic_signal = signal
        self.traffic_signal_group = group
        self.has_traffic_signal = True

    @property
    def traffic_signal_state(self):
        if self.has_traffic_signal:
            i = self.traffic_signal_group
            return self.traffic_signal.current_cycle[i]
        return True

    def update(self, dt):
        for i in range(len(self.edges)):
            n = len(self.vehicles[i])
            if n > 0:
                self.vehicles[i][0].update(None, dt)
                for j in range(1, n):
                    lead = self.vehicles[i][j - 1]
                    self.vehicles[i][j].update(lead, dt)

                if self.traffic_signal_state:
                    self.vehicles[i][0].unstop()
                    for vehicle in self.vehicles[i]:
                        vehicle.unslow()
                else:
                    if self.vehicles[i][0].x >= self.length[i] - self.traffic_signal.slow_distance:
                        self.vehicles[i][0].slow(self.traffic_signal.slow_factor * self.vehicles[i][0]._v_max)
                    if self.vehicles[i][0].x >= self.length[i] - self.traffic_signal.stop_distance and self.vehicles[i][0].x <= self.length[i] - self.traffic_signal.stop_distance / 2:
                        self.vehicles[i][0].stop()