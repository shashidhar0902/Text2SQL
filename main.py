import sys
from data_loader import load_excel, load_postgresql_table
from agents import CrewAIAgent

def main():
    print("Welcome to the CrewAI Application")
    print("Choose data source:")
    print("1. Excel file")
    print("2. PostgreSQL table")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == '1':
        file_path = input("Enter path to Excel file: ").strip().strip('\'"')
        data = load_excel(file_path)
        if data is None:
            print("Failed to load Excel file.")
            sys.exit(1)
        data_schema = str(data.columns.tolist())
        print(data_schema)
    elif choice == '2':
        table_name = input("Enter PostgreSQL table name: ").strip()
        data = load_postgresql_table(table_name)
        if data is None:
            print("Failed to load PostgreSQL table.")
            sys.exit(1)
        data_schema = str(data.columns.tolist())
    else:
        print("Invalid choice.")
        sys.exit(1)

    agent = CrewAIAgent(data_schema)

    while True:
        prompt = input("\nEnter your query in natural language (or type 'exit' to quit): ").strip()
        if prompt.lower() == 'exit':
            print("Exiting CrewAI Application.")
            break

        query = agent.generate_query(prompt)
        print(f"\nGenerated Query:\n{query}")

        result = agent.execute_query(query, data)
        if result is not None:
            print("\nQuery Result:")
            print(result)
        else:
            print("Failed to execute query.")

if __name__ == "__main__":
    main()
