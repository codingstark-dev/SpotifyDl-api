from flask import Flask, jsonify, request, render_template, send_file
import SpotiFetch
import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        url = request.form.get("spotify_url")
        dfile = SpotiFetch.execute(url)
        if dfile and os.path.exists(dfile):
            return send_file(dfile, as_attachment=True)
    if SpotiFetch.path and os.path.exists(SpotiFetch.path):
        SpotiFetch.delete_folder_contents(SpotiFetch.path)
    return render_template("index.html")
    # return jsonify({"message": "hii"})


@app.route("/trackDetails", methods=["GET", "POST"])
def trackDetails():
    url = request.args.get("url")
    print(url)
    track = SpotiFetch.get_spotify_data(SpotiFetch.get_token(), url)
    return jsonify(track)


if __name__ == "__main__":
    app.run(debug=True)
