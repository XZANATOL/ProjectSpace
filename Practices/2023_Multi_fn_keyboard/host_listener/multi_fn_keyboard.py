import threading, serial
import concurrent.futures as multiprocessing
import subprocess, json, time

# ============================================
# Global Vars Start
# ============================================
serial_data = []
arduino: serial.Serial
config_filename = "config.json"
scripts_folder = "./scripts/"
timer_frequency: int = 0.1 # Secs

with open(config_filename, "r") as file:
    commands = json.loads(file.read())
# ============================================
# Global Vars End
# ============================================

def command_exec(code):
    global commands
    script_name = commands.get(code)
    if script_name:
        print(f"[+] Executing: {script_path}")
        script_path = scripts_folder + script_name
        subprocess.popen(script_path)
    else:
        print(f"[-] No command registered for code: {code}")


def serial_monitor():
    global arduino, serial_data, timer_frequency

    bytes_to_read = arduino.inWaiting()
    if bytes_to_read > 0:
        serial_data.append(arduino.readline().decode().rstrip())
        print(serial_data)

    threading.Timer(timer_frequency, serial_monitor).start()


if __name__ == "__main__":
    arduino = serial.Serial("com7")
    print(arduino.name)

    threading.Timer(timer_frequency, serial_monitor).start()

    while True:
        if serial_data:
            with multiprocessing.ProcessPoolExecutor() as multiprocessor:
                multiprocessor.submit(command_exec, serial_data.pop(0))