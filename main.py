def main():
    msg = '''RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE
    RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
    AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE
    ACKXRRCIJ EJEKSZCNHE.
    AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE
    XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
    TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE
    HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
    DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI
    PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
    PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI
    ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
    TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI
    AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
    HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI
    E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE.'''
    
    spletterfrequency = {"e,a,o,l,s,n,d,r,u,i,t,c,p,m,y,q,b,h,g,f,v,j,ñ,z,x,k,w"}
    decrypt(msg,spletterfrequency)

def decrypt(msg,spletterfrequency):
    words = msg.split()
    lettercount = {}
    for i in words:
        for l in i:
            if l.isalpha():
                if l in lettercount:
                    lettercount[l] += 1
                else:
                    lettercount[l] = 1
    
    orderedletters = sorted(lettercount,key = lettercount.get,reverse = True)
    
    print("usage count of each letter:")
    print(lettercount)
    print("\n")
    
    print("usage of each letter in text ordered:")
    print(orderedletters)
    print("usage of each letter in spanish ordered:")
    print(spletterfrequency)
    print("\n")
    
    a,b = input("Insert letter to change:\n").split()
    i = 0
    while i >= 0:
        change = orderedletters.index(a.upper())
        if i == 0:
            msgdecrypt = msg.replace(orderedletters[change],b)
            i += 1
        else:
            msgdecrypt = msgdecrypt.replace(orderedletters[change],b)
        print(msgdecrypt)
        a,b = input("Insert letter to change:\n").split()
    
    
#execution
if __name__ == "__main__":
    main()