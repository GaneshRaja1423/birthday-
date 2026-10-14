import os
from flask import Flask, render_template, send_from_directory

app = Flask(
    __name__,
    template_folder=".",
    static_folder=".",
    static_url_path=""
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/friendship")
def friendship():
    return render_template("friendship.html")

@app.route("/static/<path:filename>")
def serve_static(filename):
    if os.path.exists(os.path.join("static", filename)):
        return send_from_directory("static", filename)
    return send_from_directory(".", filename)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)