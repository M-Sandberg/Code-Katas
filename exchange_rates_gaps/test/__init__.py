
import pandas as pd

def test( df : pd.DataFrame ) -> None :

    columns = ['order_id', 'paid_date', 'order_total', 'site_name', 'site_country', 'currency', 'currency_to_sek']

    # Prepp expected results
    expected = pd.read_csv( './test/result.csv' )
    expected["paid_date"] = pd.to_datetime( expected["paid_date"] )
    expected["paid_date"] = expected["paid_date"].apply( lambda x : x.date() )
    expected = expected.sort_values( by = "order_id", ascending = False )
    expected = expected[ columns ]

    # No result
    if len( expected ) != len( df ):
        print("Test failed.")
        print( f"Expected {len( expected )} rows got {len( df )}" )
        return 

    # Wrong or missing columns
    if len( df.columns ) != len( columns ) or sum([ int( col in columns ) for col in df.columns ]) != len( columns ):
        print("Test failed.")
        print(f"Expected columns : { columns }")
        print(f"Got              : { [*df.columns] if len(df.columns) != 0 else [] }")
        return
    


    df = df.sort_values( by = "order_id", ascending = False )
    df = df[ columns ]

    comparison_result = expected.compare( df )

    if comparison_result.empty:
        print("#"*50)
        print("\n\nTest ok.\n\n")
        print("#"*50)
        return 

    print("#"*50)
    print("\n\nTest failed.")
    print(comparison_result)
    print("#"*50)