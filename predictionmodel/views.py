from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import pickle
import os

model_url="C:/Users/swastik limbu/Desktop/ML Project/earthquake_detection/predictionmodel/earthquake.pkl"

with open(model_url, "rb") as f:
    model=pickle.load(f)

@api_view(["POST"])
def prediction(request):
    data=request.data
    magnitude= float(data.get("magnitude",0))
    depth= float(data.get("depth",0))
    cdi= float(data.get("cdi",0))
    mmi= float(data.get("mmi", 0))
    sig= float(data.get("sig",0))

    X= pd.DataFrame([[magnitude, depth, cdi, mmi, sig]], columns=['magnitude', 'depth', 'cdi', 'mmi','sig'])

    prediction= model.predict(X)[0]

    return Response({'prediction': float(prediction)})