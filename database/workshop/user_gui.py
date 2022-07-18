import tkinter as tk

main_root = tk.Tk()
main_root.title("หน้าจอหลัก (สร้างขึ้นโดยนายชานนทร์ เหลืองประเสริฐ)")
main_root.geometry("1500x1000")
main_root.configure(background='light gray')

# ส่วนของการเพิ่มข้อมูล #
def create_insert_window():
    insert_root = tk.Tk()
    insert_root.title("หน้าจอเพิ่มข้อมูล")
    insert_root.geometry("1500x1000")
    insert_root.configure(background='light gray')

    client_field = tk.Label(insert_root,text="ข้อมูลของลูกค้า สำหรับ id ควรใส่เป็นชื่อหอพักต่อด้วยลำดับเช่น ก001")
    client_field.grid(row=0 , column=0 , columnspan=2)

    client_id_label = tk.Label(insert_root,text="ใส่ id ลูกค้า: ")
    client_id_label.grid(row=1 , column=0)
    client_id_input = tk.Entry(insert_root)
    client_id_input.grid(row=1 , column=1 , pady=2)

    client_name_label = tk.Label(insert_root,text="ใส่ชื่อและนามสกุลลูกค้า: ")
    client_name_label.grid(row=2 , column=0)
    client_name_input = tk.Entry(insert_root)
    client_name_input.grid(row=2 , column=1 , pady=2)


    insert_root.mainloop()
# ส่วนของการเพิ่มข้อมูล #

# ส่วนของการเพิ่มข้อมูล #
insert_button = tk.Button(main_root,text="กดเพื่อเพิ่มข้อมูล",command=create_insert_window)
insert_button.grid(row=0 , column=0)
# ส่วนของการเพิ่มข้อมูล #


# ส่วนของการแก้ข้อมูล #
updte_button = tk.Button(main_root,text="กดเพื่อ update ข้อมูล")
updte_button.grid(row=1 , column=0)
# ส่วนของการแก้ข้อมูล #


main_root.mainloop()