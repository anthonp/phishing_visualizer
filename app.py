from flask import Flask, request, send_from_directory, jsonify, render_template
import os
import csv

app = Flask(__name__)
CSV_DIR = 'csvs'
MERGED_CSV = os.path.join(CSV_DIR, 'merged.csv')
os.makedirs(CSV_DIR, exist_ok=True)

# Ensure merged CSV exists with header
if not os.path.exists(MERGED_CSV):
    with open(MERGED_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sender', 'recipient', 'subject', 'date'])

@app.route('/upload', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and file.filename.endswith('.csv'):
        uploaded_data = file.read().decode('utf-8').replace('\r\n', '\n').splitlines()
        reader = csv.reader(uploaded_data)
        header = next(reader, None)
        with open(MERGED_CSV, 'a', newline='') as f:
            writer = csv.writer(f)
            for row in reader:
                if len(row) == 4:
                    writer.writerow(row)
        return jsonify({'message': 'File appended successfully'}), 200
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/get_merged_csv', methods=['GET'])
def get_merged_csv():
    return send_from_directory(CSV_DIR, 'merged.csv')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
