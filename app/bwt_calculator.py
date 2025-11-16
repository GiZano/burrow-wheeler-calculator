'''
Burrow Wheeler Transform Encoder

Algorithm to make similar character be near to each other,
making it easier to compress the strings afterwhile with other algorithms.

Steps:
1. Concatenate $ character
2. Calculate rotations to the left
3. Sort rotations
4. Build bwt using the last character of each sorted rotation


Input:  line     | str
Output: bwt_line | str

Example:
Input: BANANA
Output: ANNB$AA
'''
def encoder(line:str):
    ### 1. Concatenate '$' ###
    line = line + '$'

    ### 2. Calcolate rotations ###
    rotations = [] 
    '''
    if(len(line) >= 995):
        rotations = rotations_calculator_long(line)
    else:
        rotations = rotations_calculator_fast(line, rotations)
    '''
    rotations = rotations_calculator_while(line)
    
    ### 3. Sort rotations ###
    rotations.sort()

    ### 4. Trasformed Build ###
    bwt = ""
    for i in range(len(rotations)):
        bwt = bwt + rotations[i][-1]
    
    return bwt

'''
Rotation Calculator (Recursive)

Calculate all possible rotations of a string going left using a recursive function

Input:  line      | str
        rotations | list
Output: rotations | list

Example
Input: banana
Output: ['banana$', 'anana$b', 'nana$ba', 'ana$ban', 'na$bana', 'a$banan', '$banana']
'''
def rotations_calculator_recursive(line:str, rotations:list):
    ## INDUCTIVE CASE ##
    # Adding original line to the rotations list when starting #
    if(len(rotations) == 0):
        rotations.append(line)
    
    # calcolo shift
    line = line[1:] + line[0]

    ## BASE CASE ##
    # If the shift is the same as the first and the string is longer than 1 char, return the list #
    if(line == rotations[0] and len(rotations) > 0):
        return rotations
    ## BASE CASE END ##

    # Append shifted line to the rotations list #
    rotations.append(line)
    return rotations_calculator_recursive(line, rotations)
    ## INDUCTIVE CASE END ##

'''
Rotation Calculator (While)

Calculate all possible rotations of a string going left using while function

Input:  line      | str
Output: rotations | list

Example
Input: banana
Output: ['banana$', 'anana$b', 'nana$ba', 'ana$ban', 'na$bana', 'a$banan', '$banana']
'''
def rotations_calculator_while(line:str):
    rotations = [line]
    shifted_line = line
    while rotations[0] != shifted_line or len(rotations) <= 1:
        rotations.append(shifted_line)
        shifted_line = shifted_line[1:] + shifted_line[0]
    return rotations

if __name__ == '__main__':
    valore = str(input("Inserire stringa da codificare con BWT:"))
    print(f"Trasformata: {encoder(valore)}")
