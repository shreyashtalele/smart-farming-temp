from django.http import JsonResponse
import numpy as np
import pickle
from django.views.decorators.csrf import csrf_exempt
import json
import os
from smartFarming.settings import BASE_DIR

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model


# Create your views here.

@csrf_exempt
def predictCrop(request):

    # print(request.body["nitrogen"])
    form_data = json.loads(request.body.decode())

    N = form_data["nitrogen"]
    P = form_data["phosphorus"]
    K = form_data["potassium"]
    temp = form_data["temperature"]
    humidity = form_data["humidity"]
    ph = form_data["ph"]
    rainfall = form_data["rainfall"]

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1,-1)
            
    loaded_model = load_model(os.path.join(BASE_DIR, './cropReccomendation/logistic-regression-model.pkl'))
    prediction = loaded_model.predict(single_pred)
    print(prediction.item())

    return JsonResponse({
        "name":"hello",
        "success":True,
        "message":prediction.item(),
        "input":form_data
    }, safe=False)

