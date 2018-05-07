def round_to_next5(n):
    if n % 5 == 0:
        return n
    elif n % 5 != 0:
        n = n + 1
        if n % 5 == 0:
            return n
        elif n % 5 != 0:
            n = n + 1
            if n % 5 == 0:
                return n
            elif n % 5 != 0:
                n = n + 1
                if n % 5 == 0:
                    return n
                elif n % 5 != 0:
                    n = n + 1
                    if n % 5 == 0:
                        return n

def round_to_next(n):
    return n if n%5 == 0 else round_to_next5(n+1)
