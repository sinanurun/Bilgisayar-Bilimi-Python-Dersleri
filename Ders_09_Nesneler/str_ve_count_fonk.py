# Ön ve arka plandaki boşlukları ve sayaç alt dizilerini ayırır
s = " ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ "
print("[", s, "]", sep="")
s = s.strip()
print("[", s, "]", sep="")
# Alt dizinin sayılarını sayar “BCD”
print(s.count("BCD"))