def string_compression(string: str) -> str:

    """
    1. we need to read one character at a time from left to right
    2. to remember our answer we need one paper or place on the paper
    3. you also need to remember the count of chars 
    4. start from the 2nd character and compare it with first character 
    5. If they both are same  then increment the cout in memory from 0 to 2
    6. Go to next character and read it's value, if that is also same then increment counter from 2 to 3
    7. if next one is different then in answer sheet write  a < count value> , but immediately make count 1
    8. if first and second character are different then in answer sheet write first char and if count is 1 then ignore the number 
    9. do this till the end
    """
    if not string:
        return ""
    
    compressed = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            compressed.append(f"{string[i-1]}{count if count > 1 else ''}")
            count = 1
    
    # Append last character
    compressed.append(f"{string[-1]}{count if count > 1 else ''}")
    
    return "".join(compressed)

print(string_compression("aabfgfgbcde"))
