def eh_palindromo(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]
