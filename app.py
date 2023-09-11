from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)

@app.route('/api')
def index():

    # Get slack name and track 
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get  current day
    current_day = datetime.utcnow().strftime('%A')

    # Get current UTC time
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # Create the response data as a dict
    data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': 'https://github.com/olumeedee/First-task-hng/blob/main/app.py',
        'github_repo_url': 'https://github.com/olumeedee/First-task-hng.git',
        'status_code': "200"
    } 
    
 
    # turn response into json
    response = jsonify(data)

    # Set the Content-Type header to indicate that you are sending JSON
    response.headers['Content-Type'] = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)