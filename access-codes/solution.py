# OK, the dancing rabbit was pretty cool.

# Attempting to follow style guide. https://www.python.org/dev/peps/pep-0008/


def _reverse(string):
    return string[::-1]


def _get_palindrome_with_lower_half_first(access_code):
    reversed_access_code = _reverse(access_code)
    if reversed_access_code < access_code:
        return reversed_access_code + access_code
    return access_code + reversed_access_code


def answer(x):
    distinct_palindromes = set()
    for access_code in x:
        distinct_palindromes.add(
            _get_palindrome_with_lower_half_first(access_code))
    return len(distinct_palindromes)
