from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify({
        "owner": "Nidhi Mishra",
        "role": "Software Engineer at HCL Software",
        "message": "✨ Welcome to Cloud with Nidhi ✨",
        "tech_stack": [
            "Python",
            "Flask",
            "Docker",
            "Jenkins",
            "CI/CD"
        ],
        "deployment": "Built with Flask, containerized using Docker, and deployed via Jenkins Pipeline 🚀"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
