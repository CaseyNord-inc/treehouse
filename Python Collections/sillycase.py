def sillycase(string):
    half = len(string) // 2
    return string.lower()[:half] + string.upper()[half:]


test = "thisworks"
print(sillycase(test))
