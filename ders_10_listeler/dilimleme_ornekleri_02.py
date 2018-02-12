lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:5]=["a", "b", "c"] #[30, 40, 50] değerleri ["a", "b", "c"] değerleri ile değiştiriliyor
print(lst)
print("-------------------")
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:6]=["a","b"] #[30, 40, 50, 60] değerleri ["a", "b"] değerleri ile değiştiriliyor
print(lst)
print("-------------------")
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:2]=["a", "b", "c"] # 2 nolu indexten başlayarak ["a", "b", "c"] değerleri ekleniyor
print(lst)
print("-------------------")
lst=[10,20,30,40,50,60,70,80]
print(lst) # Liste yazdırılıyor
lst[2:5]=[] # [30, 40, 50] değerleri yerine [] atanıyor. (değerler siliniyor)
print(lst)