import os
import zipfile

import urllib.request

url = 'https://storage.googleapis.com/learning-datasets/horse-or-human.zip'
output_path = 'C:/path/to/your/desired/location/horse-or-human.zip'  # Change this to the desired path

# Download the file and save it locally
urllib.request.urlretrieve(url, output_path)

print(f"File downloaded successfully to {output_path}")

local_zip = 'C:/Users/kgt/OneDrive/Desktop/coding/virtualintern/horse-or-human.zip'  # Modify this path
extract_to = 'C:/Users/kgt/OneDrive/Desktop/coding/virtualintern'

# Ensure the extraction directory exists
if not os.path.exists(extract_to):
    os.makedirs(extract_to)

# Open and extract the zip file
with zipfile.ZipFile(local_zip, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f"File extracted to: {extract_to}")

