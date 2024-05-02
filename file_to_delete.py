import os
import typer

app = typer.Typer()

def delete_files_with_extension(folder_path: str, file_extension: str):
    """
    Deletes all files with the specified extension in the specified folder.
    """
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                typer.echo(f"Deleted file: {file_path}")
        typer.echo(f"Deletion of files with extension '{file_extension}' completed.")
    except FileNotFoundError:
        typer.echo(f"Folder not found: {folder_path}")
    except Exception as e:
        typer.echo(f"Error deleting file: {file_path} - {e}")

@app.command()
def delete_files(folder_path: str = typer.Argument(..., help="Path to the folder containing files to delete"),
                  file_extension: str = typer.Option(..., "--extension", "-ext", help="File extension to delete")):
    """
    Delete files with a specified extension from a specified folder.
    """
    delete_files_with_extension(folder_path, file_extension)

if __name__ == "__main__":
    app()
