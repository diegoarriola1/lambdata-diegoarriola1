
from pandas import DataFrame

from my_lambdata.assignment import add_state_names

# OBJECTIVE: test the add_state_names() function from the my_lambdata/assignment.py file


def test_add_state_names(self):
    # expect that it has one more column and the same number of rows, after we invoke the function
    # expect that certain column names exist before and certain col names exist after

    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    assert (list(df.columns) == ['abbrev'])

    result = add_state_names(df)

    assert (list(result.columns) == ["abbrev", "name"])
    assert (result.iloc[0]["abbrev"] == "CA")
    assert (result.iloc[0]["name"] == "Cali")
