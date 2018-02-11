s = "Hayatta En Hakiki Mürşit İlimdir"
print(s)
print(len(s))
for i in range(len(s)):
 print("[", s[i], "]", sep="", end="")
print() # Yeni satır başı
for ch in s:
 print("<", ch, ">", sep="", end="")
print() # Yeni satır başı