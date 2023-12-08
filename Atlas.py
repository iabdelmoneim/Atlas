import logging
from flask import Flask, make_response
import requests
import csv
from io import StringIO

app = Flask(__name__)

# log filw
logging.basicConfig(filename='app.log', level=logging.INFO)

MONGODB_ATLAS_API_URL = "your_mongodb_atlas_api_url_here"
API_KEY = "your_api_key_here"

@app.route('/export_csv', methods=['GET'])
def export_csv():
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }
        response = requests.get(MONGODB_ATLAS_API_URL, headers=headers)

        if response.status_code == 200:
            data = response.json()  

            # Define the fields to be included/mapped in the CSV
            fields = [
                "cloudID",
                "accountname",
                "entitytype",
                "accounttype",
                "owner",
                "Authmethod",
                "deletedflag",
                "deletedday",
                "comment",
                "disabledflag",
                "Account type",
                "Authmethod",
                "lastlogindate",
                "entitytype",
                "account status"
            ]

            # Create a CSV string
            csv_output = StringIO()
            csv_writer = csv.DictWriter(csv_output, fieldnames=fields)
            csv_writer.writeheader()
            for account in data:
                # Mapping 
                mapped_account = {
                    "cloudID": account.get("cloudID"),
                    "accountname": account.get("accountname"),
                    "entitytype": account.get("entitytype"),
                    "accounttype": account.get("accounttype"),
                    "owner": account.get("owner"),
                    "Authmethod": "Active directory",
                    "deletedflag": account.get("deletedflag"),
                    "deletedday": account.get("deletedday"),
                    "comment": account.get("comment"),
                    "disabledflag": account.get("disabledflag"),
                    "Account type": account.get("account_type"),
                    "Authmethod": "Active directory",
                    "lastlogindate": account.get("last_login_date"),
                    "entitytype": "cloud",
                    "previliged": "true" if account.get("previliged") else "false",
                    "account status": account.get("account_status")
                }
                csv_writer.writerow(mapped_account)

            # Create a response with CSV as attachment
            output = make_response(csv_output.getvalue())
            output.headers["Content-Disposition"] = "attachment; filename=accounts_data.csv"
            output.headers["Content-type"] = "text/csv"

            return output
        else:
            logging.error(f"Failed to fetch data from MongoDB Atlas API. Status code: {response.status_code}")
            return "Failed to fetch data from MongoDB Atlas API", 500
    except Exception as e:
        logging.exception(f"An error occurred: {str(e)}")
        return "An error occurred while processing the request", 500

if __name__ == '__main__':
    app.run(debug=True)

