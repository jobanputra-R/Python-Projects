# fundamental project 1.py

print("*--------Welcome to the interactive data collector--------*\n")

Name=str(input("Please enter your name:-"))
Age=int(input("Please enter your age:-"))
Height=float(input("Please enter your height in meter:-"))
Fav_num=int(input("Please enter your favourite number:-"))

birth_year=2025-Age

print("\n*Thank you! Here is the information we collected:*\n")

print(f"Name:-{Name}  (Type:{type(Name),id(Name)})")
print(f"Age: {Age}(Type: {type(Age),id(Age)})")
print(f"Height: {Height} (Type: {type(Height),{id(Height)}})")
print(f"Favourite Number: {Fav_num} (Type: {type(Fav_num),id(Fav_num)})")

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {Age})")

print("\nThank you for using the personal Data collector. Goodbye!")