import random
from datetime import date, timedelta
    
MALE_NAMES = [
    "Ahmed", "Muhammad", "Ali", "Hassan", "Hussain", "Bilal", "Hamza", "Umar", "Usman", "Abdullah",
    "Abdul Rahman", "Abdul Rehman", "Abdul Basit", "Abdul Hadi", "Abdul Wahab", "Abdul Samad", "Abdul Qadir", "Abdul Majeed", "Abdul Rauf", "Abdul Aziz",
    "Abdul Kareem", "Abdul Aleem", "Abdul Ghaffar", "Abdul Ghani", "Abdul Haq", "Abdul Malik", "Abdul Shakoor", "Abdul Sattar", "Abdul Wasi", "Ahmad",
    "Zeeshan", "Danish", "Faizan", "Fahad", "Waleed", "Zain", "Saad", "Ahsan", "Adeel", "Asad",
    "Arsalan", "Shahzaib", "Shehryar", "Salman", "Noman", "Omer", "Tahir", "Talha", "Kashif", "Kamran",
    "Shahid", "Naveed", "Imran", "Junaid", "Farhan", "Faisal", "Khalid", "Raza", "Rizwan", "Adnan",
    "Arif", "Yasir", "Irfan", "Zubair", "Shayan", "Sameer", "Umair", "Huzaifa", "Ayaan", "Rayyan",
    "Azaan", "Areeb", "Raheel", "Sufyan", "Haris", "Anas", "Arham", "Asim", "Moiz", "Hashir",
    "Ibtisam", "Saif", "Ilyas", "Ismail", "Ibrahim", "Eesa", "Musa", "Yousuf", "Dawood", "Yunus",
    "Nuh", "Luqman", "Taimoor", "Murtaza", "Baqir", "Rayan", "Shahmeer", "Shaheer", "Daniyal", "Arsab",
    "Zarar", "Zaryab", "Aafaq", "Abrar", "Adil", "Amaan", "Amjad", "Anees", "Anwar", "Aqeel",
    "Arqam", "Arsal", "Asghar", "Ashar", "Atif", "Awais", "Ayaz", "Azhar", "Azlan", "Barkat",
    "Basim", "Babar", "Burhan", "Ehtisham", "Ehsan", "Faraz", "Farid", "Fawad", "Feroz", "Ghazanfar",
    "Haider", "Hammad", "Hamid", "Hasan", "Haseeb", "Hashim", "Hisham", "Huzaifah", "Ijaz", "Imad",
    "Inam", "Javed", "Kamal", "Khalil", "Khizar", "Mahad", "Mahir", "Mansoor", "Maaz", "Mazhar",
    "Mehdi", "Muneeb", "Mustafa", "Naeem", "Nouman", "Qasim", "Rameez", "Rehan", "Sadiq", "Safeer",
    "Saifullah", "Sarfaraz", "Shahbaz", "Shafqat", "Shafiq", "Sharjeel", "Shehzad", "Sohail", "Subhan", "Sultan",
    "Tabish", "Talal", "Tauseef", "Tufail", "Ubaid", "Umer", "Usama", "Wajid", "Waqas", "Wasif",
    "Yasir", "Yawar", "Yameen", "Yasin", "Zakariya", "Zaman", "Zawwar", "Zia", "Zohaib", "Zubair",
    "Zainul Abidin", "Irham", "Taha", "Irtaza", "Reza", "Ehtesham", "Mirza", "Azim", "Saqib", "Shabbir",
    "Tahseen", "Salman", "Fahim", "Jawad", "Sarmad", "Nabeel", "Faiq", "Rashid", "Rahim", "Habib",
    "Munir", "Zameer", "Akram", "Zafar", "Wasim", "Nauman", "Nasir", "Khalil", "Jibran", "Kashan",
    "Emaan", "Adi", "Fakhir", "Sibtain", "Farooq", "Saifur", "Faiz", "Nisar", "Salman", "Arqam",
    "Rifat", "Tahmid", "Zohair", "Zaeem", "Jawwad", "Sarmal", "Arsal", "Areez", "Rizq", "Sarim",
    "Zayyan", "Razaq", "Azfar", "Affan", "Hanzala", "Hammad", "Fuzail", "Ziyad", "Adeel", "Jameel",
    "Karim", "Qadeer", "Hanan", "Rameen", "Tahal", "Shahroz", "Saamir", "Tahaib", "Yasrab", "Ammar",
    "Shakir", "Rauf", "Sameel", "Tahseen", "Dani", "Azaib", "Hamdaan", "Maheer", "Uzair", "Sharif",
    "Zarrar", "Firas", "Azmat", "Riaz", "Munawwar", "Kaleem", "Sufyan", "Zameel", "Sajid", "Sarim",
    "Tabriz", "Yasin", "Aniq", "Rizal", "Zaid", "Irteza", "Aabid", "Zawar", "Aneeb", "Moazzam",
    "Fida", "Najam", "Tauqeer", "Shakeel", "Rashad", "Rameel", "Najeeb", "Basit", "Fawzan"
]

FEMALE_NAMES = [
    "Aaliya", "Aaminah", "Aamna", "Aaniya", "Aanisa", "Aasia", "Aasma", "Abida", "Adeela", "Adeelah",
    "Afifa", "Afsheen", "Afza", "Afreen", "Aisha", "Aiman", "Aina", "Aini", "Aiza", "Aleena",
    "Aleesha", "Aleya", "Aliya", "Alishba", "Amal", "Amara", "Amber", "Ameena", "Amira", "Anabia",
    "Anaya", "Anila", "Aniqa", "Anisa", "Anum", "Anusha", "Anzela", "Aqsa", "Arfa", "Arisha",
    "Arwa", "Asfa", "Asfiya", "Asma", "Asmara", "Atiya", "Ayesha", "Ayra", "Aysha", "Azka",
    "Azra", "Basma", "Batool", "Benish", "Bisma", "Bushra", "Dur-e-Fatima", "Dua", "Eeman", "Eesha",
    "Eiman", "Eliza", "Eman", "Emna", "Erum", "Esma", "Faiza", "Fakhra", "Falaq", "Falak",
    "Fariha", "Farisha", "Farwah", "Farzana", "Fatima", "Fauzia", "Fiza", "Ghazal", "Ghazala", "Gulnaz",
    "Gulrukh", "Habiba", "Hafsa", "Haleema", "Hania", "Hanin", "Hareem", "Haseena", "Hiba", "Hifza",
    "Hina", "Hira", "Humaira", "Humna", "Iffat", "Ifra", "Imaan", "Inaya", "Iqra", "Iram",
    "Irum", "Isha", "Ishaal", "Ishmal", "Isra", "Jameela", "Javeria", "Jannat", "Jasmin", "Jaweria",
    "Jiya", "Kainat", "Khadija", "Khadijah", "Khansa", "Kiran", "Komal", "Laiba", "Laila", "Laraib",
    "Lina", "Lubna", "Mahira", "Mahjabeen", "Mahnoor", "Mahrukh", "Maha", "Maliha", "Marium", "Maria",
    "Mariam", "Marwa", "Maryam", "Maheen", "Mehak", "Mehr", "Mehwish", "Minal", "Mishal", "Misbah",
    "Mona", "Mubashira", "Muqaddas", "Mysha", "Nabeela", "Nadia", "Nafisa", "Naila", "Najma", "Nashitah",
    "Natasha", "Naureen", "Nayyab", "Neha", "Nida", "Nimra", "Nishat", "Noreen", "Nosheen", "Nusrat",
    "Nuha", "Obaidah", "Parveen", "Qandeel", "Quratulain", "Rabiya", "Rabia", "Rafia", "Rafiya", "Rameen",
    "Rania", "Raniah", "Rashida", "Rida", "Rimsha", "Rizwana", "Roha", "Romana", "Roohi", "Ruba",
    "Rubina", "Rukhsar", "Rumaisa", "Ruqayya", "Saba", "Sabeen", "Sabahat", "Sadia", "Sadiaa", "Sadiya",
    "Safia", "Sahar", "Saira", "Sajida", "Sakina", "Salma", "Sameena", "Samina", "Samiya", "Sana",
    "Saniya", "Sanober", "Sara", "Sarah", "Sasha", "Shabana", "Shagufta", "Shaheen", "Shaista", "Shakila",
    "Shamaila", "Shamim", "Shanza", "Shazia", "Sheeba", "Shehnaz", "Shifa", "Shiza", "Sobia", "Sonia",
    "Subha", "Subhana", "Suhana", "Sumaira", "Sumaiya", "Sundus", "Tabinda", "Tabassum", "Taha", "Tahira",
    "Tahreem", "Tahirah", "Tania", "Tanisha", "Tanzeela", "Tayyaba", "Tehreem", "Tooba", "Ujala", "Umama",
    "Umayrah", "Ume Habiba", "Ume Hani", "Ume Kulsoom", "Umme Hani", "Umme Rubab", "Umme Salma", "Umaima", "Umairah", "Urooj",
    "Urwa", "Uzma", "Wajiha", "Warda", "Wardah", "Yasira", "Yasmeen", "Yumna", "Zainab", "Zakia",
    "Zainah", "Zahida", "Zahra", "Zaib", "Zakia", "Zakiaa", "Zameena", "Zareen", "Zarish", "Zarmeen",
    "Zarqa", "Zartaj", "Zaryab", "Zehra", "Zeenat", "Zia", "Zimal", "Zinia", "Zobia", "Zohra",
    "Zonaira", "Zoya", "Zubaida", "Zulekha", "Zunaira", "Zunisha", "Zunnoor", "Aamira", "Adeeba", "Areeba",
    "Armeen", "Arooba", "Asiya", "Aqleema", "Aqra", "Armina", "Asra", "Ayisha", "Azima", "Bareera",
    "Bushra", "Dania", "Daniah", "Dua", "Eimaan", "Elina", "Elaf", "Erum", "Esha", "Eshaal",
    "Fakhira", "Faria", "Fariyal", "Fawzia", "Fareeha", "Farheen", "Fizza", "Gulshan", "Gulzar", "Hadia",
    "Hajra", "Haleemah", "Hamna", "Haniyah", "Harema", "Huma", "Humera", "Huriya", "Inara", "Insha",
    "Iqra", "Irsa", "Ishaqueen", "Ishrat", "Jannat", "Jawaria", "Javeriya", "Kanza", "Khadeeja", "Khizra",
    "Komila", "Laiba", "Laila", "Lamees", "Mahgul", "Mahnoor", "Mahwish", "Maiza", "Mamoona", "Manahil",
    "Mariam", "Marrium", "Marjan", "Maryam", "Mehreen", "Mehrunisa", "Minal", "Mishka", "Mishaal", "Mishkaat",
    "Mona", "Muqaddas", "Myra", "Naheed", "Naila", "Nimrah", "Noreen", "Noshaba", "Nusrat", "Pari",
    "Parveen", "Qurat", "Rabi", "Rafia", "Ramsha", "Rania", "Rija", "Rimsha", "Rishma", "Roohi",
    "Romaisa", "Ruba", "Rukhsana", "Saba", "Sabiha", "Saeeda", "Sahar", "Sajida", "Sakina", "Salma",
    "Sameera", "Samra", "Sania", "Saniya", "Saniah", "Saniaa", "Sania", "Saniaa", "Saniah", "Samiha"
]
    
LAST_NAMES = [
    "Abbasi", "Abbas", "Abid", "Afzal", "Ahmad", "Ahmed", "Akbar", "Akhter", "Alam", "Ali",
    "Amjad", "Anjum", "Ansari", "Arif", "Asad", "Ashfaq", "Asghar", "Aslam", "Atif", "Awan",
    "Azam", "Azhar", "Babar", "Baig", "Bajwa", "Bakht", "Baloch", "Bangash", "Basit", "Batool",
    "Bhatti", "Bukhari", "Butt", "Chaudhry", "Cheema", "Chishti", "Dar", "Danish", "Daud", "Deen",
    "Durrani", "Ejaz", "Fahim", "Faheem", "Farid", "Farooq", "Farrukh", "Fazal", "Feroz", "Ghafoor",
    "Ghani", "Ghazanfar", "Ghaznavi", "Ghauri", "Ghulam", "Gohar", "Habib", "Hadi", "Hafeez", "Hafiz",
    "Haider", "Hameed", "Hamid", "Hanif", "Hashim", "Hasnain", "Hassan", "Hayat", "Hussain", "Hyder",
    "Iftikhar", "Ijaz", "Ilyas", "Imam", "Imran", "Inam", "Iqbal", "Irshad", "Ismail", "Ishaq",
    "Jadoon", "Jahangir", "Jamal", "Jamali", "Jamshed", "Javed", "Jawad", "Kabir", "Kadir", "Kaleem",
    "Kamran", "Kamil", "Karim", "Kashif", "Kazmi", "Khalid", "Khalil", "Khan", "Khizar", "Khurram",
    "Latif", "Mahmood", "Malik", "Manzoor", "Masood", "Mazhar", "Mehmood", "Mir", "Mirza", "Moin",
    "Mohsin", "Moinuddin", "Monis", "Mubashir", "Mujeeb", "Mukhtar", "Munir", "Murad", "Mustafa", "Murtaza",
    "Nadeem", "Naeem", "Naseem", "Nasir", "Nawaz", "Niaz", "Noor", "Noman", "Numan", "Obaid",
    "Qadir", "Qaiser", "Qamar", "Qasim", "Qayyum", "Qureshi", "Rafiq", "Rafique", "Rahim", "Raja",
    "Rameez", "Rana", "Rasheed", "Rashid", "Rauf", "Raza", "Razzaq", "Rehman", "Riaz", "Rizwan",
    "Sabir", "Sadiq", "Safeer", "Safi", "Saeed", "Safiullah", "Sajid", "Salim", "Saleem", "Salman",
    "Sami", "Sarfaraz", "Sarfraz", "Shafi", "Shafique", "Shahid", "Shakeel", "Sharif", "Shaukat", "Sheikh",
    "Shehzad", "Sheraz", "Shoukat", "Siddiq", "Siddique", "Sohail", "Suleman", "Sultan", "Tahir", "Talib",
    "Tariq", "Tufail", "Ubaid", "Umar", "Usman", "Waheed", "Wali", "Waseem", "Yaseen", "Yasin",
    "Yousaf", "Younas", "Yousuf", "Zafar", "Zahid", "Zakir", "Zaman", "Zameer", "Zarif", "Zubair",
    "Abbass", "Aftab", "Akram", "Alvi", "Anwar", "Ashraf", "Aziz", "Badar", "Bari", "Bashir",
    "Basharat", "Bostan", "Burhan", "Chughtai", "Dawar", "Ejaz", "Ehsan", "Faisal", "Farhan", "Fazal",
    "Gul", "Gulzar", "Haqqani", "Hashmi", "Hayee", "Hussaini", "Jalil", "Jamil", "Junaid", "Kabir",
    "Kamal", "Khawaja", "Khattak", "Kiani", "Khoso", "Khokhar", "Khosa", "Langrial", "Lodhi", "Mahmud",
    "Malook", "Mandokhel", "Memon", "Mughal", "Naqvi", "Naseer", "Niazi", "Orakzai", "Pathan", "Pirzada",
    "Qadri", "Qasmi", "Rashidi", "Saboor", "Sadaqat", "Sajjad", "Saleh", "Samiullah", "Sarwar", "Shafiullah",
    "Shah", "Shahbaz", "Shahzad", "Shams", "Sharafat", "Sharifuddin", "Shoaib", "Sikandar", "Sohaib", "Subhan",
    "Tabassum", "Taha", "Talha", "Tanveer", "Tauqeer", "Tariq", "Uddin", "Wahid", "Wajid", "Waqas",
    "Yar", "Yaseer", "Zaheer", "Zaman", "Zarrar", "Zeeshan", "Zia", "Zubairi", "Agha", "Aliani",
    "Ansari", "Arain", "Asmat", "Atta", "Baber", "Balochi", "Bangulzai", "Bhinder", "Chohan", "Chughtai",
    "Dasti", "Daudpota", "Dogar", "Domki", "Fani", "Gabol", "Gandapur", "Gill", "Goraya", "Gulshan",
    "Hingoro", "Hoti", "Jakhrani", "Jatoi", "Junejo", "Kalhoro", "Kakar", "Kashmiri", "Khoso", "Khatri",
    "Kundi", "Laghari", "Langah", "Leghari", "Liaqat", "Lodhi", "Mahsud", "Magsi", "Marwat", "Mashwani",
    "Mengal", "Mirani", "Mitha", "Mugheri", "Mundokhel", "Naseeruddin", "Niazi", "Orakzai", "Qaimkhani", "Qasoori",
    "Rajput", "Rind", "Samar", "Samad", "Sandhu", "Sarai", "Sayyid", "Shahwani", "Sheerazi", "Sial",
    "Sindhu", "Soomro", "Soomra", "Suddiqi", "Syed", "Talpur", "Tanoli", "Tarin", "Tiwana", "Toor",
    "Turk", "Wazir", "Yusufzai", "Zehri", "Zuberi", "Awan", "Kiyani", "Khakwani", "Taj", "Meer",
    "Mirwani", "Chohan", "Bhutta", "Randhawa", "Sandhu", "Ghuman", "Raja", "Gillani", "Kazmi", "Naqash",
    "Abbassi", "Bohra", "Hanjra", "Rajpoot", "Siddiqui", "Qaim", "Shuja", "Qamar", "Irfan", "Talpur"
]


SIM_PROVIDERS = ["Jazz", "Zong", "Ufone", "Telenor", "Warid", "Onic"]

def sim_provider():
    return random.choice(SIM_PROVIDERS)


CASTES = ["Sheikh", "Ansari", "Raja", "Malik", "Qureshi", "Chaudhry", "Jutt", "Butt", "Rajput", "Rana"]   
SECTS = ["Sunni", "Shia"]

def caste():
    return random.choice(CASTES)

def sect():
    return random.choice(SECTS)
    
def dob(start_year=1950, end_year=2006):
    """Generate a random date of birth between start_year and end_year"""
    start = date(start_year, 1, 1)
    end = date(end_year, 12, 31)  
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)



def male_name():        
    """Generate a random male full name."""
    return random.choice(MALE_NAMES) + " " + random.choice(LAST_NAMES)
    
def female_name():
    """Generate a random female full name."""
    return random.choice(FEMALE_NAMES) + " " + random.choice(LAST_NAMES)

def cnic():       
    part1 = str(random.randint(10000, 99999))
    part2 = str(random.randint(1000000, 9999999))
    part3 = str(random.randint(0, 9))
    return f"{part1}-{part2}-{part3}"       

def phone_number():
    prefixes = ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309",
                "310", "311", "312", "313", "314", "315", "316", "317", "318", "319"]
    prefix = random.choice(prefixes)
    remaining = str(random.randint(1000000, 9999999))
    return f"+92{prefix}{remaining}"
