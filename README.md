# Snipping Tool

![Project Logo](images/banner.png)

> A Snipping Tool built using Python that allows users to capture screenshots, similar to windows snip tool

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

### Screenshots

![Screenshot 1](screenshots/screenshot1.png)
<!-- Add more screenshots if needed -->

## Getting Started

### Prerequisites

- Python 3.x
 - Tkinter
 - Pillow

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Python-Snipping-Tool.git
   ```
   
2. Navigate to the project directory:
   ```sh
   cd Python-Snipping-Tool
   ```

## Usage

Run the `snipping_tool.py` by double click

## Import to other programs
   ```python
   from snipper import ScreenSnipper
   
   app = ScreenSnipper()
   snips = app.snip()
   print(snips)
  
   ```
The program retruns screenshots as an array of PIL images.

## Contributing

Contributions are welcome!

## License

Distributed under the MIT License. See `LICENSE` for more information.
