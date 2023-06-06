import unittest

from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine

class TestCapulet(unittest.TestCase):
	def test_needs_service(self):
		current_mileage = 60000
		last_service_mileage = 20000

		engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.needs_service())

	def test_doesnt_needs_service(self):
		current_mileage = 60000
		last_service_mileage = 40000

		engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.needs_service())


class TestSternman(unittest.TestCase):
	def test_needs_service(self):
		warning_light_is_on = True

		engine = sternman_engine.SternmanEngine(warning_light_is_on)
		self.assertTrue(engine.needs_service())

	def test_doesnt_needs_service(self):
		warning_light_is_on = False

		engine = sternman_engine.SternmanEngine(warning_light_is_on)
		self.assertFalse(engine.needs_service())


class TestWilloughby(unittest.TestCase):
	def test_needs_service(self):
		current_mileage = 120000
		last_service_mileage = 50000

		engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertTrue(engine.needs_service())

	def test_doesnt_needs_service(self):
		current_mileage = 120000
		last_service_mileage = 70000

		engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
		self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()