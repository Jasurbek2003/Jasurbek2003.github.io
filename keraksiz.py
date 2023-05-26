from datetime import datetime
import requests

from new_data import data

country = {'name': {'common': 'Hungary', 'official': 'Hungary',
					'nativeName': {'hun': {'official': 'Magyarország', 'common': 'Magyarország'}}},
		   'tld': ['.hu'], 'cca2': 'HU', 'ccn3': '348', 'cca3': 'HUN', 'cioc': 'HUN',
		   'independent': True,  'status': 'officially-assigned', 'unMember': True,
		   'currencies': {'HUF': {'name': 'Hungarian forint', 'symbol': 'Ft'}},
		   'idd': {'root': '+3', 'suffixes': ['6']},
		   'capital': ['Budapest'],
		   'altSpellings': ['HU'],
		   'region': 'Europe', 'subregion': 'Central Europe',
		   'languages': {'hun': 'Hungarian'},
		   'translations': {'ara': {'official': 'الجمهورية المجرية', 'common': 'المجر'},
							'bre': {'official': 'Hungaria', 'common': 'Hungaria'},
							'ces': {'official': 'Maďarsko', 'common': 'Maďarsko'},
							'cym': {'official': 'Hungary', 'common': 'Hungary'},
							'deu': {'official': 'Ungarn', 'common': 'Ungarn'},
							'est': {'official': 'Ungari', 'common': 'Ungari'},
							'fin': {'official': 'Unkari', 'common': 'Unkari'},
							'fra': {'official': 'Hongrie', 'common': 'Hongrie'},
							'hrv': {'official': 'Madžarska', 'common': 'Mađarska'},
							'hun': {'official': 'Magyarország', 'common': 'Magyarország'},
							'ita': {'official': 'Ungheria', 'common': 'Ungheria'},
							'jpn': {'official': 'ハンガリー', 'common': 'ハンガリー'},
							'kor': {'official': '헝가리', 'common': '헝가리'},
							'nld': {'official': 'Hongarije', 'common': 'Hongarije'},
							'per': {'official': 'مجارستان', 'common': 'مجارستان'},
							'pol': {'official': 'Węgry', 'common': 'Węgry'},
							'por': {'official': 'Hungria', 'common': 'Hungria'},
							'rus': {'official': 'Венгрия', 'common': 'Венгрия'},
							'slk': {'official': 'Maďarsko', 'common': 'Maďarsko'},
							'spa': {'official': 'Hungría', 'common': 'Hungría'},
							'srp': {'official': 'Мађарска', 'common': 'Мађарска'},
							'swe': {'official': 'Ungern', 'common': 'Ungern'},
							'tur': {'official': 'Macaristan', 'common': 'Macaristan'},
							'urd': {'official': 'مجارستان', 'common': 'مجارستان'},
							'zho': {'official': '匈牙利', 'common': '匈牙利'}},
		   'latlng': [47.0, 20.0],
		   'landlocked': True,
		   'borders': ['AUT', 'HRV', 'ROU', 'SRB', 'SVK', 'SVN', 'UKR'],
		   'area': 93028.0,
		   'demonyms': {'eng': {'f': 'Hungarian', 'm': 'Hungarian'},
						'fra': {'f': 'Hongroise', 'm': 'Hongrois'}},
		   'flag': '🇭🇺',
		   'maps': {'googleMaps': 'https://goo.gl/maps/9gfPupm5bffixiFJ6',
								  'openStreetMaps': 'https://www.openstreetmap.org/relation/21335'},
		   'population': 9749763,
		   'gini': {'2018': 29.6}, 'fifa': 'HUN',
		   'car': {'signs': ['H'], 'side': 'right'},
		   'timezones': ['UTC+01:00'],
		   'continents': ['Europe'],
		   'flags': {'png': 'https://flagcdn.com/w320/hu.png', 'svg': 'https://flagcdn.com/hu.svg',
					 'alt': 'The flag of Hungary is composed of three equal horizontal bands of red, white and green.'},
		   'coatOfArms': {'png': 'https://mainfacts.com/media/images/coats_of_arms/hu.png',
						  'svg': 'https://mainfacts.com/media/images/coats_of_arms/hu.svg'},
		   'startOfWeek': 'monday',
		   'capitalInfo': {'latlng': [47.5, 19.08]}, 'postalCode': {'format': '####', 'regex': '^(\\d{4})$'}}


# new_data = []
# for i in data:
# 	new_country = i["name"]["common"]
# 	translates = []
# 	for j in i["translations"]:
# 		translates.append({j: i["translations"][j]["official"]})
# 		translates.append({j: i["translations"][j]["common"]})
# 	new_data.append({new_country: {
# 		"official_name":i["name"]["official"],
# 		"capital":i["capital"][0] if "capital" in i else None,
# 		"area":i["area"],
# 		"population":i["population"],
# 		"borders":i["borders"] if "borders" in i else None,
# 		"languages":i["languages"] if "languages" in i else None,
# 		"currency":i["currencies"] if "currencies" in i else None,
# 		"flag":i["flags"]["png"]if "flags" in i else None,
# 		"region":i["region"] if "region" in i else None,
# 		"subregion":i["subregion"] if "subregion" in i else None,
# 		"latlng":i["latlng"],
# 		"tld":i["tld"][0] if "tld" in i else None,
# 		"independent":i["independent"] if "independent" in i else None,
# 		"idd":i["idd"] if len(i["idd"]) > 0 else None,
# 		"timezones":i["timezones"][0] if len(i["timezones"]) > 0 else None,
# 		"altSpellings":i["altSpellings"][0] if len(i["altSpellings"]) > 0 else None,
# 		"translations":translates,
# 		"coatOfArms":i["coatOfArms"]["png"] if len(i["coatOfArms"]) > 0 else None,
# 		"capitalInfo":i["capitalInfo"]["latlng"] if len(i["capitalInfo"]) > 0 else None,
# 	}})

# name = input()
# print(data)
#
# params = {'serviceName': 'Trademark',
# 		  'perPage': 1,
# 		  'currentPage': 1,
# 		  'expert_code': 20230312}
# r = requests.get('https://testapiexpert-new.ima.uz/allapplication/my-application',
# 				 params=params,
# 				 headers={'Authorization': 'Bearer g4g4'},
# 				 timeout=15)
# print(1)
# if r.json() == []:
# 	print({'status': 'Ushbu raqam mavjud emas'})
# else:
# 	print(r.json())

today = datetime.now()
print(today.strftime("%Y-%m-%d %H:%M:%S"))

