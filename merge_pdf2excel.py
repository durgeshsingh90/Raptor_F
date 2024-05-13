import pandas as pd
import xlsxwriter

def write_tables_to_excel(all_tables, excel_path, sheet_name="CombinedTables"):
    keywords = ["function", "approved", "yes"]
    search_strings = ["This Certification covers the following functionality:", "Scheme Region"]

    current_row = 0  # Variable to keep track of the current row

    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        # Create the sheet before writing any tables
        worksheet = writer.book.add_worksheet(sheet_name)

        for i, table_path in enumerate(all_tables, 1):
            # Read Excel file
            table = pd.read_excel(table_path)
            # print (table)

            # Replace NaN values with an empty string
            table = table.fillna('')
            print(table)

            # Check if any keyword is present in the table
            if any(keyword.lower() in cell.lower() for cell in table.values.flatten() for keyword in keywords):
                print(f"Writing Table {i} to sheet: {sheet_name}")

                # Write the table to Excel (header set to True)
                table.to_excel(writer, sheet_name=sheet_name, index=False, header=True, startrow=current_row)

                # Iterate through each row
                for row_index, row_data in enumerate(table.values, current_row + 1):  # Start from the second row to keep the header
                    # Check if any of the search strings is present in the row
                    for search_str in search_strings:
                        cell_indices = [col_index for col_index, cell_value in enumerate(row_data) if search_str in str(cell_value)]
                        if cell_indices:
                            # Merge the cells in the row
                            merge_start = min(cell_indices)
                            merge_end = max(cell_indices)

                            # Use a valid index for search_strings
                            search_string_index = min(merge_start, len(search_strings) - 1)
                            
                            # Check if there's only one cell to merge
                            if merge_start == merge_end:
                                worksheet.write(row_index, merge_start, search_strings[search_string_index])
                            else:
                                worksheet.merge_range(row_index, merge_start, row_index, merge_end, search_strings[search_string_index])

                # Set values after merging
                for row_index, row_data in enumerate(table.values, current_row + 1):
                    for col_index, cell_value in enumerate(row_data):
                        if (col_index, row_index) not in [(merge_start, row_index), (merge_end, row_index)]:
                            worksheet.write(row_index, col_index, cell_value)

                current_row += len(table) + 2  # Increment the current row by the number of rows in the table + 2 for two blank rows

                # Autofit column widths to match the content
                for j, col in enumerate(table.columns):
                    worksheet.set_column(j, j, None, None, {'level': 1, 'hidden': True})  # Hide the original column
                    worksheet.set_column(j, j, None, None, {'level': 2, 'hidden': True})  # Hide the new column
                    worksheet.set_column(j + 1, j + 1, None, None, {'level': 2, 'hidden': True})  # Hide the new column

                # Unhide the new columns to make the autofit take effect
                worksheet.set_column(0, j + 1, None, None, {'hidden': False})

# Example usage:
# all_excel_files = ["path/to/excel/file1.xlsx", "path/to/excel/file2.xlsx"]
# write_tables_to_excel(all_excel_files, "output_excel.xlsx")

all_excel_files = ["Signoffs/merged_data_styled.xlsx"]
write_tables_to_excel(all_excel_files, "Signoffs/output_excel.xlsx")
