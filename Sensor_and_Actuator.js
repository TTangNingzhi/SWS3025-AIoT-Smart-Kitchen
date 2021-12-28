input.onButtonPressed(Button.A, function () {
    sendValue()
})
function init () {
    temperature = -1
    pressure = -1
    humidity = -1
    smoke = -1
    flame = -1
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "ledon") {
        pins.digitalWritePin(DigitalPin.P8, 1)
    } else if (receivedString == "ledoff") {
        pins.digitalWritePin(DigitalPin.P8, 0)
    } else if (receivedString == "bzon") {
        pins.digitalWritePin(DigitalPin.P16, 1)
    } else if (receivedString == "bzoff") {
        pins.digitalWritePin(DigitalPin.P16, 0)
    } else if (receivedString == "fanon") {
        pins.digitalWritePin(DigitalPin.P0, 1)
    } else if (receivedString == "fanoff") {
        pins.digitalWritePin(DigitalPin.P0, 0)
    } else if (receivedString == "pumpon") {
        pins.digitalWritePin(DigitalPin.P12, 1)
    } else if (receivedString == "pumpoff") {
        pins.digitalWritePin(DigitalPin.P12, 0)
    } else if (receivedString == "get") {
        sendValue()
    } else if (receivedString == "detect") {
        detect = true
    } else if (receivedString == "end") {
        detect = false
    }
})
input.onButtonPressed(Button.B, function () {
    message = "Data:" + "T:" + temperature + ";P:" + pressure + ";H:" + humidity + ";S:" + smoke + ";F:" + flame
    basic.showString(message)
    basic.showIcon(IconNames.Yes)
})
function sendValue () {
    basic.showIcon(IconNames.Diamond)
    init()
    temperature = BMP280.temperature()
    pressure = Math.round(BMP280.pressure())
    humidity = dht11.humidity()
    smoke = pins.analogReadPin(AnalogPin.P2)
    flame = pins.analogReadPin(AnalogPin.P3)
    basic.showString("T")
    radio.sendString("start")
    radio.sendValue("temp", temperature)
    radio.sendValue("pressure", pressure)
    radio.sendValue("humidity", humidity)
    radio.sendValue("smoke", smoke)
    radio.sendValue("flame", flame)
    basic.showIcon(IconNames.Happy)
    pause(1000)
basic.showIcon(IconNames.Yes)
}
let message = ""
let detect = false
let flame = 0
let smoke = 0
let humidity = 0
let pressure = 0
let temperature = 0
init()
BMP280.Address(BMP280_I2C_ADDRESS.ADDR_0x76)
dht11.set_pin(DigitalPin.P1)
radio.setGroup(8)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    if (detect == true) {
        sendValue()
        pause(3000)
    }
})
