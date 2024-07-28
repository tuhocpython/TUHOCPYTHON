"""
x = 5.2
y = 6
#print(x ## y)
"""
#x+y
#i+a
"""
#print (bool(2))
print(1 and 2) #Neu 1=True tra ve 2
print(0 and 1) # Neu 0=True thi tra ve 1 nguoc lai tra ve 0
print (1 ^ 0)
print (0 ^ 0)
print(7, 3, 4, sep="%", end='\n')
print(88)

#x = 10
#y = 0.5
#print(x/y)
#print (x//y)
# nếu số nguyên chia số nguyên thì ra phần nguyên
# nếu số nguyên chia số thực thì ra số thực

print (5 or 0)
# and
print (0 and 2) # phép and nếu giá trị đầu là true thì trả về giá trị 2
# nếu giá trị đầu là false thì lấy giá trị đầu.
print (1 ^ 2)
# phép xor tính trong hệ nhị phân
# 1 trong hệ nhị phân = 01
# 2 trong hệ nhị phân = 10
# xor = 0 khi 2 giá trị giống nhau, bằng 1 khi khác nhau
# > 1 xor 0 = 1
#   0 xor 1 = 1
# kết quả là 11 = 3 trong hệ thập phân trả về 3

#print (1 or 2)
#print (not 2)
"""
# Chuỗi
s = "hello world!"
print (s.upper() *3)
print (s.lower())
print (s.title())
t = 34
print(f"tôi đang {t} tuổi")
print ("tôi đang",t)
print ("toi dang "+ str(t))
print("i am {}".format(t)) # thay thế {} thành t

# INPUT nhập vào 1 chuỗi từ người dùng
"""user_name = input("Nhập tên người dùng: ")
print ("Tên người dùng của bạn là "+ str(user_name))

# đổi tiền
usd = float(input("Nhập số tiền usd bạn muốn đổi sang VND: "))
print (usd, "Usd bằng ", int(usd*24000), "vnd")
"""
#đếm số lượng ký tự trong chuỗi.
"""s = 334224534432
sl = str(s).count('3')
print (sl)
"""
# VẼ ĐỒ THỊ SỐ PHỨC
import matplotlib.pyplot as plt

# Tạo số phức
z = 3 + 4j

# Tọa độ của số phức
x = z.real
y = z.imag

# Vẽ mặt phẳng phức
plt.figure(figsize=(6, 6))
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)
plt.grid(True)

# Vẽ số phức
plt.plot(x, y, 'bo')  # 'bo' means blue color, circle marker
plt.text(x, y, f' {z}', fontsize=12, ha='left')

# Đặt tên trục và tiêu đề
plt.xlabel('Phần thực')
plt.ylabel('Phần ảo')
plt.title('Đồ thị của số phức trong mặt phẳng phức')

# Giới hạn trục
x = 3 + 4j
y = 3 + 4j

plt.plot(x, y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Plot')
plt.show()


