```markdown
# 💰 Smart Expense Tracker

A clean, production-minded command-line expense tracker built with Python and backed by **Supabase Postgres**. 

This is the foundation project in my Backend Software Engineering roadmap — designed to evolve from a simple CLI into a full Django REST API with authentication, caching, Docker, CI/CD, and AI-powered features.

## ✨ Current Features

- Add transactions (amount, category, description, auto date)
- View recent transactions with clean formatting
- Filter transactions by category
- Calculate total amount spent
- Persistent storage using Supabase (PostgreSQL) — no local database files

## 🛠 Tech Stack

| Layer          | Technology                  |
|----------------|-----------------------------|
| Language       | Python 3.12+                |
| Database       | Supabase (PostgreSQL)       |
| DB Client      | supabase-py                 |
| Environment    | python-dotenv               |
| Version Control| Git + GitHub                |
| Dev Environment| GitHub Codespaces           |

## 🚀 Getting Started

### Prerequisites
- Python 3.12 or higher
- Git
- A free Supabase account (for the database)

### Run in GitHub Codespaces (Recommended)

1. Open this repository in GitHub Codespaces
2. Create your `.env` file with your Supabase credentials:
   ```bash
   cat > .env << EOF
   SUPABASE_URL=https://your-project-ref.supabase.co
   SUPABASE_KEY=your-service-role-key-here
   EOF
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

### Run Locally

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/smart-expense-tracker.git
cd smart-expense-tracker

# (Optional but recommended) Create virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

pip install -r requirements.txt

# Add your Supabase credentials to .env file
python main.py
```

> **Note**: Never commit your `.env` file. It is already listed in `.gitignore`.

## 📸 Demo

**Screenshot coming soon.**

Once you take a clean screenshot of the CLI running, add it here:
```markdown
![CLI Demo](assets/screenshot.png)
```

## 🗺️ Project Roadmap

This project follows my structured backend engineering roadmap:

- [x] **Phase 1** — Python foundations + Supabase integration (current)
- [ ] Add delete, edit, and advanced filtering features
- [ ] Improve project structure + add tests (`pytest`)
- [ ] **Phase 2** — Convert to Django REST Framework + JWT auth
- [ ] Deploy API on Render (free tier)
- [ ] Add Redis caching and rate limiting
- [ ] **Phase 3 & 4** — System design improvements + ML features (expense forecasting & anomaly detection)

## 📁 Project Structure (Current)

```
smart-expense-tracker/
├── main.py                 # CLI application + ExpenseTracker class
├── requirements.txt
├── .env                    # (gitignored)
├── .gitignore
└── README.md
```

## 🤝 Contributing

This is a personal portfolio/learning project. Feel free to fork and experiment.

## 📄 License

This project is open for learning and portfolio use.