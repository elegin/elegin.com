#!/usr/bin/env python
import itertools
import base64

def rkcenc(s,k):
    ret = ""
    s = s.replace(" ","").upper()
    k = k.replace(" ","").upper()

    for i in range(0,min(len(k),len(s))):
        ret += chr((ord(s[i])-ord('A')+(ord(k[i%len(k)])-ord('A')))%26+ord('A'))
    return ret

def rkcdec(s,k):
    ret = ""
    s = s.replace(" ","").upper()
    k = k.replace(" ","").upper()

    for i in range(0,min(len(k),len(s))):
        ret += chr((ord(s[i])-ord('A')-(ord(k[i%len(k)])-ord('A')))%26+ord('A'))
    return ret

def ALPHA(s):
    return "".join(chr(int(s[i:i+2])+ord('A')) for i in range(0,len(s),2))

def ATBASH(s):
    s = s.upper().replace(" ","")
    return "".join(chr(ord('A') + ord('Z') - ord(c)) for c in s)

def rotN(s,n):
    s = s.upper().replace(" ","")
    return "".join(chr((ord(c) + n - ord('A')) % 26 + ord('A')) for c in s)

def xor(s,k):
    s = s.upper().replace(" ","")
    return "".join(chr(ord(s[i]) ^ ord(k[i])) for i in range(len(s)))

"""
Program
-- "Forewarned is fore armed"
    - 4 pips in this year's theme

-- First paragraphs
    - Fiddler on the Roof Prolouge
    - Text:
        "A hacker in the Vegas desert.. sounds crazy, no? But here at our little conference you might say every on of us is a hacker.  Trying to scratch out a leet, simple 0day without breaking too much crypto...
    - Play:
        "A fiddler on the roof... Sounds crazy, no? But here, in our little village of Anatevka, you might say every one of us is a fiddler on the foof.  Trying to scratch out a pleasant, simple tune without breaking his neck...

-- Keyword: HackerOnTheRoof
    - https://www.defcon.org/1o57/dc21/HackerOnTheRoof/
    -"Traditions!
    Seeing Everyone Come Out Near Defcon Helps All Learn Fun: (SECOND HALF)
    ydzcerxpfngmagycbjcfmapxbphogbfiyvtvyqtPEXUYXANFewmzfcxzbmhNtahrqnjyscbkdtqxjekcdmdhkkqnmdyepamcoxstutevfvpmmxrmximfsdwqhifsg"
"""
Hacker_On_The_Roof = "ydzcerxpfngmagycbjcfmapxbphogbfiyvtvyqtPEXUYXANFewmzfcxzbmhNtahrqnjyscbkdtqxjekcdmdhkkqnmdyepamcoxstutevfvpmmxrmximfsdwqhifsg"


"""
Cards -- (EXCEL)
-- 4 ciphers
    - Rotary (dt, xor)
        - Plain Alpha
        - Shift register ordering (111 to 111)
        - in the real order the first is the last be exclusive OR has it registered that tap at zero and one will be all the feedback you need in the real order (the first is the last)
        - Real Ordering: 111, 011, 001, 100, 010, 101, 110, 111
    - Skull (dt, e)
        - ROT13
        - E ordering
        - rot thirteen can be fun but sometimes leads astray try something else and you will see that finding answers may take you down paths not often repeated not all who wander are lost
        
    - Disk (lost, pi)
        - ROT13
        - Pi ordering
        - rot thirteen probably isn't right but this is fun right though his mind is not for rent don't put him down as arrogant his reserve a quiet defense riding out the days events catch the mist catch the myth catch the mystery catch the drift
            - "The River" is skipped 
            - River Song from Dr. Who
            
    - Keyhole (lost, gray decoder)
        - ROT13
        - Gray Code Ordering?
        - the skys will clear up not in black and white but shade of the bits help you turn this key x
        - 000, 100, 101, 111, 110, 010, 011, 001(, 000) //wtf kev 000,001,011,010,110,111,101,100
          000, 001, 011, 010, 110, 111, 101, 100
"""
rotary = {}
rotary[ 0 ] = "1907040508171819081819070411001819"
rotary[ 1 ] = "0813190704170400111417030417190704"
rotary[ 2 ] = "0508171819081819070411001819010404"
rotary[ 3 ] = "2302112018082104141707001808191704"
rotary[ 4 ] = "0608181904170403190700191900150019"
rotary[ 5 ] = "2504171400130314130422081111010400"
rotary[ 6 ] = "1111190704050404030100021024142013"
rotary[ 7 ] = "0404030813190704170400111417030417"

smiley = {}
smiley[ 0 ] = "04010606202104061717001513001417180700"
smiley[ 1 ] = "1407060501251706212517052417131605130506041311"
smiley[ 2 ] = "06041105012517062021001917240517"
smiley[ 3 ] = "13001611010709212424051717"
smiley[ 4 ] = "062013061821001621001913000509170405"
smiley[ 5 ] = "2513110613231711010716010900"
smiley[ 6 ] = "021306200500010601180617000417021713061716"
smiley[ 7 ] = "00010613242409200109130016170413041724010506"

floppy = {}
floppy[ 0 ] = "04010606202104061717000204011413142411210500060421192006"
floppy[ 1 ] = "1407060620210521051807000421192006"
floppy[ 2 ] = "06200107192020210525210016210500010618010404170006"
floppy[ 3 ] = "160100060207062021251601090013051304040119130006"
floppy[ 4 ] = "2021050417051704081713030721170616171817000517"
floppy[ 5 ] = "04211621001901070606201716131105170817000605"
floppy[ 6 ] = "151306152006201725210506151306152006201725110620"
floppy[ 7 ] = "15130615200620172511050617041115130615200620171604211806"

crypto = {}
crypto[ 0 ] = "062017052311050921"
crypto[ 1 ] = "242415241713040702"
crypto[ 2 ] = "000106210014241315"
crypto[ 3 ] = "231300160920210617"
crypto[ 4 ] = "140706052013161701"
crypto[ 5 ] = "180620171421060520"
crypto[ 6 ] = "172402110107060704"
crypto[ 7 ] = "000620210523171110"

print " ============ Simple Suit Decryptions: ============ "
print "Rotary Suit"
print "".join(ALPHA(rotary[x]) for x in range(0,8))
print
print "Smiley Suit"
print "".join(rotN(ALPHA(smiley[x]),13) for x in range(0,8))
print
print "Floppy Suit"
print "".join(rotN(ALPHA(floppy[x]),13) for x in range(0,8))
print
print "Crypto Suit"
print "".join(rotN(ALPHA(crypto[x]),13) for x in range(0,8))
print

"""
Key Hole Sign
    - "SEARCHING FOR ANOTHER CLUE
    THE KING OF KEY HOLES MAY HELP
    REFLECT ON WHAT YEAR THIS DEFCON IS
    YOULL FIND THE ZONE BSIDE YOU
    BASS YOUR KEYWORD NOT ON A QUIET STOP BUT THE REAL ONE WITHIN
    AND WITHOUT SPACE OF COURSE"

    - Rush album 2112 -> Twilight Zone (on BSide) -> Based on Twilight zone episodes -> WillTheRealMartianPleaseStandUp
    - https://defcon.org/1o57/dc21/WillTheRealMartianPleaseStandUp/
        -Finally I Realize Special Timing Hinders All L0sT Finalists: (FIRST HALF)
        Aehpylqvskflmavmgecestnpevcutblsuqbckgemegduqgbfaewwjsnfxtkkdsswspkvqdjzotb 
"""
Will_The_Real_Matian_Please_Stand_Up = "Aehpylqvskflmavmgecestnpevcutblsuqbckgemegduqgbfaewwjsnfxtkkdsswspkvqdjzotb"

longcipher = Will_The_Real_Matian_Please_Stand_Up + Hacker_On_The_Roof
print len(longcipher)


gray_code_order = [0,1,3,2,6,7,5,4] #Keyhole
shift_reg_order = [7,3,1,4,2,5,6,0] #Rotary
e_order = [2,7,1,4,5,0,3,6] #Smiley
pi_order = [3,1,4,5,2,6,7,0] #Floppy


rotary_key = "".join(ALPHA(rotary[x]) for x in shift_reg_order)
smiley_key = "".join(rotN(ALPHA(smiley[x]),13) for x in e_order)
floppy_key = "".join(rotN(ALPHA(floppy[x]),13) for x in pi_order)
crypto_key = "".join(rotN(ALPHA(crypto[x]),13) for x in gray_code_order)

# Pad with X
while len(rotary_key) < len(longcipher):
    rotary_key += "X"

while len(smiley_key) < len(longcipher):
    smiley_key += "X"

while len(floppy_key) < len(longcipher):
    floppy_key += "X"

while len(crypto_key) < len(longcipher):
    crypto_key += "X"

print "Key Parts:"
print "ROTARY:",rotary_key
print "SMILEY:",smiley_key
print "FLOPPY:",floppy_key
print "CRYPTO:",crypto_key




"""
Jack Sign Ciphers

        

    - 74 (J) (ATBASH)
        - EVENIFYOUWANTTOBELIEVEONEOFTHEJACKSDOESNTBEL
    - 65 (A) (ATBASH)
        - ONGDONTOUTFOXTHEMJUSTSCULLYALONGIFYOUASKTHEY
    - 81 (C) (ATBASH)
        - MIGHTLOANYOUAKEYTHEYTOOARELOOKINGFORLEEANDNO
    - 75 (K) (ATBASH)
        - TANAGRAMICALLYSPEAKING
        
    - Together:
        - EVEN IF YOU WANT TO BELIEVE ONE OF THE JACKS DOESNT BELONG DONT OUT FOX THEM
        JUST SCULLY ALONG IF YOU ASK THEY MIGHT LOAN YOU A KEY THEY TOO ARE LOOKING FOR
        LEE AND NOT ANAGRAMICALLY SPEAKING
            - Fox and Scully == X Files; Lone gunman

    -Which jack dosen't belong?
        - Guy Fawks
    -How are the remaining three related?
        - The Lone Gunman (Conspiracy Theorist"
        - Lois Runtz == Femme Fatale rival of lone gunman
    - https://www.defcon.org/1o57/dc21/LoisRuntz/
        "Having trouble with the first and second half?
        Well, put on your key suit and OTP your disc...but that's not all..."

"""
Signs = {'J':'EVENIFYOUWANTTOBELIEVEONEOFTHEJACKSDOESNTBEL',
         'A':'ONGDONTOUTFOXTHEMJUSTSCULLYALONGIFYOUASKTHEY',
         'C':'MIGHTLOANYOUAKEYTHEYTOOARELOOKINGFORLEEANDNO',
         'K':'TANAGRAMICALLYSPEAKING'}
Signs_Order = ['J','A','C','K']


lois = [rkcenc(crypto_key,floppy_key)]



"""
Floor Ciphers
    - Planetary cipher
        - Decode accoding to Couting rods? (figured out w/o wiki)
        - Alternate orientation, lines == 1, bar == 5, o = 0
        - "DEFCON21KEYWORDORRERY"
        - https://www.defcon.org/1o57/dc21/orrery/
        - "It was a sign that Lois was trying to help you, but you weren't finished.
        Take what Lois gave you and OTP with your Smiley suit.
        (But you're not done yet!)"
        - AcidBurn.jpg (Queen of Disk)
"""


orrery = [rkcenc(l,smiley_key) for l in lois]

 


"""
    - Boxes cipher
        - Decode according to "Chain of Death" cipher 2
        - "KEYWORDHOMODOXIAN"
        - https://www.defcon.org/1o57/dc21/homodoxian/
        - "Well, Lois and the solar clock must have helped, but you were missing one thing...
        Take what the solar clock showed and OTP that with your rotary suit, then by golly you've got a key."
        - JackSmiles.jpg (Jack of Smiles)
"""

homodoxian = [rkcenc(o,rotary_key) for o in orrery]

print "Answer:"
for h in homodoxian:
    print rkcdec(longcipher,h)

"""
Long Cipher Decryption:
HOPE YOUVE BEEN HAVING FUN AND YOUVE MET SOME NEW AND INTERESTING PEOPLE
BUT YOU HAVENT FINISHED YOUR JOURNEY YET
YOU NEED TO SEND EMAIL TO DEFCONDJSTEPHANIEANDMICHELLE AT GMAIL
BE SURE TO INCLUDE YOUR BEST CON MOMENT AND THEY LOVE PICTURES

Solution:  E-mail sent to DefconFullHouse@gmail.com

Response:

Final Puzzle
The uber badges were given to 1o57 by the timelords.  They used sonic encoding as a BASSis for passing to us this information.  But it will take 4 to find the truth.  They call the Ubers by their age, such as "<age> badge".  

Bring 1o57 the true age of the Uber badges, written on red paper.  

Oh, and don't forget, the time lords kept their time in seconds.  1o57 can't deal with numbers that large (14 digits? too big!) So please name the Uber in YEARS (6 digits is so much more manageable).
"""

"""
Lanyard Cipher
    - Music notes (bass cleff)
    - ADD A DEAD ACE BADGE

    - Easter eggs:
        - The classic suit symbols (hearts, diamonds, clubs, spades)
        - The Enigma machine
"""

lanyard = "ADDADEADACEBADGE"
print "Time Lord Age (seconds):",int(lanyard.replace("BADGE",""),16)
print "Years:",int(lanyard.replace("BADGE",""),16) / (60 * 60 * 24 * 365)


"""
Misc
Lost's Sign Cipher
    - Decode according to "Chain of Death" cipher 1
    - Circles -- Must turn page periodically to read correct symbols
    - "HAVE FUN NEED HELP JUST ASK PASSCODE SYZYGY"
"""
                      
lost_sign = "syzygy"


"""
Unsolved mysteries

- DT vs LOST badges
    - Rotary and Smiley suits have DT highlighted on their reverse
    - Floppy and Keyhole suits have Lost highlighted

- Crypto and Hacker badges
    - Lost and DarkTangent each had their own badges depicting themselves
    - The reverse of these badges had the Gallafrayan name of The Doctor (from dr. who)

- Doctor Who tie-ins
    - Dr. Who's name is written in Gallafrayan on the reverse of the Uber, Hacker, and Crypto badges
    - In the simple decryption of the Floppy suit, the line "the river" is skipped
        - River Song is said to be the only person who knows the doctor's real name

- The Labyrinth
    - Lost wore a shirt depicting The Labyrinth (with David Bowie)

- Other floor art
    - No apparent crypto hidden

- Solar Clock Cipher
    - Depicts two positions with 1057 written in sticks and rods
    - One with a keyhole in the middle, the other without a keyhole
    - PunkAB's theory: 15 suit symbols (~45 deg) separate the two holes.
        - Rotating the dial 45 deg would also align the clock hands
            - Hour hand at 9, minute hand at 12 (Coincidentally, 9:00pm == 21:00)
        - Also, if viewing the cipher as a depiction of a lock, the large floppy planet would act as a counter weight
        
"""


                                 
