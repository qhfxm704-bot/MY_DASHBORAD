from flask import Flask, render_template, request, redirect

app = Flask(__name__)
skills = []

@app.route('/')
def home():
    return render_template('index.html', data=skills)

@app.route('/send', methods=['POST'])
def send():
    skill = request.form.get('skill')
    skills.append(skill)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)