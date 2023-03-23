class TrafficSignal:
    def __init__(self, num, sim, roads, config={}):
        self.num = num
        self.sim = sim
        self.roads = roads
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val)
        self.init_properties()

    def init_properties(self):
        for i in self.sim.roads:
            for j in self.roads:
                if j in i.edges:
                    i.set_traffic_signal(self, j, self.num[self.roads.index(j)])

        self.slow_distance = []
        self.stop_distance = []

        for i in self.roads:
            for t in self.sim.roads:
                if i in t.edges:
                    self.slow_distance.append(3 * t.speed_lim)
                    self.stop_distance.append(0.87 * t.speed_lim)


    def set_default_config(self):
        self.cycle = [(False, True), (True, False)]
        self.slow_factor = 0.4

        self.current_cycle_index = 0

        self.last_t = 0

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, sim):
        cycle_length = 20
        k = (sim.t // cycle_length) % 2
        self.current_cycle_index = int(k)
