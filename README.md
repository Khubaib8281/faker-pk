# 🇵🇰 faker-pk
<<<<<<< HEAD

faker-pk is a Python library that generates realistic Pakistani data for testing, demos, datasets, and development.  
It includes names, CNICs, phone numbers, addresses, bank info, company details, jobs, salaries, and more.  
It also provides full support as a Faker provider so you can integrate it directly into the Faker ecosystem.
=======
![PyPI downloads](https://img.shields.io/pypi/dm/faker-pk)\
**faker-pk** is a lightweight Python library that generates **fake Pakistani data** — including names, CNICs, phone numbers, cities, and addresses — for testing, demos, and development purposes.

It’s designed for developers who want **realistic-looking Pakistani data** in their applications or ML datasets.
>>>>>>> 897d9def49723d8647963d7de9780c184b5258da

---

## Why Use faker-pk?

Developers working with Pakistani applications often struggle with:

- Generating realistic user data  
- Testing CNIC and phone formats  
- Filling databases with sample business information  
- Creating synthetic datasets  
- Running demos without exposing real personal data  

faker-pk solves this by providing structured, validated, Pakistan-focused fake data.

---

## 📦 Installation

```bash
pip install faker-pk
```

Upgrade:

```bash
pip install --upgrade faker-pk
```

---

# Quick Usage (FakerPK Class)

```python
from faker_pk import FakerPK

fake = FakerPK()

print(fake.male_name())
print(fake.cnic())
print(fake.phone_number())
print(fake.full_address())
print(fake.company_name())
```

---

# 🧩 All Attributes & Functions

Below is the full API that faker-pk generates.

---

## 👤 Personal Information

| Function | Description | Example |
|---------|-------------|---------|
| `male_name(count=1)` | Pakistani male names | `"Bilal Khan"` |
| `female_name(count=1)` | Pakistani female names | `"Ayesha Malik"` |
| `cnic(count=1)` | Valid CNIC format `xxxxx-xxxxxxx-x` | `"35201-6543210-7"` |
| `phone_number(count=1)` | Pakistani mobile format | `+923041234567` |
| `sim_provider(count=1)` | Mobile network providers | `"Jazz"` |
| `caste(count=1)` | Castes used across Pakistan | `"Ansari"` |
| `sect(count=1)` | Religious sects | `"Sunni"` |
| `dob(count=1)` | Random date of birth | `"1998-05-14"` |

---

## 🏠 Address Information

| Function | Description | Example |
|---------|-------------|---------|
| `city(count=1)` | Cities in Pakistan | `"Karachi"` |
| `province(count=1)` | Pakistani provinces | `"Punjab"` |
| `full_address(count=1)` | Complete Pakistani address | `"House No. 45, Street 10, Lahore, Punjab, 54000"` |

---

## 🏢 Company & Business Information

| Function | Description | Example |
|---------|-------------|---------|
| `company_name(count=1)` | Random company names | `"TechWorks Pvt Ltd"` |
| `industry_name(count=1)` | Industries in Pakistan | `"Telecommunications"` |
| `bank_name(count=1)` | Pakistani banks | `"HBL"` |
| `iban(count=1)` | Pakistani IBAN format | `"PK36HABB0000001234567890"` |
| `salary(count=1, industry=industry)` | Salary estimates (industry-aware) | `95000` |

> Valid ```industry``` parameters that are considered:
- Information Technology   
- Finance
- Healthcare
- Education  
- Marketing & Media
- Government / Public Sector
- Engineering / Manufacturing
- Hospitality / Retail
- Entrepreneur / Startup
- Legal / Consulting

---

## 💼 Job Information

| Function | Description | Example |
|---------|-------------|---------|
| `job_title(count=1)` | Random job titles | `"Software Engineer"` |
| `job_title_with_industry(count=1)` | Job title with industry | `"Finance Analyst – Banking"` |

---

## 🔁 Generating Multiple Items

```python
fake = FakerPK()
    
fake.city(3)
# ['Lahore', 'Islamabad', 'Multan']

fake.male_name(5)
# ['Ali Khan', 'Usman Raza', 'Zain Qureshi', 'Ahmed Farooq', 'Sami Shah']
```

---

# 🔌 Faker Provider Integration
   
faker-pk fully integrates with the Faker library via `FakerPKProvider`.

### ➤ Add Provider to Faker

```python
from faker import Faker
from faker_pk import FakerPKProvider

fake = Faker()
fake.add_provider(FakerPKProvider)

print(fake.pk_male_name())
print(fake.pk_cnic())
print(fake.pk_full_address())
```

### ➤ Provider Methods

| Provider Function | Description |
|------------------|-------------|
| `pk_male_name()` | Male name |
| `pk_female_name()` | Female name |
| `pk_cnic()` | CNIC |
| `pk_phone_number()` | Pakistani mobile number |
| `pk_sim_provider()` | Mobile network |
| `pk_caste()` | Caste |
| `pk_sect()` | Sect |
| `pk_dob()` | DOB |
| `pk_city()` | City |
| `pk_province()` | Province |
| `pk_full_address()` | Complete address |
| `pk_company_name()` | Company |
| `pk_industry_name()` | Industry |
| `pk_job_title()` | Industry-aware job title |
| `pk_job_title_with_industry()` | Combined title |
| `pk_salary(industry=industry)` | Salary range |
| `pk_bank_name()` | Bank |
| `pk_iban()` | IBAN |

---

<<<<<<< HEAD
# 🧪 Example Script

=======
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
   
>>>>>>> 897d9def49723d8647963d7de9780c184b5258da
```python
from faker_pk import FakerPK

fake = FakerPK()

for _ in range(3):
    print({
        "Name": fake.male_name(),
        "CNIC": fake.cnic(),
        "Phone": fake.phone_number(),
        "Address": fake.full_address(),
        "Company": fake.company_name(),  
        "Salary": fake.salary(industry="Information Technology")
    })
```

<<<<<<< HEAD
---

# 🛠️ Development
=======
**Output:**   
```
{'Name': 'Ali Raza', 'CNIC': '35201-6543210-7', 'Phone': '+923125678901', 'Address': 'House No. 12, Street No. 3, Islamabad, Islamabad, 44000', 'Company': 'Techworks'}
```

---   

## 🛠️ Development
  
Clone the repository and install locally:
>>>>>>> 897d9def49723d8647963d7de9780c184b5258da

```bash
git clone https://github.com/Khubaib8281/faker-pk.git
cd faker-pk
pip install -e .
```

---

# 🤝 Contributing

You can contribute by:

- Adding realistic datasets ( universities, etc.)
- Improving job industries and salaries
- Expanding address and bank coverage
- Adding validation utilities

Pull requests are welcome.

---

# 📄 License

MIT License.

---

# 👤 Author

**Muhammad Khubaib Ahmad**  
<<<<<<< HEAD
> **Email:** khubaib0.1ai@gmail.com  
> **GitHub:** https://github.com/Khubaib8281
=======
📧 [khubaib0.1ai@gmail.com](mailto:khubaib0.1ai@gmail.com)  
🌐 [GitHub: Khubaib8281](https://github.com/Khubaib8281)
🐍 [PYPI: Khubaib_01](https://pypi.org/project/faker-pk)
>>>>>>> 897d9def49723d8647963d7de9780c184b5258da

---

# ⭐ Support

If this project helps you, give it a star on GitHub!

> https://github.com/Khubaib8281/faker-pk
    