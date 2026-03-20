import decipher_api, scope_api, os, pickle
"""
Use scope_api.py in combination with the encipher_api.py to record and extract N Power Traces automatically.
Don’t forget that power traces need to be stored with some context for later analysis (i.e. input and output).
The procedure of collecting N power traces goes as:
1. Keep the configuration (vertical resolution, horizontal resolution and trigger setup) from the previous subtask
2. Do the following N times:
	a. Generate uniformly random distributed plaintext
	b. Set the plaintext (encipher_api.py)
	c. Arm the scope (scope_api.py)
	d. Request encryption (encipher_api.py)
	e. Wait until the scope gets triggered (scope_api.py)
	f. Download the Power Trace (scope_api.py)
	g. Request ciphertext (encipher_api.py)
3. Store all triples of (plaintexts, ciphertexts, power traces) for later analysis.
For this, chose an arbitrary format you like to work with.
If you cannot think about something reasonable, you could, e.g., refer to Python’s pickle library.
After serializing also attempt to deserialize to make sure you have stored the correct data.
"""

def main(iterations = 10000, channel = 1):
	dec = decipher_api.DecipherAPI("COM4")
	scope = scope_api.open_scope()
	
	for s in range(10):
		all_data = []
		for i in range(s*10, int(iterations / 10 + s*10)):
			print(f"\rProgress: {i+1}", end="")
			#print(f"Beggining iteration number {i}")
			#print("Generating random state")
			state = os.urandom(16)
			#print("Setting the state")
			dec.set_state(state)
			#print("Arming the oscilloscope")
			scope.arm()
			#print("Armed")
			dec.decrypt()

			
			while True:
				if scope.triggered():
					#print("Signal recieved")
					break
			
			trace = scope.get_samples(channel)
			cleartext = dec.get_state()

			all_data.append((state, trace, cleartext))
		
		filename = f"resultsf{s}.pkl"

		print(f"\nSaving iteration {iterations / 10 * (s + 1)}")
		with open(filename, 'wb') as f:
			pickle.dump(all_data, f)

		with open(filename, 'rb') as f:
			saved_data = pickle.load(f)
			if not all_data[-1] in saved_data:
				raise Exception
		saved_data = []

	combined_data = []

	for i in range(10):
		filename = f'result{i}.pkl'
		
		if os.path.exists(filename):
			try:
				with open(filename, 'rb') as f:
					data = pickle.load(f)
					combined_data.extend(data)
			except Exception as e:
				print(f"Error al leer {filename}: {e}")

	combined_filename = 'combined_results.pkl'
	try:
		with open(combined_filename, 'wb') as f:
			pickle.dump(combined_data, f)
		print(f"Combined data saved in {combined_filename}")
	except Exception as e:
		print(f"Error combining data: {e}")
			

if __name__ == '__main__':
	main(iterations = 5000, channel = 1)
