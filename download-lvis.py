import requests
import os

# Define the URL for downloading the dataset
url = "http://images.cocodataset.org/zips/val2017.zip"  # Replace with the actual URL of the dataset

# Set the target directory where the dataset will be downloaded and extracted
target_directory = "/l/users/salwa.khatib/lvis1.0/"  # Replace with your desired target directory

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)
print("made directory\n")

# Download the dataset file
response = requests.get(url)
file_path = os.path.join(target_directory, "lvis_dataset.zip")  # Specify the file name and path
print("downloaded the zip file!\n")
with open(file_path, "wb") as file:
    file.write(response.content)

# Extract the dataset files
import zipfile
with zipfile.ZipFile(file_path, "r") as zip_ref:
    zip_ref.extractall(target_directory)

# Remove the downloaded ZIP file (optional)
os.remove(file_path)

print("LVIS dataset downloaded and extracted successfully!")
