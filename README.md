# eTag 🎵

## 📋 Описание проекта

Добро пожаловать в **eTag** — улучшенную версию [SoundTag](https://soundtag.ru/).

## 🚀 Функциональные возможности

- **💾 Загрузка аудиофайлов**: пользователи могут загружать MP3-файлы с дополнительными метаданными, такими как название трека и URL изображения обложки.
- **🎶 Воспроизведение треков**: каждый загруженный трек доступен для воспроизведения через уникальную ссылку.
- **📂 Библиотека треков**: все загруженные треки отображаются в библиотеке, где их можно просмотреть и воспроизвести.
- **🔧 Обработка ошибок**: реализована обработка ошибок, включая отображение пользовательской страницы 404 при попытке доступа к несуществующему треку.

## 🛠️ Установка и запуск

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/yourusername/soundtag-plus.git
   cd soundtag-plus
   ```

2. **Создайте и активируйте виртуальное окружение**:

   ```bash
   python -m venv env
   source env/bin/activate  # Для Windows: env\Scripts\activate
   ```

3. **Установите зависимости**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Запустите приложение**:

   ```bash
   python app.py
   ```

5. **Откройте браузер и перейдите по адресу**:

   ```
   http://127.0.0.1:5000/
   ```

## 📂 Структура проекта

- `app.py`: основной файл приложения Flask.
- `templates/`: каталог с HTML-шаблонами.
  - `upload.html`: страница загрузки файлов.
  - `play.html`: страница воспроизведения трека.
  - `library.html`: страница библиотеки треков.
  - `404.html`: страница ошибки 404.
- `uploads/`: каталог для сохранения загруженных аудиофайлов и метаданных.

## 📝 Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле `LICENSE`.

---

*Примечание: **eTag** — это улучшенная версия оригинального [SoundTag](https://soundtag.ru/), предоставляющая дополнительные функции и улучшенный пользовательский интерфейс.*

