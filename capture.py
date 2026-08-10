import subprocess
import os
import json
import csv
import base64
import pandas as pd
from mistralai.client import Mistral

#========== MistralAI Client Setup ================
client = Mistral()

CSV_FILE = "receipts_log.csv"

def image_to_base64(file_path: str) -> str:
        """ Reads an image file and returns its base64 encoded string."""
        with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode('utf-8')

def process_image_with_mistral(base64_image):
        """Sends the base64 string to Mistral to extract data values."""
        print("Processing asset...")

        extraction_prompt = """

        Some critical rules that you need to follow when you do the analyses:
        1. Look for iconic logos or layout markers.
        - If you see a bullseye Logo or a target symbol, the `store_name` is strictly "Target".
        - If you see a flower that is made of six strokes or the word "walmart", the `store_name` is strictly "Walmart".
        - If you see a double-tail mermaid logo, the `store_name` is strictly "Starbucks".
        
        2. Please extract the following information from the document image provided and structure it as a JSON Object:
        - `store_name`: The name of the business or store.
        - `transaction_date`: The date of the transaction (use UUU-MM-DD format).
        - `tax_amount`: The tax charged (if visible).
        - `total_amount`: The final payment total.
        - `items`: [
                {
                        "name": "The name of the item",
                        "quantity": 1,
                        "price_per_item": 0.00
                }
        ]
        """

        Mistral_response = client.chat.complete(
                model = "mistral-large-latest",
                messages = [
                        {
                                "role": "user",
                                "content": [
                                        {"type": "text", "text": extraction_prompt},
                                        {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
                                ]
                        }
                ],
                response_format = {"type": "json_object"},
        )
        # Return
        return json.loads(Mistral_response.choices[0].message.content)

def log_with_pandas(data):
        """Use a pandas DataFrame to handle and clean data records."""

        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #Loop through new detailed items list to build a clean text string
        formatted_items = []
        raw_items_list = data.get('items',[])

        if isinstance(raw_items_list, list):
                for item in raw_items_list:
                        if isinstance(item, dict):
                                name = item.get('name','Unknown Item')
                                qty = item.get('quantity',1)
                                price = item.get('price_per_item', 0.00)
                                formatted_items.append(f"{qty} x {name} (${price:.2f})")
                        else:
                                formatted_items.append(str(item))
        items_string = ", ".join(formatted_items)

        # Map matching columns
        new_record = pd.DataFrame([{
        "Timestamp Logged": timestamp,
        "Store Name": data.get('store_name', 'Unknown Store'),
        "Transaction Date": data.get('transaction_date', 'Unknown Date'),
        "Tax Amount ($)": data.get('tax_amount', 0.00),
        "Items Bought": item_string,
        "Total Amount ($)": data.get('total_amount',0.00)
        }])


        # Append DatFrame into the storage file tracking log
        if not os.path.exists(CSV_FILE):
                new_record.to_csv(CSV_FILE, index = False)
        else:
                new_record.to_csv(CSV_FILE, mode = 'a', header = False, index = False)

        print(f"Pandas Log: Successfully saved entry for {data.get('store_name')}!")




def main():
        print("\n ----------PAPERLESS PI ACTIVE ------------")
        print("Align your receipt and press ENTER to scan.\n")

        try:
                while True:
                        input("Are you ready? Press Enter to snap image...")
                        temp_img = "temp_receipt.jpg"

                        # Snaps  recepts
                        print("Snapping impage asset...")
                        cmd = ["rpicam-still", "-o", "temp_receipt.jpg", "--immediate", "--nopreview"]
                        subprocess.run(cmd, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)

                        if os.path.exists(temp_img):
                                try:
                                        # 1. Turn image into base64 string
                                        base64_data = image_to_base64(temp_img)

                                        # 2. Extract  structured JSON with API
                                        raw_json_output = process_image_with_mistral(base64_data)


                                        print("\n ---- Extracted Data JSON ----")
                                        print(json.dumps(raw_json_output, indent=4))

                                        print(" ------------------------------\n")

                                        # 3. Log results to system using pandas structure
                                        log_with_pandas(raw_json_output)


                                except Exception as e:
                                        print(f"Core processing error: {e}")
                                finally:
                                        if os.path.exists(temp_img):
                                                os.remove(temp_img)

                        else:
                                print("Capture error. Check your hardware connections, such as the ribbon connections")
        except KeyboardInterrupt:
                print("\nExiting PaperLessPi. Keep tracking data!")

if __name__ == "__main__":
        main()




