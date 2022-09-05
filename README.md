# pygame_gui
Some classes for pygame to easily and quickly create user interfaces.
Interface elements:
 - Button
 - TextBox
 - CheckBox
 - ColorPicker
 - FillBox

 All of them have some attributes:
  - enabled *bool* # makes item unavailable for interaction
  - width *int*
  - height *int*
  - x *int*
  - y *int*
  - bg *(int, int, int)* #background color
  - font *pygame.Font*
  - text_color *(int, int, int)*
  - title *str* #text in the item
  - is_border *bool* # makes a border
  - border_color *(int, int, int)*
  - border_width *int*
All these attributes can be modified using methods set_<attribute_name>(value) and get_<attribute_name>()


All of them have methods that have to be called in main loop:
 - onClick()
 - onHover()
 - onPress()
 - draw() # displays the item

**class**
Label(win, pos, size = (0,35), text = "hello")
 - set_text(value) 
 - get_text()
 - set_text_height(value)
 - get_text_height()

**class**
Button(win, pos, size=(120, 25), title="", color=(207, 159, 27), color_active=(62, 39, 214))
  - color_active *(int, int, int)* #color of pressed button
  All these attributes can be modified using methods set_<attribute_name>(value) and get_<attribute_name>()

  - get_value() # returns button's state

**class**
CheckBox(win, pos, size=(15, 15))
  - get_value() # returns state of the checkbox

**class**
TextBox(win, pos, size = (120, 25))
  - event_handler(event) put it into event.get loop, without this method, textbox will not work (see example for details)
  - get_value() returns current value of textBox
  - clear() clears textbox
  - is_chosen() returns True if textBox is chosen

**class**
FillBox(win, pos, size, min, max, color = (0, 0, 255), cursor_color = (0, 0, 255), cursor_width = 2, mode = 0)
  - min # minimal value of FillBox
  - max # maximal value of FillBox
  - mode *bool* # data which FillBox will work with  0 - float values, 1 - int values
  - cursor_color *(int, int, int)*
  - cursor_width *int*
  All these attributes can be modified using methods set_<attribute_name>(value) and get_<attribute_name>()

  - get_value() # returns current value of FillBox

**class**
ColorPicker(win, pos, size)
  - get_value() #returns current chosen color from the picture, if nothing chosen, returns False
  - picture might be changed to another with the same name or name can be modified in the gui.py file
