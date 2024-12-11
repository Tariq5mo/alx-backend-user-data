# 0x01. Basic Authentication

This project is part of the ALX Software Engineering program, focusing on implementing Basic Authentication on a simple API. It introduces key concepts in authentication, Base64 encoding, and secure API practices.

## Table of Contents

- [Introduction](#introduction)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

In this project, you will learn what the authentication process means and implement Basic Authentication on a simple API. This project is for learning purposes and should not be used in production.

### Objectives

- Understand the authentication process.
- Implement Basic Authentication.
- Learn about Base64 encoding and HTTP headers.

---

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic authentication means
- How to send the Authorization header

---

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation
- All your classes should have documentation
- All your functions (inside and outside a class) should have documentation

---

## Project Tasks

### **0. Simple-basic-API**

Set up and start a simple API with one model: User.

### **1. Error handler: Unauthorized**

Add a new error handler for status code 401.

### **2. Error handler: Forbidden**

Add a new error handler for status code 403.

### **3. Auth class**

Create a class to manage the API authentication.

### **4. Define which routes don't need authentication**

Update the method `require_auth` to handle excluded paths.

### **5. Request validation!**

Validate all requests to secure the API.

### **6. Basic auth**

Create a class `BasicAuth` that inherits from `Auth`.

### **7. Basic - Base64 part**

Add a method to extract the Base64 part of the Authorization header.

### **8. Basic - Base64 decode**

Add a method to decode the Base64 string.

### **9. Basic - User credentials**

Add a method to extract user credentials from the Base64 decoded value.

### **10. Basic - User object**

Add a method to return the User instance based on email and password.

### **11. Basic - Overload current_user - and BOOM!**

Add a method to retrieve the User instance for a request.

---

## Usage

1.Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-backend-user-data.git
   ```

2.Navigate to the project directory:

   ```bash
   cd 0x01-Basic_authentication
   ```

3.Run the application:

   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   ```

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).
