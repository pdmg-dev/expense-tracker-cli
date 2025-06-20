# Handles all console output for displaying expense data and summaries

import calendar

def print_expenses(expenses):
  if not expenses:
    print("No expenses found.")
    return
  
  # Define headers and calculate column widths dynamically
  headers = {
    "ID": "ID",
    "Date": "Date",
    "Description": "Description",
    "Amount": "Amount"
    }

  col_widths = {
    "ID": max(len(headers["ID"]), max(len(str(e["id"])) for e in expenses)),
    "Date": max(len(headers["Date"]), max(len(e["date"]) for e in expenses)),
    "Description": max(len(headers["Description"]), max(len(e["description"]) for e in expenses)),
    "Amount": max(len(headers["Amount"]), max(len(f"₱{e['amount']:,.2f}") for e in expenses)),
  }

  # Add padding and separator lines for readability
  for key in col_widths:
    col_widths[key] += 2
  lines = "-" * sum(col_widths.values())

  # Print header row
  header_row = (
    f"{headers['ID']:<{col_widths['ID']}}"
    f"{headers['Date']:<{col_widths['Date']}}"
    f"{headers['Description']:<{col_widths['Description']}}"
    f"{headers['Amount'].center(col_widths['Amount'])}"
    )
  print(lines)
  print(header_row)
  print(lines)
  
  # Print each row of expense data
  for e in expenses:
    row = (
      f"{str(e['id']):<{col_widths['ID']}}"
      f"{e['date']:<{col_widths['Date']}}"
      f"{e['description']:<{col_widths['Description']}}"
      f"{(f'₱{e['amount']:,.2f}').rjust(col_widths['Amount'])}"
      )
    print(row)
  print(lines)

def print_summary(total, month=None):
  if month:
    try:
      month_name = calendar.month_name[month]
      print(f"Total expenses for {month_name}: ₱{total}")
    except IndexError:
      print(f"Invalid month: {month}")
  else:
    print(f"Total expenses: ₱{total}")