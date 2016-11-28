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

    try:
        # Here is where I am building the string to be returned.  This seems to be more Pythonic
        #   than the previous version, but this is more difficult to read.  
        #
        # What I am accomplishing with this join statement is writing all of the dictionary
        #   values to a string when the number passed in is evenly divisible by the current key
        #   of the dictionary during any iteration of the loop.  I then strip all whitespace so
        #   that if the number is not evenly divisible by any of the keys in the dictionary than
        #   number will be printed in the check at the return statement for the function.
        mod_string_or_num = '\n'.join(
            ['%s' % (mod_string if (number % mod == 0) else mod_string_or_num)
             for (mod, mod_string) in sorted(modulos_to_strings.iteritems(), reverse=False)]).strip()

    # This was mostly present for debugging, but I left it in the odd case that 0
    #  finds its way into the keys for the dictionary.
    except ZeroDivisionError as zde:
        return '{} :: {} : {} % {}'.format(str(zde), str(number), str(number), str(mod))

    # Checking the string to be returned to validate that it has been set with an even
    #   divisor's string statement.  If it has not than just return the number passed in
    return mod_string_or_num if mod_string_or_num else str(number)
