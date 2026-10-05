from app.repositories.pet_repository import (
    get_all_pets,
    get_pet_by_id,
    add_pet,
    update_pet,
    delete_pet,
)


# Get all pets through the Service Layer
def list_pets():
    pets = get_all_pets()
    return pets


# Get one pet through the Service Layer
def get_pet(pet_id):
    pet = get_pet_by_id(pet_id)
    return pet


# Add a pet through the Service Layer
def create_pet(name, pet_type, breed, age, owner_name):
    new_pet_id = add_pet(
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )
    return new_pet_id


# Update a pet through the Service Layer
def update_pet_service(pet_id, name, pet_type, breed, age, owner_name):
    rows_updated = update_pet(
        pet_id,
        name,
        pet_type,
        breed,
        age,
        owner_name,
    )
    return rows_updated


# Delete a pet through the Service Layer
def delete_pet_service(pet_id):
    rows_deleted = delete_pet(pet_id)
    return rows_deleted