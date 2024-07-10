import pandas as pd
import os


def combine_excel_files(folder_path, output_file):
    #list of all the excel files to be combined
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]

    
    if not excel_files:
        print("No Excel files found in the specified folder.")
        return

    
    combined_data = pd.DataFrame()

    
    for file in excel_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)
        combined_data = pd.concat([combined_data, df], ignore_index=True)  # Use pd.concat instead of append

    #putting combined data to a new Excel file
    combined_data.to_excel(output_file, index=False)
    print(f"Combined data written to {output_file}")


folder_path = "D:/User"
output_file = "D:/User/Sheets_Combined.xlsx"
combine_excel_files(folder_path, output_file)
