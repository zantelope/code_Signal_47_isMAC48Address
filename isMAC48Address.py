def isMAC48Address(inputString):

    ### split up string into elements between "-"
    splitString = inputString.split("-")

    ### if input string is incorrect length for a MAC address, return False
    if len(inputString) != 17:
        return False

    ### if string splits into incorrect number of elements, return False
    if len(splitString) != 6:
        return False
    
    ### for each element in splitString, check if element is a valid hex value. If it raises a valueError, return False 
    for i in range(len(splitString)):
      try:
        int(splitString[i], 16)
      except ValueError:
        return False

    ### if no problems with string, return True
    return True
