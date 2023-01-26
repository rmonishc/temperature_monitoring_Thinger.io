from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    # Get the data from the request
    data = request.get_json()

    # Write the data to a CSV file
    with open('data.csv', mode='a') as csv_file:
        fieldnames = ['Place', 'Time', 'Temperature', 'Humidity']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(data)
    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='172.16.10.129', port=8000, debug=True)