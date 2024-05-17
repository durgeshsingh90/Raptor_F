input_string = "007ABHello008CDWorlds"
string_length=len("007ABHello008CDWorlds")
print (string_length)
result = []
n=3
if n != string_length:

    length = str(input_string[:n])
    print (length)

    # Extract subfield
    subfield = input_string[n:n+2]
    print (subfield)

    # Extract value
    value = input_string[n+2:int(length)+n]
    print (value)

    # Append to result
    result.append((length, subfield, value))
    print (result)
    