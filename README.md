# CLI Expense Tracker

A simple command-line expense tracker built in Python, following software development best practices and modular architecture.

Track your expenses, view summaries, and manage spending — all from your terminal.

---

## Features

- Add expenses with descriptions, amounts, and dates
- List all recorded expenses
- Update or delete existing entries by ID
- View monthly summaries
- Modular and clean architecture
- Persistent storage using JSON
- Automatic backup on file corruption

---

## Architecture

This project uses a modular structure:

expense-tracker-cli/
│
├── data/
│ └── expenses.json # Keeps data separate
│
├── expense_tracker/
│ ├── init.py # Treats as a proper package
│ ├── config.py # Centralized config
│ ├── display.py # Separated I/O concerns
│ ├── logic.py # Core business logic
│ ├── storage.py # File read/write logic
│ └── utils.py # Helper functions
│
├── main.py # CLI entry point
├── .gitignore # Ignore unnecessary files
├── requirements.txt # Project requirements
├── LICENSE # Project license
└── README.md # Project documentation

---

## 🖥️ Usage

Run the CLI from the terminal:

```bash
python main.py [command] [options]
```

## Commands

### Add an expense

```bash
python main.py add --description "Groceries" --amount 120 --date 2025-06-20

```

### List all expenses

```bash
python main.py list

```

### Delete an expense

```bash
python main.py delete --id 3

```

### Update an expense

```bash
python main.py update --id 3 --description "Snacks" --amount 55

```

### View summary (current month by default)

```bash
python main.py summary
python main.py summary --month 6

```

---

## Example Output

```bash
# python main.py list
------------------------------------
ID  Date        Description   Amount
------------------------------------
1   2025-06-20  Groceries    ₱120.00
2   2025-06-20  Coffee        ₱50.00
3   2025-06-20  Snacks        ₱55.00
------------------------------------

```

---

## Requirements

- Python 3.8+
- No external libraries required (uses built-in modules only)

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/pdmg-dev/expense-tracker-cli.git
cd cli-expense-tracker

```

2. Run the CLI:

```bash
python main.py [command]

```

3. First run will auto-create the JSON file (`expenses.json`)

---

## File Storage

Expenses are saved in `expenses.json`. If the file is corrupted, a backup will be created as `expenses_backup_TIMESTAMP.json.`

---

## Testing

Coming soon — unit tests will be added in tests/ for core logic and file handling.

---

## License

This project is licensed under the MIT License.

---

## Future Improvements

- Export expenses to CSV
- Categorize expenses
- Set monthly budgets
- Add unit tests with pytest

---

## Project Source

This project was developed following the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) specification from [roadmap.sh](https://roadmap.sh/).
