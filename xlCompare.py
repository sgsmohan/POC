import pandas as pd

def compare_excel_files(file1_path, file2_path, output_path):
    # Load both Excel files into DataFrames
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # Find the rows that are in df2 but not in df1
    new_rows = df2[~df2.isin(df1.to_dict("list")).all(1)]

    # If there are new rows, write them to a new Excel file
    if not new_rows.empty:
        with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
            # Write the new data to a new sheet
            new_rows.to_excel(writer, sheet_name='NewData', index=False)
            
            # Copy the first row from the first file to the new sheet
            first_row = df1.iloc[0]
            first_row.to_excel(writer, sheet_name='NewData', startrow=0, index=False, header=False)

if __name__ == "__main__":
    file1_path = input("Enter the path of the first Excel file: ")
    file2_path = input("Enter the path of the second Excel file: ")
    output_path = input("Enter the path for the output Excel file: ")

    compare_excel_files(file1_path, file2_path, output_path)
    print(f"Comparison result saved to '{output_path}'.")
