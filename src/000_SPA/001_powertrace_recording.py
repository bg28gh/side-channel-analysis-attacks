import scope_api, square_and_multiply_api
import scipy.signal as signal
import matplotlib.pyplot as plt
"""
Use scope_api.py in combination with modular_exponentiation_api.py to record and extract power traces automatically:
	1. Keep the configuration (vertical, horizontal and trigger setup) from the previous subtask
	2. Arm the scope (scope_api.py)
	3. Request MODEXP (modular_exponentiation_api.py)
	4. Wait until the scope gets triggered (scope_api.py)
	5. Download the power trace (i.e. the samples) presented on the scope screen (scope_api.py)
	6. Store the power trace
"""

def main():
	scope = scope_api.open_scope()
	sqm = square_and_multiply_api.SquareAndMultiplyAPI("COM5")

	print("Arming osciloscoope")
	scope.arm()
	print("Launching Modular Exponentation")
	sqm.modexp()

	while True:
		if scope.triggered():
			break
	print("Getting samples")
	traces = scope.get_samples(2)
	lenDecimated = len(traces)
	for i, trace in enumerate(traces):
		print(f"\rPlotting... {i}/{lenDecimated}", end = "")
		plt.plot(trace)
	plt.title("Extracted Traces")
	plt.show()
    

if __name__ == '__main__':
    main()
