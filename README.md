# City Recommandation
This project is a technical test to recommend cities in France based on the user's budget, surface, and preferred department. The application was developed using Python, Docker, FastAPI, and SQLAlchemy. The project includes a web scraper to gather data.
The main project follows principles of Hexagonal architecture. It's not necessarily useful for the project but it's just a demo of what it's like.

## Project Structure
`src/`: The main application code

`scraping/`: The web scraper code

`tests/`: The unit tests

Other folders are just conventionally following hexagonal architecture.

`docker-compose.yml`: Docker Compose configuration file

## Installation
- Clone the repository
- Build the Docker containers: `docker-compose build`
- Run the containers: `docker-compose up`

## Usage
First launch the scraping of all data with the command `docker-compose run app pytest scraping/scraping_launch.py`


Navigate to http://localhost:8000/docs in your web browser.

Use the Swagger interface to input your desired budget, surface, and department.
The application will return a list of recommended cities in France based on your inputs.
You will only find cities that have a specific note.

## Testing
Build and start the Docker containers: `docker-compose up --build -d`

Run the tests: `docker-compose run app pytest src/tests`

These are just unit tests. The application is not that complex. It looks like it's overkill 
but it's a good demo of how I write unit tests.

## Future Improvements
- Allow users to search for cities in multiple departments.
- Allow users to input a range of prices, rather than a fixed budget, to give users more flexibility in their search.
- Refactor the web scraper code to be more modular, allowing for easier maintenance and reuse in future projects.
- Do the scraping part in an asynchronous way to go faster for notes scraping and population scraping parts

## Contributors
Martin Siesse - Developer