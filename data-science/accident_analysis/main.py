import argparse
import pandas as pd
import matplotlib.pyplot as plt

# Global Variables
THANK_YOU_MESSAGE = 'Thank you for using our software. Exiting now...'

CHOICES = {
    '1': 'All accidents data',
    '2': 'Frequency of accidents for each hour of the day',
    '3': 'Accidents caused by an accident type',
    '4': 'Impact of alcohol in accidents',
    '5': 'Impact of speed in accidents',
    '6': 'Exit'
}
FUNCTION_MAP = {
    '1': 'all_accidents_data',
    '2': 'hourly_accident_frequency',
    '3': 'accident_type_statistics',
    '4': 'alcohol_impact',
    '5': 'vehicle_speed_analysis',
}

# TODO: There is another column in dataframe called ALCOHOL_RELATED
OUTPUT_FIELDS = ['ACCIDENT_NO', 'ACCIDENT_DATE', 'ACCIDENT_TIME', 'ALCOHOLTIME',
                 'ACCIDENT_TYPE', 'SEVERITY', 'SPEED_ZONE']


def read_csv_file(filename: str) -> pd.DataFrame:
    """
    Reads the csv file and returns a dataframe

    Args:
        filename: Name of the csv file
    Returns:
        Dataframe of the csv file
    """
    try:
        df = pd.read_csv(filename)
        # Convert ACCIDENT_DATE to datetime
        df['ACCIDENT_DATE'] = pd.to_datetime(
            df['ACCIDENT_DATE'], format='%d/%m/%Y')
        return df
    except FileNotFoundError:
        print(f'File {filename} not found')
        exit(1)


def filter_dataframe(df: pd.DataFrame, start_date: pd.Timestamp, end_date: pd.Timestamp) -> pd.DataFrame:
    """
    Filter the dataframe based on the start and end date specified by the user.

    Args:
        df: Dataframe to be filtered
        start_date: Start date of the filter
        end_date: End date of the filter
    Returns:
        Filtered dataframe
    """
    return df[(df['ACCIDENT_DATE'] >= start_date)
              & (df['ACCIDENT_DATE'] <= end_date)].copy()


def generate_table(df: pd.DataFrame, columns: list):
    """
    Generate a table from the dataframe and print it on stdout

    Args:
        df: Dataframe to be filtered
        columns: Columns to be displayed

    Returns: 
        None
    """
    if len(df.index) == 0:
        print("No records found")
    else:
        print(df[columns].to_string(index=False), '\n')


def input_start_end_date() -> (str, str):
    """
    Prompts the user to enter a start and end date.

    Returns: Tuple of (start_date, end_date)
    """
    start_date = input('Enter start date (DD-MM-YYYY): ')
    end_date = input('Enter end date (DD-MM-YYYY): ')

    # Convert start and end date to datetime
    start_date = pd.to_datetime(start_date, format='%d-%m-%Y')
    end_date = pd.to_datetime(end_date, format='%d-%m-%Y')

    return start_date, end_date


def all_accidents_data(df) -> None:
    """
    Reads the complete dataframe of all accidents in Victoria State and filters
    the data based on the start and end date specified by the user and print
    the result on screen.

    Returns:
        None
    """
    generate_table(df, OUTPUT_FIELDS)


def hourly_accident_frequency(df) -> None:
    """
    Create a pie chart of the frequency of accidents for each hour of the day.

    Args:
        df: Dataframe to be filtered
    Returns:
        None
    """
    # Convert ACCIDENT_TIME to datetime
    df['ACCIDENT_TIME'] = pd.to_datetime(
        df['ACCIDENT_TIME'], format='%H.%M.%S')

    # Add an additional column for hour of the day
    df['ACCIDENT_HOUR'] = df['ACCIDENT_TIME'].dt.hour

    # Add a column for the count of the number of accidents in each hour
    df['ACCIDENT_COUNT'] = df.groupby(
        ['ACCIDENT_DATE', 'ACCIDENT_HOUR'])['ACCIDENT_DATE'].transform('count')

    # Group the dataframe by hour of the day and plot average(mean) number of accidents per hour
    df.groupby(['ACCIDENT_HOUR'])[
        "ACCIDENT_COUNT"].mean().plot(kind='pie', y='ACCIDENT_COUNT', figsize=(10, 10), legend=True)

    plt.show()


def accident_type_statistics(df) -> None:
    """
    Print the count of each accident type in the dataframe.

    Args:
        df: Dataframe to be filtered
    Returns:
        None
    """

    # Get Accident Type from user
    accident_type = input('Enter accident type: ').strip()
    if accident_type == "":
        print("Invalid accident type")
        accident_type_statistics(df)
        return

    filtered_df = df[(df['ACCIDENT_TYPE'].str.contains(accident_type))]

    generate_table(filtered_df, OUTPUT_FIELDS)


def alcohol_impact(df) -> None:
    """
    Print the accidents impacted by alcohol.

    Args:
        df: Dataframe to be filtered
    Returns:
        None
    """
    # Accept start and end date
    filtered_df = df[(df['ALCOHOL_RELATED'] == "Yes")]

    generate_table(filtered_df, OUTPUT_FIELDS)


def vehicle_speed_analysis(df) -> None:
    """
    Create Pie chart of the number of accidents in each speed zone.

    Args:
        df: Dataframe to be filtered
    Returns:
        None
    """
    # Convert ACCIDENT_TIME to datetime
    df['ACCIDENT_TIME'] = pd.to_datetime(
        df['ACCIDENT_TIME'], format='%H.%M.%S')


    # strip number from SPEED_ZONE column (e.g. 60 km/hr to 60)
    df['SPEED_ZONE_NUMBER'] = df['SPEED_ZONE'].str.split(' ', expand=True)[
        0]

    # Group the dataframe by hour of the day and plot average(mean) number of accidents per hour
    df.groupby(['SPEED_ZONE'])[
        "SPEED_ZONE_NUMBER"].count().plot(kind='pie', y='SPEED_ZONE', figsize=(10, 10), legend=True)

    plt.show()


def display_menu(choices: dict, function_map: dict, df: pd.DataFrame) -> None:
    """
    Display the menu of options to the user.

    Args:
        choices: List of choices to be displayed
    Returns:
        User selected option
    """
    print('Victoria State Accident Analysis Software')
    print('\n', '-'*30)
    for key, value in choices.items():
        print(f'{key}. {value}')

    # Accept user choice
    choice = input('\nEnter your choice: ')
    if choice not in choices.keys():
        print(
            f'Invalid choice {choice} entered. Please re-execute the program and select a valid option.')
    elif choices[choice] == 'Exit':
        # Exit Program
        print(THANK_YOU_MESSAGE)
        exit()
    else:
        process_menu_choice(choice, function_map, df)
        display_menu(choices, function_map, df)


def process_menu_choice(choice: str, function_map: dict, df: pd.DataFrame) -> None:
    """
    Process the user choice and call the corresponding function.

    Args:
        choice: User choice
        function_map: Dictionary of function to be called
    Returns:
        None
    """
    # Get start and end date
    start_date, end_date = input_start_end_date()

    # Filter the dataframe based on the start and end date
    filtered_df = filter_dataframe(df, start_date, end_date)

    # Call the appropriate function based on the user's choice
    function_name = FUNCTION_MAP[choice]
    globals()[function_name](filtered_df)
    return


def main():
    # Accept csv file as argument using argparse
    parser = argparse.ArgumentParser(
        description='Victoria State Accident Analysis Software')
    parser.add_argument('--input-file', required=True, help='csv file to read')
    args = parser.parse_args()

    # Read the csv file
    df = read_csv_file(filename=args.input_file)

    # Display the menu and accept user choice
    display_menu(CHOICES, FUNCTION_MAP, df)


if __name__ == '__main__':
    main()
