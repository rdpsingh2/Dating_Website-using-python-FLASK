import mysql.connector

# MySQL database configuration
config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "user"
}

try:
    # Establish connection to MySQL
    print("Connecting to MySQL...")
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
        cursor = connection.cursor()

        # Read data from the file
        with open('data.txt', 'r') as file:
            all_profiles_data = file.readlines()

        # Iterate over each data entry
        for profile_entry in all_profiles_data:
            # Process the data entry (assuming it's in a specific format)
            profile_data = eval(profile_entry)  # Convert string to dictionary
            
            # Construct the INSERT query
            insert_query = """
            INSERT INTO profiles (first_name, last_name, religion, education, net_worth, annual_income, credit_score, transportation, passport, languages, keywords, music_genre, movie_genre, gender, race, skin_tone, age, height, weight, body_type, sex_orientation, residing_status, adults_in_house, children, number_of_children_living_at_home, indoor_pets, outdoor_pets, zip_code, miles_away, current_relationship_status, relationship_goal, alcohol_use, cannabis_use, other_rec_drug_use)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            profile_values = (
                profile_data['first_name'],
                profile_data['last_name'],
                profile_data['religion'],
                profile_data['education'],
                profile_data['financial_stability']['net_worth'],
                profile_data['financial_stability']['annual_income'],
                profile_data['financial_stability']['credit_score'],
                ', '.join(profile_data['travel_status']['transportation']),
                profile_data['travel_status']['passport'],
                ', '.join(profile_data['languages']),
                profile_data['keywords'],
                ', '.join(profile_data['entertainment']['music_genre']),
                ', '.join(profile_data['entertainment']['movie_genre']),
                profile_data['human_design']['gender'],
                ', '.join(profile_data['human_design']['race']),
                ', '.join(profile_data['human_design']['skin_tone']),
                profile_data['age'],
                profile_data['height'],
                profile_data['weight'],
                ', '.join(profile_data['body_type']),
                ', '.join(profile_data['sex_orientation']),
                profile_data['household']['residing_status'],
                profile_data['household']['adults_in_house'],
                ', '.join(profile_data['household']['children']),
                profile_data['household']['number_of_children_living_at_home'],
                ', '.join(profile_data['household']['indoor_pets']),
                ', '.join(profile_data['household']['outdoor_pets']),
                profile_data['location']['zip_code'],
                profile_data['location']['miles_away'],
                ', '.join(profile_data['current_relationship_status']),
                ', '.join(profile_data['relationship_goal']),
                profile_data['alcohol_use'],
                profile_data['cannabis_use'],
                ', '.join(profile_data['other_rec_drug_use'])
            )

            cursor.execute(insert_query, profile_values)


        connection.commit()
        print("All data inserted successfully")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL:", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# import mysql.connector

# # Connect to MySQL server
# connection = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     database="user"
# )

# # Create cursor object
# cursor = connection.cursor()

# # Define SQL statement to delete data
# delete_data_query = "DELETE FROM profiles"

# # Execute the SQL statement to delete data
# cursor.execute(delete_data_query)

# # Commit changes
# connection.commit()

# # Close cursor and connection
# cursor.close()
# connection.close()

# print("Data deleted successfully!")
