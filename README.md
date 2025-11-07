# 🇵🇰 faker-pk

**faker-pk** is a lightweight Python library that generates **fake Pakistani data** — including names, CNICs, phone numbers, cities, and addresses — for testing, demos, and development purposes.

It’s designed for developers who want **realistic-looking Pakistani data** in their applications or ML datasets.

---

## 🧩 Installation

Install directly from PyPI:

```bash
pip install faker-pk
```

Or upgrade to the latest version:

```bash
pip install --upgrade faker-pk
```

---

## ⚡ Quick Start

```python
from faker_pk import FakerPK

fake = FakerPK()

print(fake.male_name())       # "Bilal Khan"
print(fake.female_name())     # "Ayesha Malik"
print(fake.cnic())            # "37405-7654321-9"
print(fake.phone_number())    # "+923001234567"
print(fake.city())            # "Lahore"
print(fake.province())        # "Punjab"
print(fake.full_address())    # "House No. 45, Street No. 6, Karachi, Sindh, 75000"
print(fake.company_name())    # "Tech Solutions"
```

---

## 🔁 Generate Multiple Entries

You can generate a list of fake entries by passing an integer count:

```python
fake.male_name(5)
# ['Ali Khan', 'Usman Raza', 'Zain Qureshi', 'Ahmed Farooq', 'Sami Shah']

fake.city(3)
# ['Lahore', 'Islamabad', 'Multan']
```

---

## 🧠 Features

- Realistic Pakistani male and female names  
- Valid CNIC format (`xxxxx-xxxxxxx-x`)  
- Pakistani-style phone numbers (`+92xxxxxxxxxx`)  
- Cities and provinces from real data  
- Randomized company and address generation  
- Easy to extend for your own data sources  

---

## 🧩 API Reference

| Function | Description | Example Output |
|-----------|--------------|----------------|
| `male_name(count=1)` | Generates one or more male names | `['Ali Khan']` |
| `female_name(count=1)` | Generates one or more female names | `['Ayesha Malik']` |
| `cnic(count=1)` | Generates valid CNIC numbers | `['37405-1234567-8']` |
| `phone_number(count=1)` | Generates Pakistani phone numbers | `['+923001234567']` |
| `city(count=1)` | Returns cities from Pakistan | `['Karachi']` |
| `province(count=1)` | Returns Pakistani provinces | `['Sindh']` |
| `full_address(count=1)` | Returns complete fake addresses | `['House No. 23, Street No. 8, Lahore, Punjab, 54000']` |
| `company_name(count=1)` | Returns random company names | `['TechNova Pvt Ltd']` |

---

## 🧪 Example Script

```python
from faker_pk import FakerPK

fake = FakerPK()  

for _ in range(3):
    print({
        "Name": fake.male_name(),
        "CNIC": fake.cnic(),
        "Phone": fake.phone_number(),
        "Address": fake.full_address(),
        "Company": fake.company_name()
    })
```

**Output:**   
```
{'Name': 'Ali Raza', 'CNIC': '35201-6543210-7', 'Phone': '+923125678901', 'Address': 'House No. 12, Street No. 3, Islamabad, Islamabad, 44000', 'Company': 'Techworks'}
```

---

## 🛠️ Development

Clone the repository and install locally:

```bash
git clone https://github.com/Khubaib8281/faker-pk.git
cd faker-pk
pip install -e .
```

---

## 🚀 Contributing

Contributions are welcome!  
If you’d like to add more realistic datasets (Pakistani districts, universities, etc.), submit a pull request.

---

## 🧾 License

This project is licensed under the **MIT License**.

---

## 👤 Author

**Muhammad Khubaib Ahmad**  
📧 [khubaib0.1ai@gmail.com](mailto:khubaib0.1ai@gmail.com)  
🌐 [GitHub: Khubaib8281](https://github.com/Khubaib8281)

---

## ⭐ Support

If you find this library useful, consider giving it a **star** on GitHub to support development!

👉 [https://github.com/Khubaib8281/faker-pk](https://github.com/Khubaib8281/faker-pk)
