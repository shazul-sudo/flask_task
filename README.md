# NexaWeb — Flask Multi-Page Website
### SE-105L Introduction to Computing · SSUET/QR/114

---

## 📁 Project Structure

```
nexaweb/
├── app.py                  ← Main Flask application (all routes)
├── requirements.txt        ← Python dependencies
├── README.md
├── templates/
│   ├── base.html           ← Shared layout (nav + footer)
│   ├── index.html          ← Home        /
│   ├── about.html          ← About       /about
│   ├── services.html       ← Services    /services
│   ├── gallery.html        ← Gallery     /gallery
│   ├── contact.html        ← Contact     /contact
│   ├── login.html          ← Login       /login
│   └── register.html       ← Register    /register
└── static/
    ├── css/
    │   ├── main.css        ← Shared styles (navbar, footer, buttons)
    │   └── pages.css       ← Page-specific styles
    └── js/
        └── main.js         ← Mobile nav, gallery filters, password strength
```

---

## 🚀 How to Run

### 1. Open this folder in VS Code

### 2. Install Flask
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```

### 4. Open your browser
```
http://127.0.0.1:5000
```

---

## 📄 Pages

| Route        | Page       | Design Theme              |
|--------------|------------|---------------------------|
| `/`          | Home       | Dark navy & gold          |
| `/about`     | About      | Warm cream & terracotta   |
| `/services`  | Services   | Teal & white cards        |
| `/gallery`   | Gallery    | Dark vivid masonry grid   |
| `/contact`   | Contact    | Sage green two-panel      |
| `/login`     | Login      | Terminal dark blue        |
| `/register`  | Register   | Coral & navy split        |

---

## ✅ Features

- **Jinja2 template inheritance** — `base.html` provides the navbar and footer; all pages `{% extends "base.html" %}`.
- **Dynamic data** — Services and Gallery items are passed as Python lists from `app.py` into templates.
- **Form validation** — All forms validate server-side using `request.form`; errors shown via `flash()`.
- **Session-based auth** — Login stores the username in `session`; the navbar updates to show the user.
- **Responsive** — Hamburger menu on mobile, stacked layouts on small screens.
- **Simulated auth** — No database; login/register workflows are demonstrated without storing any data.

---

