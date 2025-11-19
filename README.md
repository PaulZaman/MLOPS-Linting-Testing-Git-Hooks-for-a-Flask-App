# MLOps – Linting, Testing & Git Hooks for a Flask App

This project implements a simple Flask application and adds basic MLOps practices around linting, testing, and CI/CD.

## 1. Flask Application
A small Flask app was created with the following features:
- View items
- Add an item
- Delete an item
- Update an item

All data is stored in an in-memory list.

## 2. Linting (Ruff)
Ruff is used to check code style and formatting.  
The configuration is defined in `ruff.toml`.

## 3. Testing (Pytest)
Two kinds of tests were added under the `tests/` directory:
- **Unit test** for a pure helper function
- **Integration tests** using Flask’s test client

## 4. Local Git Hook
A `pre-push` hook was added under `.git/hooks/` to automatically run:
- `ruff check .`
- `pytest`

The push is blocked if either step fails.

## 5. GitHub CI
A GitHub Actions workflow (`.github/workflows/ci.yml`) was added.  
It runs Ruff and Pytest automatically for pull requests targeting the `dev` branch.  
The PR fails if linting or tests fail.