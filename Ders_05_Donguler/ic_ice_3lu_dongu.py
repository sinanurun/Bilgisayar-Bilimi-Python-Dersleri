# ABC harflerinin farklı permütasyonu:
for ilk in "ABC":
    for ikinci in "ABC":
        if ikinci != ilk:
            for ucuncu in "ABC":
                if ucuncu != ilk and ucuncu != ikinci:
                    print(ilk + ikinci + ucuncu)