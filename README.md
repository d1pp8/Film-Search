# 🎬 Film Search CLI Application

## 📌 Description

This project is a CLI-based application for searching films using a MySQL database with additional analytics stored in MongoDB.

The application allows users to:

* Search films by keyword (title)
* Search films by genre and year range
* View results with pagination (10 films per page)
* Store search queries in MongoDB
* View statistics of the most popular searches

---

## 🚀 Features

### 🔍 1. Search by Keyword

* Search films by title keyword
* Results are displayed in pages of 10 films
* User can navigate through pages interactively

---

### 🎭 2. Search by Genre and Year Range

* Displays all available genres
* Shows minimum and maximum release years
* User can input:

  * A single year
  * A range of years (e.g., 2005–2012)
* Results are paginated (10 films per page)

---

### 🗂️ 3. Search Logging (MongoDB)

* All search queries are stored in MongoDB
* Collection name:
  `your_collection`
* Stored data includes:

  * search type (keyword / genre)
  * query parameters
  * timestamp
  * page number (optional)

---

### 📊 4. Statistics

* Displays top 5 most popular search queries
* Based on:

  * frequency OR
  * recent searches

---

## 🛠️ Technologies Used

* Python 3
* MySQL
* MongoDB
* PyMongo
* python-dotenv

---

## 📁 Project Structure

```
FPJ/
│
├── config/              # Configuration and environment variables
├── controllers/         # Application logic (controllers)
├── databases/           # DB clients (MySQL, MongoDB)
├── services/            # Business logic
├── utilities/           # Helpers (input, tables, pagination)
├── main.py              # Entry point
├── .env.example         # Environment variables template
├── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create `.env` file based on `.env.example`:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=sakila

MONGO_URI=mongodb://localhost:27017/
MONGO_DB=films_db
MONGO_COLLECTION=final_project__yourgroup_yourfullname
```

---

### 5. Run the application

```
python main.py
```

---

## 🧠 Architecture Overview

The project follows a layered architecture:

* **Controllers** → handle user interaction
* **Services** → business logic
* **Databases** → DB communication
* **Utilities** → helpers (pagination, input, UI)

---

## 📌 Notes

* `.env` is excluded from Git for security reasons
* `.env.example` is provided as a template
* Pagination is implemented using SQL `LIMIT/OFFSET`

---

## 👨‍💻 Author
### Dmytro Pernai
101025 ptm

---

## 📄 License

This project is for educational purposes.
