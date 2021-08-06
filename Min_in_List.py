def mins(a):
    "Hàm tìm số nhỏ nhất trong dãy số nhập vào"
    min_number = int(a[0])
    for i in range(1, len(a)):
     if min_number > int(a[i]):
      min_number = int(a[i])
    return(min_number)

def somacdinh():
    "Hàm nhập số ngẫu nhiên"
    import random
    print("Choose:")
    choice = str(input())
    if choice != '':
        NumList = random.sample(range(10,100), int(choice))
    else :
        NumList = random.sample(range(10,100), 5)
    #NumList = random.sample(range(10, 100), n)
    print(NumList)
    x = mins(NumList)
    print(x)

def Input():
    "Hàm nhập số từ bàn phím"
    ListNumber = (input("Enter numbers from the keyboard: "))
    print(ListNumber)
    #Hàm split() để cắt dãy giá trị thành các chuỗi con chứa từng giá trị số. Các chuỗi con được lưu thành danh sách
    inpu = ListNumber.split()
    #Hàm map() và hàm int để thực hiện việc ép kiểu các chuỗi giá trị số sang số nguyên
    lists = map(int,inpu)
    #Hàm min trả về phẩn tử lớn nhất.
    x = min(lists)
    print(x)

def main():
    print("Do you want to: \n 0. day so mac dinh  \n 1. nhap tu ban phim:")
    choose = int(input("Choose 0 or 1 :"))
    if choose == 0:
        somacdinh()
    else:
        Input()
 
#Cấu trúc chuẩn của python để gọi hàm. 
if __name__ == "__main__":
    main()



