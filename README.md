# Scrapper Books Application

This repository contains a web application for scraping book data and managing it through a FastAPI backend and a React frontend. The setup is fully containerized using Docker.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository from GitHub:
    ```bash
    git clone https://github.com/wanderson-devops/books-scraper.git
    cd scrapper-books
    ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

3. Open your browser and navigate to:
    [http://localhost:3000/](http://localhost:3000/)

### Stopping and Removing Containers

To shut down the application and remove the containers, use the following command:
```bash
docker-compose down
```

## Technologies Used
## Backend

- Python
- FastAPI
- SQLAlchemy
- psycopg2-binary
- Uvicorn
- Requests
- BeautifulSoup4
- Axios
- CORS
- Frontend
- React


## Repository

- The code is available on GitHub: wanderson-devops/books-scraper

