from tkinter import *

window = Tk()
window.title("Vücut kitle indeksi hesaplama")
window.minsize(400,400)



label1= Label(text= "lütfen kilonuzu giriniz. (kg)")
label1.pack()
entry1 =Entry()
entry1.get()
entry1.pack()

label2=Label(text="lütfen boyunuzu giriniz. (cm")
label2.pack()
entry2=Entry()
entry2.pack()
entry2.get()

def clicked():
    try:
        sonuç = ( float(entry1.get()) / ((float(entry2.get())) * 0.01) ** 2)
        label_sonuç = Label(text= f"beden kitle indeksiniz {round(sonuç)} olarak hesaplanmıştır.")
        label_sonuç.pack()

        if sonuç < 18.5:
            değer1 = Label(text= "Bu zayıf kategorisinde olduğunuz anlamına gelir.\n"
                        "Sağlığınız için biraz daha kilo almanız gerekebilir.")
            değer1.pack()
        elif sonuç >18.5 and sonuç < 24.9:
            değer2 =Label(text= "Bu normal kategorisinde olduğunuz anlamına gelir.\n"
                                "kilonuzu korumayı ihmal etmeyin")
            değer2.pack()
        elif sonuç>25 and sonuç <29.9:
            değer3 = Label(text="Bu fazla kilolu kategorisinde olduğunuz anlamına gelir.\n"
                                "sağlığınız için dikkat etmeye başlamalısınız.")
            değer3.pack()
        elif sonuç < 30 and sonuç <34.5:
            değer4 =Label(text="Bu obez-1 kategorisinde olduğunuz anlamına gelir.\n"
                               "sağlığınız için zayıflamanız gerekebilir.")
            değer4.pack()
        elif sonuç < 35 and 39.9:
            değer5 =Label (text= "Bu obez-2 kategorisinde olduğunuz anlamına gelir.\n"
                                  "sağlığınız için zayıflamanız gerekebilir.")
            değer5.pack()
        elif sonuç >40:
            değer6= Label(text="Bu obez-3 kategorisinde olduğunuz anlamına gelir.\n"
                               "sağlığınız için zayıflamanız gerekebilir.")
            değer6.pack()
    except:
        hata= Label(text="girdiğiniz değerlerde bir hata olabilir. \n"
                         "lütfen sayısal değerler girdiğinizden emin olun.")
        hata.pack()


button = Button(text="Hesapla", command= clicked)
button.pack()

window.mainloop()
