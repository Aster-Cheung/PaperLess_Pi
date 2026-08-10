# PaperLess_Pi
The purpose of this project is to apply what I learned in Cornell’s Machine Learning Foundations course to a Raspberry Pi Zero 2 W. The project uses AI to capture pictures of receipts, extract relevant information from them, and organize the extracted values into an Excel spreadsheet.

## Hardware
|Name of Hardware| Hardware Picture|
-------------- | ----------------------
|Raspberry Pi Zero 2W| <img width="2254" height="861" alt="20260808_181627" src="https://github.com/user-attachments/assets/6d04cf00-e756-4ea4-9c17-c0456c968194" />|
|Raspberry Pi Camera V 1.3| <img width="4032" height="1816" alt="20260809_223157" src="https://github.com/user-attachments/assets/30ff8352-a874-48fb-950c-af60c2e835f5" />|
|SD Card| 32 bit |

## Software
- Mistral AI
- Raspberry Pi OS: Legacy 32-bit


## Steps:
- Run in Powershell
- Login to your Raspberry Pi

1. Install any updates
   ```
   sudo apt update
   ```
   
3. Install native python package installer
   ```
   sudo apt install python3-pip -y
   ```
   
5. Install camera utility (depending on which OS system)
   |OS| Command |
   -----|--------
   |Modern OS| ```sudo apt install rpi-cam-apps -y```|
   |Legacy or Lite OS| ```sudo apt install libcamera-apps -y```|

6. Install System Level Libraries (Math)
   ```
   sudo apt install libopenblas-dev -y
   ```

8. Install Mistral AI Python SDK Framework
   ```
   pip3 install mistralai --break-system-packages
   ```

9. Create initial folder
   ```
   mkdir PaperLessPi
   ```

10. Step into initial folder
    ```
    cd PaperLessPi
    ```

11. Create / Open file
    ```
    nano capture.py
    ```

12. Create an account in Mistral AI and obtain an API key, go to powershell and run the following
    ```
    export MISTRAL_API_KEY="your_actual_key_here"
    ```

### To view data
1. Type ```python3``` and press enter, you will see the ```>>>``` symbol
2. Type these 2 lines:
   ```
   import pandas as pd
   pd.read_csv("receipts_log.csv")
   ```

### To view spreadsheet
1. Type ```python3 -m http.server 8000```, press enter

   <img width="1008" height="79" alt="image" src="https://github.com/user-attachments/assets/6df85961-99fd-4821-8a6b-d040fd3486ef" />
   
2. Go to any browser, type the Pi's IP:8000, for example:

   <img width="320" height="47" alt="image" src="https://github.com/user-attachments/assets/c33b56d5-cf6b-4cf5-957d-0bccee311d75" />
   
3. Click the following and download the spreadsheet:
   
   <img width="338" height="190" alt="image" src="https://github.com/user-attachments/assets/e04565e7-ecab-4baf-b161-125f546f53eb" />

4. View the spreadsheet:

   <img width="1306" height="314" alt="image" src="https://github.com/user-attachments/assets/92d9de4d-5162-4550-9b2f-25ca1bee83cc" />


# Result
<img width="2904" height="1816" alt="20260809_190954 (2)" src="https://github.com/user-attachments/assets/5b0e28e5-26af-49ec-907d-b19c21b88e96" />
<img width="1452" height="429" alt="image" src="https://github.com/user-attachments/assets/3be1540d-3a71-4c22-a316-c2430cbdfb72" />

# Conclusion
The receipt needs to be printed clearly and dark enough for the camera to detect all of the words accurately. In the left receipt, the text was too faded, which caused the AI to miss some words and make assumptions about the unclear information.

# Future work

