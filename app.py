from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        sha256_hash = hashlib.sha256(text.encode('utf-8')).hexdigest()
        return render_template('result.html', text=text, sha256_hash=sha256_hash)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)