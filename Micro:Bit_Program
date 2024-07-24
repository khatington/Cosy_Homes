// objective: CHANGE MAX VALUE FROM WEBSITE
serial.onDataReceived(serial.delimiters(Delimiters.Comma), function () {
    if (serial.readUntil(serial.delimiters(Delimiters.Comma)) == "1" && count <= 10) {
        basic.showString("" + (count))
        count += 1
        pins.digitalWritePin(DigitalPin.P2, 1)
        pins.digitalWritePin(DigitalPin.P0, 1)
    } else if (count == 11) {
        count = 0
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P0, 0)
        basic.showLeds(`
            . # # # .
            # . . . #
            # . # . #
            # . # . #
            . # # # .
            `)
    } else {
        basic.showLeds(`
            . # # # .
            # . . . #
            # # # . #
            # . . . #
            . # # # .
            `)
        basic.showLeds(`
            . # # # .
            # . . . #
            # . # . #
            # . # . #
            . # # # .
            `)
        pins.digitalWritePin(DigitalPin.P2, 0)
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
})
let count = 0
serial.redirectToUSB()
