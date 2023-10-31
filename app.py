from flask import Flask, request

app = Flask(__name)

# Create an endpoint to handle incoming requests
@app.route('/elasticsearch-webhook', methods=['POST'])
def elasticsearch_webhook():
    # Print the received JSON data
    data = request.get_json()
    print("Received data from Elasticsearch:")
    print(data)

    return 'Request received', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
