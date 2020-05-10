
from pandas import DataFrame
# State abbreviation -> Full Name and visa versa. FL -> Florida, etc.
# (Handle Washington DC and territories like Puerto Rico etc.)

def add_state_names(my_df):
    """
    Adds a column of state names to accompany a corresponding column of state abbreviations

    Params:
        my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations

    Returns:
        copy of the original dataframe, with another column
    """
    new_df = my_df.copy()
    names_map = {"CA":"Cali", "CO":"Colo", "CT":"Conn"}
    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df




if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT","DC","TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())

    df3 = DataFrame({"a": [1, 2, 3, 4]})
    print(df3.head())
