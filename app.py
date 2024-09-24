from flask import Flask, render_template

# Flask app initialize karte hain
app = Flask(__name__)

# Home route define karte hain
@app.route('/')
def home():
    return render_template('index.html')

# Agar app ko directly run kiya jaye, toh server start hoga
if __name__ == '__main__':
    app.run(debug=True)
