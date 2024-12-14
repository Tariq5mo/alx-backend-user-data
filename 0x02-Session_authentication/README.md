# 0x02. Session Authentication

This project is part of the ALX Software Engineering program, focusing on implementing Session Authentication on a simple API. It introduces key concepts in session management, cookies, and secure API practices.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

In this project, you will learn what session authentication means and implement it on a simple API. This project explores how to secure an API using session authentication and understand the underlying mechanisms.

### Objectives

- Understand the session authentication process.
- Implement session authentication.
- Learn about cookies and HTTP headers.

**Key Topics Covered:**

- Authentication and Authorization
- Session management
- Cookies
- Flask framework

---

## Concepts and Skills

### Key Topics

1. **Authentication**:
   - What authentication means.
   - Understanding session authentication and its implementation.

2. **Session Management**:
   - How to create and manage sessions.
   - Using sessions for user authentication.

3. **Cookies**:
   - Understanding cookies and their role in session management.
   - Handling cookies in HTTP requests and responses.

4. **Python Programming**:
   - Writing secure and efficient code.
   - Adhering to the **PEP 8 style guide**.

---

## Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`.
- Code will be interpreted/compiled on **Ubuntu 18.04 LTS** using Python 3.7.
- Adhere to the **PEP 8 style guide** (version 2.5).
- No external module imports unless specified.
- All files should:
  - End with a new line.
  - Be executable.
  - Include proper documentation for modules, classes, and functions.

### Repository Structure

- **GitHub repository**: [alx-backend-user-data](https://github.com/Tariq5mo/alx-backend-user-data)
- **Directory**: `0x02-Session_authentication`
- **Files**:
  - `api/v1/app.py`: Entry point of the API.
  - `api/v1/views/index.py`: Basic endpoints of the API.
  - `api/v1/views/users.py`: User-related endpoints.
  - `api/v1/auth/auth.py`: Base class for authentication.
  - `api/v1/auth/session_auth.py`: Session Authentication class.

---

## Project Tasks

### **0. Et moi et moi et moi!**

Copy all work from the previous project and add a new endpoint: GET /users/me to retrieve the authenticated User object.

### **1. Empty session**

Create a class `SessionAuth` that inherits from `Auth`.

### **2. Create a session**

Create a session ID for a user ID and store it in a dictionary.

### **3. User ID for Session ID**

Retrieve a User ID based on a Session ID.

### **4. Session cookie**

Return a cookie value from a request.

### **5. Before request**

Update the `@app.before_request` method to handle session authentication.

### **6. Use Session ID for identifying a User**

Return a User instance based on a cookie value.

### **7. New view for Session Authentication**

Create a new Flask view that handles all routes for the Session authentication.

### **8. Logout**

Add a method to delete the user session/logout.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-backend-user-data.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x02-Session_authentication
   ```

3. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the API server:

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
   ```

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).
