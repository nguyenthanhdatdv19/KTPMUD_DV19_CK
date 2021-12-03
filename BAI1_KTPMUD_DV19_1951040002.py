print("Bài tập kiểm tra cuối kỳ - Bài 1 - Phần 1")
 
def Kiemtra(arr):
    count = 0
    for i in arr:
        if(i<2):
            count=count+1
        else:
            for j in range (2,i-1):
                if(i%j==0 and j<i):
                    count= count+1
                    break
    return len(arr)-count
a = [1,5,6,3]
print('Tổng số lượng số nguyên tố trong mảng là:') 
print(Kiemtra(a))