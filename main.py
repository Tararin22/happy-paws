from app.services.pet_service import delete_pet_service


def main():
    print("🐾 Happy Paws Pet Hotel")
    print("------------------------")

    rows_deleted = delete_pet_service(10)

    print(f"Rows deleted: {rows_deleted}")


if __name__ == "__main__":
    main()