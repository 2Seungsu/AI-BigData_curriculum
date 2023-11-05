from flask import Flask, render_template, request
import joblib
import cv2
from rembg import remove
import numpy as np
import pandas as pd
import json
import pickle
from PIL import Image



model_man = joblib.load('./man_.pkl')
model_woman = joblib.load('./woman_animal.pkl')

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main():
    return render_template('inner.html')


@app.route('/inner.html')
def mains():
    return render_template('inner.html')



@app.route('/reels.html')
def reels():
    return render_template('reels.html')


@app.route('/animal.html')
def animal():
    return render_template('animal.html')



@app.route('/upload', methods=['POST'])
def upload_file():

    gender=request.form.get("gender")
    
    uploaded_file = request.files['file']
    uploaded_file.save('./static/image/uploaded_file.png')

    if uploaded_file:

        # 1. grayscale
        imgData=cv2.imread('./static/image/uploaded_file.png',cv2.IMREAD_GRAYSCALE)

        # 2. resize
        imgData=cv2.resize(imgData,dsize=(100,100))

        # 3. remove
        output=remove(imgData)

        # 4. 정규화
        output=output/255

        # 5. reshape((1,-1))
        output_=output.reshape((1,-1))

        # 6. 데이터프레임 만들기
        new_=pd.DataFrame(np.array(output_))

        if gender == "man":
            model_man.predict(new_)
            proba=model_man.predict_proba(new_)
            proba_list=proba.tolist()
            return render_template('animal.html', data=proba_list )
        
        elif gender == "woman":
            model_woman.predict(new_)
            proba=model_woman.predict_proba(new_)
            proba_list=proba.tolist()
            return render_template('animal.html', data=proba_list )
        

    else:
        return 'No file selected'
    

if __name__ == '__main__':
    app.run()


