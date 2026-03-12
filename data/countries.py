import pycountry
import pandas as pd


cnts = pycountry.countries
all_countries_name = []
all_countries_off_name = []
all_countries_code_name = []
all_countries_flag = []
for country in cnts:
    all_countries_name.append(country.name)
    if 'official_name' in country.__dict__.keys():
        all_countries_off_name.append(country.official_name)
    else:
        all_countries_off_name.append(country.name)
    all_countries_code_name.append(country.alpha_3)
    all_countries_flag.append(country.flag)


all_countries_off_name = list(map(lambda x: x.replace('Czechia', 'Czech Republic'), all_countries_off_name))

all_countries_code_name = [i.lower() for i in all_countries_code_name]
all_countries_name = [i.lower() for i in all_countries_name]
all_countries_off_name = [i.lower() for i in all_countries_off_name]

countries_dict = {"code": all_countries_code_name,
                  "official_name": all_countries_off_name,
                  "name": all_countries_name}

countries_dfrm = pd.DataFrame.from_dict(countries_dict)