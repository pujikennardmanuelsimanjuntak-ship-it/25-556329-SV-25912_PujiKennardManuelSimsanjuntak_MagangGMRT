#Guna import ini menjadi library untuk sin,cos,acos,atan2 dan konversi sudut
import math

print("------------------------MENU------------------------")

#Variable adalah panjang segmen (cm), yang di tentukan dengan NIU dan NIF
femur = 29
tibia = 12

print("pilih 1 (Forward Kinematics) atau pilih 2 (Invers_Kinematics)")
pilihan = input("Pilihan:")

if pilihan == "1":
    print("------------------Forward_Kinematics------------------")

    #Code ini dapat menentukan pilihan sudut servo dari study case yang di inginkan dengan mengubah angka
    sudut1_deg = (float(input("Masukkan sudut Servo 1 (derajat):")))
    sudut2_deg = (float(input("Masukkan sudut Servo 2 (derajat):")))

    #sin dan cos di python itu memakai radian, jadi derajat di konversi dulu memakai math.radians
    sudut1_rad = (math.radians(sudut1_deg))
    sudut2_rad = (math.radians(sudut2_deg))

    #x1,y1 adalah posisi lutut: ujung femur dari pangkal dengan sudut θ₁
    x1 =(femur) * math.cos(sudut1_rad)
    y1 =(femur) * math.sin(sudut1_rad)

    #x2,y2 adalah end-effector: posisi lutut di tambah tibia, arah tibia= θ₁ + θ₂
    x2 = x1 + (tibia) * math.cos(sudut1_rad + sudut2_rad)
    y2 = y1 + (tibia) * math.sin(sudut1_rad + sudut2_rad)

    #Print ini dapat menampilkan hasil posisi FK, dengan :.3f mengambil 3 angka desimal
    print(f"Lutut: x = {x1:.3f}, y = {y1:.3f}")
    print(f"End-effector: x = {x2:.3f}, y = {y2:.3f}")


elif pilihan == "2":
    print("------------------Invers_Kinematics------------------")

    #Variabel ini dapat di isi manual target posisi end-effector yang sesuai di tentukan study case
    target_x = (float(input("Masukan target x =")))
    target_y = (float(input("Masukan target y =")))

    a = (tibia)
    b = (femur)
    #C jarak pangkal ke target atau end-effector, dari Pythagoras di kertas
    c = math.sqrt(target_x**2 + target_y**2)

    #Mengikuti rumus di kertas hukum cosinus untuk sudut C
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)

    if cos_C < -1 or cos_C > 1:
        print("Target ini di luar jangkauan, jarak harus antara 17 dan 41 cm")
    else:

        #acos menghasilkan radian, di ubah ke derajat
        sudut_C = math.degrees(math.acos(cos_C))
        sudut2_ik = 180 - sudut_C

        #Alpha adalah arah pangkal ke arah target dari sumbu x; atan2 aman kalau x=0
        tan_α = math.degrees(math.atan2(target_y,target_x))

        #Beta sudut di pangkal antara garis ke target dan femur
        cos_β = (b**2 + c**2 - a**2) / (2 * b * c)
        sudut_β = math.degrees(math.acos(cos_β))

        #Rumusnya θ₁ = alpha - beta
        sudut1_ik = tan_α - sudut_β

        #Print ini dapat menampilkan sudut servo IK, :.2f atau :.3f membantu mengambil digit desimal di belakang koma
        print(f"Hasil Sudut C = {sudut_C:.3f}")
        print(f"Hasil Sudut α = {tan_α:.3f}")
        print(f"Hasil Sudut β = {sudut_β:.3f}")
        print(f"Hasil θ₁ = {sudut1_ik:.2f}")
        print(f"Hasil θ₂ = {sudut2_ik:.2f}")

else:
    print("pilihan tidak valid")
