from machine import Pin, SPI, I2C
import time
import gc9a01
from qmi8658 import QMI8658

# SPI configuration for the GC9A01A display
spi = SPI(2, baudrate=80_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))

lcd = gc9a01.GC9A01(
    spi=spi,
    cs=Pin(9),
    dc=Pin(8),
    rst=Pin(15),
    backlight=Pin(2),
    width=240,
    height=240,
    rotation=0,
)

lcd.init()

# I2C for QMI8658 and touch controller
i2c = I2C(0, scl=Pin(7), sda=Pin(6))
imu = QMI8658(i2c)

count = 0
state = 0
THRESH_HIGH = 1.5
THRESH_LOW = 1.0

lcd.fill(gc9a01.BLACK)
lcd.text("Count: 0", 60, 120, gc9a01.WHITE)

while True:
    ax, ay, az, gx, gy, gz = imu.read()
    magnitude = (ax * ax + ay * ay + az * az) ** 0.5
    if state == 0 and magnitude > THRESH_HIGH:
        state = 1
    elif state == 1 and magnitude < THRESH_LOW:
        state = 0
        count += 1
        lcd.fill(gc9a01.BLACK)
        lcd.text("Count: {}".format(count), 60, 120, gc9a01.WHITE)
    time.sleep_ms(50)
