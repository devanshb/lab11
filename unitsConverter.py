def convert_units(bytes):
    kilobytes = bytes / 1000
    kibibytes = bytes / 1024
    megabytes = kilobytes / 1000
    mebibytes = kibibytes / 1024

    print("\nConversions:")
    print(f"{bytes:,} bytes")
    print(f"{kilobytes:,} kilobytes")
    print(f"{kibibytes:,} kibibytes")
    print(f"{megabytes:,} megabytes")
    print(f"{mebibytes:,} mebibytes")

def main():
    while True:
        try:
            user_input = input("Please enter a number: ")
            bytes = int(user_input)

            if bytes < 0:
                raise ValueError

            convert_units(bytes)
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
