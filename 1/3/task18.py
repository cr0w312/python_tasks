ch = int(input())
sot = ch // 100
des = ch % 100 // 10
ed = ch % 10
if (sot + des) >= (des + ed):
    print(str(sot + des) + str(des + ed))
elif (des + ed) >= (sot + des):
    print(str(des + ed) + str(sot + des))