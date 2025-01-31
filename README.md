# 📝 Shreelipi to Unicode Converter

This Python script converts **Kannada text from Shreelipi encoding to Unicode**. It processes an input text file, maps **Shreelipi characters** to their **Unicode equivalents**, and outputs the converted text.

---

## 🚀 Features

✅ **Shreelipi to Unicode Conversion** – Converts Kannada text from **Shreelipi encoding** to **Unicode**.  
✅ **Ambiguous Character Handling** – Properly resolves multiple mappings for ambiguous characters.  
✅ **Supports Special Characters** – Processes Kannada-specific ligatures and diacritics.  
✅ **Handles Ottakshara & Arka Letters** – Corrects character positioning for complex Kannada text.  
✅ **Batch Processing** – Reads from an input file and converts the entire text efficiently.  

---

## 🛠 Requirements

- **Python 3.x**  
- **shreelipi_map.py** (A character mapping file containing Shreelipi-to-Unicode mappings)  

To install dependencies (if needed):
```bash
pip install sys
```

---

## 📥 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YathishPoojary98/Shreelipi-to-Unicode-Kannada-Converter.git
```

Navigate into the cloned directory:
```bash
cd Shreelipi-to-Unicode-Kannada-Converter
```

### 2️⃣ Run the Conversion Script

Ensure you have **shreelipi_map.py** available, then execute:

```bash
python shreelipi_to_unicode.py input.txt > output.txt
```

- `input.txt` – The file containing **Shreelipi encoded text**.  
- `output.txt` – The file where the **converted Unicode text** will be saved.  

---

## 🎯 How It Works

1️⃣ **Reads the input text file** containing **Shreelipi encoded text**.  
2️⃣ **Maps each character** from Shreelipi to its **Unicode equivalent**.  
3️⃣ **Handles special cases** like ambiguous characters, ottakshara, and arka.  
4️⃣ **Reconstructs the text** with proper character alignment.  
5️⃣ **Outputs the Unicode text** to the console or a file.  

---

## 🔗 Related Projects

- **Unicode-Kannada-to-Shreelipi Converter** – [View Repository](https://github.com/YathishPoojary98/Unicode-Kannada-to-Shreelipi-Converter)

---
