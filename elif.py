c_flag = True
ip4 = 0
ip6 = 1


if c_flag == True:
    print('flag')
    if ip4 == True:
        print('ip4')
    else:
        print('no ip4')
    if ip6 == True:
        print('ip6')
else:
    print('nothing')