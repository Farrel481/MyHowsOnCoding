#IF ELSE STATEMENTS

#if {conditions}:
#    {code}

nilai = 6
#student lulus jika nilai >= 7

if nilai >= 7:
    print("Anda lulus!")
    print("Nilai Anda", nilai)
else:
    print("Anda TIDAK LULUS.")
    print("Nilai Anda", nilai)

x = 10
y = 1
if x is y:
    print("x sama dengan y ")
else:
    print("x tidak sama dengan y")

nama = "Farrel"
print(f"Hello nama saya {nama}!")

uas = 90
strata = "S1"
listCumlaude = ["S1", "S2", "S3"]

if uas >= 90:
    print(f"Selamat, anda lulus dengan nilai sempurna{uas}!")
    if strata in listCumlaude:
        print("Selamat anda lulus Cumlaude!")
elif uas >= 70 and uas < 90:
    print(f"Selamat anda lulus dengan nilai {uas}.")
else:
    print("Anda remedial.")


weekday = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
weekend = ["Sabtu", "Minggu"]
hari = "Senin"

if hari in weekday:
    print(f"Hari ini adalah weekday, yaitu {hari}.")
    
if hari in weekend:
    print(f"Hari ini adalah weekend, yaitu {hari}.")

match hari:
    case "Sabtu" | "Minggu":
        print("Hari ini Libur!")
    case _:
        print("Hari ini Bekerja!")