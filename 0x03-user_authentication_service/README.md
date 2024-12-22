# 0x03. User Authentication Service

This project is part of the ALX Software Engineering program, focusing on implementing user authentication on a simple API. It introduces key concepts in user management, password hashing, and secure API practices.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

In this project, you will learn what user authentication means and implement it on a simple API. This project explores how to secure an API using user authentication and understand the underlying mechanisms.

### Objectives

- Understand the user authentication process.
- Implement user authentication.
- Learn about password hashing and session management.

**Key Topics Covered:**

- Authentication and Authorization
- Password hashing
- Session management
- Flask framework

---

## Concepts and Skills

### Key Topics

1. **Authentication**:
   - What authentication means.
   - Understanding user authentication and its implementation.

2. **Password Hashing**:
   - How to hash passwords securely.
   - Using bcrypt for password hashing.

3. **Session Management**:
   - How to create and manage sessions.
   - Using sessions for user authentication.

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

- **GitHub repository**: [alx-backend-user-data](https://github.com/yourusername/alx-backend-user-data)
- **Directory**: `0x03-user_authentication_service`
- **Files**:
  - `user.py`: User model definition.
  - `db.py`: Database interaction class.
  - `auth.py`: Authentication class.
  - `app.py`: Flask application.

---

## Project Tasks

### **0. User model**

Create a SQLAlchemy model named `User` for a database table named `users` with the following attributes:

- `id`: integer primary key
- `email`: non-nullable string
- `hashed_password`: non-nullable string
- `session_id`: nullable string
- `reset_token`: nullable string

### **1. Create user**

Implement the `DB.add_user` method to add a user to the database.

### **2. Find user**

Implement the `DB.find_user_by` method to find a user by arbitrary keyword arguments.

### **3. Update user**

Implement the `DB.update_user` method to update a user's attributes.

### **4. Hash password**

Define a `_hash_password` method to hash passwords using bcrypt.

### **5. Register user**

Implement the `Auth.register_user` method to register a new user.

### **6. Basic Flask app**

Set up a basic Flask app with a single GET route ("/") that returns a JSON payload.

### **7. Register user endpoint**

Implement the `/users` POST route to register a user.

### **8. Credentials validation**

Implement the `Auth.valid_login` method to validate user credentials.

### **9. Generate UUIDs**

Implement a `_generate_uuid` function to generate UUIDs.

### **10. Get session ID**

Implement the `Auth.create_session` method to create a session for a user.

### **11. Log in**

Implement the `/sessions` POST route to log in a user.

### **12. Find user by session ID**

Implement the `Auth.get_user_from_session_id` method to find a user by session ID.

### **13. Destroy session**

Implement the `Auth.destroy_session` method to destroy a user's session.

### **14. Log out**

Implement the `/sessions` DELETE route to log out a user.

### **15. User profile**

Implement the `/profile` GET route to get a user's profile.

### **16. Generate reset password token**

Implement the `Auth.get_reset_password_token` method to generate a password reset token.

### **17. Get reset password token**

Implement the `/reset_password` POST route to get a password reset token.

### **18. Update password**

Implement the `Auth.update_password` method to update a user's password.

### **19. Update password endpoint**

Implement the `/reset_password` PUT route to update a user's password.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/alx-backend-user-data.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x03-user_authentication_service
   ```

3. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the API server:

   ```bash
   python app.py
   ```

---

## Author

This project was completed by **Your Name**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/yourusername).
