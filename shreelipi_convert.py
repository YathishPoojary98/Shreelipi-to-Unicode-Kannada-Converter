import sys
from shreelipi_map import *

ambiguous_chars = {}
ambiguous_chars[('ÊÜ','¿')] = ["á",'Þ','æá','æáà','æáç','æã','æãà']
ambiguous_chars['ÃÜ']=['æá','æáà','æáç','æã','æãà']
ambiguous_chars[('æ','ÃÜæká','ÃÜækã','±Üæä','¶Üæä','ÃÜæ','ÊÜæä')]= ['à','ç','ã','ãà']
ambiguous_chars[('Q','U','X','\\','b','e','i','Äká','q','t','w','{','~','£','¦','©','˜','¯','²','µ','¹')] = ['à']
ambiguous_chars[('¼','Àá','Ä','È','Ë','Î','Ñ','Ô','×','Ú','ü')] = ['à']
ambiguous_chars[('ÃÜ','ÃÜæ')]=['ká','æ','kã']
ambiguous_chars['Ä']=['ká']
ambiguous_chars[('±Ü','¶Ü','ÊÜ')]=['â','ä','æ']
ambiguous_chars[('±Üæ','¶Üæ','ÊÜæ')]=['â','ä','à','ç']
ambiguous_chars['Ë']=['á','áà']
ambiguous_chars['Áá','Áã']=['à','ç']
#ambiguous_chars['Q'] = ['Ò']

ottakshara_chars = ['Ò','R','V','Y','^','`','c','f','j','l','n','r','u','x','z','¡','¤','§','ª','œ','°','³',
                   'º','½','¾','Â','Å','É','Ì','Ï','Õ','Ø','Û','ó','÷','ð','ô','õ','ö','ø','ù','ú','¢']
special_chars = ['ಾ','ಿ','ೀ','ು','ೂ','ೃ','ೆ','ೇ','ೈ','ೊ','ೋ', 'ೌ','ಂ', 'ಃ','್']

ottakshara_kannada = [shreelipi_unicode[i] for i in ottakshara_chars]

def handle_ottakshara(val):
    #print(f"Val passed : {val}")
    temp = val.copy()
    if len(temp)<=3:
        return temp
    for i in range(1,len(val)-1):
        if temp[i]=='್' and temp[i-1] in special_chars:
            t = temp[i-1]
            temp[i-1],temp[i] = temp[i],temp[i+1]
            temp[i+1] = t
    #print(f"Val returned by handle_ottakshara : {temp}")
    return temp
    
    
def handle_arka(val):
    #print(f"Val passed to handle_arka : {val}")
    temp = val.copy()
    if len(temp)<3:
        return temp
    for i in range(1,len(val)-1):
        if temp[i]=='ರ' and temp[i+1]=='್':
            if temp[i-2:i] in ottakshara_kannada:
                j = 0
                if temp[i-4:i-2] in ottakshara_kannada:
                    j = 2
                if temp[i-3-j] in special_chars:
                    exchange = temp[i-4-j:i]
                    temp[i-4-j:i-2-j] = ['ರ','್']
                    temp[i-2-j:i+2] = exchange
                else:
                    exchange = temp[i-3-j:i]
                    temp[i-3-j:i-1-j] = ['ರ','್']
                    temp[i-1-j:i+2] = exchange
            elif temp[i-1] in special_chars:
                #print("Inside if")
                exchange_pair = temp[i-2:i]
                temp[i-2],temp[i-1] = temp[i],temp[i+1]
                temp[i:i+2] = exchange_pair
            else:
                #print("Inside else")
                exchange_char = temp[i-1]
                temp[i-1],temp[i] = temp[i],temp[i+1]
                temp[i+1] = exchange_char
    #print(f"Handle arka returned : {temp}")
    return temp
    
    
def func1(val):
    #print(f"Func1 val : {val}")
    #print(f"Ottakshara Kannada : {ottakshara_kannada}")
    temp = val.copy()
    for i in range(0,len(val)-2):
        #print(val[i+1:i+3])
        if temp[i]=='್' and temp[i+1:i+3] in ottakshara_kannada:
            t = temp[i+2]
            temp[i+2] = temp[i+1]
            temp[i+1] = t
    #print(f"Func1 returned : {temp}")
    return temp
    
from bisect import bisect_left
chars_to_replace = {'P':'PÜ','T':'S','W':'WÜ','[':'Z','a':'aÜ','d':'dÜ','h':'g','Ã':'ÃÜ','p':'o','s':'sÜ','v':'vÜ',
                   'y':'yÜ','O':'|','ñ':'ñÜ','¥':'¥Ü','¨':'¨Ü','«':'«Ü','®':'®Ü','±':'±Ü','¶':'¶Ü','¸':'Ÿ','»':'»Ü',
                   'Ê':'ÊÜ','Ã':'ÃÜ','Ç':'Æ','Í':'ÍÜ','´':'¶','Ð':'ÐÜ','Ó':'ÓÜ','Ö':'ÖÜ','Ù':'ÙÜ','û':'ûÜ','†':'Å',
                   '$':''}
def found(s):
    keys = sorted(shreelipi_unicode.keys())
    for key in keys:
        if key.startswith(s):
            return True
    else:
        return False
        
        
def convert(word):
    replace_list = {'N':'[æ','„':'ç','ææ':'æ','Œ':'÷','é':'Â','$':'','™':'\\','å':'á','Üç':'Üæç','Ýç':'æç'}
    for i in replace_list.keys():
        word = word.replace(i,replace_list[i])
        #print(f"Word : {word}")
    converted_chars = []
    chars = [char for char in word]
    for i in range(len(chars)-1):
        if chars[i]=="¿" and chars[i+1]=="å":
            chars[i+1]="á"
        if chars[i]=="Ü" and chars[i+1]=="Ü":
            chars[i+1]=""
        if chars[i] in ottakshara_chars:
            if chars[i+1]=='à':
                chars[i],chars[i+1] = chars[i+1],chars[i]
        if chars[i]=="ç" and chars[i-1]!="æ":
            if chars[i-2]=='æ':
                a = "æ"
                chars[i-2],chars[i-1]=chars[i-1],a
            elif chars[i-3]=='æ':
                a = "æ"
                chars[i-3],chars[i-2]=chars[i-2],chars[i-1]
                chars[i-1]=a
                
    #print(f"Input chars : {chars}")
    for c in chars_to_replace.keys():
        for i in range(len(chars)-1):
            if chars[i]==c and chars[i+1]!=chars_to_replace[c].replace(c,""):
                chars[i]=chars_to_replace[c]
    i = 0
    ambiguous_dict_keys = []
    for key in ambiguous_chars.keys():
        if type(key)==tuple:
            for z in key:
                ambiguous_dict_keys.append(z)
        else:
            ambiguous_dict_keys.append(key)
    #print(ambiguous_dict_keys)
    temp_arka = []
    while(i<len(chars)):
        #print("Here")
        key = chars[i]
        #print(f"Key : {key}")
        while(key not in shreelipi_unicode.keys() and found(key) and i<len(chars)-1):
            #print("Here1")
            i+=1
            #print(i)
            key+=chars[i]
            #print(f"Key : {key}")
        stop=0
        while (stop!=1):
            key_found = 0
            val_found=0
            #print(f"Key now : {key}")
            if key not in ambiguous_dict_keys:
                #print("Break")
                break
            for k in ambiguous_chars.keys():
                #print(f"Key Test : {key}")
                if type(k)==tuple:
                    #print(f"Testing tuple : {k} with key : {key}")
                    if key in k:
                        #print("Match Found")
                        key_found = 1
                        vals = sorted(ambiguous_chars[k], key=lambda x: len(x), reverse=True)
                else:
                    if key==k:
                        #print("Match Found")
                        key_found = 1
                        vals = sorted(ambiguous_chars[k], key=lambda x: len(x), reverse=True)
                if key_found == 1:
                    key_found=0
                    #print(f"Key : {key}, vals : {vals}")
                    val_found = 0
                    for x in vals:
                        #print(f"x : {x}")
                        if "".join(chars[i+1:]).startswith(x):
                            #print(f"Key to test : {key}")
                            #print("Starts")
                            #print(x)
                            #print(f"Key 1 : {key}")
                            key+=x
                            #print(f"Key 2 : {key}")
                            #print(f"Stop value : {stop}")
                            i+=len(x)
                            val_found=1
                            break
            if val_found==0:
                #print(f"Stopping for key : {key}")
                stop=1

        #print(key)
        #print(len(key))
        if key in shreelipi_unicode.keys():
            #print(f"Key to convert : {key}")
            val = shreelipi_unicode[key]
            if len(val)==1:
                val_list = [i for i in val[0]]
                converted_chars+=val_list
                #print(f"Converted in if : {converted_chars}")
            else:
                val_list = shreelipi_unicode[key]
                converted_chars+=val_list
                if key in ottakshara_chars and key!='ì':
                    #print("func1 called")
                    converted_chars = func1(converted_chars)
                if key=="ì":
                    #print(f"Temp begining : {temp_arka}")
                    #print(f"Length of temp : {len(temp_arka)}")
                    #print(f"Val Passed : {converted_chars[len(temp_arka):]}")
                    test_chars= handle_arka(converted_chars[len(temp_arka):])
                    #print(f"Test chars : {test_chars}")
                    temp_arka += test_chars
                    #print(f"Temp : {temp_arka}")
                    #print(f"Length of temp : {len(temp_arka)}")
                    #print("Here")
                    converted_chars = []
                    converted_chars+= temp_arka
                    #print(f"Temp : {temp_arka}")
                
            
        else:
            converted_chars+=[key]

        key=''
        i=i+1    
    converted_chars = handle_ottakshara(converted_chars)
    #converted_chars = handle_arka(converted_chars)
    #print(f"chars at end : {converted_chars}")    
    #print("".join(converted_chars))
    return "".join(converted_chars)
    
    
def convert_text(data):
    words = data.split(" ")
    res = [convert(word) for word in words]
    res1 = " ".join(res)
    print(res1)
    #return res1
	
with open(sys.argv[1],"r") as f:
	data = f.read()
	
convert_text(data)


