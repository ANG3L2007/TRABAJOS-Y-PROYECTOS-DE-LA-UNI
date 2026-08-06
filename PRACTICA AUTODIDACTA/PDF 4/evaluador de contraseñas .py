def extraer_tweet(tweet):
    cont = 0
    tweet_extraido = ""
    while cont !=len(tweet):
        
        if tweet[cont] == "#":
            while tweet[cont != " "]:
                tweet_extraido += tweet[cont]
                cont += 1
        else:
            tweet_extraido = "0"
        cont +=1
    return tweet_extraido

tweet = input("ingrese el tweet que desea extraer \n")
print(extraer_tweet(tweet))
