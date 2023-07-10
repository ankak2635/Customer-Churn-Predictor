from flask import Flask, render_template, request
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.logger import logging
 
application = Flask(__name__)

app = application

# Route for homepage
logging.info('Entered the application')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_data():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
                 SeniorCitizen = request.form.get('SeniorCitizen'),
                 Partner = request.form.get('Partner'),
                 Dependents = request.form.get('Dependents'), 
                 TenureMonths = request.form.get('TenureMonths'),
                 PhoneService = request.form.get('PhoneService'),
                 MultipleLines = request.form.get('MultipleLines'),
                 InternetService = request.form.get('InternetService'),
                 OnlineSecurity = request.form.get('OnlineSecurity'),
                 OnlineBackup = request.form.get('OnlineBackup'),
                 DeviceProtection = request.form.get('DeviceProtection'),
                 TechSupport = request.form.get('TechSupport'),
                 StreamingTV = request.form.get('StreamingTV'),
                 StreamingMovies = request.form.get('StreamingMovies'),
                 Contract = request.form.get('Contract'),
                 PaperlessBilling = request.form.get('PaperlessBilling'),
                 PaymentMethod = request.form.get('PaymentMethod'),
                 MonthlyCharges = request.form.get('MonthlyCharges'),
                 ChurnScore = request.form.get('ChurnScore'),
                 CLTV = request.form.get('CLTV')
        )

        pred_df = data.get_as_dataframe()
        logging.info('Got user input as dataframe')
        print(pred_df)

        make_prediction = PredictPipeline()
        results = make_prediction.predict(pred_df)
        if results[0] ==1:
            result  = "The customer will churn!"
        else:
            result =  "The customer will not churn!"
        
        logging.info('Made prediction')
        print(result)

        return render_template('home.html', results = result)




if __name__ == "__main__":
    app.run(host='0.0.0.0')