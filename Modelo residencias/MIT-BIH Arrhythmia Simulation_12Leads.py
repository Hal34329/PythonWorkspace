#Load NeuroKit and other useful packages
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

import os

savePath = "C:/Users/HP/Documents/2024/Itesco/ECG_Sim/12-Lead"
folderNum = 1

###########################################################
# Localización de la carpeta de guardado
while True:
    folder_name = f"Simulation_{folderNum}"
    full_path = os.path.join(savePath, folder_name)
    
    if not os.path.exists(full_path):  # Verifica si la carpeta ya existe
        os.makedirs(full_path)  # Crea la carpeta si no existe
        break  # Sale del bucle si la carpeta se creó correctamente
    
    folderNum += 1  # Incrementa el contador si la carpeta ya existe
###########################################################

plt.rcParams['figure.figsize'] = [15, 9]

# Simulate 30 seconds of ECG Signal (recorded at 250 samples / second)
ecg_signal = nk.ecg_simulate(duration=30, sampling_rate=360, method="multileads")

signal_II = ecg_signal["II"]  
signal_V5 = ecg_signal["V5"]

###########################################################
# Signal processing
###########################################################
### Lead II
# Automatically process the (raw) ECG signal
signals_II, info_II = nk.ecg_process(signal_II, sampling_rate=360)
# Extract clean ECG and R-peaks location
rpeaks_II = info_II["ECG_R_Peaks"]
cleaned_ecg_II = signals_II["ECG_Clean"]

### Lead V5
signals_V5, info_V5 = nk.ecg_process(signal_V5, sampling_rate=360)
rpeaks_V5 = info_V5["ECG_R_Peaks"]
cleaned_ecg_V5 = signals_V5["ECG_Clean"]

###########################################################

valid_indices_II = rpeaks_II[rpeaks_II < len(cleaned_ecg_II)]
r_peak_amplitudes_II = cleaned_ecg_II[valid_indices_II]

valid_indices_V5 = rpeaks_V5[rpeaks_V5 < len(cleaned_ecg_V5)]
r_peak_amplitudes_V5 = cleaned_ecg_V5[valid_indices_V5]

###########################################################

# Visualize R-peaks in ECG signal II
plot = nk.events_plot(rpeaks_II, cleaned_ecg_II)

plt.xlim(0, 5000)
plt.plot([], [], 'ro', label="R peaks")
plt.legend() 
plt.title("Picos R en la derivación II")
plt.savefig(f"{full_path}/R_Peak_II.png")
plt.close()

# Visualize R-peaks in ECG signal V5
plot = nk.events_plot(rpeaks_V5, cleaned_ecg_V5)

plt.xlim(0, 5000)
plt.plot([], [], 'ro', label="R peaks")
plt.legend() 
plt.title("Picos R en la derivación V5")
plt.savefig(f"{full_path}/R_Peak_V5.png")
plt.close()

###########################################################
# Delineate the ECG signal
_, waves_peak_II = nk.ecg_delineate(signal_II, rpeaks_II, sampling_rate=360, method="peak")

# Zooming into the first 3 R-peaks, with focus on T_peaks, P-peaks, Q-peaks and S-peaks
plot = nk.events_plot([waves_peak_II['ECG_T_Peaks'][:3], 
                       waves_peak_II['ECG_P_Peaks'][:3],
                       waves_peak_II['ECG_Q_Peaks'][:3],
                       waves_peak_II['ECG_S_Peaks'][:3]], signal_II[:1500])

plt.title("Gráfica TPQS para la señal de la derivación II")
plt.savefig(f"{full_path}/TPQS_Peaks_II.png")
plt.close()

###########################################################
# Delineate the ECG signal
_, waves_peak_V5 = nk.ecg_delineate(signal_V5, rpeaks_V5, sampling_rate=360, method="peak")

# Zooming into the first 3 R-peaks, with focus on T_peaks, P-peaks, Q-peaks and S-peaks
plot = nk.events_plot([waves_peak_V5['ECG_T_Peaks'][:3], 
                       waves_peak_V5['ECG_P_Peaks'][:3],
                       waves_peak_V5['ECG_Q_Peaks'][:3],
                       waves_peak_V5['ECG_S_Peaks'][:3]], signal_V5[:1500])

plt.title("Gráfica TPQS para la señal de la derivación V5")
plt.savefig(f"{full_path}/TPQS_Peaks_V5.png")
plt.close()

###########################################################
# Delineate the ECG signal
_, waves_peak_II = nk.ecg_delineate(signal_II, rpeaks_II, sampling_rate=360, method="peak")

# Zooming into the first 3 R-peaks, with focus on T_peaks, P-peaks, Q-peaks and S-peaks
plot = nk.events_plot([rpeaks_II[:3],
                       waves_peak_II['ECG_T_Peaks'][:3], 
                       waves_peak_II['ECG_P_Peaks'][:3],
                       waves_peak_II['ECG_Q_Peaks'][:3],
                       waves_peak_II['ECG_S_Peaks'][:3]], signal_II[:1500])

plt.title("Gráfica RTPQS para la señal de la derivación II")
plt.savefig(f"{full_path}/RTPQS_Peaks_II.png")
plt.close()

###########################################################
# Delineate the ECG signal
_, waves_peak_V5 = nk.ecg_delineate(signal_V5, rpeaks_V5, sampling_rate=360, method="peak")

# Zooming into the first 3 R-peaks, with focus on T_peaks, P-peaks, Q-peaks and S-peaks
plot = nk.events_plot([rpeaks_V5[:3],
                       waves_peak_V5['ECG_T_Peaks'][:3], 
                       waves_peak_V5['ECG_P_Peaks'][:3],
                       waves_peak_V5['ECG_Q_Peaks'][:3],
                       waves_peak_V5['ECG_S_Peaks'][:3]], signal_V5[:1500])

plt.title("Gráfica RTPQS para la señal de la derivación V5")
plt.savefig(f"{full_path}/RTPQS_Peaks_V5.png")
plt.close()

###########################################################
plt.figure(figsize=(15, 9)) 

plt.subplot(2, 1, 1)  # Crea un subplot para la señal II
plt.plot(signal_II[0:10000])  # Ajusta el rango si es necesario
plt.title("Señal ECG - Derivación II")

plt.subplot(2, 1, 2)  # Crea un subplot para la señal V5
plt.plot(signal_V5[0:10000]) # Ajusta el rango si es necesario
plt.title("Señal ECG - Dericación V5")

plt.tight_layout()  # Ajusta el espaciado entre los subplots
plt.savefig(f"{full_path}/Leads_II_V5.png")
plt.close()

###########################################################
## Almacenar los picos del lead-II
# Store the peaks
t_peaks_II = waves_peak_II['ECG_T_Peaks']
p_peaks_II = waves_peak_II['ECG_P_Peaks']
q_peaks_II = waves_peak_II['ECG_Q_Peaks']
s_peaks_II = waves_peak_II['ECG_S_Peaks']

# Remove nan values from peak lists before indexing
t_peaks_II = [x for x in t_peaks_II if not np.isnan(x)]
p_peaks_II = [x for x in p_peaks_II if not np.isnan(x)]
q_peaks_II = [x for x in q_peaks_II if not np.isnan(x)]
s_peaks_II = [x for x in s_peaks_II if not np.isnan(x)]

# Convert peak lists to integers for indexing
t_peaks_II = [int(x) for x in t_peaks_II]
p_peaks_II = [int(x) for x in p_peaks_II]
q_peaks_II = [int(x) for x in q_peaks_II]
s_peaks_II = [int(x) for x in s_peaks_II]

# Get the amplitudes of the different waves
t_peak_amplitudes_II = cleaned_ecg_II[t_peaks_II]
p_peak_amplitudes_II = cleaned_ecg_II[p_peaks_II]
q_peak_amplitudes_II = cleaned_ecg_II[q_peaks_II]
s_peak_amplitudes_II = cleaned_ecg_II[s_peaks_II]

## Almacenar los picos del lead-V5
# Store the peaks
t_peaks_V5 = waves_peak_V5['ECG_T_Peaks']
p_peaks_V5 = waves_peak_V5['ECG_P_Peaks']
q_peaks_V5 = waves_peak_V5['ECG_Q_Peaks']
s_peaks_V5 = waves_peak_V5['ECG_S_Peaks']

# Remove nan values from peak lists before indexing
t_peaks_V5 = [x for x in t_peaks_V5 if not np.isnan(x)]
p_peaks_V5 = [x for x in p_peaks_V5 if not np.isnan(x)]
q_peaks_V5 = [x for x in q_peaks_V5 if not np.isnan(x)]
s_peaks_V5 = [x for x in s_peaks_V5 if not np.isnan(x)]

# Convert peak lists to integers for indexing
t_peaks_V5 = [int(x) for x in t_peaks_V5]
p_peaks_V5 = [int(x) for x in p_peaks_V5]
q_peaks_V5 = [int(x) for x in q_peaks_V5]
s_peaks_V5 = [int(x) for x in s_peaks_V5]

# Get the amplitudes of the different waves
t_peak_amplitudes_V5 = cleaned_ecg_V5[t_peaks_V5]
p_peak_amplitudes_V5 = cleaned_ecg_V5[p_peaks_V5]
q_peak_amplitudes_V5 = cleaned_ecg_V5[q_peaks_V5]
s_peak_amplitudes_V5 = cleaned_ecg_V5[s_peaks_V5]

###########################################################
# Calculate intervals (in seconds) for lead-II
sampling_rate = 360  # Your sampling rate

# QRS intervals for lead-II
qrs_intervals_II = [(s_peaks_II[i] - q_peaks_II[i]) / sampling_rate for i in range(min(len(q_peaks_II), len(s_peaks_II)))]
pq_intervals_II = [(q_peaks_II[i] - p_peaks_II[i]) / sampling_rate for i in range(min(len(p_peaks_II), len(q_peaks_II)))]
qt_intervals_II = [(t_peaks_II[i] - q_peaks_II[i]) / sampling_rate for i in range(min(len(q_peaks_II), len(t_peaks_II)))]
st_intervals_II = [(t_peaks_II[i] - s_peaks_II[i]) / sampling_rate for i in range(min(len(s_peaks_II), len(t_peaks_II)))]
# QRS intervals for lead-V5
qrs_intervals_V5 = [(s_peaks_V5[i] - q_peaks_V5[i]) / sampling_rate for i in range(min(len(q_peaks_V5), len(s_peaks_V5)))]
pq_intervals_V5 = [(q_peaks_V5[i] - p_peaks_V5[i]) / sampling_rate for i in range(min(len(p_peaks_V5), len(q_peaks_V5)))]
qt_intervals_V5 = [(t_peaks_V5[i] - q_peaks_V5[i]) / sampling_rate for i in range(min(len(q_peaks_V5), len(t_peaks_V5)))]
st_intervals_V5 = [(t_peaks_V5[i] - s_peaks_V5[i]) / sampling_rate for i in range(min(len(s_peaks_V5), len(t_peaks_V5)))]

###########################################################
##### Store the R-peaks for lead-II
r_peaks_II = info_II["ECG_R_Peaks"]
# Remove nan values from peak lists and convert to integers
def clean_peaks(peaks):
    peaks = [x for x in peaks if not np.isnan(x)]
    peaks = [int(x) for x in peaks]
    return peaks

# Remove nan values and convert to integers
r_peaks_II = clean_peaks(r_peaks_II)
# Calculate RR intervals (in seconds) for lead-II
rr_intervals_II = [(r_peaks_II[i + 1] - r_peaks_II[i]) / sampling_rate for i in range(len(r_peaks_II) - 1)]

##### Store the R-peaks for lead-V5
r_peaks_V5 = info_V5["ECG_R_Peaks"]
# Remove nan values and convert to integers
r_peaks_V5 = clean_peaks(r_peaks_V5)
# Calculate RR intervals (in seconds) for lead-V5
rr_intervals_V5 = [(r_peaks_V5[i + 1] - r_peaks_V5[i]) / sampling_rate for i in range(len(r_peaks_V5) - 1)]

###########################################################
# Calculate time between first R-peak and start of signal
time_to_first_r_peak_II = r_peaks_II[0] / sampling_rate  # Time in seconds
time_to_first_r_peak_V5 = r_peaks_V5[0] / sampling_rate

###########################################################
import pandas as pd

# Create a list of dictionaries to store the data
data = []
num_heartbeats = min(len(rr_intervals_II), len(rr_intervals_V5))  # Número de latidos a considerar

for i in range(num_heartbeats):
    data_row = {}  # Diccionario para almacenar los datos de un latido

    # Datos del Lead II
    data_row["0_pre-RR"] = (time_to_first_r_peak_II * 1000) if i == 0 else (rr_intervals_II[i - 1] * 1000)
    data_row["0_post-RR"] = (rr_intervals_II[i] * 1000)
    data_row["0_pPeak"] = p_peak_amplitudes_II.iloc[i] if i < len(p_peak_amplitudes_II) else None
    data_row["0_tPeak"] = t_peak_amplitudes_II.iloc[i] if i < len(t_peak_amplitudes_II) else None
    data_row["0_rPeak"] = r_peak_amplitudes_II.iloc[i] if i < len(r_peak_amplitudes_II) else None
    data_row["0_sPeak"] = s_peak_amplitudes_II.iloc[i] if i < len(s_peak_amplitudes_II) else None
    data_row["0_qPeak"] = q_peak_amplitudes_II.iloc[i] if i < len(q_peak_amplitudes_II) else None
    data_row["0_qrs_interval"] = (qrs_intervals_II[i] * 100) if i < len(qrs_intervals_II) else None
    data_row["0_pq_interval"] = (pq_intervals_II[i] * 100) if i < len(pq_intervals_II) else None
    data_row["0_qt_interval"] = (qt_intervals_II[i] * 100) if i < len(qt_intervals_II) else None
    data_row["0_st_interval"] = (st_intervals_II[i] * 100) if i < len(st_intervals_II) else None

    # Datos del Lead V5
    data_row["1_pre-RR"] = (time_to_first_r_peak_V5 * 1000) if i == 0 else (rr_intervals_V5[i - 1] * 1000)
    data_row["1_post-RR"] = rr_intervals_V5[i]
    data_row["1_pPeak"] = p_peak_amplitudes_V5.iloc[i] if i < len(p_peak_amplitudes_V5) else None
    data_row["1_tPeak"] = t_peak_amplitudes_V5.iloc[i] if i < len(t_peak_amplitudes_V5) else None
    data_row["1_rPeak"] = r_peak_amplitudes_V5.iloc[i] if i < len(r_peak_amplitudes_V5) else None
    data_row["1_sPeak"] = s_peak_amplitudes_V5.iloc[i] if i < len(s_peak_amplitudes_V5) else None
    data_row["1_qPeak"] = q_peak_amplitudes_V5.iloc[i] if i < len(q_peak_amplitudes_V5) else None
    data_row["1_qrs_interval"] = (qrs_intervals_V5[i] * 100) if i < len(qrs_intervals_V5) else None
    data_row["1_pq_interval"] = (pq_intervals_V5[i] * 100) if i < len(pq_intervals_V5) else None
    data_row["1_qt_interval"] = (qt_intervals_V5[i] * 100) if i < len(qt_intervals_V5) else None
    data_row["1_st_interval"] = (st_intervals_V5[i] * 100) if i < len(st_intervals_V5) else None

    data.append(data_row)  # Agregar el diccionario a la lista data

# Crear DataFrame y guardar en CSV
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv(f"{full_path}/ecg_data_testII_V5.csv", index=False)  # Set index=False to avoid writing row numbers
