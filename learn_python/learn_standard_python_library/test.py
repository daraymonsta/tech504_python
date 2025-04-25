# Rename files in a directory
import os

directory = "/path/to/files"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        new_name = f"renamed_{filename}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
print("Files renamed successfully!")