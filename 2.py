branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\n--- Chi nhánh {branch} ---")
    
    total_students = 0 

    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count
        
    print(f"Chi nhánh {branch}: {total_students} học viên")
    '''
    nguyên nhân gây ra lỗi logic "cộng dồn sai tổng học viên giữa các chi nhánh" là do 
    vị trí đặt biến total_students = 0 . Vì biến này đang được khởi tạo ở bên ngoài cả 
    2 vòng lặp nên giá trị của nó không hề được reset về $0$ khi chương trình chuyển 
    sang một chi nhánh mới
    '''