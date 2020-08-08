import json
import random
import time
from datetime import datetime
import csv

from flask import Flask, Response, render_template

random.seed()
application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')


@application.route('/chart-data')
def chart_data():
    def generate_bandwidth_data():
        count = 0
        while True:
            with open('log.csv', 'r') as file:
                reader = csv.reader(file)
                my_list = list(reader)
            json_data = json.dumps(
                {'time': my_list[count][1], 'value': my_list[count][0]})
            count = count + 2
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_bandwidth_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)