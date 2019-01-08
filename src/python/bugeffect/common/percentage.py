from decimal import Decimal


def diff(v1, v2):
    if isinstance(v1, Decimal):
        dv1 = v1
    else:
        dv1 = Decimal(v1)

    if isinstance(v2, Decimal):
        dv2 = v2
    else:
        dv2 = Decimal(v2)

    return (dv1 - dv2) / dv1 * 100
