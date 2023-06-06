from datetime import date

from interfaces import Car
from model import calliope
from model import glissade
from model import palindrome
from model import rorschach
from model import thovex
from engine import capulet_engine
from engine import sternman_engine
from engine import willoughby_engine
from battery import spindler_battery
from battery import nubbin_battery
from tires import carrigan_tires
from tires import octoprime_tires

"""
current_date: date
last_service_date: date
current_mileage: int
last_service_mileage: int
warning_light_on: bool
tire_sensors: list
"""

class MakeCar():
	def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
		car = calliope.Calliope(last_service_date)
		car.engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
		car.battery = spindler_battery.SpindlerBattery(last_service_date)
		car.tire = carrigan_tires.CarriganTires(tire_sensors)
		return car

	def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
		car = glissade.Glissade(last_service_date)
		car.engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
		car.battery = spindler_battery.SpindlerBattery(last_service_date)
		car.tire = carrigan_tires.CarriganTires(tire_sensors)
		return car

	def create_palindrome(self, current_date, last_service_date, warning_light_on, tire_sensors) -> Car:
		car = palindrome.Palindrome(last_service_date)
		car.engine = sternman_engine.SternmanEngine(warning_light_on)
		car.battery = spindler_battery.SpindlerBattery(last_service_date)
		car.tire = carrigan_tires.CarriganTires(tire_sensors)
		return car

	def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
		car = rorschach.Rorschach(last_service_date)
		car.engine = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
		car.battery = nubbin_battery.NubbinBattery(last_service_date)
		car.tire = octoprime_tires.OctoprimeTires(tire_sensors)
		return car

	def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_sensors) -> Car:
		car = thovex.Thovex(last_service_date)
		car.engine = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
		car.battery = nubbin_battery.NubbinBattery(last_service_date)
		car.tire = octoprime_tires.OctoprimeTires(tire_sensors)
		return car