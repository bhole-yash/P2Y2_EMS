# Employee Management System

This project is an Employee Management System built using React.js for the frontend, Django for the backend, and SQLite as the database. It is deployed using Docker with three separate services.

## Project Structure
```
employee-management-system/
│── backend/         # Django project
│── frontend/        # React project
│── docker-compose.yml
│── backend/Dockerfile
│── frontend/Dockerfile
│── .env
```

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup & Execution

### 1. Clone the Repository
```sh
git clone <repo-url>
cd employee-management-system
```

### 2. Build and Start Containers
```sh
docker-compose up --build
```
This will:
- Start the React frontend on port **3000**
- Start the Django backend on port **8000**
- Use SQLite as the database

### 3. Access the Application
- **Frontend:** `http://localhost:3000`
- **Backend API:** `http://localhost:8000`

## Project Configuration

### Frontend (React)
Located in the `frontend/` directory.

#### `frontend/Dockerfile`
```dockerfile
FROM node:18
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "build", "-l", "3000"]
EXPOSE 3000
```

### Backend (Django)
Located in the `backend/` directory.

#### `backend/Dockerfile`
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
```

### Database (SQLite)
SQLite is used as the database, and data is stored in a persistent volume.

### `docker-compose.yml`
```yaml
version: "3.8"
services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=sqlite:///db.sqlite3

  db:
    image: nouchka/sqlite3
    volumes:
      - sqlite_data:/var/lib/sqlite

volumes:
  sqlite_data:
```

## Stopping the Application
To stop the running containers, use:
```sh
docker-compose down
```

## Notes
- Ensure **CORS** is enabled in Django to allow frontend requests.
- You can define **environment variables** in `.env` for configurations.
- Consider using **Gunicorn** for Django in production.

## License
This project is licensed under the MIT License.

