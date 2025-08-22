import os
import shutil

# Path to the folder you want to organize
folder_path = r"C:\Users\YourDesktopName\Downloads"  # Change this to your folder

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Scripts": [".py", ".js", ".java", ".cpp"],
    "Codes/Scripts":[".sql"], # Add anything you want
    "Others": []  # Anything that doesn't match
}

def organize_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        for category, extensions in file_types.items():
            if ext in extensions:
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename} → {category}")
                moved = True
                break

        # If not matched, move to "Others"
        if not moved:
            others_folder = os.path.join(folder, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} → Others")

# Run the organizer
organize_files(folder_path)
print("✅ File organization complete!")
