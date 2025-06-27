radio.onReceivedNumber(function (receivedNumber) {
    basic.showString("" + (receivedNumber))
    if (receivedNumber == 1) {
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 30)
    }
    if (receivedNumber == 2) {
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 51)
    }
    if (receivedNumber == 0) {
        kitronik_motor_driver.motorOn(kitronik_motor_driver.Motors.Motor1, kitronik_motor_driver.MotorDirection.Forward, 51)
    }
})
input.onButtonPressed(Button.A, function () {
    basic.showString("on")
    basic.showIcon(IconNames.Yes)
    radio.sendString("on")
})
radio.setGroup(35)
