# Step 1: This must come first
def mod(employee):
    return f"{employee['name']}_{employee['department']}"

# Step 2
def to_mod_list(employee_list):
    map_emp = map(mod, employee_list)
    return list(map_emp)

# Step 3
def generate_usernames(mod_list):
    return [entry.replace(" ", "_") for entry in mod_list]

# Step 4
def map_id_to_initial(employee_dict):
    return {name[0]: emp_id for name, emp_id in employee_dict.items()}

# Step 5: Run/test code at the bottom
if __name__ == "__main__":
    employees = [
        {'name': 'Lisa', 'department': 'Cold Storage'},
        {'name': 'John', 'department': 'HR'},
        {'name': 'Mary', 'department': 'Finance'}
    ]

    ids = {
        'Lisa': 'E123',
        'John': 'E456',
        'Mary': 'E789'
    }

    modded = to_mod_list(employees)  # ✅ NOW it will work
    print("Modified:", modded)

    usernames = generate_usernames(modded)
    print("Usernames:", usernames)

    initials = map_id_to_initial(ids)
    print("Initial Map:", initials)
