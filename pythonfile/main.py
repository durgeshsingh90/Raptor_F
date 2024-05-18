# input_string = str(input("Enter a string : "))

input_string = '01232Thisworlds0033310023200433hi01734Hello! 01Br 820'

while len(input_string) > 0:
    # Extract the length field (assuming it represents the length of the data field)
    length_field = int(input_string[:3])

    # Extract the entire data field using the length obtained above
    data_field = input_string[3:3 + length_field]

    # Extract the subfield (assuming it is a substring of the data field)
    subfield = input_string[3:5]

    # Extract the value field (excluding the first two characters)
    value_field = input_string[5:5 + length_field - 2]

    # Remove data_field from input_string
    modified_input_string = input_string[3 + length_field:]

    # Print the results
    print ()
    print("Length :", length_field)
    print("Data Field:", data_field)
    print("Subfield:", subfield)
    print("Value :", value_field)
    # print("Modified Input String:", modified_input_string)
    print ()

    # Update input_string for the next iteration
    input_string = modified_input_string
