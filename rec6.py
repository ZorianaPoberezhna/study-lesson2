def recursive_dec_to_bin_converter(n):
    if n < 2:
        return str(n)
    else:
        return recursive_dec_to_bin_converter(n // 2) + str(n % 2)


result = recursive_dec_to_bin_converter(12)
