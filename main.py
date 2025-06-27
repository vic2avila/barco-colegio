def on_received_number(receivedNumber):
    basic.show_string("" + str((receivedNumber)))
    if receivedNumber == 1:
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.FORWARD,
            30)
    if receivedNumber == 2:
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.FORWARD,
            51)
    if receivedNumber == 0:
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.FORWARD,
            51)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    basic.show_string("on")
    basic.show_icon(IconNames.YES)
    radio.send_string("on")
input.on_button_pressed(Button.A, on_button_pressed_a)

radio.set_group(35)