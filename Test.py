elif self.sim.roads[k].prio == i.prio:
if t in i.edges:
    if i.edges.index(t) > i.edges.index(i.edges[self.current_edge_index]):
        continue
    else:
        for car in i.vehicles[i.edges.index(t)]:
            if i.length[i.edges.index(t)] - car.x <= car.v * 2:
                self.a = -self.b_max * self.v / self._v_max - 0.1337