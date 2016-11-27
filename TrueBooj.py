def truebooj(number):
    # do code here

    # Decided to map the divisor to the string in a dictionary so that future
    #   development would be easier by adding new KVPs
    modulos_to_strings = {3: "**True**",
                          5: "**Booj**",
                          10: "**TrueBooj**"}
    # Creating the string to be returned here so that it stays in scope to be returned
    #   after it is formatted by the logic below
    mod_string_or_num = ''

    # Decided to loop through the dictionary for ease of future development, I am also
    #   making sure that the dictionary is sorted by the keys and not read in reverse
    #   so that the print statements are arranged in relation to numerical order of
    #   its divisor in the dictionary.
    for mod, mod_string in sorted(modulos_to_strings.iteritems(), reverse=False):
        try:
        	# Here is where I am constructing the string to be returned.  I will
        	#   concatenate all of the string statements for the even divisors of the
        	#   number being passed in by the caller.
            mod_string_or_num = mod_string_or_num +\
            					mod_string + '\n' if (number % mod == 0) else\
            					mod_string_or_num
        # This was mostly present for debugging, but I left it in the odd case that 0
        #  finds its way into the keys for the dictionary.        
        except ZeroDivisionError as zde:
            return str(zde) + ':: ' + str(number) + ' : ' + str(number) + ' % ' + str(mod)

    # Checking the string to be returned to validate that it has been set with an even
    #   divisor's string statement.  If it has not than just return the number passed in
    return mod_string_or_num.strip() if mod_string_or_num else str(number)