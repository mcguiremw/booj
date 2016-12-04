def truebooj(number):
    # do code here
    modulos_to_strings = {3: "**True**",
                          5: "**Booj**",
                          10: "**TrueBooj**"}
    mod_string_or_num = ''

    try:

        mod_string_or_num = '\n'.join(
            ['{}'.format(mod_string if (number % mod == 0) else mod_string_or_num)
             for (mod, mod_string) in sorted(modulos_to_strings.iteritems(), reverse=False)]).strip()

    except ZeroDivisionError as zde:
        return '{} :: {} : {} % {}'.format(str(zde), str(number), str(number), str(mod))

    return mod_string_or_num if mod_string_or_num else str(number)
