# Encoder
An interative program that encodes a line of text or message

# Conditions
(1) Convert each character, including blank spaces, to its ASCII equivalent.
(2) Generate a positive random integer. Add this integer to the ASCII
equivalent of each character. The same random integer will be used for
the entire line of text.
(3) Suppose that N1 represents the lowest permissible value in the ASCII
code, and N2 represents the highest permissible value. If the number
obtained in step 2 above (i.e., the original ASCII equivalent plus the
random integer) exceeds N2, then subtract the largest possible multiple
of N2 from this number, and add the remainder to N1. Hence the
encoded number will always fall between N1 and N2, and will always
therefore always represent some ASCII character.
(4) Display the characters that correspond to the encoded ASCII values.
The procedure is reversed when decoding a line of text. Be certain,
however, that the same random number is used in decoding as was used in encoding.
