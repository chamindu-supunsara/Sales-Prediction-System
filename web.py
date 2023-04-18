from flask import Flask, render_template,request
import pickle
import numpy as np


app = Flask(__name__)


def prediction(lst):
    filename = 'ML_Model/store-sales-model.pickle'
   
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    predict_value =  model[1].predict([lst])
    return predict_value

@app.route('/',methods = ['POST','GET'])
def index():
    pred = 0

    if request.method == 'POST':

        store_number = request.form['store_num'] # varibles can chnge
        family = request.form['family']
        promotion = request.form['onpromotion']
        year = request.form['year']
        month = request.form['month']
       
        
        feuture_list=[]
        feuture_list.append(int(promotion))
        feuture_list.append(int(store_number))

    
        family_list = ['AUTOMOTIVE','BABY CARE','BEAUTY','BEVERAGES','BOOKS','BREAD/BAKERY',
        'CELEBRATION','CLEANING','DAIRY','DELI','EGGS','FROZEN FOODS','GROCERY I',
        'GROCERY II','HARDWARE','HOME AND KITCHEN I','HOME AND KITCHEN II',
        'HOME APPLIANCES','HOME CARE','LADIESWEAR','LAWN AND GARDEN','LINGERIE',
        'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE','PET SUPPLIES',
        'PLAYERS AND ELECTRONICS','POULTRY','PREPARED FOODS','PRODUCE',
        'SCHOOL AND OFFICE SUPPLIES','SEAFOOD']
        year_list = ['2013','2014','2015','2016','2017']
        month_list = ['1','2','3','4','5','6','7','8','9','10','11','12']
        
       
        def traverse(lists,value): 
            for item in lists:
                if item == value:
                    feuture_list.append(1)
                else:
                    feuture_list.append(0)    

        traverse(family_list,family)
        traverse(year_list,year)
        traverse(month_list,month)
        print(feuture_list)

        pred = prediction(feuture_list)*344
        pred = np.round(pred[0])
        print(pred)
       
    return render_template("index.html",pred=pred)

if __name__=='__main__':
    app.run(debug=True)