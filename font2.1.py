import PySimpleGUI as sg 
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
Window = sg.Window(title="Font",
                   layout=[[sg.Text("FTI UNISKA ")],
                           [sg.Text("FAKULTAS TEKNOLOGI INFORMASI ")],
                           [sg.Text("UNISKA MAB BANJARMASIN ")]],
                    size=(430,200),
                    font=("times", 18))
Window()
Window.close()