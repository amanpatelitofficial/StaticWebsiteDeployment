from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'alok_secret_key'  # Change to secure secret key

# Connect DB
def get_db_connection():
    conn = sqlite3.connect('database/users.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['user'] = username
            flash('Login Successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

# Add below login route in app.py

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)
        conn = get_db_connection()

        # Check if user already exists
        existing = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if existing:
            flash('Username already exists', 'danger')
            conn.close()
            return redirect(url_for('register'))

        # Insert new user
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()
        flash('User registered successfully! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)

