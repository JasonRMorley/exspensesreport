import pandas as pd
import os


class Statements:
    def __init__(self):
        self.directory = "data/statements"
        self.all_statements = {}
        self.make_statements()

    def make_statements(self):
        for file_name in os.listdir(self.directory):
            if file_name in os.listdir(self.directory):
                filepath = os.path.join(self.directory, file_name)
                if os.path.isfile(filepath):
                    self.process_file(filepath, file_name)

    def process_file(self, filepath, file_name):
        print(f"processing {filepath}")

        statement = pd.read_csv(filepath)
        statement = Statement(statement)
        name = file_name.split(".")[0]
        self.all_statements[name] = statement


class Statement:
    def __init__(self, statement):
        self.statement = statement
        self.statement = self.statement.drop(columns=["Transaction Type", "Sort Code", "Account Number"])
        self.categorise_statement()
        self.statement_expenses = self.get_expenses()
        self.statement_income = self.get_income()

    def categorise_statement(self):
        bills_list = ["RENT", "MEMBERSHIP FEE", "MOBILE"]
        groceries_list = ["ICELAND", "TESCO STORES 0000", "MORRISON'S"]
        eating_out_list = ["ITALIAN", "SPICE"]
        travel_list = ["ESSO"]
        entertainment_list = ["NETFLIX", "spotify"]
        payments_transfers_list = []
        shopping_list = ["GO OUTDOORS", "AMZNMktplace*TA4E6"]
        category = []

        for item in self.statement.get("Transaction Description"):
            if item in bills_list:
                category.append("Bills")

            elif item in groceries_list:
                category.append("Groceries")

            elif item in eating_out_list:
                category.append("Eating out")

            elif item in travel_list:
                category.append("Travel")

            elif item in entertainment_list:
                category.append("Entertainment")

            elif item in payments_transfers_list:
                category.append("Payments & Transfers")

            elif item in shopping_list:
                category.append("Shopping")

            elif item == "STAGECOACH SERVICE":
                category.append("Work Pay")
            else:
                category.append("Misk")

        self.statement.insert(5, "Category", category)

    def get_expenses(self):
        statement = self.statement.dropna(subset=["Debit Amount"])
        statement = statement.drop(columns=["Credit Amount"])
        return statement

    def get_income(self):
        statement = self.statement.dropna(subset=["Credit Amount"])
        statement = statement.drop(columns=["Debit Amount"])
        return statement

