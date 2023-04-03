import PySimpleGUI as sg
import qrcode

sg.theme("GreenTan")
font = ('Monaco',18)

qr_image= [sg.Image('',key ='-QRCODE-')]

layout = [
     [sg.Text('INPUT YOUR TEXT TO CREATE QRCODE?')],
     [sg.Input('',key='-TEXT-')],
     [sg.Button('CREATE', key='-CREATE-'), sg.Button('EXIT')],
     [sg.Column([qr_image], justification='center')]
             
]
 
window = sg.Window(" QR CODE GENERATOR", layout,font=font)

while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    elif event =='-CREATE-':
        text = values['-TEXT-']
        if text:
            img = qrcode.make(text)
            img.save('qr.png')
            window['-QRCODE-'].update('qr.png')

window.close()
'''
ID: 10959957
'''