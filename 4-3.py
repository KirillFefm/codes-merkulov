import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(7, GPIO.OUT)
pwm = GPIO.PWM(7, 1000)

try:
    pwm.start(0)
    while True:
        duty_cycle = input("Введите коэффициент заполнения ШИМ (0-100): ")
        try:
            duty = float(duty_cycle)
            if 0 <= duty <= 100:
                pwm.ChangeDutyCycle(duty)
                pred_volt = 3.3 * (duty / 100)
                print("Предполагаемое напряжение на выходе цепи: {:.2f} V".format(pred_volt))
            else:
                print("Ошибка: коэффициент заполнения должен быть в диапазоне от 0 до 100")
        except ValueError:
            print("Неверный ввод коэффициента заполнения")
finally:
    pwm.stop()
    GPIO.cleanup()
    print("Завершение работы!")
