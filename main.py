from subnet import subnet_calculator
from utils import get_ip_class, ip_to_binary


def show_menu():
    print("\n" + "=" * 40)
    print("         NETCALC LITE")
    print("=" * 40)
    print("1. Subnet Calculator")
    print("2. IP Class Checker")
    print("3. IP to Binary Converter")
    print("4. About")
    print("5. Exit")
    print("=" * 40)


while True:

    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":

        ip = input("Enter IP Address: ")
        prefix = input("Enter Prefix Length (Example: 24): ")

        result = subnet_calculator(ip, prefix)

        if result is None:
            print("\nInvalid IP Address or Prefix!")

        else:
            print("\n----- SUBNET RESULTS -----")

            for key, value in result.items():
                print(f"{key:<20}: {value}")

    elif choice == "2":

        ip = input("Enter IP Address: ")

        print("\nIP Class:", get_ip_class(ip))

    elif choice == "3":

        ip = input("Enter IP Address: ")

        print("\nBinary IP:")

        print(ip_to_binary(ip))

    elif choice == "4":

        print("\n========== ABOUT ==========")
        print("NetCalc Lite v1.0")
        print("Developed by: Your Name")
        print("University of Colombo")
        print("===========================")

    elif choice == "5":

        print("\nThank you for using NetCalc Lite!")

        break

    else:

        print("\nInvalid option. Please try again.")