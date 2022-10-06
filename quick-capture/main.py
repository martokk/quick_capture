from pathlib import Path
from typing import Union, Dict
import yaml
import PySimpleGUI as sg

CONFIG_PATH_DEFAULT = Path('./quick-capture/.vapps/quick-capture.yaml')
CONFIG_PATH_DOTFILE = Path(f'{str(Path.home())}/.vapps/quick-capture.yaml')
CONFIG_PATH = CONFIG_PATH_DOTFILE if CONFIG_PATH_DOTFILE.exists() else CONFIG_PATH_DEFAULT
CONFIG_WARNING = not CONFIG_PATH_DOTFILE.exists()
CONFIG = yaml.safe_load(open(CONFIG_PATH))

CAPTURE_FILE_PATH = Path(CONFIG.get('capture_file'))
CAPTURE_FILE_ERROR = not CAPTURE_FILE_PATH.exists()
THEME = CONFIG.get('theme', 'DarkGrey15')
FONT = CONFIG.get('font', 'hack')
FONT_SIZE = CONFIG.get('font_size', 14)


class QuickCapture:
    def __init__(self):
        self.main()

    def main(self) -> None:
        sg.theme(THEME)
        layout = [
            [sg.Multiline(key='-IN-', enable_events=True, size=(60, 3), font=(FONT, FONT_SIZE))],
        ]

        if CONFIG_WARNING:
            warning = [sg.Text(text="WARNING! You are not using '~/.vapps/quick-capture.yaml dotfile'. See martokk/dotfiles to install.",
                               text_color="orange")]
            layout.append(warning)

        if CAPTURE_FILE_ERROR:
            error = [sg.Text(text=f"ERROR! Capture file '{CAPTURE_FILE_PATH}' does not exist. Text will not be saved. Update config dotfile.",
                               text_color="red")]
            layout.append(error)

        window = sg.Window('QuickCapture', layout, margins=(10, 20), no_titlebar=False, finalize=True)
        window.bind("<Return>", "Keypress_Return")
        window.bind("<Escape>", "Keypress_Escape")

        # Event Loop
        while True:
            event, values = window.read()
            if event in [sg.WIN_CLOSED, 'Keypress_Escape']:
                break
            if event == 'Keypress_Return':
                self.save_value_to_file(value=values, file_path=CAPTURE_FILE_PATH)
                break
        window.close()

    @staticmethod
    def save_value_to_file(value: Dict[str, str], file_path: Union[str, Path], append=True) -> None:
        with open(file_path, "a" if append else "w") as file:
            # print(value['-IN-'])
            file.write(f"- {value['-IN-'].removeprefix('-').strip()}\n")


if __name__ == '__main__':
    QuickCapture()
