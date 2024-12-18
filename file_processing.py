import os
import shutil
from tkinter import filedialog, messagebox


class FileProcessor:
    def __init__(self, tk, target_directory):
        """
        target_directory requires a relative directory such as:
        target_directory = os.path.join(os.getcwd(), "data", "statements")
        set up to take a path as a list which is then turned into a string.
        """
        self.window = tk
        self.window.title("File Uploader")

        self.target_directory = os.path.join(os.getcwd(), target_directory)
        os.makedirs(self.target_directory, exist_ok=True)

        # upload_button = Button(self.window, text="Upload File", command=self.upload_file)
        # upload_button.pack(pady=20)

    def upload_file(self, file_name):
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("All Files", "*.csv")]
        )
        if not file_path:
            return

        try:
            original_extension = os.path.splitext(file_path)[1]  # Get the file extension
            new_name = f"{file_name}{original_extension}"

            destination_path = os.path.join(self.target_directory, new_name)

            shutil.copy(file_path, destination_path)

            messagebox.showinfo("Success", f"File saved as: {new_name}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
