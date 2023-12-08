MongoDB Atlas data retrieving using API and data mapping


  Install Flask and Requests libraries by running the following commands in your terminal or install as packages.
        
        pip install Flask ... 
        or as packages 
    


configure the Flask App:
    - Open the Flask app file (e.g., `app.py`) and replace the placeholders (`your_mongodb_atlas_api_url_here` and `your_api_key_here`) with your actual MongoDB Atlas API endpoint URL and API key.

Run the Flask App:
        
        python app.py
        
    - This will start the Flask app locally.

Access the Export Endpoint: you can always change your endpoint in your script to serve the needs.
    - Once the Flask app is running, open a web browser and access the following URL:
        http://localhost:5000/export_csv
      
     This will trigger the CSV file download with the exported data from MongoDB Atlas.

 Logs 
    `app.log` file in the same directory as the Flask app to view logs of events and errors generated during the app's execution.

