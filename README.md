# Format Converter

The Format Converter is software created to automate the creation of two email lists that need to be sent out each day. After receiving input, the Format Converter creates a .txt file to be imported to turboSMTP's SendBlaster 4 and copies a semi-colon delimited list to the user's clipboard to be pasted in Outlook.

Format Converter is created for use on Windows, although the .py file has been included so a user could implement the same code on a Mac or Linux machine with minor adjustments.

## Installation

Download the required files from GitHub and store them wherever is preferable. The formatconverter.exe must be in the same folder as the Dependencies folder for the program to run correctly. The logo.ico file also must remain in the Dependencies folder. No other installation is required.

## Usage

After launching the program, the user is to enter each email in the list into the light blue box, with each email being on its own line. Once entered, press **Convert**, and the Format Converter will do two things:

1. Create a .txt file where each email is on a newline so it can be imported into SendBlaster 4, our email software
2. Copy a semi-colon delimited list of the same emails to the user's clipboard, which can then be pasted into the recipients section of Microsoft Outlook

Each time **Convert** is pressed, the blue box is saved as a .txt file, and the orange box is copied to the user's clipboard. The program can be run repeatedly in the same session, but each time **Convert** is pressed, the previous .txt file will be overwritten.

The .txt file will be saved in the same directory as formatconverter.exe unless otherwise specified.

## Inputting the .txt file into SendBlaster 4

The .txt file will be named emailList.txt by default. To import this file into SendBlaster 4:

1. Launch the program and select the **Lists and addresses** tab on the left-hand side
2. Select **Import**
3. Under the first drop down box, make sure the desired tip list to import to is selected
4. For **Select data source to be imported** select **Import from external text file**
5. For **Select desired operation** select **Add to the list and subscribe new addresses**
6. Select **Import**
7. for **Import file path** select the location of the .txt file
8. Make sure **Delimited** is selected and ";" for **Field delimiter**
9. Uncheck **First row contains field names**
10. Check **Don't add addresses when duplicated or already present in the list**
11. Check **Subscribe addresses already present in list**
12. Select **Next >**
13. Under the **Email** drop down box, select the first email listed
14. Select **Next >**

The emails in the .txt file will then be imported into the selected list. If the email was already present on the list, it will not be added, but it will be re-subscribed if it is unsubscribed.

## Python Information

The program has been written in python 3.9 but has been compiled as a .exe. Because future users may desire to modify the program, the .py file has been included in the Dependencies folder, along with a breakdown of the code.

The python written for this is incredibly simple (just 43 lines) and anyone with familiarity with python will find this section unnecessary (except perhaps the section on compiling code). Instead, the following is written for those with little to no experience in python.

#### Dependencies

```python
import os
import tkinter as tk
```
`os` is required for the program to copy the code to the clipboard, and `tkinter` is the module used to run the window view. Both must be installed for the .py file to run, but after the program is compiled, they (along with python as a whole) do not need to be installed on the computer.

#### Code to change

The name of the .txt file can be changed by altering the string:

```python
file_name = 'emailList.txt'
```

The [color](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter) of the background can be changed by altering the string:

```python
background_color = 'gray'
```

And the other colors can be found in the code below and altered by changing:
```python
inputtxt = tk.Text(root, height = 10, width = 40, bg = "cornflower blue")
Output = tk.Text(root, height = 10, width = 40, bg = "salmon1")
```

Finally, there is a logo at the upper left side of the window, to change it, simply create a new .ico file, store it in the Dependencies folder, and then update the relative directory path at:

```Python
root.iconbitmap('Dependencies\logo.ico')
```

#### Running the code

Depending on the version of python installed, the code is now able to be run from the terminal by typing:

```bash
python formatconverter.py
```

But it is possible that rather than `python`, the user may need to type `python3`


#### Compiling the code

For this project, the code was compiled using [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/). Installation and usage instructions are available online, but a great starting point is [here](https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi)
