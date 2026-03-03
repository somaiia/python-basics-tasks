# Guest List Manager
# Task 1 - Python Basics

# List of five guests
guests = ["Ahmed", "Sara", "Mona", "Omar", "Laila"]

# Print initial invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Replace a guest who can't attend
print("
Omar can't attend the dinner.")
guests[3] = "Youssef"
print(guests)

# Add more guests
guests.insert(0, "Nour")
guests.insert(2, "Hassan")
guests.append("Salma")
print(guests)

# Sort the guest list
guests.sort()
print(guests)

# Print invitations again
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

# Limit the guest list to two people
print("
Sorry, the dinner table can only accommodate two guests.")

# Remove extra guests
removed_guests = guests[2:]
guests = guests[:2]
for removed_guest in removed_guests:
    print(f"Sorry {removed_guest}, you are no longer invited.")
print(guests)

# Confirm remaining invitations
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

# Completely clear the guest list
del guests[:]
print(guests)
