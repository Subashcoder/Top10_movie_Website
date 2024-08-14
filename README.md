# Top 10 Movies Web App

This web application allows users to manage a list of the **Top 10 Movies**. Users can add, delete, and update movies, as well as manage reviews and ratings.

## Features

- **Add New Movies**: Add movies to the top 10 list.
- **Delete Movies**: Remove movies from the list.
- **Update Reviews & Ratings**: Modify and update movie ratings and reviews.
- **View Detailed Information**: See movie details including title, release year, and description.

## Technology Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Subashcoder/Top10_movie_Website.git
    cd Top10_movies
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:
    
        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:
    
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Initialize the database:**

    ```bash
    flask db upgrade
    ```

## How to use

### Adding a Movie

- Navigate to the "Add_Movie" page.
- Fill out the movie title and API will return all the movies detail related to title.
- Select the movie you want.
- Page will be redirected to review add the review and rating and movie will be added.

### Deleting a Movie

- Go to the list of movies.
- Click the "Delete" button next to the movie you want to remove.

### Updating Reviews and Ratings

- Select a movie from the movie list.
- Click the Update button and fill the review and rating fields.
- Click "Save" to update the movie information.
