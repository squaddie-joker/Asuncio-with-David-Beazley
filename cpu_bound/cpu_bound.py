# CPU bound functions

def fibbonachy(sequence_len: int) -> list:
    if sequence_len == 0:
        return None
    elif sequence_len == 1:
        return [0, ]
    elif sequence_len == 2:
        return [0, 1]
    elif sequence_len > 2:
        x1, x2 = [0, 1]
        result = [x1, x2]
        while sequence_len - 2:
            x3 = x1 + x2
            result.append(x3)
            x1, x2 = x2, x3
            sequence_len -= 1
        return result
