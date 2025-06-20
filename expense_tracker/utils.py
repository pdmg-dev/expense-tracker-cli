# Validation helpers to sanitize and check inputs before processing.

from datetime import datetime
from .config import DATE_FORMAT

def is_valid_amount(amount):
  # Accept only finite, positive n+umbers
  if not isinstance(amount, (int, float)):
    return False
  if amount < 0 or amount != amount or amount == float('inf') or amount == float('-inf'):
    return False
  return True

def is_valid_description(description):
  # Must be non-empty and <=100 characters, no whitespace-only strings
  if not isinstance(description, str):
    return False
  description = description.strip()
  return 0 < len(description) <= 100

def is_valid_id(expense_id):
  return isinstance(expense_id, int ) and expense_id > 0

def is_valid_date(date):
  try:
    datetime.strptime(date, DATE_FORMAT)
    return True
  except ValueError:
    return False


