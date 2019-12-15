import cgi
import datetime
import requests
import os
from . import report_extractor, token_generator
from . import REPORTS_FOLDER, LOGGER


def pull_sales_report(key_identifier, issuer, vendor_number, requested_date=None):
    """
    Retrieve the sales report and save it locally.
    :return: None if there was an error with the request else the filename of the saved report.
    """
    base_url = 'https://api.appstoreconnect.apple.com/v1/salesReports'
    authorization_token = token_generator.generate_jwt_token(key_identifier=key_identifier, issuer=issuer)
    if requested_date is None or type(requested_date) is not str:
        requested_date = datetime.date.today().isoformat()
    querystring = {'filter[frequency]': 'DAILY',
                   'filter[reportType]': 'SALES',
                   'filter[reportSubType]': 'SUMMARY',
                   'filter[vendorNumber]': vendor_number,
                   'filter[reportDate]': requested_date}
    headers = {
        'Authorization': 'Bearer {}'.format(authorization_token),
    }
    response = requests.request("GET", base_url, headers=headers, params=querystring)
    if response.status_code == 200:
        LOGGER.info('Response status %s for date %s', response.status_code, requested_date)
        response_content = response.content
        content_header = response.headers.get("Content-Disposition")
        filename = None
        if content_header is not None:
            value, params = cgi.parse_header(content_header)
            if value == "attachment":
                preferred_filename = params.get('filename')
                if preferred_filename is not None:
                    filename = preferred_filename
        if filename is None:
            filename = datetime.date.isoformat(datetime.date.today() - datetime.date.day)
        report_path = os.path.join(os.curdir, REPORTS_FOLDER, filename)
        with open(report_path, 'wb') as fp:
            fp.write(response_content)
        field_names, rows = report_extractor.extract(report_path)
        # 1F value comes from https://help.apple.com/app-store-connect/#/dev63c6f4502
        first_time_download_rows = list(filter(lambda x: x['Product Type Identifier'] == '1F', rows))
        total = sum(list(map(lambda x: int(x['Units']), first_time_download_rows)))
        return requested_date, total, report_path
    LOGGER.error('Response status %s for date %s', response.status_code, requested_date)
    return None
