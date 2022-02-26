from operator import truediv


x_button = True
y_button = False
button_pressed = input('Enter the button: ')

if(button_pressed == 'x') :
    if(x_button == False): 
        x_button == False
        y_button == True
    else: 
        print('X_button is already ON')

if(button_pressed == 'y') :
    if(y_button == False): 
        x_button == False
        y_button == True
    else: 
        print('X_button is already ON')
