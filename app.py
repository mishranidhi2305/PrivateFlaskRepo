from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': 'Nidhi Mishra',
        'role': 'Software Engineer',
        'company': 'HCL Software',
        'description': 'Hi Everyone 👋, It’s Nidhi Mishra. I am a passionate Software Engineer working at HCL Software with experience in Python, Automation Testing, API Testing, CI/CD Pipelines, Docker, Jenkins, and modern web technologies. I love building beautiful applications and solving real-world problems through technology.',
        'skills': [
            'Python',
            'Flask',
            'Docker',
            'Jenkins',
            'CI/CD',
            'API Testing',
            'Automation',
            'GitHub',
            'SQL'
        ]
    }

    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)