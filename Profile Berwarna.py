import PySimpleGUI as sg
sg.theme("Blackwhite4")
sg.theme_text_color("#00ffCC")
Window = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010496'),],
        [sg.Text('Nama :Patra Robianas')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200)).read(close=True)
event, values=Window.read()
Window.close()