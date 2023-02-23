#GPIO code to get input from user from GPIO pin when it is connected to Jetson nano
def program():
    GPIO.setwarnings(False)
    GPIO .setmode(GPIO.BOARD)
    inPin = 15
    GPIO.setup(inPin,GPIO.IN)
    while True:
        x = GPIO.input(inPin)
        if x==1:
            return x 
