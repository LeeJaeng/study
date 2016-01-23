def cal_upper(price):
    increment = price * 0.3
    upper = price + increment
    return upper


def cal_lower(price):
    decrement = price * 0.3
    lower = price + decrement
    return lower


author = "pystock"
