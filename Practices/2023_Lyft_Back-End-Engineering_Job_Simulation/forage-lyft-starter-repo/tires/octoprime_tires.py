from interfaces import Tire

class OctoprimeTires(Tire):
	def needs_service(self):
		if sum(self.sensors_status) >= 3:
			return True
		return False