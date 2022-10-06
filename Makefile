APP_NAME=quick_capture
.DEFAULT_GOAL := help

#---------------------------------------------------------------
# Pyinstaller options
PYINSTALLER_LINUX=pyinstaller
PYINSTALLER_WIN=pyinstaller.exe
MAIN_FILE=$(APP_NAME).py
OUTPUT_NAME=--name $(APP_NAME)
ICON=--icon $(APP_NAME)/resources/icon.png
CLEAN=--clean
EXTRA_HOOKS=--additional-hooks-dir extra-hooks
ONEFILE=--onefile
WINDOWED=--windowed
PATHS=--paths ./$(APP_NAME)
WORKPATH_LINUX=--workpath ./build_linux
WORKPATH_WIN=--workpath ./build_win
DISTPATH_LINUX=--distpath ./dist_linux
DISTPATH_WIN=--distpath ./dist_win

.PHONY: build install build_linux install_linux install_linux_binary install_linux_desktop_file install_linux_user_config

build: build_linux ## Build on Linux

install: build_linux install_linux ## Builds from source, then installs Application to system.

build_linux: ## (MODULE) Builds executable to ./dist_linux folder. Must be on Linux!
	rm -rf ./build_linux
	rm -rf ./dist_linux
	$(PYINSTALLER_LINUX) $(MAIN_FILE) $(CLEAN) $(ONEFILE) $(WINDOWED) $(OUTPUT_NAME) $(ICON) $(WORKPATH_LINUX) $(DISTPATH_LINUX)
	chmod a+rx ./dist_linux/$(APP_NAME)

#build_windows: ## (MODULE) Builds executable to ./dist_win folder. Must be on Windows!
#	$(PYINSTALLER) $(MAIN_FILE) $(CLEAN) $(ONEFILE) $(WINDOWED) $(OUTPUT_NAME) $(ICON) $(WORKPATH_LINUX) $(DISTPATH_LINUX)

install_linux_binary: ## (MODULE) Installs binary in ~/bin
	mkdir -p ~/bin

	# cp ${CURDIR}/dist_linux/quick_capture /home/${USER}/bin/quick_capture
	ln -s ${CURDIR}/dist_linux/$(APP_NAME) /home/${USER}/bin/$(APP_NAME)

install_linux_user_config: ## (MODULE) Installs config in ~/.vapps
	mkdir -p ~/.vapps
	cp -n ./quick_capture/.vapps/quick_capture.yaml ~/.vapps/quick_capture.yaml

create_desktop_file: ## (MODULE) Create .desktop in /dist_linux
	@echo '[Desktop Entry]\nName=$(APP_NAME)\nIcon=${CURDIR}/$(APP_NAME)/resources/icon.png\nType=Application\nExec=${HOME}/bin/$(APP_NAME)\nTerminal=false' > ./dist_linux/$(APP_NAME).desktop
	cat ./dist_linux/$(APP_NAME).desktop

install_linux_desktop_file: ## (MODULE) Installs .desktop file
	desktop-file-install --dir=${HOME}/.local/share/applications ./dist_linux/$(APP_NAME).desktop
	update-desktonp-database ${HOME}/.local/share/applications

install_linux: install_linux_binary install_linux_user_config create_desktop_file install_linux_desktop_file ## (MODULE) Builds from source, then installs Application to system.
	# TODO: Create Keyboard Shortcut
	# handled by dotfile atm.

	@echo "Completed Install."

clean: ## Remove all files created my Makefile
	rm -rf ./build_linux
	rm -rf ./dist_linux
	rm -rf ${HOME}/.local/share/application/$(APP_NAME).desktop
	rm -rf /home/${USER}/bin/$(APP_NAME)
	update-desktop-database ${HOME}/.local/share/application

help: ## Self-documented Makefile Help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
