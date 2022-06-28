N_pakkarnmuang = int(input())
all_data = []

for N in range(N_pakkarnmuang):
    VDC = input("")
    VDC_list = [int(x) for x in VDC.split(" ")]
    all_data.append(VDC_list)

#cal_by_1
total_cal_by_1 = 0

for V in all_data:
    total_cal_by_1 = total_cal_by_1+V[0]

total_cal_by_1 = total_cal_by_1/500

#cal_by_2
total_sor_sor_after567  = []
total_sor_sor_before567  = []
for V in all_data:
    total_sor_sor_before567.append(V[0]/total_cal_by_1)

#check_by_5
total_sor_sor_party_list = 0
for C in all_data:
    total_sor_sor_party_list = total_sor_sor_party_list + C[2]

quota_left = 0
for D in range(len(all_data)):
    if all_data[D][1] >= total_sor_sor_before567[D]:
        total_sor_sor_after567.append(all_data[D][1])
        to_quota = all_data[D][1] - total_sor_sor_before567[D]
        quota_left = quota_left+to_quota
    else:
        # สูตรนี้ยังอาจจะมี quota เกิน (2) ต้องเขียน if แก้ก่อนใช้
        total_sor_sor_after567.append(total_sor_sor_before567[D]+(quota_left*(all_data[D][2]/total_sor_sor_party_list)))

