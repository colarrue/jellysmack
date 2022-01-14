import datetime
import os
import json
import sqlite3
import src.models
import src.db.database
import src.crud.character
import src.crud.episode


def create_tables(db_name):
    """ "
    Use sqlite3 to initialize database tables.

    :param db_name: name of the database
    """
    file_path = os.path.abspath(db_name)

    if os.path.exists(file_path):
        os.remove(file_path)

    # Connect to sqlite database
    connection = sqlite3.connect(file_path)

    # Creating a cursor object to execute
    # SQL queries on a database table
    cursor = connection.cursor()

    # Table Definition
    create_table_character = """CREATE TABLE character(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        status TEXT NOT NULL,
                        species TEXT NOT NULL,
                        type TEXT,
                        gender TEXT NOT NULL);
                        """

    create_table_episode = """CREATE TABLE episode(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        air_date TEXT NOT NULL,
                        episode TEXT NOT NULL);
                        """

    create_table_junction = """CREATE TABLE association(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        character_id int NOT NULL,
                        episode_id TEXT NOT NULL,
                        FOREIGN KEY (character_id) REFERENCES character(id)
                            ON DELETE CASCADE,
                        FOREIGN KEY (episode_id) REFERENCES episode(id)
                            ON DELETE CASCADE);
                        """

    create_table_comment = """CREATE TABLE comment(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        content TEXT NOT NULL,
                        episode_id int,
                        character_id int);
                        """

    # Creating the tables into our database
    cursor.execute(create_table_character)
    cursor.execute(create_table_episode)
    cursor.execute(create_table_junction)
    cursor.execute(create_table_comment)

    connection.close()


def populate_character_table(db_session, input_filename):
    """
    Populate character table with json input.

    :param db_session: the database session
    :param input_filename: name of the json file containing data
    :return association: the association for many to many relationship
    """
    # Read json data about tables
    with open(input_filename) as f:
        characters_dict = json.load(f)

    association = {}
    # Convert it to a list of SQLAlchemy objects
    for character in characters_dict:
        association[character["id"]] = character["episode"]
        orm_char = src.models.Character(
            name=character["name"],
            status=character["status"],
            species=character["species"],
            type=character["type"],
            gender=character["gender"],
        )
        db_session.add(orm_char)
    db_session.commit()

    return association


def populate_episode_table(db_session, input_filename):
    """
    Populate character table with json input.

    :param db_session: the database session
    :param input_filename: name of the json file containing data
    """
    # Read json data about tables
    with open(input_filename) as f:
        episodes_dict = json.load(f)

    # Convert it to a list of SQLAlchemy objects
    for episode in episodes_dict:
        air_date = datetime.datetime.strptime(episode["air_date"], "%B %d, %Y")
        epi = src.models.Episode(
            name=episode["name"], air_date=air_date, episode=episode["episode"]
        )
        db_session.add(epi)
    db_session.commit()


def create_many_to_many_rel(db_session, association):
    """
    Create many-to-many relationship between characters and episodes.

    :param db_session: the db session
    :param association: dict representing association table
    """
    for character_id, episodes in association.items():
        # Get associated character
        character_crud = src.crud.character.Character()
        character = character_crud.get(db_session, character_id)
        # Add relationship
        episode_crud = src.crud.episode.Episode()
        for episode in episodes:
            orm_episode = episode_crud.get(db_session, episode)
            character.episodes.append(orm_episode)
        db_session.commit()


def init_database(db_name, db_session, characters_input, episodes_input):
    """
    Create and initialize the database with proper data.

    :param db_name: name of the database
    :param db_session: database session
    :param characters_input: json data of characters
    :param episodes_input: json data of episodes
    """
    # Initialize database with empty tables
    create_tables(db_name)

    # Load characters and get back association relationship
    association = populate_character_table(db_session, characters_input)

    # Load episodes
    populate_episode_table(db_session, episodes_input)

    # Create many-to-many relationship
    create_many_to_many_rel(db_session, association)


if __name__ == "__main__":
    # Set input data
    db_name = "jellysmack.db"
    characters_input = "rick_morty-characters_v1.json"
    episodes_input = "rick_morty-episodes_v1.json"
    # Intialize database
    db_session = src.db.database.SessionLocal()
    init_database(db_name, db_session, characters_input, episodes_input)
