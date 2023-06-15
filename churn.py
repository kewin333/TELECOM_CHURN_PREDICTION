from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('telco_model.pkl', 'rb'))



@app.route("/")
@cross_origin()
def home():
    return render_template("churn.html")




@app.route("/", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Gender
        Gender = request.form["Gender"]
        if (Gender == 'Male'):
            Male = 1
            Female = 0

        elif (Gender == 'Female'):
            Male = 0
            Female = 1

        else:
            Male = 0
            Female = 0
            
       
        # Partner
        Partner = request.form["Partner"]
        if (Partner == 'Yes'):
            p_Yes = 1
            p_No = 0

        elif (Partner == 'No'):
            p_Yes = 0
            p_No = 1

        else:
            p_Yes = 0
            p_No = 0

        # Dependents
        Dependents = request.form["Dependents"]
        if (Dependents == 'Yes'):
            d_Yes = 1
            d_No = 0

        if (Dependents == 'No'):
            d_Yes = 0
            d_No = 1

        else:
            d_Yes = 0
            d_No = 0
            

         # Internet Service
        Internet_Service = request.form["Internet Service"]
        if (Internet_Service == 'DSL'):
            DSL = 1
            Fiber_optic = 0
            i_No = 0

        elif (Internet_Service == 'Fiber optic'):
            DSL = 0
            Fiber_optic = 1
            i_No = 0

        elif (Internet_Service == 'No'):
            DSL = 0
            Fiber_optic = 0
            i_No = 1

        else:
            DSL = 0
            Fiber_optic = 0
            i_No = 0

         
         # Device Protection
        Device_Protection = request.form["Device Protection"]
        if (Device_Protection == 'No internet service'):
            No_internet_service = 1
            dp_Yes = 0
            dp_No = 0

        elif (Device_Protection == 'Yes'):
            No_internet_service = 0
            dp_Yes = 1
            dp_No = 0

        elif (Device_Protection == 'No'):
            No_internet_service = 0
            dp_Yes = 0
            dp_No = 1

        else:
            No_internet_service = 0
            dp_Yes = 0
            dp_No = 0

         # Contract
        Contract = request.form["Contract"]
        if (Contract == 'Month-to-month'):
            Month_to_month = 1
            One_year = 0
            Two_year = 0

        elif (Contract == 'One year'):
            Month_to_month = 0
            One_year = 1
            Two_year = 0

        elif (Contract == 'Two year'):
            Month_to_month = 0
            One_year = 0
            Two_year = 1

        else:
            Month_to_month = 0
            One_year = 0
            Two_year = 0


         # Payment Method
        Payment_Method = request.form["Payment Method"]
        if (Payment_Method == 'Electronic check'):
            Electronic_check = 1
            Mailed_check = 0
            Bank_transfer_automatic = 0
            Credit_card_automatic = 0

        elif (Payment_Method == 'Mailed check'):
            Electronic_check = 0
            Mailed_check = 1
            Bank_transfer_automatic = 0
            Credit_card_automatic = 0

        elif (Payment_Method == 'Bank transfer (automatic)'):
            Electronic_check = 0
            Mailed_check = 0
            Bank_transfer_automatic = 1
            Credit_card_automatic = 0

        elif (Payment_Method == 'Credit card (automatic)'):
            Electronic_check = 0
            Mailed_check = 0
            Bank_transfer_automatic = 0
            Credit_card_automatic = 1

        else:
            Electronic_check = 0
            Mailed_check = 0
            Bank_transfer_automatic = 0
            Credit_card_automatic = 0

        # Monthly Charges
        Monthly_Charges = request.form.get("Monthly Charges", False)


        prediction=model.predict([[
            Male,
            Female,
            p_Yes,
            p_No,
            d_Yes,
            d_No,
            DSL,
            Fiber_optic,
            i_No,
            No_internet_service,
            dp_Yes,
            dp_No,
            Month_to_month,
            One_year,
            Two_year,
            Electronic_check,
            Mailed_check,
            Bank_transfer_automatic,
            Credit_card_automatic,
            Monthly_Charges
        ]])

        if prediction == 1:
            output = ("This customer is likely to be churn")
      
        else:
            output = ("This customer is likely to continue")


        return render_template('churn.html', output = output)


    return render_template("churn.html")




if __name__ == "__main__":
    app.run(debug=True)