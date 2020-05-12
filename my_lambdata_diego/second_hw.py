
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
    names_map = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona",
                 "AR": "Arkansas", "CA": "California", "CO": "Colorado",
                 "CT": "Connecticut", "DE": "Delaware", "FL": "Florida",
                 "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
                 "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
                 "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
                 "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
                 "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
                 "MO": "Missouri", "MT": "Montana", "NE": "Nebraska",
                 "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
                 "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
                 "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
                 "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island",
                 "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
                 "TX": "Texas", "UT": "Utah", "VT": "Vermont",
                 "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
                 "WI": "Wisconsin", "WY": "Wyoming", "DC": "Washington D.C."}

    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df
<<<<<<< HEAD
=======

>>>>>>> c8c064ae4d07db9eabce867e55b017a6b013c473

# def add_state_abbrev(my_df):
#     new_df = my_df.copy
#     names_map = {"AL": "Alabama", "AK": "Alaska", "AZ": "Arizona",
#                  "AR": "Arkansas", "CA": "California", "CO": "Colorado",
#                  "CT": "Connecticut", "DE": "Delaware", "FL": "Florida",
#                  "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
#                  "IL": "Illinois", "IN": "Indiana", "IA": "Iowa",
#                  "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
#                  "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts",
#                  "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
#                  "MO": "Missouri", "MT": "Montana", "NE": "Nebraska",
#                  "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
#                  "NM": "New Mexico", "NY": "New York", "NC": "North Carolina",
#                  "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
#                  "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island",
#                  "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
#                  "TX": "Texas", "UT": "Utah", "VT": "Vermont",
#                  "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
#                  "WI": "Wisconsin", "WY": "Wyoming", "DC": "Washington D.C."}

#     for name in df["name"]:
#         df["abbrev"] = df
#     return new_df

if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT","DC","TX"]})
    print(df)

    df2 = add_state_names(df)
<<<<<<< HEAD
    print(df2)

    # df = DataFrame({"name": ["California", "Colorado",
    #                          "Connecticut", "Washington D.C.",
    #                          "Texas"]})
    # print(df)

    # df2 = add_state_abbrev(df)
    # print(df2)
=======
    print(df2.head())

    df3 = DataFrame({"a": [1, 2, 3, 4]})
    print(df3.head())
>>>>>>> c8c064ae4d07db9eabce867e55b017a6b013c473
