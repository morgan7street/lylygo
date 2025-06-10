# ESP32-S3 Movement Counter

This repository contains a simple MicroPython application for the Waveshare ESP32-S3 Touch LCD 1.28" board. The program reads motion data from the onboard **QMI8658** accelerometer/gyroscope and shows a counter on the round 1.28" LCD (GC9A01A).

The application is designed for fitness tracking. Wear the device on your chest or arm during exercises. Each detected movement increments the displayed count.

## Installation

1. Flash the Waveshare MicroPython firmware provided on the [product wiki](https://www.waveshare.com/wiki/ESP32-S3-Touch-LCD-1.28) using `esptool.py`.
2. Install `mpremote` (comes with recent MicroPython packages) on your computer:
   ```bash
   pip install mpremote
   ```
3. Clone this repository and copy `main.py` and `qmi8658.py` to the board:
   ```bash
   mpremote connect /dev/ttyACM0 fs cp main.py :/main.py
   mpremote connect /dev/ttyACM0 fs cp qmi8658.py :/qmi8658.py
   ```
   Replace the serial port with the one shown on your system.

## Usage

1. Reset or power the board.
2. The display shows the current movement count starting from zero.
3. Perform your workout. Each time the algorithm detects a complete motion, the counter increases.

## Configuration

The detection threshold values in `main.py` may require adjustment depending on the exercise and how the board is worn. Edit `THRESH_HIGH` and `THRESH_LOW` in the script for best results.

## Files

- `main.py` – application entry point; sets up the display and IMU and updates the counter.
- `qmi8658.py` – minimal driver for the QMI8658 accelerometer/gyroscope.

