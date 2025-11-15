import random   

COMPANIES = [
    "Tech Solutions", "Global Enterprises", "NexGen Software", "Bright Future Ltd",
    "Innovatech", "Pak Logistics", "Star Industries", "FutureTech Labs", "NextEra Solutions",
    "Digital Horizons", "GreenField Enterprises", "Alpha Systems", "Skyline Technologies",
    "Visionary Solutions", "Prime Consulting", "BlueWave Software", "Omega Solutions",
    "Sunrise Industries", "Quantum Tech", "Everest Solutions", "Peak Dynamics",
    "Galaxy Enterprises", "Crescent Innovations", "Summit Tech", "Aurora Systems",
    "Infinity Solutions", "Pioneer Technologies", "Vertex Labs", "NextGen Analytics",
    "Momentum Solutions", "Nova Systems", "Titan Tech", "Elite Software", "GlobalTech",
    "Fusion Enterprises", "Legacy Solutions", "Vortex Innovations", "Ascend Tech",
    "CoreLogic", "Hyperion Labs", "Luminous Software", "EverTech", "Matrix Solutions",
    "Sapphire Systems", "Digital Minds", "Vertex Solutions", "Zenith Tech", "Precision Labs",
    "Altair Enterprises", "Phoenix Systems"
]

BANKS = [
    "Habib Bank", "MCB Bank", "UBL", "Bank Alfalah", "Standard Chartered", "Allied Bank", "Meezan Bank", "Bank of Punjab", "HBL"
]
  
def bank_name():
    return random.choice(BANKS)

def iban():
    # Basic mock IBAN: PK + 2-digit checksum + 4-digit bank code + random 16 digits
    return f"PK{random.randint(10,99)}{random.randint(1000,9999)}{random.randint(10**15,10**16-1)}"
    
def company_name():   
    return random.choice(COMPANIES)


# Industries
INDUSTRIES = [
    "Information Technology", "Finance", "Healthcare", "Education",
    "Marketing & Media", "Government / Public Sector", "Engineering / Manufacturing",
    "Hospitality / Retail", "Entrepreneur / Startup", "Legal / Consulting"
]

# Job titles mapped to industries

JOB_TITLE_MAPPING = {
    "Information Technology": [
        "Software Engineer", "Frontend Developer", "Backend Developer",
        "Full Stack Developer", "DevOps Engineer", "Data Scientist",
        "Machine Learning Engineer", "AI Researcher", "Cybersecurity Engineer",
        "Cloud Solutions Architect", "Mobile App Developer", "Blockchain Developer",
        "QA / Test Engineer", "UI/UX Designer", "Network Engineer", "Database Administrator",
        "IT Support Specialist", "Systems Analyst"
    ],
    "Finance": [
        "Accountant", "Auditor", "Financial Analyst", "Investment Analyst",
        "Tax Consultant", "Risk Manager", "Credit Analyst", "Loan Officer",
        "Treasury Manager", "Financial Controller"
    ],
    "Healthcare": [
        "Doctor", "Nurse", "Pharmacist", "Lab Technician", "Radiologist",
        "Medical Researcher", "Physiotherapist", "Dietitian", "Surgeon", "Psychologist"
    ],
    "Education": [
        "Teacher", "Lecturer", "Professor", "Research Associate", 
        "Academic Coordinator", "Curriculum Designer", "Educational Consultant"
    ],
    "Marketing & Media": [
        "Graphic Designer", "Content Writer", "Copywriter", "Video Editor",
        "Animator", "Photographer", "Digital Marketing Specialist",
        "Social Media Manager", "Art Director", "Marketing Manager", "Sales Executive"
    ],
    "Government / Public Sector": [
        "Civil Servant", "Policy Analyst", "Administrative Officer",
        "Diplomat", "Law Enforcement Officer", "Urban Planner"
    ],
    "Engineering / Manufacturing": [
        "Civil Engineer", "Mechanical Engineer", "Electrical Engineer",
        "Chemical Engineer", "Industrial Engineer", "Production Manager",
        "Quality Assurance Engineer"
    ],
    "Hospitality / Retail": [
        "Hotel Manager", "Chef", "Waiter", "Waitress", "Store Manager",
        "Sales Associate", "Customer Service Representative"
    ],
    "Entrepreneur / Startup": [
        "Entrepreneur", "Startup Founder", "Business Development Manager",
        "Operations Manager", "Strategy Analyst", "Consultant"
    ],
    "Legal / Consulting": [
        "Legal Advisor", "Lawyer", "Advocate", "Compliance Officer", "Consultant"
    ]
}

# Functions

def job_title(industry=None):
    """
    Return a random job title. If industry is specified, choose from that industry.
    """
    if industry:
        if industry not in JOB_TITLE_MAPPING:
            raise ValueError(f"Industry '{industry}' not found.")
        return random.choice(JOB_TITLE_MAPPING[industry])
    # Randomly pick an industry first
    selected_industry = random.choice(list(JOB_TITLE_MAPPING.keys()))
    return random.choice(JOB_TITLE_MAPPING[selected_industry])


def job_title_with_industry():
    """
    Return a tuple of (job_title, industry) for consistency.
    """
    selected_industry = random.choice(list(JOB_TITLE_MAPPING.keys()))
    title = random.choice(JOB_TITLE_MAPPING[selected_industry])
    return title, selected_industry

def industry_name():
    return random.choice(INDUSTRIES)

def salary(industry=None):
    """
    Generate a random salary in PKR based on industry rough ranges.
    """
    # Rough salary ranges (monthly PKR)
    ranges = {
        "Information Technology": (50000, 250000),
        "Finance": (40000, 200000),
        "Healthcare": (30000, 180000),
        "Education": (25000, 120000),
        "Marketing & Media": (30000, 150000),
        "Government / Public Sector": (25000, 120000),
        "Engineering / Manufacturing": (35000, 180000),
        "Hospitality / Retail": (20000, 100000),
        "Entrepreneur / Startup": (50000, 300000),
        "Legal / Consulting": (40000, 200000)
    }  

    if industry and industry in ranges:
        low, high = ranges[industry]
    else:
        low, high = random.choice(list(ranges.values()))

    return random.randint(low, high)     