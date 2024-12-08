# 0x00. Personal Data

This project is part of the ALX Software Engineering program, focusing on the importance of handling personal data securely and responsibly in software systems. It introduces key concepts in data privacy, encryption, and secure storage practices.

## Table of Contents

- [Introduction](#introduction)
- [Concepts and Skills](#concepts-and-skills)
- [Requirements](#requirements)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Author](#author)

---

## Introduction

Personal data is any information related to an identifiable individual, and its protection is critical in modern software systems. This project explores how to collect, store, and handle personal data responsibly while complying with security best practices.

### Objectives

- Understand data privacy laws and regulations.
- Implement encryption techniques for secure storage.
- Develop anonymization strategies to protect user privacy.

**Key Topics Covered:**

- Personally Identifiable Information (PII)
- Hashing and encryption algorithms
- Logging without exposing sensitive data
- Data anonymization

---

## Concepts and Skills

### Key Topics

1. **Data Privacy**:
   - What constitutes personal data.
   - Understanding the General Data Protection Regulation (GDPR) and related laws.

2. **Encryption**:
   - Using hashing and symmetric encryption techniques to protect data.
   - Implementing secure storage solutions.

3. **Logging and Anonymization**:
   - Best practices for logging without exposing sensitive data.
   - Techniques for masking or removing PII from datasets.

4. **Python Programming**:
   - Writing secure and efficient code.
   - Adhering to the **PEP 8 style guide**.

---

## Requirements

### General

- **Allowed editors**: `vi`, `vim`, `emacs`.
- Code will be interpreted/compiled on **Ubuntu 20.04 LTS** using Python 3.7.
- Adhere to the **PEP 8 style guide** (version 2.5).
- No external module imports unless specified.
- All files should:
  - End with a new line.
  - Be executable.
  - Include proper documentation for modules, classes, and functions.

### Repository Structure

- **GitHub repository**: [alx-backend](https://github.com/Tariq5mo/alx-backend)
- **Directory**: `0x00-personal_data`
- **Files**:
  - `filtered_logger.py`: Implements logging with PII filtering.
  - `encrypt_data.py`: Handles encryption and decryption of sensitive information.
  - `main.py`: Example script demonstrating project features.

---

## Project Tasks

### **0. Regex-ing**

Write a function `filter_datum()` that obfuscates specific fields in logs using regular expressions.

#### Requirements

- Replace field values with the string `"[FILTERED]"`.
- Specify fields to filter as input parameters.

---

### **1. Log Formatter**

Implement a class `RedactingFormatter` that inherits from `logging.Formatter`.
It ensures that sensitive fields are filtered out from logs.

#### Features

- Define `PII_FIELDS` to specify which fields to filter.
- Use `filter_datum()` to replace sensitive information.

---

### **2. Encrypting passwords**

Write a function `hash_password()` that hashes a password for secure storage using bcrypt.

#### Features

- Use `bcrypt.gensalt()` for salt generation.
- Verify passwords using `bcrypt.checkpw()`.

---

### **3. Updating credentials**

Implement a function `update_credentials()` to safely hash and update user passwords in a database.

#### Features

- Ensure passwords are not stored in plaintext.
- Provide functionality to verify the hashed password.

---

### **4. Secure Database**

Set up a database for storing user credentials securely.

#### Features

- Use hashed passwords for all entries.
- Ensure PII is anonymized or encrypted as needed.

---

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Tariq5mo/alx-backend.git
   ```

2. Navigate to the project directory:

   ```bash
   cd 0x00-personal_data
   ```

3. Run the example script:

   ```bash
   ./main.py
   ```

---

## Author

This project was completed by **Tariq Omer**, a student of the ALX Software Engineering program specializing in back-end development. Connect with me on [GitHub](https://github.com/Tariq5mo).
