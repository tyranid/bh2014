# Simple script to export a GUID under the current cursor selection
# (c) James Forshaw 2014

guid = ScreenEA()

if guid != BADADDR:
    data1 = Dword(guid)
    data2 = Word(guid+4)
    data3 = Word(guid+6)    
    data4 = []
    
    for i in range(8):
        #data4 += "%02X" % Byte(guid+8+i)
        data4.append(Byte(guid+8+i))
        
    name = Name(guid)
    
    print "// %08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X%02X%02X" % (data1, data2, data3, data4[0], data4[1], data4[2], data4[3], data4[4], data4[5], data4[6], data4[7])
    print 'const GUID %s = { 0x%08X, 0x%04X, 0x%04X, {0x%02X,0x%02X,0x%02X,0x%02X,0x%02X,0x%02X,0x%02X,0x%02X } };' % (name, data1, data2, data3, data4[0], data4[1], data4[2], data4[3], data4[4], data4[5], data4[6], data4[7])
    
    