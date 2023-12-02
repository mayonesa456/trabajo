import time

def digitalRead(pin):
    return input("Presiona 'g' para simular el sensor de gas: ") == 'g'

# FUNCION DE SENSOR DE GAS
def sensor_gas(pin_sensor_gas, pin_led_sirena, pin_interruptor):
    while True:
        if digitalRead(pin_sensor_gas) == 0:
            print("Sensor de gas activado")
            activar_sirena(pin_led_sirena)
        elif digitalRead(pin_interruptor) == 1:
            desactivar_sirena(pin_led_sirena)
        else:
            print("Sensor de gas desactivado")
        time.sleep(0.5) 
