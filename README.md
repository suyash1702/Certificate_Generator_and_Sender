# Certificate-Generator-and-SenderHere’s a professional and informative **`README.md`** file for your GitHub repo:  
[`Certificate_Generator_and_Sender`](https://github.com/suyash1702/Certificate_Generator_and_Sender)

# 🏆 Certificate Generator and Sender

This project automates the process of generating participation certificates from a Canva-designed template using student data from an Excel sheet. It also includes functionality to customize the certificate text (like inserting student name and event) and optionally send the certificates via email.

---

## 📌 Features

- ✅ Read student details from an Excel sheet
- 🎨 Dynamically insert **Name** and **Event** into a Canva-based certificate design
- 🖋️ Name written in **Shelley Script font**, in golden color
- 📤 Automatically save certificates as image files
- 📧 Optional: Email the generated certificates (Coming Soon)

---

## 📁 Folder Structure

```
Certificate_Generator_and_Sender/
├── fonts/                             # Font files (e.g., ShelleyAllegroScript.ttf)
├── certificates/                      # Output certificates
├── students.xlsx                      # Excel sheet with student data
├── certificate_template.png           # Certificate image from Canva
├── generate_certificates.py           # Main Python script
└── README.md                          # Project documentation
```

---

## 📥 Prerequisites

Install dependencies:

```bash
pip install pandas pillow openpyxl
```

Ensure you have the **Shelley Script font** (e.g., `ShelleyAllegroScript.ttf`) inside a folder named `fonts/`.

---

## 📋 Excel Format (`students.xlsx`)

| Team ID | Name           | Event               | E-mail               |
|---------|----------------|---------------------|----------------------|
| T001    | Ritesh Ukade   | Poster Presentation | ritesh@example.com   |
| T002    | Sneha Kulkarni| Coding Competition  | sneha.kul@example.com|

---

## 🚀 Usage

```bash
python generate_certificates.py
```

Certificates will be generated and saved in the `certificates/` folder.

---

## 📧 Email Sending (Coming Soon)

We're working on integrating an email-sending script using SMTP, to automatically email each participant their certificate.

---

## 📃 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

- Certificate design created using [Canva](https://www.canva.com/)
- Font: [Shelley Script](https://www.dafont.com/shelley-allegro.font)

---

## 💡 Author

Made with ❤️ by [@suyash1702](https://github.com/suyash1702)
```
