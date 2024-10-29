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

"""new0 = np.array(new0, dtype=[('0_pre-RR', np.int64), ('0_post-RR', np.float64), ('0_pPeak', np.float64), ('0_tPeak', np.float64), ('0_rPeak', np.float64), ('0_sPeak', np.float64), 
                             ('0_qPeak', np.float64), ('0_qrs_interval', np.int64), ('0_pq_interval', np.int64), ('0_qt_interval', np.int64), ('0_st_interval', np.int64),
                             ('1_pre-RR', np.int64), ('1_post-RR', np.float64), ('1_pPeak', np.float64), ('1_tPeak', np.float64), ('1_rPeak', np.float64), ('1_sPeak', np.float64), 
                             ('1_qPeak', np.float64), ('1_qrs_interval', np.int64), ('1_pq_interval', np.int64), ('1_qt_interval', np.int64), ('1_st_interval', np.int64)])"""

new_2d = np.reshape(new0, (1, -1))
new_2d_scale = loaded_scaler.transform(new_2d)
new_2d_scale = new_2d_scale.flatten()
#new_2d_scale = new_2d_scale.reshape(1, -1) #No
#print(new_2d_scale)

prediccion0 = loaded_model.predict([new_2d_scale])
#prediccion0 = loaded_model.predict([new0])
print(prediccion0)

"""dataset_columns = ['0_pre-RR','0_post-RR','0_pPeak','0_tPeak','0_rPeak','0_sPeak','0_qPeak','0_qrs_interval','0_pq_interval','0_qt_interval','0_st_interval',
                   '1_pre-RR','1_post-RR','1_pPeak','1_tPeak','1_rPeak','1_sPeak','1_qPeak','1_qrs_interval','1_pq_interval','1_qt_interval', '1_st_interval']

new0_df = pd.DataFrame([new0], columns=dataset_columns)

new0_scaled = loaded_scaler.transform(new0_df)
#new0_scaled = new0_scaled.reshape(new0_scaled.shape[0], -1)

prediccion = loaded_model.predict(new0_scaled)
print(prediccion)"""
