### Secure Coding Review

## CodeAlpha Cyber Security Internship - Task 3

### Overview

This project was completed as part of the CodeAlpha Cyber Security Internship program. The objective of this task was to perform a secure coding review on a Flask-based authentication application, identify security vulnerabilities, and recommend remediation measures following industry-standard secure coding practices.

---

## Objective

* Review application source code for security weaknesses.
* Identify vulnerabilities that could be exploited by attackers.
* Assess the impact and severity of discovered issues.
* Recommend secure coding practices and remediation strategies.
* Document findings in a professional security review report.

---

## Technologies Used

* Python
* Flask
* Bandit (Static Analysis Tool)

---

## Vulnerabilities Identified

### 1. Debug Mode Enabled

* Exposure of sensitive debugging information.
* Potential information disclosure risk.

### 2. Hardcoded Credentials

* Credentials stored directly in source code.
* Increased risk if source code is leaked.

### 3. Insecure Password Storage

* Passwords stored in plain text.
* Vulnerable to credential theft.

### 4. Missing CSRF Protection

* Susceptible to Cross-Site Request Forgery attacks.

### 5. Insufficient Input Validation

* Increased risk of injection attacks and unexpected behavior.

---

## Recommended Remediation

* Disable debug mode in production environments.
* Remove hardcoded credentials.
* Implement password hashing using bcrypt or Argon2.
* Add CSRF protection using Flask-WTF.
* Validate and sanitize all user inputs.
* Use secure session management.
* Enforce HTTPS communication.
* Configure secure HTTP headers.

---

## Project Structure

Task3_Secure_Coding_Review/

├── app.py

├── Secure_Coding_Review_Report.pdf

├── Screenshots/

│   ├── Application_Output.png

│   ├── Code_Review.png

│   └── Bandit_Output.png

└── README.md

---

## Outcome

The security review successfully identified multiple vulnerabilities within the application and provided practical remediation strategies to improve the overall security posture. This task demonstrates the importance of integrating secure coding principles throughout the software development lifecycle.

---
