import os
file_extention=input("Enter the file extention")
def delete_txt_files(folder_path): #function to delete
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(file_extention):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except Exception as e:
        print(f"Error deleting file: {file_path} - {e}")

# Example usage:
folder_path = "C:\\Users\\risha\\Music\\disc" #change with your actual path of folder
delete_txt_files(folder_path)
