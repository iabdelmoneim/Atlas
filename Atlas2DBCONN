
from flask import Flask, make_response
import pymongo
import csv
from io import StringIO

app = Flask(__name__)

# Connection1
MONGODB_ATLAS_URI = "your_mongodb_atlas_uri_here"
DATABASE_NAME = "your_database_name"
COLLECTION_NAME = "your_collection_name"

# connection2
client = pymongo.MongoClient(MONGODB_ATLAS_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Define the fields to be retrieved and mapped 
fields = {
    "Account type": "account_type",
    "Authmethod": "Active directory",
    "lastlogindate": "last_login_date",
    "entitytype": "cloud",
    "previliged": "privileged",
    "lifecycle id": "_id",  # Assuming _id is the Cloud account ID
    "account status": "account_status"
}

@app.route('/export_csv', methods=['GET'])
def export_csv():
    # Fetch data from MongoDB Atlas
    data = collection.find({}, fields)

    csv_output = StringIO()
    csv_writer = csv.DictWriter(csv_output, fieldnames=fields.keys())
    csv_writer.writeheader()
    for account in data:
        account["previliged"] = "true" if account.get("previliged") else "false"
        csv_writer.writerow(account)

    # Create a response with CSV as attachment
    output = make_response(csv_output.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=accounts_data.csv"
    output.headers["Content-type"] = "text/csv"

    return output

if __name__ == '__main__':
    app.run(debug=True)
