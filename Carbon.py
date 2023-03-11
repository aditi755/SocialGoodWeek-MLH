#Energy Efficiency
import time

while True:
    # Check the time
    now = time.localtime()
    
    # Turn off the lights between 9 pm and 6 am
    if now.tm_hour >= 21 or now.tm_hour < 6:
        turn_off_lights()
    
    # Wait for an hour before checking again
    time.sleep(3600)
    
#Renewable energy    
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
    # Read the voltage from the solar panel
    voltage = read_voltage()
    
    # Calculate the optimal angle based on the voltage
    angle = calculate_angle(voltage)
    
    # Adjust the angle of the solar panel
    GPIO.output(11, angle)
    
    # Wait for an hour before checking again
    time.sleep(3600)

