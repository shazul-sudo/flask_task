from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'nexaweb-secret-key-2024'

# ─── HOME ────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html', active='home')

# ─── ABOUT ───────────────────────────────────────────────────────────
@app.route('/about')
def about():
    return render_template('about.html', active='about')

# ─── SERVICES ────────────────────────────────────────────────────────
@app.route('/services')
def services():
    service_list = [
        {'icon': '🎨', 'title': 'UI/UX Design',        'desc': 'Beautiful, user-centred interfaces built with precision and care.',          'price': '$500'},
        {'icon': '🐍', 'title': 'Flask Development',   'desc': 'Robust Python backends with clean routing and Jinja2 templates.',            'price': '$800'},
        {'icon': '🗄️', 'title': 'Database Integration','desc': 'SQLAlchemy-powered schemas for SQLite, PostgreSQL, or MySQL.',               'price': '$300'},
        {'icon': '🔐', 'title': 'Authentication',      'desc': 'Secure login, registration, and session management with Flask-Login.',       'price': '$250'},
        {'icon': '🚀', 'title': 'Cloud Deployment',    'desc': 'Deploy to Heroku or AWS with Gunicorn, Nginx, and SSL configured.',          'price': '$200'},
        {'icon': '📊', 'title': 'Data Visualisation',  'desc': 'Interactive dashboards with Chart.js or Plotly integrated into Flask.',      'price': '$450'},
    ]
    return render_template('services.html', active='services', services=service_list)

# ─── GALLERY ─────────────────────────────────────────────────────────
@app.route('/gallery')
def gallery():
    items = [
        {'emoji': '🌌', 'title': 'Cosmic Dashboard',  'tag': 'Web Design',    'cls': 'g1 h2'},
        {'emoji': '🌸', 'title': 'Bloom UI Kit',      'tag': 'UI Components', 'cls': 'g2 h3'},
        {'emoji': '🌊', 'title': 'Ocean Analytics',   'tag': 'Data Viz',      'cls': 'g3 h4'},
        {'emoji': '🌅', 'title': 'Sunset Landing',    'tag': 'Web Design',    'cls': 'g4 h3'},
        {'emoji': '🌿', 'title': 'Botanical Cards',   'tag': 'Digital Art',   'cls': 'g5 h2'},
        {'emoji': '⚡', 'title': 'Energy Dashboard',  'tag': 'Projects',      'cls': 'g6 h5'},
        {'emoji': '🦋', 'title': 'Metamorphic Art',   'tag': 'Digital Art',   'cls': 'g7 h1'},
        {'emoji': '🏙️', 'title': 'Urban Interface',   'tag': 'UI Components', 'cls': 'g8 h4'},
        {'emoji': '🔥', 'title': 'Blaze Theme',       'tag': 'Web Design',    'cls': 'g9 h2'},
    ]
    return render_template('gallery.html', active='gallery', items=items)

# ─── CONTACT ─────────────────────────────────────────────────────────
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name',    '').strip()
        email   = request.form.get('email',   '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()

        errors = []
        if not name:                 errors.append('Full name is required.')
        if not email or '@' not in email: errors.append('A valid email address is required.')
        if not message:              errors.append('Message cannot be empty.')

        if errors:
            for e in errors:
                flash(e, 'error')
        else:
            flash('✅ Thank you! Your message has been sent successfully.', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', active='contact')

# ─── LOGIN ────────────────────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash('Please enter both username and password.', 'error')
        else:
            # Simulated login — no real DB check
            session['user'] = username
            flash(f'✅ Welcome back, {username}! (Simulated login)', 'success')
            return redirect(url_for('home'))

    return render_template('login.html', active='login')

# ─── LOGOUT ───────────────────────────────────────────────────────────
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

# ─── REGISTER ─────────────────────────────────────────────────────────
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        full_name = request.form.get('full_name', '').strip()
        email     = request.form.get('email',     '').strip()
        username  = request.form.get('username',  '').strip()
        password  = request.form.get('password',  '').strip()

        errors = []
        if not full_name:                   errors.append('Full name is required.')
        if not email or '@' not in email:   errors.append('A valid email address is required.')
        if not username:                    errors.append('Username is required.')
        if len(password) < 6:              errors.append('Password must be at least 6 characters.')

        if errors:
            for e in errors:
                flash(e, 'error')
        else:
            flash('✅ Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html', active='register')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
