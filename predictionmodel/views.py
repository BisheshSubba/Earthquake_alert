from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import pickle

model_url = "C:/Users/swastik limbu/Desktop/ML Project/earthquake_detection/predictionmodel/earthquake.pkl"
label_path = "C:/Users/swastik limbu/Desktop/ML Project/earthquake_detection/predictionmodel/label_encoder.pkl"

with open(model_url, "rb") as f:
    model = pickle.load(f)
with open(label_path, "rb") as f:
    label = pickle.load(f)

@api_view(["POST"])
def prediction(request):
    data = request.data
    magnitude = float(data.get("magnitude", 0))
    depth = float(data.get("depth", 0))
    cdi = float(data.get("cdi", 0))
    mmi = float(data.get("mmi", 0))
    sig = float(data.get("sig", 0))

    # Prepare input
    X = pd.DataFrame([[magnitude, depth, cdi, mmi, sig]],
                     columns=['magnitude', 'depth', 'cdi', 'mmi', 'sig'])

    # Predict
    prediction = model.predict(X)[0]  # model outputs encoded label (e.g. 0, 1, 2)
    decoded_label = label.inverse_transform([int(prediction)])[0]  # decode to string
    decoded_label = str(decoded_label)

    return Response({
        'class': decoded_label
    })
