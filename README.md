# 🔐 Static Website with Login System

Welcome to the **Static Website Deployment with Flask Login System** project!  
This is a simple, responsive landing page with secure user authentication, built using **Flask + Bootstrap** with **SQLite DB**.

---

## 📌 Features

- 🚀 Beautiful Landing Page (Responsive & Mobile-friendly)
- 🔐 Secure Login & Registration with password hashing
- 🧠 SQLite3 Database integration
- ✨ Flash messages and session handling
- 🛠️ `init_db.py` to create or update users easily

---

## 🧱 Tech Stack

| Layer       | Tools Used              |
|-------------|------------------------|
| Frontend    | HTML, CSS, Bootstrap   |
| Backend     | Python, Flask          |
| Database    | SQLite3                |
| Styling     | Bootstrap 5 + Custom CSS |

---

## 📂 Project Structure

```
staticwebsitedeployments/
├── app.py              # Flask main app
├── init_db.py          # Script to create/update users
├── requirements.txt    # Dependencies
├── database/
│   └── users.db        # SQLite DB (optional for .gitignore)
├── templates/
│   ├── index.html      # Landing page
│   ├── login.html      # Login form
│   └── register.html   # Registration form
├── static/
│   └── css/
│       └── style.css   # Custom responsive styles
```

---

## 🚀 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Alok77it/staticwebsitedeployments.git
cd staticwebsitedeployments
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database with Default User

```bash
python3 init_db.py
```

> Creates/updates a user:  
> - Username: **alok**  
> - Password: **alok123**

### 5. Run the App

```bash
python3 app.py
```
Then open 👉 http://localhost:5000

---

## 🔁 How to Contribute

We welcome contributions! Here’s how you can get started:

1. **Fork** the repository  
2. **Clone** your forked repo  
3. **Create a new branch:**
    ```bash
    git checkout -b feature-branch-name
    ```
4. **Add your code** ✅  
5. **Commit and push:**
    ```bash
    git add .
    git commit -m "Added new feature"
    git push origin feature-branch-name
    ```
6. Go to GitHub → **Create Pull Request**

---
