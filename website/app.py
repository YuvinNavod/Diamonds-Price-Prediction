
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
def prediction(lst):
    filename='model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([ lst ])
    return pred_value



@app.route('/', methods=['GET', 'POST'])
def index():
     pred_value = 0
     if request.method == 'POST':
        Engine_Size=request.form['Engine_Size']
        Bore=request.form['Bore']
        Stroke=request.form['Stroke']
        Horse_Power=request.form['Horse_Power']
        Top_RPM=request.form['Top_Rpm']
        Brand_Name=request.form['Brand_Name']
        Design =request.form['Design']
        Wheel_Drive=request.form['Wheel_Drive']
        Fuel_type_diesel=request.form.getlist('Fuel_type_diesel')
        Fuel_type_gas=request.form.getlist('Fuel type_gas')
        Aspiration_std=request.form.getlist('Aspiration_std')
        Aspiration_turbo=request.form.getlist('Aspiration_turbo')
        Engine_Location_front=request.form.getlist('Engine_Location_front')
        Engine_Location_rear=request.form.getlist('Engine_Location_rear')
        Engine_Type_Other=request.form.getlist('Engine_Type_Other')
        Engine_Type_ohc=request.form.getlist('Engine_Type_ohc')

        feature_list = []
        feature_list.append(int(Engine_Size))
        feature_list.append(float(Bore))
        feature_list.append(float(Stroke))
        feature_list.append(int(Horse_Power))
        feature_list.append(int(Top_RPM))

    
        BrandName_list = ['Brand_Name_Other', 'Brand_Name_honda', 'Brand_Name_mazda',
       'Brand_Name_mitsubishi', 'Brand_Name_nissan', 'Brand_Name_peugot',
       'Brand_Name_subaru', 'Brand_Name_toyota', 'Brand_Name_volkswagen',
       'Brand_Name_volvo']
        Design_list = ['Design_Other','Design_hatchback', 'Design_sedan', 'Design_wagon']
        WheelDrive_list = ['Wheel_Drive_4wd', 'Wheel_Drive_fwd', 'Wheel_Drive_rwd']


        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(BrandName_list, Brand_Name)
        feature_list.append(len(Fuel_type_diesel))
        feature_list.append(len(Fuel_type_gas))
        feature_list.append(len(Aspiration_std))
        feature_list.append(len(Aspiration_turbo))
        traverse_list(Design_list, Design)
        traverse_list(WheelDrive_list, Wheel_Drive)
        feature_list.append(len(Engine_Location_front))
        feature_list.append(len(Engine_Location_rear))
        feature_list.append(len(Engine_Type_Other))
        feature_list.append(len(Engine_Type_ohc))
        
        print(feature_list)

        pred_value= prediction(feature_list)
        print(pred_value)
        pred_value = np.round(pred_value[0],2)*344
       

   
     return render_template('index.html', pred_value=pred_value)

if __name__ == '__main__':
    app.run(debug=True)