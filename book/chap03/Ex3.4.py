int_list = [ 12, 120, 100, 20, 24, 56, 20, 32, 556, 176, 116 ]

def division_even_count( ary, cnt=0 ):
    flg = True
    conv_list = ary

    for i in conv_list:
        if i % 2:
            flg =  False

    if flg:
        conv_list = list(map(lambda val: val // 2, conv_list))
        return division_even_count(conv_list, cnt+1)
    else:
        return cnt


res = division_even_count(int_list)
print(res)

