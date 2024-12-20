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

# Create your views here.
def predictFertilizer(request):

    form_data = json.loads(request.body.decode())

    TEMPERATURE = form_data["temperature"]
    HUMIDITY = form_data["humidity"]
    MOISTURE = form_data["moisture"]
    SOIL_TYPE = form_data["soil_type"]
    CROP_TYPE = form_data["crop_type"]
    NITROGEN = form_data["nitrogen"]
    POTASSIUM = form_data["potassium"]
    PHOSPHOROUS = form_data["phosphorus"]


    feature_list = [TEMPERATURE, HUMIDITY, MOISTURE, SOIL_TYPE, CROP_TYPE, NITROGEN, POTASSIUM, PHOSPHOROUS]
    single_pred = np.array(feature_list).reshape(1,-1)
            
    loaded_model = load_model(os.path.join(BASE_DIR, './fertlizerReccomendation/fertilizers-model.pkl'))
    print(loaded_model)
    prediction = loaded_model.predict(single_pred)

    return JsonResponse({
        "name":"hello",
        "success":True,
        "message":prediction.item(),
        "input":form_data
    })


