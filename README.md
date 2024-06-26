# Snipping Tool

<img src='https://i.imgur.com/VZYChL1.png' />

> A Snipping Tool built using Python that allows users to capture screenshots, similar to windows snip tool (WIN + Shift + S)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [About](#about)
  - [Features](#features)
  - [Screenshots](#screenshots)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

The Python Snipping Tool is an open-source project, similar to the one found in Windows. Users can capture single or multiple screen snips using this tool. The tool is actually made to use in another project. So not optimized much to use alone.

### Features

- Capture screenshots of the  specific region.
- Capture screenshots of multiple ROIs.
- Save screenshots in popular image formats (PNG, JPEG, etc.).


## Getting Started

### Prerequisites

- Python 3.x
 - Tkinter
 - Pillow

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/abdxzi/sniptool.git
   ```
   
2. Navigate to the project directory:
   ```sh
   cd sniptool
   ```

## Usage

Run the `snipping_tool.py` by double click

## Import to other programs
   ```python
   from snipper import ScreenSnipper
   
   app = ScreenSnipper()
   snips = app.snip()
   print(snips)

   # [<PIL.Image.Image image mode=RGB size=310x250 at 0x228AEDB4D50>, <PIL.Image.Image image mode=RGB size=454x307 at 0x228AEDB4E10>]
  
   ```
The program retruns screenshots as an array of PIL images that can be processed further. We can save the images to suitable formate as using Pillow library `save()`:

   ```python
   
   for image in snips:
      image.save(output_path, format='PNG')
  
   ```

## Contributing

Contributions are welcome!

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt) for more information.
