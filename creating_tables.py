import mysql.connector

db_config = {
    'host': 'db',
    'user': 'user',
    'password': 'userpassword',
    'database': 'mydatabase'
}


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


create_users_table = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
'''

create_metrics_table = '''
CREATE TABLE IF NOT EXISTS metrics (
    metric_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    talked_time INT,
    microphone_used BOOLEAN,
    speaker_used BOOLEAN,
    voice_sentiment VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''

create_talked_time_table = '''
CREATE TABLE IF NOT EXISTS talked_time (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    talked_time INT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''

create_microphone_used_table = '''
CREATE TABLE IF NOT EXISTS microphone_used (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    microphone_used BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''

create_speaker_used_table = '''
CREATE TABLE IF NOT EXISTS speaker_used (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    speaker_used BOOLEAN,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''

create_voice_sentiment_table = '''
CREATE TABLE IF NOT EXISTS voice_sentiment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    voice_sentiment VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''


cursor.execute(create_users_table)
cursor.execute(create_metrics_table)
cursor.execute(create_talked_time_table)
cursor.execute(create_microphone_used_table)
cursor.execute(create_speaker_used_table)
cursor.execute(create_voice_sentiment_table)


connection.commit()
cursor.close()
connection.close()
