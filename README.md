# FileDeletion
File delete using python script
The script defines a function delete_files_with_extension that deletes all files with a specified extension in a given folder.
The Typer app is created using typer.Typer().
The delete_files command is defined, which takes two arguments:
folder_path: Path to the folder containing the files to delete (provided as an argument).
file_extension: File extension to delete (provided as an option).
Inside the delete_files command, the delete_files_with_extension function is called with the provided folder path and file extension.
If the folder or any file is not found, appropriate error messages are displayed.
After deletion, a message indicating the completion of the deletion process is printed.
