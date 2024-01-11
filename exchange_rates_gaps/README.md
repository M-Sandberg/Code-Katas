
# Info / Data

### You have the following 2 .csv files

## <strong> riksbanken_exchange_rates.csv </strong>
### HEAD
```

   series_id  group_id  currency_to_sek        date currency             currency_description             source
0  SEKGBPPMI       130          13.0163  2024-01-10      GBP                   pound sterling  Sveriges Riksbank
1     SEKETT       130           1.0000  2024-01-10      SEK  Used for inverted exchange rate  Sveriges Riksbank
2  SEKEURPMI       130          11.1970  2024-01-10      EUR                    Euroland euro  Sveriges Riksbank
3  SEKDKKPMI       130           1.5013  2024-01-10      DKK                     Danish krone  Sveriges Riksbank
4  SEKUSDPMI       130          10.2293  2024-01-10      USD                        US dollar  Sveriges Riksbank

```

### DTYPES
```

series_id                object
group_id                  int64
currency_to_sek         float64
date                     object
currency                 object
currency_description     object
source                   object
dtype: object

```

<br>

## <strong> orders_data.csv </strong>
### HEAD
```

   order_id   paid_date  order_total   site_name site_country currency
0    100000  2023-08-10       207.02  stickerapp           dk      DKK
1    100001  2023-11-12       960.25  stickerapp           us      USD
2    100002  2023-07-10       337.24  stickerapp           dk      DKK
3    100003  2023-01-12        42.55  stickerapp           de      EUR
4    100004  2023-07-22       490.71  stickerapp           se      SEK

```

### DTYPES
```

order_id          int64
paid_date        object
order_total     float64
site_name        object
site_country     object
currency         object
dtype: object

```

<br>

# Task

#### The orders data only contains the currency in which it was paid, but not the actual currency value.
#### Your task is to add the correct 'currency_to_sek' (from the 'riksbanken_exchange_rates' data) to the 'orders_data.'

#### Unfortunately, the data in 'riksbanken_exchange_rates' lacks information on non-banking days. In the event that there is missing data for a particular date, we want to use the currency from the last (previous) day.

## Example :

#### Given an order that was paid in 'USD' and the paid_date was '2024-01-07'<br>
#### We would want the currency_to_sek to come from '2024-01-05'<br>

```

5      SEKUSDPMI       130          10.2293  2024-01-10      USD            US dollar  Sveriges Riksbank
11     SEKUSDPMI       130          10.2482  2024-01-09      USD            US dollar  Sveriges Riksbank
17     SEKUSDPMI       130          10.2407  2024-01-08      USD            US dollar  Sveriges Riksbank
23     SEKUSDPMI       130          10.2875  2024-01-05      USD            US dollar  Sveriges Riksbank
29     SEKUSDPMI       130          10.2168  2024-01-04      USD            US dollar  Sveriges Riksbank


```

# Expected result

### <strong> This is only an example based on the example above, the actual result should contain all of the orders </strong>

### HEAD 

```

order_id  paid_date  order_total   site_name site_country currency  currency_to_sek
  100000 2024-01-07       207.02  stickerapp           us      USD          10.2875

```