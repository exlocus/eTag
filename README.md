# eTag 🎵

## 📋 Project description

[**Русская версия / Russian Version**](README.ru.md)

Welcome to **eTag** — an improved version of SoundTag.

## 🚀 Functional capabilities

- **💾 Audio file uploads**: Users can upload MP3 files with additional metadata, such as track name and cover image URL.
- **🎶 Track playback**: Each uploaded track is available for playback via a unique link.
- **📂 Track library**: All uploaded tracks are displayed in the library, where they can be viewed and played.
- **🔧 Error handling**: Error handling is implemented, including displaying a custom 404 page when attempting to access a non-existent track.

## 🛠️ Installation and startup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/exlocus/eTag.git
   cd eTag
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # Для Windows: env\Scripts\activate
   ```

3. **Set dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application**:

   ```bash
   python app.py
   ```

5. **Open your browser and go to**:

   ```
   http://127.0.0.1:5000/
   ```

## 📂 Project structure

- `app.py`: the main Flask application file.
- `templates/`: directory with HTML templates.
  - `upload.html`: file upload page.
  - `play.html`: track playback page.
  - `library.html`: track library page.
  - `404.html`: 404 error page.
- `uploads/`: directory for storing uploaded audio files and metadata.

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

*Note: **eTag** is an improved version of the original SoundTag, offering additional features and an enhanced user interface.*
