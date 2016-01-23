def cal_upper(price):
    increment = price * 0.3
    upper_price = price + increment
    return upper_price


def cal_upper_lower(price):
    offset = price * 0.3
    upper_price = price + offset;
    lower_price = price - offset;
    return upper_price, lower_price


def main():
    print(cal_upper(50000))
    result = cal_upper_lower(24240)
    print(type(result))


if __name__ == '__main__':
    main()
