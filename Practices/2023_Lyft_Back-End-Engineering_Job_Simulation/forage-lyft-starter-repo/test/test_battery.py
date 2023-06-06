from datetime import date
import unittest

from battery import nubbin_battery
from battery import spindler_battery

class TestNubbin(unittest.TestCase):
	def test_needs_service(self):
		last_service_date = date(2017, 5, 2)

		battery = nubbin_battery.NubbinBattery(last_service_date)
		self.assertTrue(battery.needs_service())

	def test_doesnt_needs_service(self):
		last_service_date = date(2022, 5, 2)

		battery = nubbin_battery.NubbinBattery(last_service_date)
		self.assertFalse(battery.needs_service())


class TestSpindler(unittest.TestCase):
	def test_needs_service(self):
		last_service_date = date(2017, 5, 2)

		battery = spindler_battery.SpindlerBattery(last_service_date)
		self.assertTrue(battery.needs_service())

	def test_doesnt_needs_service(self):
		last_service_date = date(2022, 5, 2)

		battery = spindler_battery.SpindlerBattery(last_service_date)
		self.assertFalse(battery.needs_service())