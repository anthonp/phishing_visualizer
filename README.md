# 📊 Phishing Email Metadata Visualizer

This project is a tool to **upload, merge, and visualize phishing email metadata**.  

It uses a **Flask backend** for handling CSV uploads and a **D3.js + PapaParse frontend** for rendering an interactive force-directed graph.

![Full View](/full_view.png)

---

## 🚀 Features

- **Upload & Merge**: Upload multiple CSVs; all rows are appended into `csvs/merged.csv`.
- **Force-Directed Graph**: Nodes = senders/recipients, edges = phishing email relations.
- **Tooltips**: Hover over edges to see subject + date.
- **Pan & Zoom**: Left-click drag to pan, mouse wheel to zoom.
- **Sidebar Summary**: Sender domains with counts + latest date observed.
- **Highlighting**: Top 5 phishing senders highlighted in amber.
- **WHOIS Links**: One-click external WHOIS lookups for top 10 domains.

⚠️ Security Warning
- Do not deploy this application on a publicly accessible server.
- This tool is designed for internal, local analysis of phishing email metadata.
- Uploaded CSVs may contain sensitive email addresses, subjects, or other confidential information.
- Exposing this app publicly is not recommended.
- Always run the app behind a secure network or VPN, or on your local machine only.

Some security tools do not export CSVs with SPF/DMARC/DKIM reporting, thus, I have not supported it at this time. Secuity tools will often come with additional fields within CSVs, e.x. 15-20 CSV fields rather than just 4. You will have to modify this code to support your own initiatives, such as sanitizing CSV fields (to remove special characters and encoding), and define the CSV field headers to populate (`writer.writerow([])` has worked for me). Once you have additional fields such as "action on email", etc, I recommend adding the field under the tool tips display when you hover over connectors. The next phase are drill-downs and basic searching.

![Tool Tips](/tool_tips.png)

---

## 🛠️ Tech Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML, JavaScript, [PapaParse](https://github.com/mholt/PapaParse) (MIT), [D3.js](https://d3js.org/) (BSD-3-Clause)
- **Data Format**: CSVs with headers: sender,recipient,subject,date

![Animated Gif](/screen_recording.gif)

---

## 📂 Project Structure
```
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend (D3.js + PapaParse)
├── csvs/ # Uploaded CSVs + merged file
│ └── merged.csv # Created automatically after uploads
├── requirements.txt
└── LICENSE
```

---

## ⚙️ Installation (Ubuntu-based system)

1. Clone the repo:
```bash
git clone https://github.com/anthonp/phishing_visualizer.git
cd phishing_visualizer
```
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Flask app:
```bash
python3 app.py
```
5. Open in your browser:
```bash
http://127.0.0.1:5000
```

---

## 📦 Requirements:

requirements.txt contains:
```bash
Flask
```

---

## ⚖️ License (See NOTICE.md):

This project is licensed under the MIT License.

It also makes use of the following third-party libraries:

PapaParse – MIT License;
D3.js - BSD-3-Clause License / ISC License
