from flask import Flask, request

app = Flask(__name__)

# Create an endpoint to handle incoming requests
@app.route('/elasticsearch-webhook', methods=['POST'])
def elasticsearch_webhook():
    # Print the received JSON data
    data = request.get_json()
    print(data)
    lat_lon_data = json.loads(data["lat_lon_data"])

    # Convert the extracted data to a list
    lat_lon_list = lat_lon_data["_value"]
    print("Received data from Elasticsearch:")

    return 'Request received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
