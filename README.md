# Project

This project includes:

1. A **responsive webpage** with a fixed navbar, collapsible left menu, main content area, right-side panel, and footer.
2. A **Django chat application** with user authentication, real-time messaging using WebSocket, and a database to store users and messages.
3. **AWS Lambda functions** to add two numbers and upload a file to an S3 bucket.

---

## Table of Contents

1. [Frontend Development](#frontend-development)
2. [Django Chat Application](#django-chat-application)
3. [AWS Lambda Functions](#aws-lambda-functions)
4. [How to Run](#how-to-run)
5. [Hosted Links](#hosted-links)

---

## Frontend Development

### Features

- Fixed navbar.
- Collapsible left menu.
- Main content area and right-side panel.
- Footer at the bottom.
- JavaScript function to adjust page size based on screen width.

### Code

- **GitHub Code**: [Frontend Code](https://github.com/kar137/90North-assignment/blob/main/webpage.html)

## Django Chat Application

### Features

- User authentication (signup/login).
- left menu to display registered users.
- Real-time chat using WebSocket.
- Database to store users and messages.
- Retrieve and display old messages.

### Code

- **GitHub Code**: [Django Code](https://github.com/kar137/90North-assignment/tree/main/chat_project)

### Hosted Link

- [PythonAnywhere](https://www.pythonanywhere.com/user/Karan137/webapps/#id_karan137_pythonanywhere_com)

---

## AWS Lambda Functions

### Features

1. **Add Two Numbers**:
   - Takes two numbers as input and returns their sum.
2. **Upload File to S3**:
   - Uploads a document or PDF file to an S3 bucket.

### Code

- **GitHub Code**: [Lambda Code](https://github.com/kar137/90North-assignment/tree/main/lambda_project)

---

## How to Run

### chat app

```bash
1. Navigate to the `chat_project` folder:

   cd chat_project

2. Install requirements.txt file
    pip install -r requirements.txt

3. Run the server
    python manage.py runserver

```
