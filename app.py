import os
import uuid
import json
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, abort

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    message = ""
    if request.method == "POST":
        if "file" not in request.files:
            message = "Нет файла"
            return render_template("upload.html", message=message)
        
        file = request.files["file"]
        if file.filename == "":
            message = "Файл не выбран"
            return render_template("upload.html", message=message)

        title = request.form.get("title", "").strip()
        image_url = request.form.get("image_url", "").strip()

        if file:
            unique_id = str(uuid.uuid4())[:8]
            filename = f"{unique_id}.mp3"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            metadata = {"title": title, "image_url": image_url}
            metadata_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{unique_id}.json")
            with open(metadata_path, "w", encoding="utf-8") as f:
                json.dump(metadata, f)

            play_link = url_for('play_sound', sound_id=unique_id)
            message = f"Файл загружен! Слушать: <a href='{play_link}'>{request.host_url}sound/{unique_id}</a>"
            return render_template("upload.html", message=message)
    return render_template("upload.html", message=message)

@app.route("/sound/<sound_id>")
def play_sound(sound_id):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{sound_id}.mp3")
    if os.path.exists(file_path):
        metadata_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{sound_id}.json")
        image_url = None
        title = None
        if os.path.exists(metadata_path):
            with open(metadata_path, "r", encoding="utf-8") as f:
                metadata = json.load(f)
                image_url = metadata.get("image_url")
                title = metadata.get("title")
        return render_template("play.html", sound_id=sound_id, image_url=image_url, title=title)
    else:
        abort(404)

@app.route("/uploads/<filename>")
def get_uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/library")
def library():
    sounds = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.endswith(".json"):
            sound_id = filename[:-5]  # Убираем расширение .json
            json_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    metadata = json.load(f)
            except Exception:
                metadata = {}
            mp3_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{sound_id}.mp3")
            if os.path.exists(mp3_path):
                sounds.append({
                    "sound_id": sound_id,
                    "title": metadata.get("title") or sound_id,
                    "image_url": metadata.get("image_url"),
                    "play_url": url_for("play_sound", sound_id=sound_id)
                })
    sounds.sort(key=lambda x: x["title"].lower())
    return render_template("library.html", sounds=sounds)

# Обработчик ошибки 404, возвращающий шаблон 404.html
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
