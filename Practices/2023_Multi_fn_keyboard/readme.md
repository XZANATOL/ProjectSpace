## Multi Function Keyboard

A customizable keyboard built using Arduino & Python for running custom commands with easy-to-reach keys. System was built as a hands-on practice on Proteus VSM.

### Features

* Easy to change registered commands from the host listener.
* No need to update the embedded code. Just send the number and let the host take care of the rest.
* Expandable design.
* Can run on Windows, Linux, and Mac.

### Description

The project consists of 2 parts: Host Listener & Arduino System

### Host Listener

A Python script that monitors Serial data comming from the Arduino System. It's the part the receives the command code & compares it with its registered commands to run it. The script utilizes threading for near real-time monitoring of Serial data, and multi-processing for running commands independent of the Serial monitoring process to avoid blocking of time-comsuming commands.

#### Usage

* Write your Bash/Batch script in the `scripts` folder.
* Edit `config.json` & Enter a key value of `<command_number>: <script_filename>`.
* (Run Once) `pip install -r requirements.txt`.
* Run `python multi_fn_keyboard.py`.

### Arduino System

An Arduino UNO with a circuit of push buttons, capacitors, diodes, & a resistor. The setup is built to eleminate bouncing behavior in the push buttons.

#### Usage

The project can be totally simulated on Proteus. Code can be found within `Multi_fn_keyboard.pdsprj`.

* Press the run button to start the simulation.
* A button can be pressed once, as a state tracking code is placed to register the last pressed button to avoid command spam on the host.
* To reset the state tracker: press the last pressed button along with any other one (or just press the 3 together).

### Future Ideas

* Expand with more buttons (around 3x3) and add a matrix tracker code for a more compact design.
* Write a more versatile code to allow specific buttons to be added to the state tracker.
* Add an LCD Screen & code some Serial results to be returned from the host to inform the user of the state of the pressed command.
