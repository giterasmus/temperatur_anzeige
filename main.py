# DisplayIsBusy Variable dient zur Steuerung der Ausgabe, damit auf alle Fälle die Zahl vollständig angezeigt wird

def on_button_pressed_a():
    global DisplayIsBusy
    DisplayIsBusy = True
    basic.show_number(input.temperature())
    basic.pause(1000)
    DisplayIsBusy = False
input.on_button_pressed(Button.A, on_button_pressed_a)

# Das Video dazu:
# https://www.youtube.com/watch?v=-fZm1JCvxlE
# 
DisplayIsBusy = False
DisplayIsBusy = False

def on_forever():
    if DisplayIsBusy == False:
        led.plot_bar_graph(input.temperature(), 30)
basic.forever(on_forever)
