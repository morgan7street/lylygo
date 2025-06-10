from machine import I2C
import struct
import time

class QMI8658:
    """Minimal driver for the QMI8658 6-axis IMU."""

    def __init__(self, i2c: I2C, addr: int = 0x6B) -> None:
        self.i2c = i2c
        self.addr = addr
        self.init()

    def init(self) -> None:
        """Basic initialization of the sensor."""
        try:
            # Reset and wake up
            self.i2c.writeto_mem(self.addr, 0x02, b"\x80")
            time.sleep_ms(10)
            self.i2c.writeto_mem(self.addr, 0x02, b"\x00")
            # Configure ranges (±8g, ±2000 dps) and start
            self.i2c.writeto_mem(self.addr, 0x1F, b"\x03")
            self.i2c.writeto_mem(self.addr, 0x20, b"\x07")
        except OSError:
            pass

    def read(self):
        """Read and return acceleration (g) and gyro (dps) values."""
        data = self.i2c.readfrom_mem(self.addr, 0x35, 12)
        ax, ay, az, gx, gy, gz = struct.unpack("<hhhhhh", data)
        ax /= 4096.0
        ay /= 4096.0
        az /= 4096.0
        gx /= 32.8
        gy /= 32.8
        gz /= 32.8
        return ax, ay, az, gx, gy, gz
