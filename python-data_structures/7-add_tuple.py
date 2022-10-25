#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    nmb_1 = tuple_a + ('0', '0')
    nmb_2 = tuple_b + ('0', '0')

    rslt_1 = int(nmb_1[0]) + int(nmb_2[0])
    rslt_2 = int(nmb_1[1]) + int(nmb_2[1])

    return (rslt_1, rslt_2)
