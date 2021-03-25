import os
import tkinter as tk

file_name = 'emailList.txt'
background_color = 'gray'

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

def take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    file_string = INPUT
    email_list = file_string.split("\n")
    email_list = [i for i in email_list if i]#Remove blank entries

    semicolon_string = "; ".join(email_list)
    addToClipBoard(semicolon_string)
    Output.delete('1.0', tk.END)
    Output.insert(tk.END, semicolon_string)

    output_file = open(file_name, "w")
    output_file.write(file_string)
    output_file.close()
    output_label.pack()

root = tk.Tk()
root.iconbitmap('Dependencies\logo.ico')
root.title("Email List Formatter")
root.geometry("600x450")
root.configure(bg= background_color)

input_label = tk.Label(text = "Input each email on its own line:", background = background_color)
inputtxt = tk.Text(root, height = 10, width = 40, bg = "cornflower blue")
Output = tk.Text(root, height = 10, width = 40, bg = "salmon1")
Display = tk.Button(root, height = 2, width = 20, text = "Convert", command = lambda:take_input(), background = background_color)
output_label = tk.Label(text = "Your input has been written to file: " + file_name + " and your output has been copied to your clipboard", background = background_color)

input_label.pack()
inputtxt.pack()
Display.pack()
Output.pack()
tk.mainloop()
