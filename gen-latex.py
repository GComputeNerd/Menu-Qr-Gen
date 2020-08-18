import re, shutil
from os import system
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pyqrcode
from pyqrcode import QRCode
import png

template = open("format.txt").read().splitlines()
head = []

assert template[0] == "---", "Invalid Format File"

c_line = 0
last_line = len(template)
tempBool = True
i = 0

# Generating Head
while(tempBool):
    head.append(template[c_line])
    if (template[c_line] == "---" and c_line != 0):
        tempBool = False
    c_line += 1
head = head[1:-1]

# Getting FileName
for i in head:
    if (len(re.findall("=Name: (.{1,})", i)) != 0):
        fileName = re.findall("=Name: (.{1,})", i)[0]

shutil.copy('boilerplate.tex', fileName+".tex") # Copy Preamble to Template

f = open(fileName+".tex", "a")

f.write("\\begin{document}\n")


f.write("\\begin{center}\n")
# Generates Title Page
if ("&Logo" in head):
    f.write("\\includegraphics{logo.png} \\\\\n")

f.write("\\textbf{" + fileName + "} \\\\\n")

for i in head:
    if (len(re.findall("=Phone: (.{1,})", i)) != 0):
        f.write("\\textit{Phone : " + re.findall("=Phone: (.{1,})", i)[0] + "} \\\\\n")

f.write("\\end{center}\n")
f.write("\\newpage\n")

# Generates main menu
while (c_line < last_line):
    line = template[c_line]
    if (line[0] == "="):
        f.write("\\begin{Group}{"+ line[1:] + "}\n")
    elif (line[0] == "]"):
        f.write("\\Entry{" + line[1:].split("-")[0] + "}{" + line[1:].split("-")[1] + "} \\\\\n")
    elif (line[0] == "!"):
        f.write("\\Expl{" + line[1:] + "} \\\\\n")
    elif (line[0] == "+") :
        f.write("\\newpage\n")
    elif (line[0] == "-"):
        f.write("\end{Group} \\\\\\\\\n")
    c_line += 1

f.write("\\end{document}\n")

f.close()

# Generate PDF

system("pdflatex '" + fileName + ".tex'")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file1 = drive.CreateFile({'title': fileName + ".pdf"})
file1.SetContentFile(fileName + ".pdf")
file1.Upload()

permission = file1.InsertPermission({'type': 'anyone', 'value': 'anyone', 'role': 'reader'})

print("File is available at",file1['alternateLink'])

system("rm '" + fileName + "'.*")

link = pyqrcode.create(file1['alternateLink'])
link.png(fileName+"-QR_Code.png", scale=6)
