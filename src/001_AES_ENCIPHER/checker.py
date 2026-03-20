import pickle

with open("combined_results.pkl", 'rb') as f:
    data = pickle.load(f)
    for i, elemento in  enumerate(data):
        if len(elemento[1]) == 0:
            print(f"cagaste{i}")
        