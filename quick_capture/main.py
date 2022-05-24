from pathlib import Path
from typing import Union, Dict
import yaml
import PySimpleGUI as sg


config = yaml.safe_load(open(Path(f'{str(Path.home())}/.vapps/quick_capture.yaml')))

CAPTURE_FILE_PATH = config.get('capture_file')
THEME = config.get('theme', 'DarkGrey15')
FONT = config.get('font', 'hack')
FONT_SIZE = config.get('font_size', 14)


class QuickCapture:
    def __init__(self):
        self.main()

    def main(self) -> None:
        sg.theme(THEME)
        layout = [
            [sg.Multiline(key='-IN-', enable_events=True, size=(60, 3), font=(FONT, FONT_SIZE))],
        ]
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
