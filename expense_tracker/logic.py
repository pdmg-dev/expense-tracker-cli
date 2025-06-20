# Core business logic for managing expenses: CRUD operations and summaries

from datetime import datetime, date
from .config import DATE_FORMAT
from .storage import load_expenses, save_expenses
from .utils import is_valid_amount, is_valid_description, is_valid_id, is_valid_date

def add_expense(description, amount, expense_date):
  # Validate inputs
  if not is_valid_description(description):
    raise ValueError("Invalid description: must be 1-100 non-whitespace characters.")
  if not is_valid_amount(amount):
    raise ValueError("Invalid amount: must be a positive number.")
  
  # Use today's date if not provided
  if expense_date:
    if not is_valid_date(expense_date):
      raise ValueError("Invalid date format: use YYYY-MM-DD.")
  else:
    expense_date = date.today().strftime(DATE_FORMAT)

  # Load current expenses and assign new unique ID
  expenses = load_expenses()
  expense_id = max([e["id"] for e in expenses], default=0) + 1
  
  # Append new expense
  expenses.append({
    "id": expense_id,
    "date": expense_date,
    "description": description.strip(),
    "amount": round(amount, 2)
  })

  save_expenses(expenses)
  return expense_id
  
def delete_expense(expense_id):
  if not is_valid_id(expense_id):
    raise ValueError("Invalid ID: must be a positive integer.")
  
  expenses = load_expenses()
  # Remove expenses with matching ID
  new_expenses = [e for e in expenses if e["id"] != expense_id]
  if len(expenses) == len(new_expenses):
    return False
  save_expenses(new_expenses)
  return True

def list_expenses():
  # Return full list of expenses (unfiltered)
  return load_expenses()

def update_expense(expense_id, new_description=None, new_amount=None, new_date=None):
  if new_description is None and new_amount is None and new_date is None:
    raise ValueError("At least one of --description, --amount, or --date must be provided.")
  if not is_valid_id(expense_id):
    raise ValueError("Invalid ID: must be a positive integer.")
  if new_description is not None:
    if not is_valid_description(new_description):
      raise ValueError("Invalid description: must be 1–100 non-whitespace characters.")
  if new_amount is not None:
    if not is_valid_amount(new_amount):
      raise ValueError("Invalid amount: must be a positive number.")
  if new_date is not None:
    if not is_valid_date(new_date):
      raise ValueError("Invalid date format: use YYYY-MM-DD.")

  expenses = load_expenses()
  updated = False
  for e in expenses:
    if e["id"] == expense_id:
      # Apply any updated if provided
      if new_description:
        e["description"] = new_description.strip()
      if new_amount:
        e["amount"] = round(new_amount, 2)
      if new_date:
        e["date"] = new_date
      updated = True
  if updated:
    save_expenses(expenses)
  return updated
    
def summary(month=None):
  # Calculate total expenses; filter by month if provided
  expenses = load_expenses()
  if month:
    current_year = date.today().year
    expenses = [
      e for e in expenses
      if datetime.strptime(e["date"], DATE_FORMAT).month == month
      and datetime.strptime(e["date"], DATE_FORMAT).year == current_year
    ]
  total = sum(e["amount"] for e in expenses)
  return round(total, 2)