from app.database.connection import get_connection


# 1. Get all pets
def get_all_pets():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, type, breed, age, owner_name
        FROM pets
        ORDER BY id
    """)

    pets = cursor.fetchall()

    cursor.close()
    connection.close()

    return pets


# 2. Get one pet by ID
def get_pet_by_id(pet_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, type, breed, age, owner_name
        FROM pets
        WHERE id = ?
        """,
        (pet_id,),
    )

    pet = cursor.fetchone()

    cursor.close()
    connection.close()

    return pet


# 3. Add a new pet
def add_pet(name, pet_type, breed, age, owner_name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO pets (name, type, breed, age, owner_name)
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, pet_type, breed, age, owner_name),
    )

    connection.commit()

    new_pet_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return new_pet_id