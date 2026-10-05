from app.repositories.pet_repository import add_pet


def main():
    print("🐾 Happy Paws Pet Hotel")
    print("------------------------")

    new_pet_id = add_pet(
        "Buddy",
        "Dog",
        "Beagle",
        2,
        "Anan",
    )

    print(f"New pet added with ID: {new_pet_id}")


if __name__ == "__main__":
    main()