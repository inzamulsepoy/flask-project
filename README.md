# Flask User Registration Project

A simple **Flask** web application for **user registration** with **MySQL database integration**, designed to run using **Uvicorn** (ASGI server).

---

## Features

- User registration form with fields like **name** and **email**.
- Backend powered by **Flask** with **ASGI support**.
- Data storage in **MySQL**.
- Template rendering using **Jinja2** (`index.html` in the `templates` folder).
- Organized project structure with **models, schemas, and database connection**.

---

## Project Structure

```

FLASK-PROJECT/
│
├── app/
│   ├── **pycache**/           # Compiled Python files
│   ├── database.py            # MySQL database connection
│   ├── main.py                # Flask app and routes
│   ├── models.py              # Database models
│   └── schemas.py             # Data validation schemas
│
├── templates/
│   └── index.html             # Registration form template
│
├── .env                       # Environment variables (DB credentials)
├── requirements.txt           # Python dependencies
├── README.md                  # Project description
└── venv/                      # Python virtual environment

````

---

## Installation

1. **Clone the repository**
   ````
   git clone https://github.com/yourusername/flask-user-registration.git
   cd flask-user-registration
````

2. **Create a virtual environment**

   ```b
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root folder:

   ```
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=yourpassword
   DB_NAME=yourdatabase
   ```

---

## Running the Project

Since this project uses **Uvicorn**:

```
uvicorn app.main:app --reload
```

* The app will be available at `http://127.0.0.1:8000`.
* `--reload` automatically restarts the server on code changes.

> ⚠️ Make sure no other process is using port 8000. If needed, change the port with `--port 5000`.

---

## Usage

* Open your browser and navigate to `http://127.0.0.1:8000`.
* Fill out the registration form.
* Submit the form to store data in the MySQL database.

---

## Dependencies

* Flask
* SQLAlchemy
* MySQL Connector (or pymysql)
* python-dotenv
* Uvicorn (ASGI server)

## License

This project is licensed under the MIT License.
