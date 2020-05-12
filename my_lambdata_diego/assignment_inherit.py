from pandas import DataFrame

class MyFrame(DataFrame):

    def add_state_names(self):
        """
        Adds a column of state names to accompany a corresponding column of state abbreviation.
        """
        names_map = {"CA":"Cali", "CO":"Colo", "CT":"Conn"}
        self["name"] = self["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html

if __name__ == "__main__":

    my_frame = MyFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(my_frame.columns)
    print(my_frame.head())

    my_frame.add_state_names()
    print(my_frame.head())
