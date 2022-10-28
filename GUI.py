from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

win = Tk()
win.title("LED TOGGLER")
def ledToggle1():
    ## for LED 1 ##
    if led1.is_lit:
        led1.off()
        ledButton1["text"] =  "Turn LED 1 on"
        
    else:
        led1.on()
        led2.off()
        led3.off()
        ledButton1["text"] =  "Turn LED 1 off"
        ledButton2["text"] =  "LED 2 is off"
        ledButton3["text"] =  "LED 3 is off"
        
def ledToggle2():
      ## for LED 2 ##
    if led2.is_lit:
        led2.off()
        ledButton2["text"] =  "Turn LED 2 on"
        
    else:
        led2.on()
        led1.off()
        led3.off()
        ledButton2["text"] =  "Turn LED 2 off"
        ledButton1["text"] =  "LED 1 is off"
        ledButton3["text"] =  "LED 3 is off"

def ledToggle3():   
        ## for LED 3 ##
    if led3.is_lit:
        led3.off()
        ledButton3["text"] =  "Turn LED 3 on"
        
    else:
        led3.on()
        led2.off()
        led1.off()
        ledButton3["text"] =  "Turn LED 3 off"
        ledButton1["text"] =  "LED 1 is off"
        ledButton2["text"] =  "LED 2 is off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
ledButton1 = Button(win, text = "Turn LED1 ", command =ledToggle1,bg = "bisque2", height = 1, width =24)
ledButton2 = Button(win, text = "Turn LED2", command =ledToggle2,bg = "bisque2", height = 1, width =24)
ledButton3 = Button(win, text = "Turn LED3", command =ledToggle3,bg = "bisque2", height = 1, width =24)
ledButton1.grid(row=0, column =1)
ledButton2.grid(row=1, column =1)
ledButton3.grid(row=2, column =1)

exitButton = Button(win, text = "EXIT", command = close, bg = "red", height =1 , width = 6)
exitButton.grid(row = 3, column = 1)