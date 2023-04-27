import numpy as np

class Auto:
    def __init__(self, graph, sim, config={}):

        self.graph = graph
        self.sim = sim
        self.set_default_config()

        # possibility to edit default config:
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
        c = 0
        for i in self.v_max:
            c += 1
        if c != (self.current_edge_index + 1):
            if self.v_max[self.current_edge_index + 1] < self.v_max[self.current_edge_index]:
                self.slow(self.v_max[self.current_edge_index + 1])
        # find all incoming streets to the intersect the street currently driving on leads to:
        for t in self.graph.in_edges(nbunch = self.path[self.current_edge_index][1], data = 'weight'):
            # find corresponding road and set index:
            for i in range(len(self.sim.roads)):
                if self.path[self.current_edge_index] in self.sim.roads[i].edges:
                    k = i
            # check if has to give way:
            for i in self.sim.roads:
                if self.sim.roads[k].prio < i.prio:
                    continue
                elif t == self.path[self.current_edge_index]:
                    continue
                elif self.sim.roads[k].prio == i.prio:
                    if t in i.edges:
                        if i == self.sim.roads[k]:
                            if c != (self.current_edge_index + 1):
                                # if streets are on the same road, set giving way priority to lower index in given road:
                                if not (t[0], t[1]) == (self.path[self.current_edge_index + 1][1], self.path[self.current_edge_index + 1][0]):
                                    if i.edges.index(t) < i.edges.index(self.path[self.current_edge_index]):
                                        continue
                                    else:
                                        # use dynamic braking equation to slow down:
                                        for car in i.vehicles[i.edges.index(t)]:
                                            if i.length[i.edges.index(t)] - car.x <= car.v * 2:
                                                self.a = -self.b_max * self.v / self._v_max - 0.2
                            else:
                                if i.speed_lim < self.sim.roads[k].speed_lim:
                                    continue
                                else:
                                    # use dynamic braking equation to slow down:
                                    for car in i.vehicles[i.edges.index(t)]:
                                        if i.length[i.edges.index(t)] - car.x <= car.v * 2:
                                            self.a = -self.b_max * self.v / self._v_max - 0.2
                # use dynamic braking equation to slow down:
                elif t in i.edges:
                    for car in i.vehicles[i.edges.index(t)]:
                        if i.length[i.edges.index(t)] - car.x <= car.v * 2:
                            self.a = -self.b_max * self.v / self._v_max - 0.2

    def update(self, lead, leadnext, len, dt):
        # when encountering negative speeds, set speed to 0:
        if self.v + self.a * dt < 0:
            self.x -= 1 / 2 * self.v * self.v / self.a
            self.v = 0
        else:
            # use basic movement equation:
            self.v += self.a * dt
            self.x += self.v * dt + self.a * dt * dt / 2

        alpha = 0
        # if has a car in front implement IDM for leading car:
        # car in front on same street:
        if lead:
            delta_x = lead.x - self.x - lead.l
            delta_v = self.v - lead.v

            alpha = (self.s0 + max(0, self.T * self.v + delta_v * self.v / self.sqrt_ab)) / delta_x
            # if following a car for longer, adapt their max speed:
            c = 0
            d = 0
            for i in self.path:
                c += 1
            for i in lead.path:
                d += 1
            if c != (self.current_edge_index + 1):
                if d != (lead.current_edge_index + 1):
                    if lead.path[lead.current_edge_index + 1] == self.path[self.current_edge_index + 1]:
                        self.slow(lead._v_max)
                    else:
                        self.unslow()

        # car in front on next street:
        if leadnext:
            # if car speed on next street is lower than maximum speed of self on current road, set it to lead car:
            if leadnext.v < self.v_max[self.current_edge_index]:
                delta_x = leadnext.x + len - self.x - leadnext.l
                delta_v = self.v - leadnext.v

                alpha = (self.s0 + max(0, self.T * self.v + (delta_v * self.v / self.sqrt_ab))) / delta_x

        self.a = self.a_max * (1 - (self.v / self._v_max) ** 4 - alpha ** 2)

        # stop car:
        if self.stopped:
            self.a = -self.b_max * self.v / self._v_max - 0.2

        # start check if has to give way:
        if self.kreuzung:
            self.vorfahrt()

    def stop(self):
        self.stopped = True
        self.kreuzung = False

    def unstop(self):
        self.stopped = False
        self.kreuzung = True

    def slow(self, v):
        self._v_max = v
        self.kreuzung = False

    def unslow(self):
        self._v_max = self.v_max[self.current_edge_index]
        self.kreuzung = True



