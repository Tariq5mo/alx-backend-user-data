# 0x01. Basic Authentication

This project is part of the ALX Software Engineering program, focusing on implementing Basic Authentication on a simple API. It introduces key concepts in authentication, Base64 encoding, and secure API practices.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

In this project, you will learn what the authentication process means and implement Basic Authentication on a simple API. This project explores how to secure an API using Basic Authentication and understand the underlying mechanisms.

### Objectives

- Understand the authentication process.
- Implement Basic Authentication.
- Learn about Base64 encoding and HTTP headers.

**Key Topics Covered:**

- Authentication and Authorization
- Base64 encoding
- HTTP headers and status codes
- Flask framework

---

## Concepts and Skills

### Key Topics

1. **Authentication**:
   - What authentication means.
   - Understanding Basic Authentication and its implementation.

2. **Base64 Encoding**:
   - How to encode and decode strings in Base64.
   - Using Base64 for HTTP headers.

3. **HTTP Headers**:
   - Understanding the Authorization header.
   - Handling HTTP status codes for authentication.

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
- **Directory**: `0x01-Basic_authentication`
- **Files**:
  - `api/v1/app.py`: Entry point of the API.
  - `api/v1/views/index.py`: Basic endpoints of the API.
  - `api/v1/views/users.py`: User-related endpoints.
  - `api/v1/auth/auth.py`: Base class for authentication.
  - `api/v1/auth/basic_auth.py`: Basic Authentication class.

---

## Project Tasks

### **0. Simple-basic-API**

Setup and start the API server.

### **1. Error handler: Unauthorized**

Add an error handler for 401 status code.

### **2. Error handler: Forbidden**

Add an error handler for 403 status code.

### **3. Auth class**

Create a base class for managing API authentication.

### **4. Define which routes don't need authentication**

Update the method to exclude certain paths from authentication.

### **5. Request validation!**

Validate requests to secure the API.

### **6. Basic auth**

Create a BasicAuth class inheriting from Auth.

### **7. Basic - Base64 part**

Extract the Base64 part of the Authorization header.

### **8. Basic - Base64 decode**

Decode the Base64 string from the Authorization header.

### **9. Basic - User credentials**

Extract user credentials from the decoded Base64 string.

### **10. Basic - User object**

Retrieve the User instance based on email and password.

### **11. Basic - Overload current_user - and BOOM!**

Complete the Basic Authentication implementation.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-backend-user-data.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x01-Basic_authentication
   ```

3. Install the dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the API server:

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).
