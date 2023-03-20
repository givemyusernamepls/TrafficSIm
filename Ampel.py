class TrafficSignal:
    def __init__(self, num, sim, roads, config={}):
        self.num = num
        self.sim = sim
        self.roads = roads
        self.set_default_config()
        for attr, val in config.items():
            setattr(self, attr, val)
        self.init_properties()

    def set_default_config(self):
        self.cycle = [(False, True), (True, False)]
        self.slow_distance = 50
        self.slow_factor = 0.5
        self.stop_distance = 15

        self.current_cycle_index = 0

        self.last_t = 0

    def init_properties(self):
        for i in self.sim.roads:
            for j in self.roads:
                if j in i.edges:
                    i.set_traffic_signal(self, j, self.num)

    @property
    def current_cycle(self):
        return self.cycle[self.current_cycle_index]

    def update(self, sim):
        cycle_length = 30
        k = (sim.t // cycle_length) % 2
        self.current_cycle_index = int(k)
