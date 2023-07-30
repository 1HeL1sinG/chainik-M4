def palindrom_check(str1):
    a = "".join(reversed(str1))
    if a == str1:
        return True
    else:
        return False
    

print(palindrom_check("abba"))