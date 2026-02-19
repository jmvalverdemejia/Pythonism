from flask import Flask, jsonify

app = Flask(__name__)

# This is a 'Route'. In your day, this was a Servlet mapping.
@app.route('/')
def home():
    return "<h1>Project Manager Dashboard API</h1><p>The server is running!</p>"

# This returns JSON - the universal language of modern apps.
@app.route('/api/status')
def get_status():
    # In Java 2, you'd need a library to turn an object into JSON.
    # Here, we just return a dictionary.
    status_report = {
        "project": "Bridge the Gap",
        "progress": "95%",
        "health": "Green"
    }
    return jsonify(status_report)

if __name__ == "__main__":
    # This starts the web server on your own computer!
    app.run(debug=True)