# จากโจทย์เห็นว่ามี disks ทั้งหมด 4 ชิ้น ผู้เรียนกำหนดให้ disks ลำดับที่ 1 คือชิ้นเล็กที่สุด (และอยู่บนสุดตอนเริ่มต้น) และลำดับที่ 2,3,4 ไล่ลงไป

def tower_of_hanoi(disks, left, mid, right):  
    if(disks == 1):  
        print('เคลื่อน disk 1 จาก {} ไปที่ {}'.format(left, right))  
        return  
    tower_of_hanoi(disks - 1, left, right, mid)  
    print('เคลื่อน disk {} จาก {} ไปที่ {}'.format(disks, left, right))  
    tower_of_hanoi(disks - 1, mid, left, right)  
  
  
disks = 4  

tower_of_hanoi(disks, 'ซ้าย', 'กลาง', 'ขวา')   
