
import requests
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('branding.xml')
root = tree.getroot()

# Extract class names
class_names = []
for elem in root.findall('.//name'):  # Adjust the path according to your XML structure
    class_names.append(elem.text)    
    print(elem.text)


# URL of the website to scrape
url = 'https://www.friendbank.net/'

# Send a request to the website
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements with the class names
extracted_data = {}
for class_name in class_names:
    elements = soup.find_all(class_=class_name)
    for element in elements:
        # You can customize what data to extract (text, images, etc.)
        extracted_data[class_name] = extracted_data.get(class_name, []) + [element.text]

# Convert the extracted data to JSON format
json_data = json.dumps(extracted_data, indent=4)
print(json_data)
