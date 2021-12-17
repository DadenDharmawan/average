avg = eval(input('Masukkan banyaknya angka: '))
x = 0
for j in range(avg):
    nilai = eval(input(f'Masukkan nilai ke-{j+1}: '))
    x += nilai
bagi = x / avg
print(bagi)