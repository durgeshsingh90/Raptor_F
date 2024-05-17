import json
from datetime import datetime
import random

def generate_timestamp():
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%m%d%H%M%S")
    return formatted_timestamp

def generate_random_number():
    first_digit = random.choice([1, 9])
    remaining_digits = [random.randint(0, 9) for _ in range(11)]
    random_number = int(''.join(map(str, [first_digit] + remaining_digits)))
    return random_number

def generate_random_six_digit_number():
    random_six_digit_number = random.randint(100000, 999999)
    return random_six_digit_number

def get_local_time_hhmmss():
    current_time = datetime.now().time()
    hhmmss_format = current_time.strftime('%H%M%S')
    return hhmmss_format

def get_current_date_MMDD():
    current_date = datetime.now().date()
    MMDD_format = current_date.strftime('%m%d')
    return MMDD_format

# Create a dictionary with the desired keys and values
output_data = {
    "DE007": generate_timestamp(),
    "DE011": str(generate_random_six_digit_number()).zfill(6),
    "DE012": get_local_time_hhmmss(),
    "DE013": get_current_date_MMDD(),
    "DE037": str(generate_random_number()).zfill(12),  # Modified this line
    
}

# Convert the dictionary to a JSON-formatted string
json_output = json.dumps(output_data, indent=2)

# Print the JSON-formatted string
print(json_output)
