input.onButtonPressed(Button.A, function () {
    basic.showString(message)
    basic.showIcon(IconNames.Yes)
})
serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    cmd = serial.readLine()
    radio.sendString(cmd)
})
function init () {
    temperature = -1
    pressure = -1
    humidity = -1
    smoke = -1
    flame = -1
}
radio.onReceivedString(function (receivedString) {
    if (receivedString == "start") {
        basic.showString("R")
        init()
    }
})
radio.onReceivedValue(function (name, value) {
    if (name == "temp") {
        temperature = value
    } else if (name == "pressure") {
        pressure = value
    } else if (name == "humidity") {
        humidity = value
    } else if (name == "smoke") {
        smoke = value
    } else if (name == "flame") {
        flame = value
        end = true
    }
})
let index = 0
let end = false
let flame = 0
let smoke = 0
let humidity = 0
let pressure = 0
let temperature = 0
let message = ""
let cmd = ""
init()
radio.setGroup(8)
radio.setTransmitSerialNumber(true)
radio.setTransmitPower(7)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    if (end == true) {
        index = index + 1
        message = "" + index + ".T:" + temperature + ";P:" + pressure + ";H:" + humidity + ";S:" + smoke + ";F:" + flame
        basic.showString("T")
        serial.writeLine(message)
        end = false
        basic.showIcon(IconNames.Yes)
    }
})
