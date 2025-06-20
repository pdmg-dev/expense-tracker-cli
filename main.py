# CLI entry point for the Expense Tracker CLI app.
# Uses argparse to parse and dispatch commands to respective functions.

import argparse
from expense_tracker.display import print_expenses, print_summary
from expense_tracker.logic import add_expense, delete_expense, list_expenses, update_expense, summary

def main():  
  parser = argparse.ArgumentParser(prog="expense-tracker")
  subparsers = parser.add_subparsers(dest="command")

  # Define 'add' command and its required arguments
  add_parser = subparsers.add_parser("add")
  add_parser.add_argument("--description", required=True)
  add_parser.add_argument("--amount", type=float, required=True)
  add_parser.add_argument("--date", help="Optional date (format: YYYY-MM-DD)")

  # Define 'update' command and its required arguments
  update_parser = subparsers.add_parser("update")
  update_parser.add_argument("--id", type=int, required=True)
  update_parser.add_argument("--description")
  update_parser.add_argument("--amount", type=float)
  update_parser.add_argument("--date", help="New date (format: YYYY-MM-DD)")
  
  # Define 'delete' command by expense ID
  delete_parser = subparsers.add_parser("delete")
  delete_parser.add_argument("--id", type=int, required=True)

  # Define 'list' command
  subparsers.add_parser("list")
  
  # Define 'summary' command to show total, optionally filtered by month
  summary_parser = subparsers.add_parser("summary")
  summary_parser.add_argument("--month", type=int, help="Month number (1-12)")
  
  args = parser.parse_args()

  try:
    # Dispatch based on subcommand
    match args.command:
      case "add":
        expense_id = add_expense(args.description, args.amount, args.date)
        print(f'Expense added successfully (ID: {expense_id})')
      
      case "update":
        success = update_expense(args.id, args.description, args.amount, args.date)
        if success:
          print("Expense updated successfully")
        else:
          print("Expense ID not found")
      
      case "delete":
        success = delete_expense(args.id)
        if success:
          print("Expense deleted successfully")
        else:
          print("Expense ID not found")
      
      case "list":
        expenses = list_expenses()
        print_expenses(expenses)

      case "summary":
        total = summary(month=args.month)
        print_summary(total, month=args.month)

      case _: # Unrecognized or missing command
        parser.print_help()
  except ValueError as ve:
    # Show validation errors from logic module
    print(f"Error: {ve}")
  except RuntimeError as re:
    print(f"Aborted: {re}")

if __name__ == "__main__":
  main()