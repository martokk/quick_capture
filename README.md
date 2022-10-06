# quick_capture

## Summary

quick_capture is a simple app to add a task/note to a local file.

## Usage

The app can be triggered by keyboard shortcut (Meta+N).
After entering your note and pressing Enter, your note is appended to the end of a local text file.

Tip: Automatically sync local text file via Dropbox, Google Drive, etc.

## Install

Builds from Source, Installs to Linux, Creates Binaries & Desktop files:

```shell
make install
```

## Config

Edit `~/.vapps/quick_capture.yaml` configuration dotfile.

## Build from source

Linux:

```shell
make build
```

Windows (Windows support not addded to Makefile yet):

```shell
pyinstaller.exe quick_capture.py ^
	--onefile ^
	--windowed ^
	--paths=./quick_capture ^
	--icon=./quick_capture/resources/icon.png ^
	--workpath=./build_win ^
	--distpath=./dist_win
```
