"""
Perform Correlation Power Analysis to disclose the secret key, as discussed in the lecture.
Do not forget to annotate your implementation with comments and describe what you have been doing in the lab report.
Plots depicting your analysis results should be included in the report and should be explained.
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle

# Pickle file reading
def load_data(archivo_pickle):
    with open(archivo_pickle, 'rb') as f:
        data = pickle.load(f)
        # Exclude empty traces
        datos_filtrados = [(np.array(traces, dtype=np.float32), cipher_text) for _, traces, cipher_text in data if traces]
        traces, cipher_texts = zip(*datos_filtrados)
    
# Load data
traces, textos_cifrados = load_data('combined_results.pkl')
    
num_traces, num_points = traces.shape

# Create an array to store correlation values for each hypothesis
hypotheses = np.zeros((256, num_points))

# Perform CPA hypothesis testing
for byte_hypothesis in range(256):
    for point_index in range(num_points):
        # Extract the hypothetical intermediate result for the byte hypothesis
        intermediate_result_hypothesis = byte_hypothesis

        # Extract the power trace at the specified point
        power_trace_point = traces[:, point_index]

        # Compute correlation between power trace and hypothesized intermediate result
        correlation = np.corrcoef(power_trace_point, intermediate_result_hypothesis)[0, 1]

        # Accumulate correlation for each hypothesis and point
        hypotheses[byte_hypothesis, point_index] = correlation

# Identify the byte with maximum correlation for each point
key_bytes = np.argmax(hypotheses, axis=0)

# Display the results (plotting and reporting)
plt.figure(figsize=(10, 6))
for point_index in range(num_points):
    plt.plot(hypotheses[:, point_index], label=f'Point {point_index}')

plt.xlabel("Hypothesized Byte Value")
plt.ylabel("Correlation with Power Trace")
plt.title("Correlation Power Analysis Results for Each Point")
plt.legend()
plt.show()

# Display the potential key bytes for each point
print("Potential key bytes for each point:", key_bytes)

