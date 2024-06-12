import random


def read_variables(file_path):
    variables = {}
    with open(file_path, 'r') as file:
        exec(file.read(), variables)
    return variables
variables = read_variables('variables.txt')

first_name = variables['first_name']
last_name = variables['last_name']
religions = variables['religions']
educations = variables['educations']
net_worth = variables['net_worth']
annual_income = variables['annual_income']
credit_scores = variables['credit_scores']
transportation_options =variables['transportation_options']
passport_options = variables['passport_options']
languages = variables['languages']
keywords = variables['keywords']
music_genres = variables['music_genres']
movie_genres = variables['movie_genres']
genders = variables['genders']
races = variables['races']
skin_tones = variables['skin_tones']
age=variables['age']
height=variables['height']
weight=variables['weight']
body_types = variables['body_types']
sex_orientations = variables['sex_orientations']
residing_statuses = variables['residing_statuses']
adults_in_house_options = variables['adults_in_house_options']
children_options = variables['children_options']
indoor_pets_options = variables['indoor_pets_options']
outdoor_pets_options = variables['outdoor_pets_options']
zip_codes = variables['zip_codes']
miles_away = variables['miles_away']
relationship_goals = variables['relationship_goals']
relationship_status = variables['relationship_status']
alcohol_use_options = variables['alcohol_use_options']
cannabis_use_options = variables['cannabis_use_options']
other_rec_drug_use_options = variables['other_rec_drug_use_options']
 

def generate_fake_profile(genders, first_name):
    gender=genders
    if gender == 'Natural Male':
        first_name = random.choice(first_name)
    elif gender == 'Natural Female':
        first_name = random.choice(first_name)
    elif gender == 'Trans Female':
        first_name = random.choice(first_name)  
    elif gender == 'Trans Male':
        first_name = random.choice(first_name) 
    else:
        raise ValueError("Invalid gender specified")


    profile = {
        'first_name': first_name,
        'last_name': random.choice(last_name),
        'religion': random.choice(religions),
        'education': random.choice(educations),
        'financial_stability': {
            'net_worth': random.randint(net_worth[0] // 100, net_worth[1] // 100) * 100,
            # 'net_worth': random.choice(net_worth),
            'annual_income':random.randint(annual_income[0] // 100, annual_income[1] // 100) * 100,
            # 'annual_income': random.choice(annual_income),
            'credit_score': random.randint(credit_scores[0],credit_scores[1])
        },
        'travel_status': {
            'transportation': random.sample(transportation_options, random.randint(1, len(transportation_options))),
            'passport': random.choice(passport_options)
        },
        'languages': random.sample(languages, random.randint(1, 7)),
        'keywords': ', '.join(random.sample(keywords, random.randint(1, 5))),
        'entertainment': {
            'music_genre': random.sample(music_genres, random.randint(1, 3)),
            'movie_genre': random.sample(movie_genres, random.randint(1, 3))
        },
        'human_design': {
            'gender': gender,
            'race': random.sample(races, random.randint(1, 2)),
            'skin_tone': random.choices(skin_tones)
        },
        'age': random.randint(age[0],age[1]),
        'height': round(random.uniform(height[0], height[1]), 1),
        # 'height': random.choice(height),
        'weight': random.randint(weight[0], weight[1]),
        # 'weight': random.choice(weight),
        'body_type': random.choices(body_types),
        'sex_orientation': random.sample(sex_orientations,random.randint(1,7)),
        'household': {
            'residing_status': random.choice(residing_statuses),
            'adults_in_house': random.choice(adults_in_house_options),
            'children': random.sample(children_options, random.randint(0, 4)),
            'number_of_children_living_at_home': random.randint(0, 10),
            'indoor_pets': random.sample(indoor_pets_options, random.randint(0, 5)),
            'outdoor_pets': random.sample(outdoor_pets_options, random.randint(0, 5))
        },
        'location': {
            'zip_code': random.choice(zip_codes),
            'miles_away': random.choice(miles_away)
        },
        'current_relationship_status': random.sample(relationship_status,random.randint(1,7)),
        'relationship_goal': random.sample(relationship_goals, random.randint(1, 11)),
        'alcohol_use': random.choice(alcohol_use_options),
        'cannabis_use': random.choice(cannabis_use_options),
        'other_rec_drug_use': random.sample(other_rec_drug_use_options,random.randint(1,3))
    }
    return profile

def generate_fake_profiles(num_profiles):
    natural_male_profiles = [generate_fake_profile('Natural Male',first_name) for _ in range(num_profiles // 4)]
    natural_female_profiles = [generate_fake_profile('Natural Female', first_name) for _ in range(num_profiles // 4)]
    trans_female_profiles = [generate_fake_profile('Trans Female', first_name) for _ in range(num_profiles // 4)]
    trans_male_profiles = [generate_fake_profile('Trans Male', first_name) for _ in range(num_profiles // 4)]
    profiles = natural_male_profiles + natural_female_profiles + trans_female_profiles + trans_male_profiles

    random.shuffle(profiles)

    return profiles

fake_profiles = generate_fake_profiles(1000)
with open('data.txt', 'w') as file:
    for profile in fake_profiles:
        file.write(str(profile) + '\n')
print("Text Document created")

    





