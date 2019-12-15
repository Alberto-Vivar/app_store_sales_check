import sys
from appstoreconnect_library import request_maker
import datetime

KEY_IDENTIFIER = 'YOUR_KEY_IDENTIFIER'
ISSUER = 'YOUR_ISSUER_IDENTIFIER'
VENDOR_NUMBER = 'YOUR_APP_VENDOR_NUMBER'

# The input arguments of this script are:
# 1.- The date to request the daily report.
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('The program should be called with one parameter, the date. This should be formatted as "YYYY-MM-DD".')
    else:
        first_parameter = sys.argv[1]
        try:
           _ = datetime.datetime.fromisoformat(first_parameter)
        except ValueError as v:
            sys.exit('The date is not properly entered: {}.'.format(v))
        print(
            request_maker.pull_sales_report(
                key_identifier=KEY_IDENTIFIER,
                issuer=ISSUER,
                vendor_number=VENDOR_NUMBER,
                requested_date=sys.argv[1]
            )
        )
