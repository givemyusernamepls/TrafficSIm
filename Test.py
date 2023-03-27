if self.max_car == - 1:
    self.sim.roads[i].vehicles[road].append(self.upcoming_vehicle)
elif self.vehicle_num >= self.max_car:
    self.sim.roads[i].vehicles[road].append(self.upcoming_vehicle)
    self.vehicle_num += 1