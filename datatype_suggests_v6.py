import pandas as pd
import datetime

class DataTypeSuggester:
    @staticmethod
    def suggest_datatype(column, threshold=90):
        try:
            total_values = len(column)
            # print('Count-----------' + str(total_values))

            # Count occurrences of each data type
            datatype_counts = {
                'int': 0,
                'float': 0,
                'bool': 0,
                'string': 0,
                'datetime': 0
            }

            for value in column:
                if isinstance(value, int):
                    datatype_counts['int'] += 1
                elif isinstance(value, float):
                    datatype_counts['float'] += 1
                elif isinstance(value, bool):
                    datatype_counts['bool'] += 1
                elif isinstance(value, str):
                    datatype_counts['string'] += 1
                elif isinstance(value, datetime.datetime):
                    datatype_counts['datetime'] += 1

            # print(datatype_counts)

            # Calculate the percentage of each data type
            datatype_percentages = {
                datatype: count / total_values * 100
                for datatype, count in datatype_counts.items()
            }

            # print(datatype_percentages)

            # Find the data type(s) with the highest percentage
            max_percentage = max(datatype_percentages.values())
            suggested_datatypes = [
                datatype for datatype, percentage in datatype_percentages.items()
                if percentage >= threshold and percentage == max_percentage
            ]

            return suggested_datatypes[0]

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return None

    @staticmethod
    def suggest_datatypes_for_dataframe(dataframe, threshold=90):
        try:
            dt_dict_ = {}
            for column_name, column_values in dataframe.items():
                suggested_datatypes = DataTypeSuggester.suggest_datatype(column_values, threshold)
                if suggested_datatypes:
                    print(f'{column_name}: {", ".join(suggested_datatypes)}')
                else:
                    suggested_datatypes = 'string'
                    #print(f'No dominant datatype, marking as string type')
                    print(f'{column_name}: {", ".join(suggested_datatypes)}')
                dt_dict_[column_name] = suggested_datatypes
            return dt_dict_
        except Exception as e:
            print(f"Error occurred: {str(e)}")

# Example usage
try:
    data = pd.read_csv('vehicles.csv').sample(n=100)
    res = DataTypeSuggester.suggest_datatypes_for_dataframe(data, threshold=90)
    print(res)

except FileNotFoundError:
    print("File not found. Please provide the correct file path.")

except pd.errors.EmptyDataError:
    print("Empty dataframe. Please provide a valid dataframe with data.")

except Exception as e:
    print(f"Error occurred: {str(e)}")
