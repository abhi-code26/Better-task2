📋 Project Overview

This is the frontend for my Better Assignment project.
It is built using React.js and connected with the Flask backend APIs from Task 1.
The app allows users to add, view, edit, and delete comments for a given task.

⚙️ Tech Stack

React.js

Axios (for API calls)

HTML, CSS, JavaScript

Flask backend (running on port 5000)

🚀 How to Run

1.Clone the repository
git clone https://github.com/abhi-code26/Better-task2.git
cd Better-task2/frontend

2.Install dependencies
npm install

3.Start the development server
npm start
The app will run on → http://localhost:3000

4.Make sure Flask backend is running (from Task 1)
python app.py
The backend should run on → http://localhost:5000

🔗 API Connection

React communicates with Flask through these endpoints:
| Method | Endpoint                        | Description                 |
| ------ | ------------------------------- | --------------------------- |
| GET    | `/api/tasks/<task_id>/comments` | Get all comments for a task |
| POST   | `/api/tasks/<task_id>/comments` | Add a new comment           |
| PUT    | `/api/comments/<comment_id>`    | Update a comment            |
| DELETE | `/api/comments/<comment_id>`    | Delete a comment            |

🧩 Folder Structure
frontend/
 ┣ src/
 ┃ ┣ components/
 ┃ ┃ ┗ Comments.js   ← Main component for comment CRUD
 ┃ ┣ App.js
 ┃ ┗ index.js
 ┣ package.json
 ┗ README.md

🎥 Demo Video
https://www.loom.com/share/854fdb8f61aa44399d49753f5a581e32
