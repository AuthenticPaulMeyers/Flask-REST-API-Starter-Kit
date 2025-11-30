# Contributing to This Project

Thank you for your interest in contributing! Your help is greatly appreciated.
This document provides guidelines and best practices to ensure a smooth and productive contribution process for everyone.

## Table of Contents

1. Code of Conduct
2. How to Contribute
3. Reporting Issues
4. Requesting Features
5. Development Workflow
6. Coding Standards
7. Commit Message Guidelines
8. Pull Request Process
9. Project Structure Overview
10. Community & Support


## 1. Code of Conduct

By participating in this project, you agree to uphold the principles outlined in the **Code of Conduct**.
Be respectful, collaborative, and inclusive. Harassment or discrimination of any form will not be tolerated.


## 2. How to Contribute

You can contribute in several ways:

* Fix bugs
* Improve documentation
* Add features
* Improve code quality
* Write tests
* Review pull requests

No contribution is too small!

## 3. Reporting Issues

When reporting an issue:

1. Search existing issues to avoid duplicates
2. Provide a clear and descriptive title
3. Include steps to reproduce the issue
4. Add screenshots or logs when relevant
5. Specify your environment (OS, Python version, dependencies)

## 4. Requesting Features

To request a new feature:

1. Explain *why* the feature is needed
2. Provide examples or use cases
3. Suggest possible implementation details


## 5. Development Workflow

### Step 1: Fork the Repository

Click **Fork** on GitHub to create your own copy.

### Step 2: Clone Your Fork

```
https://github.com/AuthenticPaulMeyers/Flask-REST-API-Starter-Kit.git
```

### Step 3: Create a New Branch

```
git checkout -b feature/my-new-feature
```

### Step 4: Make Your Changes

Follow the coding guidelines and write tests where possible.

### Step 5: Commit Your Work

See the commit message guidelines below.

### Step 6: Push Your Branch

```
git push origin feature/my-new-feature
```

### Step 7: Open a Pull Request

Go to the original repository and submit a PR.

## 6. Coding Standards

### Testing

* Write unit tests for new features
* Ensure existing tests pass
* Prefer **pytest**


## 7. Commit Message Guidelines

Use clear, descriptive commit messages.

### Format

```
<type>(scope): short description
```

### Types

* **feat**: new feature
* **fix**: bug fix
* **docs**: documentation
* **refactor**: code restructure
* **test**: testing
* **chore**: maintenance tasks

### Examples

```
feat(auth): add JWT login endpoint
fix(api): correct null response for /me route
docs: update README installation instructions
```

## 8. Pull Request Process

Your PR should:

* Be focused and limited to a single feature or fix
* Pass all tests
* Follow coding standards
* Include documentation updates if needed
* Reference related issues (e.g., “Closes #42”)

Maintainers will review your PR and may request changes.

## 9. Project Structure Overview

```
Flask-API-Starter/
  ─ src/                # Source code
  ─ tests/              # Test files
  ─ CONTRIBUTING.md
  ─ README.md
  ─ pyproject.toml
  ─ LICENSE
```

Understanding the project structure will help you navigate efficiently.

---

I welcome collaborations and am excited to see your contributions!

---

Thank you again for helping improve this project.
Your contributions truly make a difference!
