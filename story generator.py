import random
when = ['A few years ago','Yesterday','A long time ago','On 20th Jan','Last night']
who = ['a rabbit','a cat','a turtle','an elephant','a mouse']
name = ['Ali','Miriam','Naruto','Sasuke','Kakashi']
residence = ['Konohagakure','Sunagakure','Kirigakure','Tetsugakure','Amegakure']
went = ['a cinema','a BTS concert','a Legoland','an Anime Village','a market']
happened = ['made a lot of friends','solved a mystery','had fun','found a secret key','went into the Animeverse']
print(random.choice(when)+','+random.choice(who)+' named '+random.choice(name)+' who lived in '+random.choice(residence)+' went to '+random.choice(went)+' and '+random.choice(happened))