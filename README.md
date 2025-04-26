# Todo List API in Python Flask

> A simple and efficient RESTful API for managing todos, built with Flask. This project is part of the 4Geeks Academy Self-Paced Full-Stack Developer Bootcamp, demonstrating the fundamentals of building REST APIs with Python and Flask.

[![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Keywords:** Flask, REST API, Todo List, Python, Backend Development, API Development, 4Geeks Academy

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Testing the API](#testing-the-api)
- [Development](#development)
- [License](#license)
- [Contact](#contact)

## Features

- Create, read, and delete todo items
- Simple and intuitive API endpoints
- In-memory storage for quick operations
- JSON response format
- Error handling for invalid requests
- Clean and maintainable codebase

## Tech Stack

- **Backend:**
  - Flask 3.0.2
  - Werkzeug 3.0.1
  - Python 3.9+

- **Development Tools:**
  - pip for package management
  - Git for version control
  - VS Code (recommended IDE)

## Project Structure
```
/
├── app.py           # Main application file with API endpoints
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```

## Setup & Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/dantefasano/python-todo-list-API.git
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python app.py
   ```

4. The API will be available at http://127.0.0.1:5000

## Usage

The API provides three main endpoints:

1. Get all todos:
   ```sh
   GET /todos
   ```
   Response:
   ```json
   [
       {
           "done": true,
           "label": "Sample Todo 1"
       }
   ]
   ```

2. Add a new todo:
   ```sh
   POST /todos
   Content-Type: application/json

   {
       "label": "Buy groceries",
       "done": false
   }
   ```

3. Delete a todo:
   ```sh
   DELETE /todos/<position>
   ```

## API Documentation

### Endpoints

1. `GET /todos`
   - Returns a list of all todos
   - Response format: Array of todo objects

2. `POST /todos`
   - Creates a new todo
   - Request body must include:
     - `label` (string): The todo description
     - `done` (boolean): Completion status
   - Returns the updated list of todos

3. `DELETE /todos/<position>`
   - Deletes the todo at the specified position
   - Position is zero-based
   - Returns the updated list of todos

### Response Format

All successful responses return a JSON array of todo objects:
```json
[
    {
        "done": true,
        "label": "Sample Todo 1"
    },
    {
        "done": false,
        "label": "Sample Todo 2"
    }
]
```

## Testing the API

You can test the API using several methods:

### 1. Browser Console
Open your browser's developer tools (F12) and use these commands:

```javascript
// Get all todos
fetch('http://127.0.0.1:5000/todos')
  .then(response => response.json())
  .then(data => console.log(data));

// Add a new todo
fetch('http://127.0.0.1:5000/todos', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    label: "Buy groceries",
    done: false
  })
}).then(response => response.json())
  .then(data => console.log(data));

// Delete a todo
fetch('http://127.0.0.1:5000/todos/0', {
  method: 'DELETE'
}).then(response => response.json())
  .then(data => console.log(data));
```

### 2. Using Postman or Insomnia
- Import the following collection:
  - GET http://127.0.0.1:5000/todos
  - POST http://127.0.0.1:5000/todos
  - DELETE http://127.0.0.1:5000/todos/0

### 3. Using curl
```bash
# Get all todos
curl http://127.0.0.1:5000/todos

# Add a new todo
curl -X POST -H "Content-Type: application/json" -d '{"label":"Buy groceries","done":false}' http://127.0.0.1:5000/todos

# Delete a todo
curl -X DELETE http://127.0.0.1:5000/todos/0
```

## Development

This project is part of the 4Geeks Academy Self Paced program, designed to teach:
- REST API development with Flask
- HTTP methods and endpoints
- JSON request/response handling
- Basic error handling
- API testing

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Dante Fasano** - [GitHub](https://github.com/dantefasano)

Project Link: [https://github.com/dantefasano/python-todo-list-API](https://github.com/dantefasano/python-todo-list-API)

---

Made with ❤️ by Dante Fasano 