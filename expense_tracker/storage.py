# Handles reading from and writing to persistent JSON storage.

import os
import json
from datetime import datetime
from .config import EXPENSE_FILE

def load_expenses():
  if not os.path.exists(EXPENSE_FILE):
    # First-time setup: create empty file
    with open(EXPENSE_FILE, "w") as f:
      json.dump([], f)
    return []

  try:
    if os.path.getsize(EXPENSE_FILE) == 0:
      # Empty file (likely first run); treat as clean slate
      with open(EXPENSE_FILE, "w") as f:
        json.dump([], f)
      return []

    # Attempt to load the existing data
    with open(EXPENSE_FILE, "r") as f:
      data = json.load(f)
      warn_if_corrupt_backup_exists()  # Show warning if other corrupt backups exist
      return data

  except json.JSONDecodeError:
    # File exists and is non-empty but invalid — actual corruption
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    corrupt_backup = f"{EXPENSE_FILE}.{timestamp}.corrupt"
    os.rename(EXPENSE_FILE, corrupt_backup)
    raise RuntimeError(f"Corrupted data detected. Original file backed up as '{corrupt_backup}'. Aborting.")

def save_expenses(expenses):
  with open(EXPENSE_FILE, "w") as f:
    json.dump(expenses, f, indent=2)

def warn_if_corrupt_backup_exists():
  for f in os.listdir("."):
    if f.startswith(EXPENSE_FILE) and f.endswith(".corrupt"):
      raise RuntimeError(f"Found corrupted backup file: '{f}'. Inspection needed.")
