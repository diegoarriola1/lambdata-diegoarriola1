from pandas import DataFrame

class DataProcessor():
    def __init__(self, something_else):
        """
        Params: something_else (pandas.DataFrame) has a column called "abbrev" with state abbreviations
        """
        self.df = something_else

    def add_state_names(self):
        """
        Adds a column of state names to accompany a corresponding column of state abbreviation.
        """
        names_map = {"CA":"Cali", "CO":"Colo", "CT":"Conn"}
        self.df["name"] = self.df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        return self.df

if __name__ == "__main__":

    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})

    processor = DataProcessor(df)
    print(processor.df.head())

    processor.add_state_names()
    print(processor.df.head())
