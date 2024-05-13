import json
import re
from datetime import datetime, timedelta

#Defining default values
visa_card_number=['4970110000000005']
mc_card_number=['5534218827246242','6759050000000096']
diners_card_number=['3970110000000005']
jcb_card_number=[]
dummy_track2_BM35=['=1212000000000000000']
default_inst_num_BM32='000050'
default_merchant_num_BM42='226000000021357'
default_cvv2_BM48='861'
default_pinblock_BM52='9CAE2E2A395F8564'
default_emvdata_BM55='9F6E04230000005F2A02097882021A2B95051A2B3C4D5F9A032404199C01009F02060000000003019F03060000000000009F1006010003A410009F1A0209789F1E0831323334353637389F26080123456789ABCDEF9F2701809F3303E0E8809F34030000009F3501219F3602C3D49F3704CCDDEEFF'

#Some working details
#"DE035": "5413330089010574=1412201010640646",
#"DE052": "969DB26F2601096F",
#"DE053":"3030313030323030303030303030303030303030303030303030303030303030303030303030"
#---
#"DE035": "6799998900000010575=1412220007790407",
#"DE052": "9CAE2E2A395F8564",
#"DE053":"3030313030323030303030303030303030303030303030303030303030303030303030303030"
#---

print("Enter multi-line input data (press Enter twice to finish):")
input_lines = []
while True:
    line = input().strip()
    if not line:
        break
    input_lines.append(line)

# Combine the input lines into a single string
input_data = '\n'.join(input_lines)
#===
# Regular expression pattern to match the index and value
sq1index_pattern = r'in\[ *(\d+): *\]'

# Find all occurrences of index and value pairs using regex
matches = re.findall(r'in\[ *(\d+): *\]<(.+?)>', input_data)

# Specify the indices that should be concatenated
indices_to_concatenate = [7,43]

# Get the current date
current_date = datetime.now()

# Initialize index_35_value with None

# Constructing the JSON data
json_data = {
    "mti": 100,
    "data_elements": {}
}


# Populate data elements in the JSON data
for match in matches:
    index = match[0]
    value = match[1]
    if int(index) == 129:
        continue

    # Check if the index should be concatenated
    if int(index) in indices_to_concatenate:
        # If the index already exists, concatenate the new value with the existing value
        if f"DE{index.zfill(3)}" in json_data["data_elements"]:
            json_data["data_elements"][f"DE{index.zfill(3)}"] += value
        else:
            # Add index and value to data_elements
            json_data["data_elements"][f"DE{index.zfill(3)}"] = value
    
    elif int(index) == 2:
        # Update value for index 2 based on starting digit
        if value.startswith('3'):
            json_data["data_elements"][f"DE{index.zfill(3)}"] = diners_card_number[0]
        elif value.startswith('4'):
            json_data["data_elements"][f"DE{index.zfill(3)}"] = visa_card_number[0]
        elif value.startswith('5'):
            json_data["data_elements"][f"DE{index.zfill(3)}"] = mc_card_number[0]
        elif value.startswith('6'):
            json_data["data_elements"][f"DE{index.zfill(3)}"] = mc_card_number[1]
    
    elif int(index) == 3:
        # Ensure that the value associated with index 3 is always six digits long
        value = value.ljust(6, '0')
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value
    
    elif int(index) == 4:
        # Remove leading zeros from the value
        value = (int(value))
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value
    
    elif int(index) == 11 or int(index) == 12:
        # Ensure that the value associated with index 11 and 12 is always six digits long
        value = value.zfill(6)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value
    
    elif int(index) == 13:
        # Ensure that the value associated with index 13 is always 4 digits long
        value = value.zfill(4)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value

    elif int(index) == 14 and '*' in value:
        # Update value for index 14 to 3 years from now in YYMM format if it contains asterisks
        three_years_from_now = current_date + timedelta(days=3*365)
        value = three_years_from_now.strftime('%y%m')
        # Directly modify the dictionary key for index 14
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value

    elif int(index) == 22 or int(index) == 23:
        # Ensure that the value associated with index 13 is always 4 digits long
        value = value.zfill(3)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value

    elif int(index) == 25:
        # Ensure that the value associated with index 13 is always 4 digits long
        value = value.zfill(2)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value

    elif int(index) == 32:
        # Ensure that the value associated with index 13 is always 4 digits long
        value = value.zfill(2)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = default_inst_num_BM32

    elif int(index) ==35:
        json_data["data_elements"][f"DE{index.zfill(3)}"]=json_data["data_elements"]["DE002"] + dummy_track2_BM35

    elif int(index) == 42:
        # Ensure that the value associated with index 13 is always 4 digits long
        value = value.zfill(2)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = default_merchant_num_BM42

    elif int(index) == 48:
        # Update value for index 48 to '861'
        json_data["data_elements"][f"DE{index.zfill(3)}"] = default_cvv2_BM48

    elif int(index) == 49:
        value=(int(value))
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value

    elif int(index) == 52:
        # Ensure that the value associated with index 13 is always 4 digits long
        value = value.zfill(2)
        json_data["data_elements"][f"DE{index.zfill(3)}"] = default_pinblock_BM52

    elif int(index) == 55:
        json_data["data_elements"][f"DE{index.zfill(3)}"] = default_emvdata_BM55

    elif int(index) == 60 or int(index) == 61 or int(index) == 62 or int(index) == 63 or int(index) == 64:
        # Process index 60-64 value into subfields and values
        subfields = []
        values = []
        i = 0
        while i < len(value):
            subfield_length = int(value[i:i + 3])
            subfield = value[i + 3:i + 5]
            subfields.append(subfield)
            values.append(value[i + 5:i + 5 + subfield_length - 2])
            i += 5 + subfield_length - 2
        
        # Create a dictionary for indexes
        index_6x_dict = {subfield: val for subfield, val in zip(subfields, values)}

        # Add indexes dictionary to the main JSON data
        json_data["data_elements"][f"DE{index.zfill(3)}"] = index_6x_dict
         
    else:
        # Add index and value to data_elements without special treatment
        json_data["data_elements"][f"DE{index.zfill(3)}"] = value

# Ensure that the concatenated value for index 7 is always 10 digits long
if "DE007" in json_data["data_elements"]:
    value = json_data["data_elements"]["DE007"]
    json_data["data_elements"]["DE007"] = value.zfill(10)

# Convert the dictionary to JSON format
json_output = json.dumps(json_data, indent=4)

# Print the JSON output
print(json_output)
