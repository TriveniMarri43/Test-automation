import os
import shutil

def organize_files(directory):
    """
    Organizes files in the specified directory into subfolders by file type.
    """
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
        "Code": [".py", ".java", ".c", ".cpp", ".html", ".css", ".js"],
        "Others": []  # Catch-all for unclassified file types
    }

    # Ensure subfolders exist
    for category in file_categories.keys():
        category_path = os.path.join(directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Move files into respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify the file's category
        file_moved = False
        for category, extensions in file_categories.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break

        # Move files that don't match any category to "Others"
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Others", filename))

    print("Files organized successfully!")

# Specify the directory to organize
directory_to_organize = input("Enter the path of the directory to organize: ").strip()
organize_files(directory_to_organize)
