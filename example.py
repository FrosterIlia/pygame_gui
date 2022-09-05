import pygame
from gui import *

pygame.init()

WIDTH, HEIGHT = 900, 600
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
button1 = Button(win, (10,10)) # creating button object
button1.set_title("Hello world") # setting new text for button
button1.set_font(pygame.font.SysFont("menlo", button1.get_height() - 8)) # changing button's font
checkBox1 = CheckBox(win, (10,40)) # creating checkbox object
checkBox1.set_bg((255,0,0)) # setting background to red
checkBox1.set_border_color((0, 255, 0)) # setting border_color to green
fillBox1 = FillBox(win, (10, 80), (100, 25), 0, 255) # creating fillbox object
fillBox1.set_text_color(pygame.Color("orange")) # setting text_color to orange
textBox1 = TextBox(win, (10, 120)) # creating textBox
colorPicker1 = ColorPicker(win, (10,170), (300,300)) # creating colorPicker

label_for_button = Label(win, (140, 10))
label_for_checkBox = Label(win, (140, 40))
label_for_fillBox = Label(win, (140, 80))
label_for_textBox = Label(win, (140, 120))
label_for_colorPicker = Label(win, (340, 170))

def draw_everything(): # drawing all the gui
    button1.draw()
    checkBox1.draw()
    fillBox1.draw()
    textBox1.draw()
    colorPicker1.draw()
    label_for_button.draw()
    label_for_checkBox.draw()
    label_for_colorPicker.draw()
    label_for_fillBox.draw()
    label_for_textBox.draw()

run = True
while run:
    clock.tick()
    for event in pygame.event.get():
        textBox1.event_handler(event) # necessary method here
        if event.type == pygame.QUIT:
            run = False
            exit()

    fillBox1.set_title("value" if checkBox1.get_value() else "") # changing fillBox title if checkbox is on

    label_for_button.set_text(str(button1.get_value()))
    label_for_fillBox.set_text(str(fillBox1.get_value()))
    label_for_colorPicker.set_text(str(colorPicker1.get_value()))
    label_for_checkBox.set_text(str(checkBox1.get_value()))
    label_for_textBox.set_text(textBox1.get_value())
    draw_everything()

    pygame.display.flip()
    win.fill(pygame.Color("white"))

pygame.quit()