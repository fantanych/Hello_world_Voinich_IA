choice = input("Куда пойдешь? (направо/налево/прямо): ").strip().lower()

if choice == "направо":
 print("жизнь потеряешь")
elif choice == "налево":
 print( "коня потеряешь")
elif choice == "прямо":
 print("жив будешь")
else:
 print("Остаешься на месте.")