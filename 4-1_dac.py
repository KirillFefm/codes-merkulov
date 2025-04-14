import RPi.GPIO as GPIO

dac = [8,11,7,1,0,5,12,6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal_to_binary_list(value):
    return [int(bit) for bit in format(value, '08b')]

try:
    while True:
        user_input = input("Введите число:")
        
        if user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            
            if number < 0:
                print("отрицательное число.")
                continue
            elif number > 255:
                print("больше 255.")
                continue
            binary_output = decimal_to_binary_list(number)
            GPIO.output(dac, binary_output)
            voltage = number * (3.3 / 255)  
            print(f"{voltage:.2f} В")

        except ValueError:
            print("целое число.")

finally:
    GPIO.output(dac, [0] * len(dac))
    GPIO.cleanup()
