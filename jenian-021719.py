#! /usr/bin/env python3
"""
Steps:

  1. Take the data we want and [join
    ](https://blog.codinghorror.com/a-visual-explanation-of-sql-joins/) against
    the data we have.

  2. reorder our data to look like how we want
"""
import pandas as pd
import numpy as np

def add_revised_ticker(df,
    prefix="PX",
    columns=["LAST", "OPEN", "HIGH", "LOW", "VOLUME"]
    ):
    """This constructs and joins the two columns"""

    # construct the new column names
    new_columns = []
    for column in columns:
        new_columns.append(prefix+"_"+column);

    # create a new data frame of dummy data
    data = np.array([
        np.arange(len(df.index))
        ]*len(new_columns)).T
    columns_to_insert = pd.DataFrame(
        data=data,           # our data
        index=df.index,      # specify index -- we want it the same
        columns=new_columns  # specify the new columns we're adding
        );

    # Then we join them into one DataFrame
    df = df.join(columns_to_insert,
        on=None,    # this means it will join on the indexes of both datafames
        how="left"
        );

    # return our new dataframe
    return df;




if __name__ == "__main__":
    xf = pd.read_excel("output.xlsx")
    xf = add_revised_ticker(xf)

    new_ordering_of_columns = ['Unnamed: 0', # unnamed column from xlsx
    'Included',
    'Pricing Date',
    'PX_LAST',      # I put the data here arbitrarily, you can put it wherever
    'PX_OPEN',
    'PX_HIGH',
    'PX_LOW',
    'PX_VOLUME',   # # # # # # # #
    'year',
    'Original Ticker',
    'Revised Ticker',
    'Issuer Name',
    'Offer Size (M)',
    'Offer Price',
    'Bookrunner',
    'Current Market Cap',
    'M&A1',
    'M&A2',
    'AnnounceDate1',
    'AntitrustApproveDate1',
    'ShareholderApproveDate1',
    'CompleteDate1',
    'Terminated1',
    'AnnounceDate_Fail',
    'AntitrustApproveDate_Fail',
    'TerminateDate_Fail',
    'Delisted',
    'Acquired',
    'Acquired US(M)',
    'Acquired Date',
    'TV/Revenue',
    'Comps',
    'Sector',
    'Notes'
    ]

    xf = xf[new_ordering_of_columns]
    print(xf.head(5))  # sample the output

    #xf.to_csv("output.csv")
