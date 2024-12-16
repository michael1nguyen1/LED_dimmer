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

