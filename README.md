# Assignment-1 – TOPSIS Implementation

**Author:** Vanshika Saini  
**Roll No:** 102303735  

---

##  Project Description

This repository contains a Python implementation of the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** multi-criteria decision-making method.  
The solution is implemented as a **command-line program** as required in Assignment-1.

---

##  Repository Structure

```
.
├── topsis/
│   └── topsis.py        # Main TOPSIS implementation (CLI)
├── data.csv             # Sample input file
├── result.csv           # Output file
├── setup.py             # Package configuration
├── README.md            # Documentation
```

---

##  Requirements

- Python **3.8 or above**
- Required libraries:
  - `numpy`
  - `pandas`

---

##  How to Run (Windows / PowerShell)

### 1️⃣ Install required libraries

```bash
pip install pandas numpy
```

---

### 2️⃣ Run TOPSIS from command line

```bash
python topsis/topsis.py data.csv "1,1,1,1" "+,+,+,+" result.csv
```

---

### 3️⃣ Output

After execution, the result will be saved in:

```
result.csv
```

The output file contains:
- **Topsis Score**
- **Rank** (higher score = better rank)

---

## ▶️ Running in Google Colab (Testing)

To run this project in **Google Colab**:

1. Upload all files (`topsis.py`, `data.csv`)
2. Install dependencies:
```python
!pip install pandas numpy
```
3. Run using:
```python
!python topsis/topsis.py data.csv "1,1,1,1" "+,+,+,+" result.csv
```

---

## 📑 Input File Format

- Input must be a **CSV file**
- Minimum **three columns**
- **First column**: Identifier (string)
- **Remaining columns**: Numeric criteria values only

Example:

```csv
Option,C1,C2,C3
A,250,16,12
B,200,12,8
C,300,18,11
```

---

## 🧮 Parameters Explanation

- **Weights**  
  Comma-separated numeric values  
  Example:
  ```
  1,1,1,1
  ```

- **Impacts**  
  Comma-separated symbols  
  - `+` → Benefit criterion  
  - `-` → Cost criterion  

  Example:
  ```
  +,+,+,+
  ```

---

##  Validation Rules

- Number of weights = number of criteria columns
- Number of impacts = number of criteria columns
- Impacts must be either `+` or `-`
- From the second column onward, values must be numeric

---

##  Conclusion

This project satisfies all requirements of **Assignment-1** by providing a validated, command-line-based implementation of the TOPSIS decision-making method.


