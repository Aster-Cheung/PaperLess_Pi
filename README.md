# PaperLess_Pi
The purpose of this project is to apply what I learned in Cornell’s Machine Learning Foundations course to a Raspberry Pi Zero 2 W. The project uses AI to capture pictures of receipts, extract relevant information from them, and organize the extracted values into an Excel spreadsheet.

## Hardware
|Name of Hardware| Hardware Picture|
-------------- | ----------------------
|Raspberry Pi Zero 2W| <img width="2254" height="861" alt="20260808_181627" src="https://github.com/user-attachments/assets/6d04cf00-e756-4ea4-9c17-c0456c968194" />|
|Raspberry Pi Camera V 1.3| <img width="4032" height="1816" alt="20260809_223157" src="https://github.com/user-attachments/assets/30ff8352-a874-48fb-950c-af60c2e835f5" />|



Steps
1. sudo apt update
2. sudo apt install libcamera-apps -y
3. sudo apt install python3-pip -y
4. pip3 install google-genai --break-system-packages (originally pip3 install google-genai - tell Pi that I know what I am doing)
5. mkdir PaperLessPi
cd PaperLessPi
6. sudo apt update && sudo apt install libopenblas-dev -y


# Result
<img width="2904" height="1816" alt="20260809_190954 (2)" src="https://github.com/user-attachments/assets/5b0e28e5-26af-49ec-907d-b19c21b88e96" />
<img width="1452" height="429" alt="image" src="https://github.com/user-attachments/assets/3be1540d-3a71-4c22-a316-c2430cbdfb72" />

# Conclusion
The receipt needs to be printed clearly and dark enough for the camera to detect all of the words accurately. In the left receipt, the text was too faded, which caused the AI to miss some words and make assumptions about the unclear information.

# Future work

