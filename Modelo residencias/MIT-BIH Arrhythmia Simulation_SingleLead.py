################################################
#                   Listo                      #
################################################

# Load NeuroKit and other useful packages
import neurokit2 as nk
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [15, 9]

# Simulate 30 seconds of ECG Signal (recorded at 250 samples / second)
ecg_signal = nk.ecg_simulate(duration=30, sampling_rate=360)

# Automatically process the (raw) ECG signal
signals, info = nk.ecg_process(ecg_signal, sampling_rate=360)

# Extract clean ECG and R-peaks location
rpeaks = info["ECG_R_Peaks"]
cleaned_ecg = signals["ECG_Clean"]

valid_indices = rpeaks[rpeaks < len(cleaned_ecg)]
r_peak_amplitudes = cleaned_ecg[valid_indices]

###################################################
# Guarda la gráfica con los picos R en la señal ECG
# Visualize R-peaks in ECG signal
plot = nk.events_plot(rpeaks, cleaned_ecg)

plt.xlim(0, 5000)
plt.plot([], [], 'ro', label="R peaks")
plt.legend() 
plt.savefig("C:/Users/HP/Documents/2024/Itesco/ECG_Sim/R_Peak.png")
plt.close()
###################################################

# Delineate the ECG signal
_, waves_peak = nk.ecg_delineate(ecg_signal, rpeaks, sampling_rate=360, method="peak")

###################################################
# Zooming into the first 3 R-peaks, with focus on T_peaks, P-peaks, Q-peaks and S-peaks
plot = nk.events_plot([waves_peak['ECG_T_Peaks'][:3], 
                       waves_peak['ECG_P_Peaks'][:3],
                       waves_peak['ECG_Q_Peaks'][:3],
                       waves_peak['ECG_S_Peaks'][:3]], ecg_signal[:1500])

plt.savefig("C:/Users/HP/Documents/2024/Itesco/ECG_Sim/TPQS_Peaks.png")
plt.close()
###################################################

plot = nk.events_plot([rpeaks[:3],
                       waves_peak['ECG_T_Peaks'][:3], 
                       waves_peak['ECG_P_Peaks'][:3],
                       waves_peak['ECG_Q_Peaks'][:3],
                       waves_peak['ECG_S_Peaks'][:3]], ecg_signal[:1500])
plt.savefig("C:/Users/HP/Documents/2024/Itesco/ECG_Sim/RTPQS_Peaks.png")
plt.close()
###################################################

# Store the peaks
t_peaks = waves_peak['ECG_T_Peaks']
p_peaks = waves_peak['ECG_P_Peaks']
q_peaks = waves_peak['ECG_Q_Peaks']
s_peaks = waves_peak['ECG_S_Peaks']

# Remove nan values from peak lists before indexing
t_peaks = [x for x in t_peaks if not np.isnan(x)]
p_peaks = [x for x in p_peaks if not np.isnan(x)]
q_peaks = [x for x in q_peaks if not np.isnan(x)]
s_peaks = [x for x in s_peaks if not np.isnan(x)]

# Convert peak lists to integers for indexing
t_peaks = [int(x) for x in t_peaks]
p_peaks = [int(x) for x in p_peaks]
q_peaks = [int(x) for x in q_peaks]
s_peaks = [int(x) for x in s_peaks]

# Get the amplitudes of the different waves
t_peak_amplitudes = cleaned_ecg[t_peaks]
p_peak_amplitudes = cleaned_ecg[p_peaks]
q_peak_amplitudes = cleaned_ecg[q_peaks]
s_peak_amplitudes = cleaned_ecg[s_peaks]

# Calculate intervals (in seconds)
sampling_rate = 360  # Your sampling rate

# QRS interval
qrs_intervals = [(s_peaks[i] - q_peaks[i]) / sampling_rate for i in range(min(len(q_peaks), len(s_peaks)))]

# PQ interval
pq_intervals = [(q_peaks[i] - p_peaks[i]) / sampling_rate for i in range(min(len(p_peaks), len(q_peaks)))]

# QT interval
qt_intervals = [(t_peaks[i] - q_peaks[i]) / sampling_rate for i in range(min(len(q_peaks), len(t_peaks)))]

# ST interval
st_intervals = [(t_peaks[i] - s_peaks[i]) / sampling_rate for i in range(min(len(s_peaks), len(t_peaks)))]

# Store the R-peaks
r_peaks = info["ECG_R_Peaks"]

# Remove nan values from peak lists and convert to integers
def clean_peaks(peaks):
    peaks = [x for x in peaks if not np.isnan(x)]
    peaks = [int(x) for x in peaks]
    return peaks

# Remove nan values and convert to integers
r_peaks = clean_peaks(r_peaks)

# Calculate RR intervals (in seconds)
sampling_rate = 360  # Your sampling rate
rr_intervals = [(r_peaks[i + 1] - r_peaks[i]) / sampling_rate for i in range(len(r_peaks) - 1)]

# Calculate time between first R-peak and start of signal
time_to_first_r_peak = r_peaks[0] / sampling_rate  # Time in seconds

import pandas as pd

# Create a list of dictionaries to store the data
data = []
for i in range(len(rr_intervals)):
    data.append({
        "Pre-RR": time_to_first_r_peak if i == 0 else rr_intervals[i - 1],  # Use time_to_first_r_peak for the first row
        "Post-RR": rr_intervals[i],
        "P-peak": p_peak_amplitudes.iloc[i] if i < len(p_peak_amplitudes) else None,  # Handle cases where peak lists have different lengths
        "T-Peak": t_peak_amplitudes.iloc[i] if i < len(t_peak_amplitudes) else None,
        "R-Peak": r_peak_amplitudes.iloc[i] if i < len(r_peak_amplitudes) else None,
        "S-Peak": s_peak_amplitudes.iloc[i] if i < len(s_peak_amplitudes) else None,
        "Q-Peak": q_peak_amplitudes.iloc[i] if i < len(q_peak_amplitudes) else None,
        "QRS-interval": qrs_intervals[i] if i < len(qrs_intervals) else None,
        "PQ-Interval": pq_intervals[i] if i < len(pq_intervals) else None,
        "QT-Interval": qt_intervals[i] if i < len(qt_intervals) else None,
        "ST-Interval": st_intervals[i] if i < len(st_intervals) else None,
    })


# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Export the DataFrame to a CSV file
df.to_csv("C:/Users/HP/Documents/2024/Itesco/ECG_Sim/ecg_data_test2.csv", index=False)  # Set index=False to avoid writing row numbers