pay = int(input("Received payment ="))
kid = int(input("Number of kid ="))

if pay <3000:
    oldpay = (pay*0.18)+pay
    newpay = (pay*0.2)+pay

elif pay>=3000 and pay<4000:
    oldpay = (pay*0.17)+pay
    newpay = (pay*0.15)+pay

else:
    oldpay = (pay*0.14)+pay
    newpay = (pay*0.1)+pay

kidoldpapel=kid*90
kidnewpapel=kid*70

oldpara=oldpay+kidoldpapel
newpara=newpay+kidnewpapel

if oldpara>newpara:
    print("Eski zam üzerinden devam ediceksiniz, Maasiniz= {}".format(oldpara))

else:
    print("Yeni zam üzerinden devam ediceksiniz, Maasiniz= {}".format(newpara))
