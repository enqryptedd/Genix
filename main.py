from id_generator import FakeIDGenerator

def main():
    print("@enqryptedd | Starting Genix...")
    generator = FakeIDGenerator()
    generator.create_fake_id()
    print("@enqryptedd | Your ID is ready in the output folder. Don’t get caught.")

if __name__ == "__main__":
    main()