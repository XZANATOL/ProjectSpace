import unittest

from tires import carrigan_tires
from tires import octoprime_tires

class TestCarrigan(unittest.TestCase):
	def test_needs_service(self):
		sensors_status = [1, 0, 0.3, 0.5]

		tires = carrigan_tires.CarriganTires(sensors_status)
		self.assertTrue(tires.needs_service())

	def test_doesnt_needs_service(self):
		sensors_status = [0.8, 0, 0.3, 0.5]

		tires = carrigan_tires.CarriganTires(sensors_status)
		self.assertFalse(tires.needs_service())


class TestOctoprime(unittest.TestCase):
	def test_needs_service(self):
		sensors_status = [1, 1, 1, 0]

		tires = octoprime_tires.OctoprimeTires(sensors_status)
		self.assertTrue(tires.needs_service())

	def test_doesnt_needs_service(self):
		sensors_status = [1, 1, 0.3, 0]

		tires = octoprime_tires.OctoprimeTires(sensors_status)
		self.assertFalse(tires.needs_service()) 