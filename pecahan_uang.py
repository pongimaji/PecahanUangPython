uang = int(input('masukan jumlah uang: '))
uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
array_pecahan = ['100rb', '50rb', '20rb', '10rb','5rb', '2rb', '1rb', '500', '200', '100']
jumlah_pecahan = {}
sisa = uang
no=0
print('Input uang {},  Pecahan yang kita butuhkan yaitu: '.format(uang))
for pecahan in uang_pecahan:
    no+=1
    if sisa < pecahan:
        continue
    banyak_pecahan = int(sisa / pecahan)
    sisa = sisa - ( pecahan * banyak_pecahan )
    print('Pecahan {} : {}'.format(array_pecahan[no-1], banyak_pecahan))
    
