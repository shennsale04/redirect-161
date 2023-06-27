from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registation', methods=['POST'])
def registration():
    # Process the registration form data here
    pay_load = {'name': request.form['name'],
                'subject': request.form['subject'],
                'email': request.form['email'],
                'phone': request.form['phone'],
                'tel': request.form['tel'],
                'dob': request.form['dob']}
    # Redirect to the 'admissionreference' page
    register_student(payload)
    return redirect(url_for('admissionreference'))

@app.route('/admissionreference')
def adref():
    return render_template('adrefscreen.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port) 
