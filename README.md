# Side-Channel Analysis: DPA & CPA Attacks 🛡️⚡

This repository contains two detailed implementations of **Side-Channel Attacks (SCA)** on cryptographic systems. The project focuses on recovering secret keys from power consumption traces using statistical methods.

## 🚀 Project Overview
Side-channel attacks exploit information leaked by the physical implementation of an algorithm rather than weaknesses in the algorithm itself. In this project, I implemented two of the most powerful power analysis techniques:
* **DPA (Differential Power Analysis)**
* **CPA (Correlation Power Analysis)**

## 🧠 Implementations

### 1. CPA Attack (Correlation Power Analysis)
Uses the **Pearson Correlation Coefficient** to establish a relationship between a power model (Hamming Weight) and the actual power consumption traces.
* **Methodology:** Hypothesis testing across all 256 possible values for each key byte.
* **Tools:** `NumPy` for matrix operations and `SciPy` for statistical correlation.
* **Key Feature:** High efficiency in noisy environments by isolating the correct hypothesis through correlation peaks.

### 2. DPA Attack (Differential Power Analysis)
Uses statistical differences to leak information. By partitioning traces based on an intermediate bit's value, the secret key is revealed when the "difference of means" shows a significant spike.
* **Methodology:** Implementation of selection functions and bit-level partitioning.
* **Signal Processing:** Applied **Gaussian filters** (`gaussian_filter1d`) and **Median filters** (`medfilt`) to clean power traces and improve the signal-to-noise ratio.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Libraries:** * `NumPy`: For high-performance array manipulation.
    * `Matplotlib`: For visualizing power traces and correlation results.
    * `SciPy`: For statistical analysis and signal processing.
    * `Cryptography`: For handling AES primitives and ciphertext verification.

## 📁 Repository Structure
* `CPA_Notebook.ipynb`: Detailed walkthrough and implementation of the Correlation Power Analysis.
* `DPA_notebook.ipynb`: Step-by-step implementation of the Differential Power Analysis.

---
> **⚠️ Confidentiality Note:**
> Some datasets or specific hardware-specific parameters might be omitted or simplified due to academic confidentiality agreements. The logic and methodology remain fully transparent for review.

*Developed as part of the Hardware Security curriculum at TU Berlin.*
