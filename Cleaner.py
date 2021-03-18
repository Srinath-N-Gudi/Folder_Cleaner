import os
import time
def createAFile(fileName):
    if not os.path.exists(fileName):
        os.makedirs(fileName)
def move(folder, file):
    for files in file:
        os.replace(files, f"{folder}/{files}")
    
    
files = os.listdir()
files.remove("Cleaner.py")

createAFile("Images")
createAFile("Media")
createAFile("Documents")
createAFile("Applications")
createAFile("Others")
imgExt = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExt]
docExt = [".txt", ".docx", ".doc", ".pdf", ".ppt", ".xls", ".xlsx"]
doc = [file for file in files if os.path.splitext(file)[1].lower() in docExt]
medExt = [".mp3", ".mp4", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in medExt]
app = [".exe", ".msi"]
application = [file for file in files if os.path.splitext(file)[1].lower() in app]
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if  (ext not in imgExt) and (ext not in docExt) and (ext not in medExt) and (ext not in app) and os.path.isfile(file):
         others.append(file)
         
move("Images", images)
print("Seperating Images")
time.sleep(1)
move("Media", medias)
print("Seperating Medias")
time.sleep(1)
move("Documents", doc)
print("Seperating Documents")
time.sleep(1)
move("Applications", application)
print("Seperating Applications")
time.sleep(1)
move("Others", others)
print("Seperating Other files")
time.sleep(1)
print("Ending process")
print("Thank you")
time.sleep(5)
