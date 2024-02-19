import tkinter as tk
from tkinter import messagebox
from tkinter import Text  # Added import for Text

class ResumeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Resume App")
        self.name = None
        self.email = None
        self.education = None
        self.additional_info = None
        self.skills = None
        self.interests = None
        self.courses = None
        self.projects = None

        tk.Label(master, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        tk.Label(master, text="Email:").grid(row=1, column=0, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=1, column=1)

        tk.Label(master, text="Jop Title:").grid(row=2, column=0, sticky="e")
        self.education_entry = tk.Entry(master)
        self.education_entry.grid(row=2, column=1)

        tk.Label(master, text="Additional Information:").grid(row=3, column=0, columnspan=2, sticky="w")
        self.additional_info_text = tk.Text(master, height=5, width=30)
        self.additional_info_text.grid(row=4, column=0, columnspan=2)

        tk.Label(master, text="Skills:").grid(row=5, column=0, columnspan=2, sticky="w")
        self.skills_text = tk.Text(master, height=5, width=30)
        self.skills_text.grid(row=6, column=0, columnspan=2)

        tk.Label(master, text="Interests:").grid(row=7, column=0, columnspan=2, sticky="w")
        self.interests_text = tk.Text(master, height=5, width=30)
        self.interests_text.grid(row=8, column=0, columnspan=2)

        tk.Label(master, text="Courses:").grid(row=9, column=0, columnspan=2, sticky="w")
        self.courses_text = tk.Text(master, height=5, width=30)
        self.courses_text.grid(row=10, column=0, columnspan=2)

        tk.Label(master, text="Projects:").grid(row=11, column=0, columnspan=2, sticky="w")
        self.projects_text = tk.Text(master, height=5, width=30)
        self.projects_text.grid(row=12, column=0, columnspan=2)

        tk.Button(master, text="Display Resume", command=self.display_resume).grid(row=13, column=0, columnspan=2)

    def display_resume(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        education = self.education_entry.get()
        additional_info = self.additional_info_text.get("1.0", tk.END).strip()
        skills = self.skills_text.get("1.0", tk.END).strip()
        interests = self.interests_text.get("1.0", tk.END).strip()
        courses = self.courses_text.get("1.0", tk.END).strip()
        projects = self.projects_text.get("1.0", tk.END).strip()

        # Generate HTML content
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{name}'s Resume</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 20px;
        }}
        h1, h2, p {{
            color: #333;
        }}
        .resume-container {{
            width: 60%;
            margin: auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
    </style>
</head>
<body>
    <div class="resume-container">
        <img src="shady.jpg" alt="Profile Image" style="width: 100px; border-radius: 50%;">
        <h1>{name}</h1>
        <p>Email: {email}</p>
        <p>Job Title: {education}</p>
        <h2>Additional Information:</h2>
        <p>{additional_info}</p>
        <h2>Skills:</h2>
        <p>{skills}</p>
        <h2>Interests:</h2>
        <p>{interests}</p>
        <h2>Courses:</h2>
        <p>{courses}</p>
        <h2>Projects:</h2>
        <p>{projects}</p>
    </div>
</body>
</html>
"""

        # Save the HTML content to a file or display it in a browser
        with open("resume.html", "w") as html_file:
            html_file.write(html_content)

        messagebox.showinfo("Resume", "Resume HTML generated and saved to 'resume.html'")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeApp(root)
    root.mainloop()
