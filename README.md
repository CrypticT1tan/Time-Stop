# COLOR PALETTE

Eyedropper application that allows you to extract colors and hex codes from any image file on your computer.

## Installation
Use package manager pip to install the following:

```bash
pip install tkinter
pip install pillow
```

## Usage
To build the executable file, run the command below in your terminal in the directory with the project files:

```bash
pyinstaller main.py --hidden-import=tkinter -y --icon=palette.icns --onefile --windowed --add-data="start.png:." --name "Color Palette"
```

To start, click the "Browse Image File" button to open up your computer's file system. 
Then, select the image file you want to open. Your image will be displayed on the canvas.
Click anywhere on the image to get the hex code and color of the clicked pixel.
You can hold up to 8 hex codes/colors at once.

## Contact
For any questions, contact me at gavinkiosco@gmail.com or CrypticT1tan on GitHub.

Icon made by Freepik from www.flaticon.com