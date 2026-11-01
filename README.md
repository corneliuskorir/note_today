# Note Today

A Flask backend journal application that uses JWT for authentication. It was built as part of a challenge to create a journal API with user accounts, where each user can create, view, update and delete their own entries.

---

## Tech Stack

- Flask
- JWT authentication (`Bearer <token>` headers)
- Pipenv for the virtual environment
- SQLite database (included in the repo)
- React frontend (login and signup flow)

---

## Getting Started

### 1. Install dependencies and activate the virtual environment

```bash
pipenv install
pipenv shell
```

### 2. Seed the database (optional)

The database is included in the repo. To populate it with sample data, run the seed file from the **root directory**:

```bash
python -m server.seed
```

### 3. Run the server

The Flask app can only be run from inside the `server` directory.

```bash
cd server
export FLASK_APP=.
flask run
```

### 4. Run the frontend

In a separate terminal, from the frontend directory:

```bash
npm install
npm start
```

The frontend runs on `http://localhost:3000`. Make sure it is pointed at the backend (via a proxy or the backend URL).

---

## Testing the API

- **Login and signup** can be tested directly through the frontend.
- **All other endpoints** (entries) need an API client such as [Postman](https://www.postman.com/). Log in first, then send the returned token in the header:

```
Authorization: Bearer <token>
```

---

## API Endpoints

All endpoints are prefixed with `/api`.

| Method | Endpoint            | Description              | Auth required |
| ------ | ------------------- | ------------------------ | ------------- |
| POST   | `/api/signup`       | Register a new user      | No            |
| POST   | `/api/login`        | Log in and receive a JWT | No            |
| GET    | `/api/me`           | Get the current user     | Yes           |
| GET    | `/api/entries`      | Get all journal entries  | Yes           |
| POST   | `/api/entries`      | Create a journal entry   | Yes           |
| PATCH  | `/api/entries/<id>` | Update a journal entry   | Yes           |
| DELETE | `/api/entries/<id>` | Delete a journal entry   | Yes           |
