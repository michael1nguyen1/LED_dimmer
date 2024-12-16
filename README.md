# **LED Brightness Control with PWM on Raspberry Pi**

This project demonstrates how to control the brightness of an LED connected to a Raspberry Pi using **Pulse Width Modulation (PWM)**. It uses the Raspberry Pi's GPIO pins to output a PWM signal that adjusts the LED's brightness by varying its duty cycle.

## **Project Video**

Check out the demo video of the LED brightness control in action:

[![LED PWM Demo](https://img.youtube.com/vi/tn53XlbMxW8/0.jpg)](https://youtu.be/tn53XlbMxW8?feature=shared)

## **Features**
- Controls the brightness of an LED using PWM.
- Gradually increases and decreases the brightness of the LED.
- Uses a Raspberry Pi and a breadboard setup.
- Simple Python code with `RPi.GPIO` library to handle PWM.

## **Requirements**
- Raspberry Pi (any model with GPIO pins).
- LED (any standard 5mm LED).
- 220Ω resistor.
- Jumper wires.
- Breadboard.
- Python 3.
- `RPi.GPIO` library (installed by default on most Raspberry Pi systems).

## **Wiring Setup**

1. **LED Setup**:
   - Connect the **anode (long leg)** of the LED to GPIO pin 17 (or any available GPIO pin).
   - Connect the **cathode (short leg)** of the LED to the **GND rail** on the breadboard through a **220Ω resistor**.

2. **GPIO Pin Setup**:
   - Use **GPIO17** for the PWM signal (you can change the pin in the code if needed).
   - Connect the **GND** pin of the Raspberry Pi to the **GND rail** on the breadboard.

## **Python Code**

```python
import RPi.GPIO as GPIO
import time

# Pin setup
LED_PIN = 17

GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(LED_PIN, GPIO.OUT)  # Set LED pin as output

# Set up PWM
pwm = GPIO.PWM(LED_PIN, 100)  # 100 Hz frequency
pwm.start(0)  # Start PWM with 0% duty cycle (LED off)

try:
    while True:
        # Gradually increase brightness
        for duty_cycle in range(0, 101, 5):  # From 0% to 100% in steps of 5%
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)  # Small delay for smooth transition

        # Gradually decrease brightness
        for duty_cycle in range(100, -1, -5):  # From 100% to 0% in steps of 5%
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")
finally:
    pwm.stop()  # Stop PWM
    GPIO.cleanup()  # Clean up GPIO settings
