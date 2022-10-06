# quick_capture

## Summary
quick_capture is a simple app to add a task/note to a local file.

## Usage
The app can be triggered by keyboard shortcut (Meta+N). 
After entering your note and pressing Enter, your note is appended to the end of a local text file.

Tip: Automatically sync local text file via Dropbox, Google Drive, etc.

## Install/Run
Run executable found in `/dist_linux/` folder

## Config
Copy `/quick_capture/.vapps/quick_capture.yaml` to `~/.vapps/quick_capture.yaml`

## Build from source
Linux:
```shells
pyinstaller quick_capture.py \
	--onefile \
	--windowed \
	--paths=./quick_capture \
	--icon=./quick_capture/resources/icon.png \
	--workpath=./build_linux \
	--distpath=./dist_linux
```

Windows:
```shell
pyinstaller.exe quick_capture.py ^
	--onefile ^
	--windowed ^
	--paths=./quick_capture ^
	--icon=./quick_capture/resources/icon.png ^
	--workpath=./build_win ^
	--distpath=./dist_win
```
