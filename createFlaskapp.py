import os

app_name = input("Enter your Flask app name: ")

# Create the app directory and files
os.mkdir(app_name)
os.chdir(app_name)


with open('app.py', 'w') as f:
    f.write(f'''from flask import Flask, render_template, request, redirect, url_for
#If you plan to use a database
from cs50 import SQL

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
''')

# Create the templates directory and HTML files
os.mkdir('templates')
os.chdir('templates')

open('base.html', 'w').write('''
<!DOCTYPE html>
<html>
<head>
  <title>{% block title %}{% endblock %}</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
''')

open('home.html', 'w').write('''
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome to the home page!</h1>
{% endblock %}
''')

open('about.html', 'w').write('''
{% extends "base.html" %}
{% block title %}About{% endblock %}
{% block content %}
  <h1>About Us</h1>
  <p>We are a company that does stuff.</p>
{% endblock %}
''')

open('contact.html', 'w').write('''
{% extends "base.html" %}
{% block title %}Contact Us{% endblock %}
{% block content %}
  <h1>Contact Us</h1>
  <form method="POST" action="{{ url_for('contact') }}">
    <input type="text" name="name" placeholder="Your name" required><br>
    <input type="email" name="email" placeholder="Your email" required><br>
    <textarea name="message" placeholder="Your message" required></textarea><br>
    <button type="submit">Send</button>
  </form>
{% endblock %}
''')

open('thank_you.html', 'w').write('''
{% extends "base.html" %}
{% block title %}Thank You{% endblock %}
{% block content %}
  <h1>Thank You</h1>
  <p>Thank you for contacting us. </p>
{% endblock %}
''')

os.chdir('..')

# Create the static directory
os.mkdir('static')

# Print a success message
print(f'Successfully created {app_name} app!')
