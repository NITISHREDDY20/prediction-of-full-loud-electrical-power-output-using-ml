from flask import Flask, render_template,request
import pickle
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def index():
    
 return render_template("index.html")

@app.route('/data_predict', methods=['POST'])
def predict():
    at = request.form['at']
    v = request.form['v']
    ap = request.form['ap']
    rh = request.form['rh']

    data = [[float(at), float(v), float(ap), float(rh)]]

    # Load the model properly
    with open('CCPP.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    prediction = model.predict(data)[0]

    return render_template('predict.html', prediction=prediction)

# Ensure app runs properly
if __name__ == '__main__':
    app.run()
