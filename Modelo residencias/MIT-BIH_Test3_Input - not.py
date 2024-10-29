import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import warnings

# Ignora la advertencia sobre las características faltantes
warnings.filterwarnings('ignore', message='X does not have valid feature names, but')

# Load model from file
loaded_model, loaded_scaler = joblib.load('C:/Users/HP/Documents/2024/Python/GitKraken/PythonWorkspace/Modelo residencias/Nehemiah.pkl')

new0 = [76,313,0.07434712,-0.160547951,1.036401408,-0.285662496,-0.026823649,41,18,66,7,76,313,0.038309507,0.025784325,0.025930319,0.02527078,0.025930319,2,18,22,2] # N
new1 = [313,315,-0.052078893,-0.264784292,0.886596913,-0.366297705,-0.059710405,21,4,33,8,313,315,0.014263639,0.045458043,0.032572702,-0.104502953,-0.042008529,26,27,62,9] # N
new2 = [151,439,0.463362235,0.519227559,0.399900123,-0.835039794,-0.206610994,47,39,171,85,151,439,-0.277927062,-0.273391493,-0.574060719,-0.597215122,-0.574060719,2,11,23,10] # VEB

new_2d = np.reshape(new0, (1, -1))
new_2d_scale = loaded_scaler.transform(new_2d)
new_2d_scale = new_2d_scale.flatten()
#new_2d_scale = new_2d_scale.reshape(1, -1) #No
#print(new_2d_scale)

prediccion0 = loaded_model.predict([new_2d_scale])
#prediccion0 = loaded_model.predict([new0])
print(prediccion0)
