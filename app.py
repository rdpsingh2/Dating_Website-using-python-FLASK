from flask import Flask, render_template,jsonify
import mysql.connector

app = Flask(__name__, static_url_path='/static')

# MySQL database configuration
config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "user"
}

@app.route('/')
def index():
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Fetch data from the database
            cursor.execute("SELECT * FROM profiles")
            profiles = cursor.fetchall()

            return render_template('index.html', profiles=profiles)

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return "Failed to fetch data from the database"

@app.route('/profile/<profile_id>')
def get_profile(profile_id):
    print("get profile route has been called")
    # if connection.is_connected():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

            # Fetch data from the database
    cursor.execute("SELECT * FROM profiles WHERE id = %s", (profile_id,))
    profiles = cursor.fetchone()
    return render_template('profile_detail.html',profile_id=profile_id,profile=profiles)
    try:
        # Establish connection to MySQL
        connection = mysql.connector.connect(**config)

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)

            # Fetch data for the specified profile from the database
            cursor.execute("SELECT * FROM profiles WHERE id = %s", (profile_id,))
            profile = cursor.fetchone()

            return jsonify(profile)

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    return "Failed to fetch profile from the database"


if __name__ == '__main__':
    app.run(debug=True)
