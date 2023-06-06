from interfaces import Tire

class CarriganTires(Tire):
	def needs_service(self):
		if any([
			0.9 in self.sensors_status,
			1 in self.sensors_status
			]):
			return True
		return False