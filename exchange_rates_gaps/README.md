
# Info / Data

You have the following 2 .csv files

## <strong> riksbanken_exchange_rates.csv </strong>
### HEAD
```

   series_id  group_id  currency_to_sek        date currency             currency_description             source
0     SEKETT       130           1.0000  2024-01-10      SEK  Used for inverted exchange rate  Sveriges Riksbank
1  SEKDKKPMI       130           1.5013  2024-01-10      DKK                     Danish krone  Sveriges Riksbank
2  SEKEURPMI       130          11.1970  2024-01-10      EUR                    Euroland euro  Sveriges Riksbank
3  SEKGBPPMI       130          13.0163  2024-01-10      GBP                   pound sterling  Sveriges Riksbank
4  SEKNOKPMI       130           0.9916  2024-01-10      NOK                  Norwegian krone  Sveriges Riksbank

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


```

<br>

## <strong> orders_data.csv </strong>
### HEAD
```

    site_name site_country currency         paid_datetime  order_id  order_total
0  stickerapp           dk      DKK  2023-08-10T04:48:56Z    100000       207.02
1  stickerapp           us      USD  2023-11-12T15:08:40Z    100001       960.25
2  stickerapp           dk      DKK  2023-07-10T17:48:36Z    100002       337.24
3  stickerapp           de      EUR  2023-01-12T01:19:35Z    100003        42.55
4  stickerapp           se      SEK  2023-07-22T02:36:59Z    100004       490.71

```

### DTYPES
```

site_name         object
site_country      object
currency          object
paid_datetime     object
order_id           int64
order_total      float64

```

# Task
The orders data only contains what currency it was paid in, but not the actual currency value.
Your task is to add the correct currency_to_sek ( from the riksbanken_exchange_rates data ) to the orders_data.

Unfortunately the data in riksbanken_exchange_rates is lacking data on non banking days.
We want to use the last ( previous ) days currency.

## Example :

Given an order that was paid in 'USD' and the paid_date was '2024-01-07'
We would want the currency_to_sek to come from '2024-01-05'

```

5      SEKUSDPMI       130          10.2293  2024-01-10      USD            US dollar  Sveriges Riksbank
11     SEKUSDPMI       130          10.2482  2024-01-09      USD            US dollar  Sveriges Riksbank
17     SEKUSDPMI       130          10.2407  2024-01-08      USD            US dollar  Sveriges Riksbank
23     SEKUSDPMI       130          10.2875  2024-01-05      USD            US dollar  Sveriges Riksbank
29     SEKUSDPMI       130          10.2168  2024-01-04      USD            US dollar  Sveriges Riksbank


```

# Expected result

## Using the example above
### <strong> This is only an example, the actual result should contain all of the orders </strong>

### DTYPES

```
site_name         object
site_country      object
currency          object
currency_to_sek   float64
paid_datetime     object
order_id           int64
order_total      float64

```

### HEAD 

```

site_name  site_country currency currency_to_sek         paid_datetime  order_id  order_total
stickerapp           us      USD         10.2875  2024-01-07T02:36:59Z    100004       490.71

```