import RPi.GPIO as GPIO
from gpiozero import Servo
import time

#Left Door, 5V: ALIMENTAZIONE PIN 2
#Left Door, SIGNAL, GPIO 14 PIN 8 
#Left Door, GND, Pin 20

#Right Door, 5V: Pin 4
#Right Door, SIGNAL: GPIO 18 PIN 12
#Right Door, GND: Pin 6

#Led GPIO, 17 PIN 11
#Led Ground, PIN 9

#Button, GPIO 26, PIN 37
#Button, Ground PIN 39

LED_PIN_1 = 17
ASSOCIATION_PIN = 26

GPIO_DOOR = {'left': 14, 'right': 18}
ANGLES = {'max': 1, 'min': -1}

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(ASSOCIATION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def control_door(side: str, opened: bool) -> bool:
    servo = None
    try:
        servo = Servo(GPIO_DOOR[side])
        if side == 'right':
            servo.value = ANGLES['max'] if opened == 'false' else ANGLES['min']
        else:
            servo.value = ANGLES['min'] if opened == 'false' else ANGLES['max']
        time.sleep(1)
        return True
    except Exception:
        return False
    finally:
        if servo is not None:
            servo.close()

def control_headlights(opened: bool) -> bool:
    try:
        if opened == 'true':
            GPIO.output(LED_PIN_1, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN_1, GPIO.LOW)
        return True
    except Exception:
        return False


def is_button_pressed_within_timeout(timeout: int) -> bool:
    start_time = time.time()
    print("sono nel botton press")    
    while True:
        if GPIO.input(ASSOCIATION_PIN) == GPIO.HIGH:
            print("premuto")
            return True 
        if time.time() - start_time >= timeout:
            return False 

