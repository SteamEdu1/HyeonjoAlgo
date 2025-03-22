"""
Given a roman numeral, convert it into a base 10 number.
The maximum input for roman numerals is up to 39

Example:
    converter("X") ➞ 10
    converter("IV") ➞ 9
    converter("III") ➞ 3

"""
roman_numerals = {
    "I": 1,
    "V": 5,
    "X": 10
}


def converter(target_string: str):
    index = 0
    sum = 0
    while index < len(target_string):
        if target_string[index] == "X":
            sum += 10
        elif target_string[index] == "V":
            sum += 5
        elif target_string[index] == "I":
            if  index != len(target_string) - 1:
                current_value = roman_numerals[target_string[index]]
                future_value = roman_numerals[target_string[index + 1]]
                if current_value < future_value:
                    sum -=1
                else:
                    sum +=1
            else:
                sum+=1

        index +=1
    return  sum

    
