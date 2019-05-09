from microbit import *

# pin13 is a 1-channel relay unit to open and close the circuit
pin13.write_digital(0)  # set circuit to be open by default

while True:
    display.off()  # Micro:Bit display must be off to avoid module errors

    # pin0 is the pressure-sensitive sensor
    # define variable for pressure
    pressure = (pin0.read_analog())

    # calculate the temperature in Fahrenheit
    # pin10 is the temperature sensor
    v = pin10.read_analog()  # read voltage
    mV = v * (5000 / 1024)  # calculate millivolts
    c = .005 * (mV) + 4.4375  # calculate celsius
    temp = (c * (9 / 5)) + 32  # calculate Fahrenheit

    # pressure sensitivity must be calibrated for your setup
    if((pressure >= 1023) and (temp <= 87)):  # pressure values 0—1024
        pin13.write_digital(1)  # close the circuit by writing to the relay unit
    # set conditions to stop heating above acceptable temperature
    elif((pressure >= 1023) and (temp >= 88)):
        pin13.write_digital(0)  # for safety, open the circuit before the break
        break
    else:
        pin13.write_digital(0)