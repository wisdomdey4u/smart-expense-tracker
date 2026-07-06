import os
from datetime import date
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


def get_supabase_credentials():
    supabase_url = (os.getenv("SUPABASE_URL") or "").strip()
    if supabase_url:
        supabase_url = supabase_url.replace("HTTPS://", "https://", 1).replace("HTTP://", "http://", 1)
    supabase_key = (os.getenv("SUPABASE_KEY") or os.getenv("SUPABASE_KEK") or "").strip()
    return supabase_url, supabase_key


SUPABASE_URL, SUPABASE_KEY = get_supabase_credentials()

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Missing Supabase credentials in .env file")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


class ExpenseTracker:
    """Simple expense tracker backed by Supabase Postgres."""

    def add_transaction(self, amount: float, category: str, description: str = "") -> dict:
        """Add a new transaction."""
        data = {
            "amount": amount,
            "category": category.strip().title(),
            "description": description.strip(),
            "date": str(date.today()),
        }
        response = supabase.table("transactions").insert(data).execute()
        print("✅ Transaction added successfully!")
        return response.data[0] if response.data else {}

    def get_all_transaction(self, limit: int = 20) -> list:
        """Get recent transactions."""
        response = (
            supabase.table("transactions")
            .select("*")
            .order("date", desc=True)
            .limit(limit)
            .execute()
        )
        return response.data or []

    def get_total_spent(self) -> float:
        """Calculate total amount spent."""
        response = supabase.table("transactions").select("amount").execute()
        if not response.data:
            return 0.0
        return sum(float(t["amount"]) for t in response.data)


def display_transaction(txns):
    if not txns:
        print("No transactions found.")
        return
    for txn in txns:
        print(f"{txn.get('date')} | {txn.get('category')} | {txn.get('description')} | {txn.get('amount')}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n" + "=" * 50)
        print("💰 SMART EXPENSE TRACKER (Supabase)")
        print("=" * 50)
        print("1. Add new transaction")
        print("2. View all transactions")
        print("3. View by category")
        print("4. Show total spent")
        print("5. Exit")
        print("=" * 50)

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            try:
                amount = float(input("Amount: "))
                category = input("Category (e.g. Food, Transport, Rent): ")
                description = input("Description (optional): ")
                tracker.add_transaction(amount, category, description)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == "2":
            txns = tracker.get_all_transaction()
            display_transaction(txns)

        elif choice == "3":
            category = input("Enter category to filter: ")
            print("Category filtering is not implemented yet.")

        elif choice == "4":
            total = tracker.get_total_spent()
            print(f"\n💵 Total spent so far: ₦{total:,.2f}")

        elif choice == "5":
            print("Goodbye! Keep building.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()