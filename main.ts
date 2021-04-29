// DisplayIsBusy Variable dient zur Steuerung der Ausgabe, damit auf alle Fälle die Zahl vollständig angezeigt wird
input.onButtonPressed(Button.A, function () {
    DisplayIsBusy = true
    basic.showNumber(input.temperature())
    basic.pause(1000)
    DisplayIsBusy = false
})
/**
 * Das Video dazu: https://www.youtube.com/watch?v=-fZm1JCvxlE
 */
let DisplayIsBusy = false
DisplayIsBusy = false
basic.forever(function () {
    if (DisplayIsBusy == false) {
        led.plotBarGraph(
        input.temperature(),
        30
        )
    }
})
