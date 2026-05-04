# Branching-Out 🔍

A small Python command-line utility that loads user data from a JSON file and filters it by name, age, or email. Built to practice JSON handling, list comprehensions, and clean error management.

## Features

- 🔎 **Filter by name** — case-insensitive exact match
- 🎂 **Filter by age** — integer comparison with input validation
- 📧 **Filter by email** — case-insensitive exact match
- 🛡️ **Error handling** — gracefully handles missing files and invalid JSON
- 📄 **JSON data source** — reads user records from `users.json`

## Project Structure

```
Branching-Out/
├── filter_users.py    # Filter logic & CLI
└── users.json         # User data (name, age, email)
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Branching-Out.git
cd Branching-Out
```

**2. Run the script**
```bash
python filter_users.py
```

**3. Choose a filter option**
```
What would you like to filter by? (name / age / email): name
Enter a name to filter users: Alice
{'name': 'Alice', 'age': 30, 'email': 'alice@example.com'}
```

## Example `users.json` format

```json
[
  {"name": "Alice", "age": 30, "email": "alice@example.com"},
  {"name": "Bob", "age": 25, "email": "bob@example.com"},
  {"name": "Charlie", "age": 30, "email": "charlie@example.com"}
]
```

## What I Learned

- Reading and parsing JSON files with Python's `json` module
- Using list comprehensions for clean, readable data filtering
- Handling `FileNotFoundError` and `json.JSONDecodeError` gracefully
- Building a simple interactive CLI with `input()` and branching logic
