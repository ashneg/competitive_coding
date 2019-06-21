def is_leap(n):
    leap = False;
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
    # Write your logic here
    
    return leap
