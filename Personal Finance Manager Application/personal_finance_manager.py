from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext
from sqlalchemy.orm import Session

# Define the Requirements:

# Expense tracking
# Budgeting
# Financial reporting
# User authentication (optional)

DATABASE_URL = "sqlite:///finance_manager.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)

class Income(Base):
    __tablename__ = "income"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    source = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)

class Budget(Base):
    __tablename__ = "budgets"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    limit = Column(Float, nullable=False)

Base.metadata.create_all(bind=engine)
# user authentication
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def create_user(db: Session, username: str, password: str):
    hashed_password = get_password_hash(password)
    db_user = User(username=username, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_expense(db: Session, user_id: int, date: str, category: str, amount: float, description: str = None):
    db_expense = Expense(user_id=user_id, date=date, category=category, amount=amount, description=description)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def create_income(db: Session, user_id: int, date: str, category: str, amount: float, description: str = None):
    db_income = income(user_id=user_id, date=date, category=category, amount=amount, description=description)
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

def create_budgets(db: Session, user_id: int, date: str, category: str, amount: float, description: str = None):
    db_budgets = budgets(user_id=user_id, date=date, category=category, amount=amount, description=description)
    db.add(db_budgets)
    db.commit()
    db.refresh(db_budgets)
    return db_budgets

# Similar functions for income and budgets

from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_user, get_user_by_username, create_expense, get_expenses, create_income, get_income, create_budget, get_budgets, verify_password
from datetime import datetime

def main():
    session = SessionLocal()
    while True:
        print("\n--- Personal Finance Manager ---")
        print("1. Register")
        print("2. Login")
        choice = input("Choose an option: ")
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            create_user(session, username, password)
            print("User registered successfully!")
        elif choice == "2":
            username = input("Username: ")
            password = input("Password: ")
            user = get_user_by_username(session, username)
            if user and verify_password(password, user.password):
                print("Login successful!")
                user_menu(session, user.id)
            else:
                print("Invalid credentials")

def user_menu(session: Session, user_id: int):
    while True:
        print("\n--- User Menu ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Add Income")
        print("4. View Income")
        print("5. Add Budget")
        print("6. View Budgets")
        print("0. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(session, user_id)
        elif choice == "2":
            view_expenses(session, user_id)
        elif choice == "3":
            add_income(session, user_id)
        elif choice == "4":
            view_income(session, user_id)
        elif choice == "5":
            add_budget(session, user_id)
        elif choice == "6":
            view_budgets(session, user_id)
        elif choice == "0":
            break

def add_expense(session: Session, user_id: int):
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    create_expense(session, user_id, date, category, amount, description)
    print("Expense added successfully!")

def view_expenses(session: Session, user_id: int):
    expenses = get_expenses(session, user_id)
    for expense in expenses:
        print(f"Date: {expense.date}, Category: {expense.category}, Amount: {expense.amount}, Description: {expense.description}")

def add_income(session: Session, user_id: int):
    date = input("Date (YYYY-MM-DD): ")
    source = input("Source: ")
    amount = float(input("Amount: "))
    description = input("Description: ")
    create_income(session, user_id, date, source, amount, description)
    print("Income added successfully!")

def view_income(session: Session, user_id: int):
    income_records = get_income(session, user_id)
    for income in income_records:
        print(f"Date: {income.date}, Source: {income.source}, Amount: {income.amount}, Description: {income.description}")

def add_budget(session: Session, user_id: int):
    category = input("Category: ")
    limit = float(input("Limit: "))
    create_budget(session, user_id, category, limit)
    print("Budget added successfully!")

def view_budgets(session: Session, user_id: int):
    budgets = get_budgets(session, user_id)
    for budget in budgets:
        print(f"Category: {budget.category}, Limit: {budget.limit}")

if __name__ == "__main__":
    main()
