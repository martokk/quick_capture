# Quick Capture

---

<div align="center">

[![Build status](https://github.com/martokk/quick_capture/workflows/build/badge.svg?branch=master&event=push)](https://github.com/martokk/quick_capture/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/quick_capture.svg)](https://pypi.org/project/quick_capture/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/martokk/quick_capture/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/martokk/quick_capture/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/martokk/quick_capture/releases)
[![License](https://img.shields.io/github/license/martokk/quick_capture)](https://github.com/martokk/quick_capture/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

A simple app to add a task/note to a local file

</div>

---

## Usage

The app can be triggered by keyboard shortcut (Meta+N).
After entering your note and pressing Enter, your note is appended to the end of a local text file.

Tip: Automatically sync local text file via Dropbox, Google Drive, etc.

## Installation

```shell
make install-linux
```

## Build & Install

Install Requirements/Dependencies

```shell
make install
make install-pyinstaller
make build-pyinstaller-linux
make install-linux
```

## Config

Edit `~/.vapps/quick_capture.yaml` configuration dotfile.

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/martokk/quick_capture/releases) page.

## 🛡 License

[![License](https://img.shields.io/github/license/martokk/quick_capture)](https://github.com/martokk/quick_capture/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/martokk/quick_capture/blob/master/LICENSE) for more details.
