from eudplib import *

mapSizeX = 256
mapSizeY = 256
tilesetInfo = EUDVArray(mapSizeX*mapSizeY)()
realTileInfo = EUDVArray(mapSizeX*mapSizeY)()
checkList = [
    [177,1],   #1 바다
]


def TilesetInit():
    checkX, checkY = [], []
    for i in range(0, len(checkList)):
        tempX,tempY = checkList[i][0], checkList[i][1]
        checkX.append(tempX)
        checkY.append(tempY)
    chkt = GetChkTokenized()
    MTXM = bytearray(chkt.getsection("MTXM"))
    for i in range(0,mapSizeX):
        for j in range(0,mapSizeY):
            index = mapSizeX*j + i
            l = index*2
            #realTileInfo[index] = MTXM[l] * 10000 + MTXM[l+1]
            for k in range(0, len(checkList)):
                if(MTXM[l] == checkX[k] and MTXM[l+1] == checkY[k]):
                    tilesetInfo[index] = k+1
                    break
