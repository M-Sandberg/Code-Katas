
__TESTS = [
    ( 0,            'now'),
    ( 1,            '1 second'),
    ( 62,           '1 minute and 2 seconds'),
    ( 120,          '2 minutes'),
    ( 3600,         '1 hour'),
    ( 3662,         '1 hour, 1 minute and 2 seconds'),
    ( 15731080,     '182 days, 1 hour, 44 minutes and 40 seconds'),
    ( 132030240,    '4 years, 68 days, 3 hours and 4 minutes'),
    ( 205851834,    '6 years, 192 days, 13 hours, 3 minutes and 54 seconds'),
    ( 253374061,    '8 years, 12 days, 13 hours, 41 minutes and 1 second'),
    ( 242062374,    '7 years, 246 days, 15 hours, 32 minutes and 54 seconds'),
    ( 101956166,    '3 years, 85 days, 1 hour, 9 minutes and 26 seconds'),
    ( 33243586,     '1 year, 19 days, 18 hours, 19 minutes and 46 seconds'),
    ( 9601557,      '111 days, 3 hours, 5 minutes and 57 seconds'),
    ( 7089143,      '82 days, 1 hour, 12 minutes and 23 seconds'),
    ( 723301,       '8 days, 8 hours, 55 minutes and 1 second'),
    ( 436986,       '5 days, 1 hour, 23 minutes and 6 seconds'),
    ( 1914860,      '22 days, 3 hours, 54 minutes and 20 seconds'),
    ( 1565096,      '18 days, 2 hours, 44 minutes and 56 seconds'),
    ( 6537770,      '75 days, 16 hours, 2 minutes and 50 seconds'),
    ( 6336524,      '73 days, 8 hours, 8 minutes and 44 seconds'),
    ( 9148783,      '105 days, 21 hours, 19 minutes and 43 seconds'),
    ( 4986672,      '57 days, 17 hours, 11 minutes and 12 seconds'),
    ( 8038958,      '93 days, 1 hour, 2 minutes and 38 seconds'),
    ( 5805048,      '67 days, 4 hours, 30 minutes and 48 seconds'),
    ( 5928821,      '68 days, 14 hours, 53 minutes and 41 seconds'),
    ( 4942229,      '57 days, 4 hours, 50 minutes and 29 seconds'),
    ( 9632227,      '111 days, 11 hours, 37 minutes and 7 seconds'),
    ( 480206,       '5 days, 13 hours, 23 minutes and 26 seconds'),
    ( 8203972,      '94 days, 22 hours, 52 minutes and 52 seconds'),
    ( 2743917,      '31 days, 18 hours, 11 minutes and 57 seconds'),
    ( 2370751,      '27 days, 10 hours, 32 minutes and 31 seconds'),
    ( 7489451,      '86 days, 16 hours, 24 minutes and 11 seconds'),
    ( 9081921,      '105 days, 2 hours, 45 minutes and 21 seconds'),
    ( 8452787,      '97 days, 19 hours, 59 minutes and 47 seconds'),
    ( 3171446,      '36 days, 16 hours, 57 minutes and 26 seconds'),
    ( 5535208,      '64 days, 1 hour, 33 minutes and 28 seconds'),
    ( 8738348,      '101 days, 3 hours, 19 minutes and 8 seconds'),
    ( 3659942,      '42 days, 8 hours, 39 minutes and 2 seconds'),
    ( 5067930,      '58 days, 15 hours, 45 minutes and 30 seconds'),
    ( 2937657,      '34 days and 57 seconds'),
    ( 4295521,      '49 days, 17 hours, 12 minutes and 1 second'),
    ( 5035257,      '58 days, 6 hours, 40 minutes and 57 seconds'),
    ( 6394512,      '74 days, 15 minutes and 12 seconds'),
    ( 1418649,      '16 days, 10 hours, 4 minutes and 9 seconds'),
    ( 2750707,      '31 days, 20 hours, 5 minutes and 7 seconds'),
    ( 7763735,      '89 days, 20 hours, 35 minutes and 35 seconds'),
    ( 5956421,      '68 days, 22 hours, 33 minutes and 41 seconds'),
    ( 3071337,      '35 days, 13 hours, 8 minutes and 57 seconds'),
    ( 2750913,      '31 days, 20 hours, 8 minutes and 33 seconds'),
    ( 7497430,      '86 days, 18 hours, 37 minutes and 10 seconds'),
    ( 6431487,      '74 days, 10 hours, 31 minutes and 27 seconds'),
    ( 2402971,      '27 days, 19 hours, 29 minutes and 31 seconds'),
    ( 4033767,      '46 days, 16 hours, 29 minutes and 27 seconds'),
    ( 3093646,      '35 days, 19 hours, 20 minutes and 46 seconds'),
    ( 8735423,      '101 days, 2 hours, 30 minutes and 23 seconds'),
    ( 4789613,      '55 days, 10 hours, 26 minutes and 53 seconds'),
    ( 6413637,      '74 days, 5 hours, 33 minutes and 57 seconds'),
    ( 6853350,      '79 days, 7 hours, 42 minutes and 30 seconds'),
    ( 3331343,      '38 days, 13 hours, 22 minutes and 23 seconds'),
    ( 9721575,      '112 days, 12 hours, 26 minutes and 15 seconds'),
    ( 9053431,      '104 days, 18 hours, 50 minutes and 31 seconds'),
    ( 6097134,      '70 days, 13 hours, 38 minutes and 54 seconds'),
    ( 4063446,      '47 days, 44 minutes and 6 seconds'),
    ( 4664669,      '53 days, 23 hours, 44 minutes and 29 seconds'),
    ( 1918785,      '22 days, 4 hours, 59 minutes and 45 seconds'),
    ( 8018545,      '92 days, 19 hours, 22 minutes and 25 seconds'),
    ( 351996,       '4 days, 1 hour, 46 minutes and 36 seconds'),
    ( 3577837,      '41 days, 9 hours, 50 minutes and 37 seconds'),
    ( 6057876,      '70 days, 2 hours, 44 minutes and 36 seconds'),
    ( 6045504,      '69 days, 23 hours, 18 minutes and 24 seconds'),
    ( 6425050,      '74 days, 8 hours, 44 minutes and 10 seconds'),
    ( 1041412,      '12 days, 1 hour, 16 minutes and 52 seconds'),
    ( 4476241,      '51 days, 19 hours, 24 minutes and 1 second'),
    ( 9463028,      '109 days, 12 hours, 37 minutes and 8 seconds'),
    ( 3267120,      '37 days, 19 hours and 32 minutes'),
    ( 2605652,      '30 days, 3 hours, 47 minutes and 32 seconds'),
    ( 264009,       '3 days, 1 hour, 20 minutes and 9 seconds'),
    ( 9102587,      '105 days, 8 hours, 29 minutes and 47 seconds'),
    ( 5322641,      '61 days, 14 hours, 30 minutes and 41 seconds'),
    ( 3951085,      '45 days, 17 hours, 31 minutes and 25 seconds'),
    ( 9471252,      '109 days, 14 hours, 54 minutes and 12 seconds'),
    ( 1157827,      '13 days, 9 hours, 37 minutes and 7 seconds'),
    ( 5167227,      '59 days, 19 hours, 20 minutes and 27 seconds'),
    ( 674215,       '7 days, 19 hours, 16 minutes and 55 seconds'),
    ( 8970490,      '103 days, 19 hours, 48 minutes and 10 seconds'),
    ( 8654437,      '100 days, 4 hours and 37 seconds'),
    ( 9835683,      '113 days, 20 hours, 8 minutes and 3 seconds'),
    ( 3608195,      '41 days, 18 hours, 16 minutes and 35 seconds'),
    ( 7356352,      '85 days, 3 hours, 25 minutes and 52 seconds'),
    ( 3689628,      '42 days, 16 hours, 53 minutes and 48 seconds'),
    ( 5094338,      '58 days, 23 hours, 5 minutes and 38 seconds'),
    ( 3531615,      '40 days, 21 hours and 15 seconds'),
    ( 4686188,      '54 days, 5 hours, 43 minutes and 8 seconds'),
    ( 7104462,      '82 days, 5 hours, 27 minutes and 42 seconds'),
    ( 4705982,      '54 days, 11 hours, 13 minutes and 2 seconds'),
    ( 1331214,      '15 days, 9 hours, 46 minutes and 54 seconds'),
    ( 632811,       '7 days, 7 hours, 46 minutes and 51 seconds'),
    ( 8606505,      '99 days, 14 hours, 41 minutes and 45 seconds'),
    ( 3241414,      '37 days, 12 hours, 23 minutes and 34 seconds'),
    ( 5560153,      '64 days, 8 hours, 29 minutes and 13 seconds'),
    ( 995091,       '11 days, 12 hours, 24 minutes and 51 seconds'),
    ( 4491925,      '51 days, 23 hours, 45 minutes and 25 seconds'),
    ( 7612967,      '88 days, 2 hours, 42 minutes and 47 seconds'),
    ( 7899419,      '91 days, 10 hours, 16 minutes and 59 seconds'),
    ( 1165526,      '13 days, 11 hours, 45 minutes and 26 seconds'),
    ( 2259745,      '26 days, 3 hours, 42 minutes and 25 seconds'),
    ( 6311971,      '73 days, 1 hour, 19 minutes and 31 seconds'),
    ( 371736,       '4 days, 7 hours, 15 minutes and 36 seconds'),
    ( 7615466,      '88 days, 3 hours, 24 minutes and 26 seconds'),
    ( 7053577,      '81 days, 15 hours, 19 minutes and 37 seconds'),
    ( 3172844,      '36 days, 17 hours, 20 minutes and 44 seconds'),
    ( 1139596,      '13 days, 4 hours, 33 minutes and 16 seconds'),
]



def human_readable_duration_format_test( func ) -> None :

    failed_tests = 0

    print("*"*100)
    print("\n\n")

    for idx, test in enumerate( __TESTS ):

        expected_result = test[1]
        provided_result = func( test[0] )

        if expected_result != provided_result:

            print( f"\n\tTest {idx+1} Fail\n" )
            print( f"\tInput    : { test[0] }")
            print( f"\tExpected : { expected_result }")
            print( f"\tRecieved : { provided_result }\n")
            failed_tests += 1
    
    if failed_tests == 0:
        print(f"{ len(__TESTS) - failed_tests } out of {len(__TESTS)} tests passed!")

    print("\n\n")
    print("*"*100)
        
