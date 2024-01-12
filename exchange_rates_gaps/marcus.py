
import pandas as pd

# DataFrames to use
orders_df           = pd.read_csv( './data/orders_data.csv' )
exchange_rates_df   = pd.read_csv( './data/riksbanken_exchange_rates.csv' )

# date-fix
orders_df["paid_date"] = pd.to_datetime( orders_df["paid_date"] )
orders_df["paid_date"] = orders_df["paid_date"].apply( lambda x : x.date() )

# date-fix
exchange_rates_df["date"] = pd.to_datetime( exchange_rates_df["date"] )
exchange_rates_df["date"] = exchange_rates_df["date"].apply( lambda x : x.date() )


def fix_non_bankdays( exchange_rates_df : pd.DataFrame ) -> pd.DataFrame :

    dataframes = []
    
    for currency in exchange_rates_df.currency.unique():
        
        # Extract needed data and copy to a temporary dataframe
        temp_df = exchange_rates_df[exchange_rates_df["currency"] == currency][:]
        
        # Find missing days
        missing_dates = pd.DataFrame( columns = ["date"] )
        missing_dates["date"] = pd.date_range( start = temp_df["date"].min(), end = temp_df["date"].max(), freq = "D" ).date
        missing_dates["date"] = missing_dates[ ~missing_dates["date"].isin( set(temp_df["date"]) ) ]
        missing_dates = missing_dates.dropna() # Remove NaT

        # Add missing dates to the temp_df
        temp_df = pd.concat([ temp_df, missing_dates ])

        # Sort to have the dates in order
        temp_df = temp_df.sort_values( by = "date", ascending = False )
        
        # Backwards fill the data
        temp_df = temp_df.bfill()

        dataframes.append( temp_df )

    return pd.concat( dataframes )

def append_exchange_rates_to_orders( orders_df : pd.DataFrame, exchange_rates_df : pd.DataFrame ) -> pd.DataFrame :

    df = orders_df.merge( exchange_rates_df, left_on = ["paid_date", "currency"], right_on = ["date", "currency"], how = "inner" )

    return df[[ "order_id", "paid_date", "order_total", "site_name", "site_country", "currency", "currency_to_sek" ]]


exchange_rates_fixed        = fix_non_bankdays( exchange_rates_df )                                 # "Fixed" currencies
orders_with_exchange_rates  = append_exchange_rates_to_orders( orders_df, exchange_rates_fixed )    # "Fixed" orders


from test import test
test( orders_with_exchange_rates )