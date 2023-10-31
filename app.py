from flask import Flask, request

app = Flask(__name__)

# Create an endpoint to handle incoming requests
@app.route('/elasticsearch-webhook', methods=['POST'])
def elasticsearch_webhook():
    # Print the received JSON data
    data = request.get_json()

    lat_lon_str = data["lat_lon_data"]

    # Remove the outermost double quotes from the string
    lat_lon_str = lat_lon_str[1:-1]
    
    # Split the string into individual lists
    lat_lon_list = [list(map(float, item.strip("[]").split(','))) for item in lat_lon_str.split("], [")]
    
    # Now, lat_lon_list contains the list of latitudes and longitudes as lists of floats
    for index, lat_lon in enumerate(lat_lon_list):
        print(f"Index {index}: Latitude {lat_lon[0]}, Longitude {lat_lon[1]}")
    
    print("Received data from Elasticsearch:")
    print(data)

    return 'Request received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
