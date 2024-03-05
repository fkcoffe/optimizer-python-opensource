import ctypes
import os
import sys

import PySimpleGUI as sg


# Pedir permissões de administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    pass
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# Obter o nome de usuário do PC
user_name = os.environ.get('USERNAME')

sg.theme('Reddit')
layout = [
    [sg.Text('Escolha até três pastas para limpar:')],
    [sg.Input(key='folder1'), sg.FolderBrowse()],
    [sg.Input(key='folder2'), sg.FolderBrowse()],
    [sg.Input(key='folder3'), sg.FolderBrowse()],
    [sg.Button('Limpar')],
]

# GUI
gui = sg.Window('OPTIMIZER 1.0 – PTBR ', layout)

while True:
    events, values = gui.read()
    if events == sg.WINDOW_CLOSED:
        break

    if events == 'Limpar':
        folders_to_clean = [values[key] for key in ['folder1', 'folder2', 'folder3'] if values[key]]

        if not folders_to_clean:
            sg.popup('Por favor, selecione pelo menos uma pasta para limpar!')
            continue

        for folder in folders_to_clean:
            arquivos = os.listdir(folder)

            # Remover todos os arquivos do diretório
            for file in arquivos:
                endereco_final = os.path.join(folder, file)
                if os.path.isfile(endereco_final):
                    os.remove(endereco_final)

        sg.popup('Pastas limpas com sucesso!')

# Créditos
# CRIADOR E DESENVOLVEDOR: fkcoffe (github)
print('fkcoffe é o dev!')
gui.close()