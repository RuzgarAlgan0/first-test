devam = True
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }
while devam:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        # Kelime eşleşiyorsa ne yapmalıyız?
        print(meme_dict[word])
        continue
    else:
        # Kelime eşleşmiyorsa ne yapmalıyız?
        print("İçerikte yok.")
        break
