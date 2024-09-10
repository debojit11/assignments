# Which of the following strings is the longest?
# Use the len() function to find out.

longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}/(<bCGHv^FfM}.;)khpkSYTfMA@>N"
len(longest_german_word)
len(longest_hungarian_word)
len(longest_finnish_word)
len(strong_password)
longest = max(len(longest_german_word) , len(longest_hungarian_word) , len(longest_finnish_word) , len(strong_password))
if longest == len(longest_german_word):
    print("longest_german_word")
elif longest == len(longest_hungarian_word):
    print("longest_hungarian_word")
elif longest == len(longest_finnish_word):
    print("longest_finnish_word ")
else:
    print("strong_password")
