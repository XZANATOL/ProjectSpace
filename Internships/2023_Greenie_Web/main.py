from time import sleep
from math import ceil
import subprocess
import psutil
import json
import sys
import re

platform: str = sys.platform

if platform == "win32":
	import wmi

db: dict = {}
cpu_model: str
cpu_average_consumption: int
ram_capacity: int
ram_average_consumption: int

def read_process_from_task_manager() -> None:
	"""
	Read & Print running processes from task manager/monitor
	and load them into global variable 'processes'
	"""
	global processes
	print("====================================")
	for process in psutil.process_iter():
		print(f"{process.pid:5} {process.name()}")
	print("\n", end="")


def read_db() -> dict:
	"""
	Read JSON DB
	# This function can be later refactored to implement databases
	"""
	data: dict
	with open("./db.json", "r") as file:
		data = json.loads(file.read())
	return data


def get_cpu_model() -> set:
	"""
	Cross platform function to retrieve CPU model and power consumption for apps
	"""
	global platform
	if platform in ["linux", "linux2"]:
		model = subprocess.check_output("lscpu | grep 'Model name:'", shell=True).decode().split(":")[-1].strip()
	elif platform == "darwin":
		print("Not Implemented")
		sys.exit(1)
	elif platform == "win32":
		model = subprocess.check_output("wmic CPU get name").decode().strip().split("\n")[-1]

	# Reference P.7: https://inria.hal.science/hal-01069142v1/preview/noureddine-ause-2015.pdf
	consumption = db.get("cpu").get(model, 0) * 0.7

	# Implemented for Intel models only
	if consumption == 0 and "Intel" in model:
		if "i3" in model:
			consumption = db.get("cpu").get("Intel i3", 0) * 0.7
		elif "i5" in model:
			consumption = db.get("cpu").get("Intel i5", 0) * 0.7
		elif "i7" in model:
			consumption = db.get("cpu").get("Intel i7", 0) * 0.7
		else:
			consumption = db.get("cpu").get("Intel top end", 0) * 0.7

	return (model, round(consumption, 2))


def get_ram_average_consumption() -> set:
	"""
	Cross platform function to retrieve RAM capacity and power consumption for apps
	"""
	global platform, db
	average_consumption: int = 0
	total_capacity: int = 0
	if platform in ["linux", "linux2"]:
		memos = subprocess.check_output("sudo dmidecode -t memory | grep 'Size: [0-9]'", shell=True).decode().strip().split("\n")
		for memo in memos:
			capcity = re.search(r"\d+", memo)[0]
			capcity = str( int( int(capcity)/1024 ) ) # Convert to GB
			total_capacity += int(capcity)

			average_consumption += db["ram"]["capacity"].get(capcity, 0)
			average_consumption -= db["ram"]["idle"]
	elif platform == "darwin":
		print("Not Implemented")
		sys.exit(1)
	elif platform == "win32":
		winquery = wmi.WMI()
		for memo in winquery.Win32_PhysicalMemory():
			capcity = str( int( int(memo.Capacity)/(1024**3) ) ) # Convert to GB
			total_capacity += int(capcity)

			average_consumption += db["ram"]["capacity"].get(capcity, 0)
			average_consumption -= db["ram"]["idle"]

	return (total_capacity, average_consumption)


def instantenous_test(pid) -> None:
	global cpu_average_consumption, ram_average_consumption
	process = psutil.Process(pid)
	cpu_power = round(process.cpu_percent() * cpu_average_consumption, 2)
	ram_power = round(process.memory_percent() * ram_average_consumption, 2)

	print(f"At this instant process '{process.pid}: {process.name()}' consumes:")
	print(f"CPU: Usage: {round(process.cpu_percent(), 2)}% / Consumption: {cpu_power}W")
	print(f"RAM: Usage: {round(process.memory_percent(), 2)}% / Consumption: {ram_power}W")
	print(f"Total: {cpu_power+ram_power}W")


def time_interval_test(pid) -> None:
	global cpu_average_consumption, ram_average_consumption
	process = psutil.Process(pid)

	# Test duration
	time_interval = int(input("Enter test time interval (seconds) > "))
	# number of times to sample the readings in between the intervals
	frequency = int(input("Enter number of sampling points > "))

	total_power = []
	times = time_interval//frequency
	wait = time_interval / ceil(time_interval/frequency)
	for time in range(times):
		cpu_cons = round(process.cpu_percent() * cpu_average_consumption, 2)
		ram_cons = round(process.memory_percent() * ram_average_consumption, 2)
		total_power.append(cpu_cons+ram_cons)

		print(f"Sample {time+1}")
		print("===============")
		print(f"CPU: Usage: {round(process.cpu_percent(), 2)}% / Consumption: {cpu_cons}W")
		print(f"RAM: Usage: {round(process.memory_percent(), 2)}% / Consumption: {ram_cons}W")
		print(f"Total: {cpu_cons+ram_cons}W")
		print("\n", end="")
		sleep(wait)

	# Average Model
	res = sum(total_power)/len(total_power)
	print(f"Average Power Consumption on the provided interval is: {res}W") 


if __name__ == "__main__":
	print("========================================")
	print("Power Consumption per process Calculator")
	print("========================================", end="\n\n")

	print("[+] Reading Database...")
	print("[+] Gathering system info...")
	db = read_db()
	print("[+] Analyzing CPU...")
	cpu_model, cpu_average_consumption = get_cpu_model()
	print(f"[+] CPU: {cpu_model}")
	print(f"[+] CPU Average Consumption for Apps: {cpu_average_consumption}W")
	if cpu_average_consumption == 0:
		print(f"[-] CPU TDP value not in database!")
	print("[+] Analyzing RAM...")
	ram_capacity, ram_average_consumption = get_ram_average_consumption()
	print(f"[+] Found RAM Capacity: {ram_capacity}GB")
	print(f"[+] RAM Average Consumption for Apps: {ram_average_consumption}W", end="\n\n")

	# Check to import read process from task manager/monitor
	# or would the user just provide the PID
	import_process_toggle: str = "y"
	import_process_toggle: str = input("List processes? (Y/n) > ")
	if import_process_toggle.lower().strip() in ["y", ""]:
		read_process_from_task_manager()

	while True:
		pid_to_analyze = int(input("Enter PID > "))
		if not psutil.pid_exists(pid_to_analyze):
			print("[-] PID doesn't exist")
			continue
		break
	print("\n", end="")

	# Test mode
	print("Note: Make sure the process is in active mode before beginning the test")
	print("1) Instantinous")
	print("2) Time interval")
	while True:
		test_mode = int(input("Choose test mode > "))
		if not test_mode in [1,2]:
			print("[-] Invalid test mode")
			continue
		else:
			print("\n", end="")
			if test_mode == 1:
				instantenous_test(pid_to_analyze)
			elif test_mode == 2:
				time_interval_test(pid_to_analyze)
		break