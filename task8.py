#!/usr/bin/env python3

import json

change = ["i","oraz","nigdy","dlaczego"]
changeOn = ["oraz","i","prawie nigdy","czemu"]

try:
    with open('texts/text_1.txt',"r",encoding="utf-8") as f:
        text = f.read().split(" ")
        div = dict()
        for letter in change:
            div[letter]= []
            for id,word in enumerate(text):
                if(word == letter):
                    div[letter].append(id)

        for letterId,letter in enumerate(change):
            for id in div[letter]:
                text[id]=changeOn[letterId]



        print("------------------------------------------------")
        text = " ".join(text)
        print(text)


except:
    print("No file with saved code")