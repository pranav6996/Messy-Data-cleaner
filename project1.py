import os
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

def clean_dialogue_file_gui():
    file_path = filedialog.askopenfilename(title="Select your  file", filetypes=[("Text files", "*.txt")])
    
    if not file_path:
        return  
    
    logs = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
            single_line = ' '.join(raw_content.split())
            logs.append(f"[{datetime.now()}] File opened and cleaned.")

        base_dir = os.path.dirname(file_path)
        cleaned_path = os.path.join(base_dir, 'cleaned_output.txt')
        numbered_path = os.path.join(base_dir, 'numbered_output.txt')
        log_path = os.path.join(base_dir, 'log.txt')

        with open(cleaned_path, 'w', encoding='utf-8') as f:
            f.write(single_line)
            logs.append(f"[{datetime.now()}] Cleaned file saved at: {cleaned_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(numbered_path, 'w', encoding='utf-8') as f:
            for i, line in enumerate(lines):
                fixed = ' '.join(line.strip().split())
                if fixed:
                    f.write(f"{i + 1}. {fixed}\n")
            logs.append(f"[{datetime.now()}] Numbered file saved at: {numbered_path}")

        with open(log_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(logs))
            logs.append(f"[{datetime.now()}] Log saved at: {log_path}")

        messagebox.showinfo("✨ All Done!", f"Cleaned + Numbered files saved.\nCheck:\n{base_dir}")
    
    except Exception as e:
        messagebox.showerror("💥 Error!", str(e))

# 🎨 UI Setup
def launch_gui():
    root = tk.Tk()
    root.title("Messy Data  Cleaner 💬✨")
    root.geometry("400x250")
    root.resizable(False, False)

    tk.Label(root, text="MESSY DATA  CLEANER", font=("Courier", 16, "bold")).pack(pady=20)

    tk.Button(
        root,
        text="📂 Select the you File you want,human",
        font=("Helvetica", 12),
        command=clean_dialogue_file_gui,
        bg="#e1eaff",
        padx=20,
        pady=10
    ).pack(pady=10)

    tk.Label(root, text="Made with 🖐️ by Pranav", font=("Courier", 10)).pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == '__main__':
    launch_gui()
