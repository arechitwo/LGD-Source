from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x66450C, Add, -512),# units:Graphics  index:21    from 80 To 78
        SetMemory(0x66450C, Add, 7208960),# units:Graphics  index:22    from 86 To 196
        SetMemory(0x664520, Add, 77),# units:Graphics  index:40    from 1 To 78
        SetMemory(0x664520, Add, 3932160),# units:Graphics  index:42    from 12 To 72
        SetMemory(0x664524, Add, 4849664),# units:Graphics  index:46    from 4 To 78
        SetMemory(0x664524, Add, 1828716544),# units:Graphics  index:47    from 0 To 109
        SetMemory(0x66452C, Add, 122),# units:Graphics  index:52    from 4 To 126
        SetMemory(0x66452C, Add, 10496),# units:Graphics  index:53    from 8 To 49
        SetMemory(0x664530, Add, 7),# units:Graphics  index:56    from 7 To 14
        SetMemory(0x664530, Add, 22528),# units:Graphics  index:57    from 12 To 100
        SetMemory(0x664534, Add, -9699328),# units:Graphics  index:62    from 185 To 37
        SetMemory(0x664534, Add, -2315255808),# units:Graphics  index:63    from 187 To 49
        SetMemory(0x664538, Add, 536870912),# units:Graphics  index:67    from 45 To 77
        SetMemory(0x664540, Add, 512),# units:Graphics  index:73    from 41 To 43
        SetMemory(0x664540, Add, -754974720),# units:Graphics  index:75    from 46 To 1
        SetMemory(0x664544, Add, 553648128),# units:Graphics  index:79    from 45 To 78
        SetMemory(0x664548, Add, 34),# units:Graphics  index:80    from 43 To 77
        SetMemory(0x664548, Add, 8448),# units:Graphics  index:81    from 47 To 80
        SetMemory(0x664548, Add, 553648128),# units:Graphics  index:83    from 47 To 80
        SetMemory(0x66454C, Add, 10092544),# units:Graphics  index:86    from 37 To 191
        SetMemory(0x66454C, Add, 536870912),# units:Graphics  index:87    from 45 To 77
        SetMemory(0x664550, Add, -35),# units:Graphics  index:88    from 43 To 8
        SetMemory(0x664550, Add, -29184),# units:Graphics  index:89    from 115 To 1
        SetMemory(0x664550, Add, -2490368),# units:Graphics  index:90    from 116 To 78
        SetMemory(0x664554, Add, -31744),# units:Graphics  index:93    from 198 To 74
        SetMemory(0x664554, Add, -9961472),# units:Graphics  index:94    from 199 To 47
        SetMemory(0x664554, Add, -1778384896),# units:Graphics  index:95    from 114 To 8
        SetMemory(0x664584, Add, 11),# units:Graphics  index:140    from 32 To 43
        SetMemory(0x6645A0, Add, -7),# units:Graphics  index:168    from 66 To 59
        SetMemory(0x6645A4, Add, -262144),# units:Graphics  index:174    from 68 To 64
        SetMemory(0x6645A8, Add, 352321536),# units:Graphics  index:179    from 43 To 64
        SetMemory(0x6645AC, Add, 21),# units:Graphics  index:180    from 43 To 64
        SetMemory(0x6645AC, Add, 5376),# units:Graphics  index:181    from 43 To 64
        SetMemory(0x6645AC, Add, 1376256),# units:Graphics  index:182    from 43 To 64
        SetMemory(0x6645B0, Add, 5376),# units:Graphics  index:185    from 43 To 64
        SetMemory(0x6645B0, Add, 1376256),# units:Graphics  index:186    from 43 To 64
        SetMemory(0x6645B0, Add, 352321536),# units:Graphics  index:187    from 43 To 64
        SetMemory(0x6645B4, Add, -16777216),# units:Graphics  index:191    from 43 To 42
        SetMemory(0x6645B8, Add, -1),# units:Graphics  index:192    from 43 To 42
        SetMemory(0x6645B8, Add, -256),# units:Graphics  index:193    from 43 To 42
        SetMemory(0x6645C4, Add, -27904),# units:Graphics  index:205    from 173 To 64
        SetMemory(0x6645C4, Add, -7208960),# units:Graphics  index:206    from 174 To 64
        SetMemory(0x6645C4, Add, -1862270976),# units:Graphics  index:207    from 175 To 64
        SetMemory(0x6645C8, Add, -112),# units:Graphics  index:208    from 176 To 64
        SetMemory(0x6645C8, Add, -7602176),# units:Graphics  index:210    from 180 To 64
        SetMemory(0x6645C8, Add, -1979711488),# units:Graphics  index:211    from 182 To 64
        SetMemory(0x6645CC, Add, -117),# units:Graphics  index:212    from 181 To 64
        SetMemory(0x6645CC, Add, -30464),# units:Graphics  index:213    from 183 To 64
        SetMemory(0x6645D0, Add, -21760),# units:Graphics  index:217    from 128 To 43
        SetMemory(0x6645D4, Add, -53),# units:Graphics  index:220    from 131 To 78
        SetMemory(0x6645D4, Add, -13824),# units:Graphics  index:221    from 132 To 78
        SetMemory(0x6645D4, Add, -1526726656),# units:Graphics  index:223    from 134 To 43
        SetMemory(0x6645D8, Add, -92),# units:Graphics  index:224    from 135 To 43
        SetMemory(0x6645D8, Add, -23808),# units:Graphics  index:225    from 136 To 43
        SetMemory(0x6645D8, Add, -6160384),# units:Graphics  index:226    from 137 To 43
        SetMemory(0x6645D8, Add, -1593835520),# units:Graphics  index:227    from 138 To 43
        SetMemory(0x661158, Add, -44),# units:Construction Animation  index:42    from 44 To 0
        SetMemory(0x66116C, Add, -2),# units:Construction Animation  index:47    from 2 To 0
        SetMemory(0x661180, Add, -15),# units:Construction Animation  index:52    from 15 To 0
        SetMemory(0x661184, Add, -31),# units:Construction Animation  index:53    from 31 To 0
        SetMemory(0x661190, Add, 25),# units:Construction Animation  index:56    from 27 To 52
        SetMemory(0x661194, Add, 283),# units:Construction Animation  index:57    from 44 To 327
        SetMemory(0x6611EC, Add, 0),# units:Construction Animation  index:79    from 0 To 0
        SetMemory(0x66137C, Add, -325),# units:Construction Animation  index:179    from 325 To 0
        SetMemory(0x661380, Add, -325),# units:Construction Animation  index:180    from 325 To 0
        SetMemory(0x661384, Add, -325),# units:Construction Animation  index:181    from 325 To 0
        SetMemory(0x661388, Add, -325),# units:Construction Animation  index:182    from 325 To 0
        SetMemory(0x661394, Add, -325),# units:Construction Animation  index:185    from 325 To 0
        SetMemory(0x661398, Add, -325),# units:Construction Animation  index:186    from 325 To 0
        SetMemory(0x66139C, Add, -325),# units:Construction Animation  index:187    from 325 To 0
        SetMemory(0x660604, Add, -2097152),# units:Unit Direction  index:22    from 32 To 0
        SetMemory(0x66061C, Add, 1245184),# units:Unit Direction  index:46    from 13 To 32
        SetMemory(0x660628, Add, -3328),# units:Unit Direction  index:57    from 13 To 0
        SetMemory(0x6606C0, Add, 2097152),# units:Unit Direction  index:210    from 0 To 32
        SetMemory(0x6647B0, Add, 1),# units:Shield Enable  index:0    from 0 To 1
        SetMemory(0x6647B0, Add, 256),# units:Shield Enable  index:1    from 0 To 1
        SetMemory(0x6647B0, Add, 65536),# units:Shield Enable  index:2    from 0 To 1
        SetMemory(0x6647B8, Add, 1),# units:Shield Enable  index:8    from 0 To 1
        SetMemory(0x6647B8, Add, 65536),# units:Shield Enable  index:10    from 0 To 1
        SetMemory(0x6647BC, Add, 1),# units:Shield Enable  index:12    from 0 To 1
        SetMemory(0x6647C0, Add, 1),# units:Shield Enable  index:16    from 0 To 1
        SetMemory(0x6647C0, Add, 256),# units:Shield Enable  index:17    from 0 To 1
        SetMemory(0x6647C0, Add, 16777216),# units:Shield Enable  index:19    from 0 To 1
        SetMemory(0x6647C4, Add, 1),# units:Shield Enable  index:20    from 0 To 1
        SetMemory(0x6647C4, Add, 256),# units:Shield Enable  index:21    from 0 To 1
        SetMemory(0x6647CC, Add, 1),# units:Shield Enable  index:28    from 0 To 1
        SetMemory(0x6647CC, Add, 256),# units:Shield Enable  index:29    from 0 To 1
        SetMemory(0x6647D0, Add, 1),# units:Shield Enable  index:32    from 0 To 1
        SetMemory(0x6647D4, Add, 256),# units:Shield Enable  index:37    from 0 To 1
        SetMemory(0x6647D4, Add, 65536),# units:Shield Enable  index:38    from 0 To 1
        SetMemory(0x6647D4, Add, 16777216),# units:Shield Enable  index:39    from 0 To 1
        SetMemory(0x6647D8, Add, 1),# units:Shield Enable  index:40    from 0 To 1
        SetMemory(0x6647D8, Add, 16777216),# units:Shield Enable  index:43    from 0 To 1
        SetMemory(0x6647E0, Add, 1),# units:Shield Enable  index:48    from 0 To 1
        SetMemory(0x6647E0, Add, 16777216),# units:Shield Enable  index:51    from 0 To 1
        SetMemory(0x6647E4, Add, 256),# units:Shield Enable  index:53    from 0 To 1
        SetMemory(0x6647E4, Add, 65536),# units:Shield Enable  index:54    from 0 To 1
        SetMemory(0x6647E4, Add, 16777216),# units:Shield Enable  index:55    from 0 To 1
        SetMemory(0x6647E8, Add, 1),# units:Shield Enable  index:56    from 0 To 1
        SetMemory(0x6647EC, Add, -1),# units:Shield Enable  index:60    from 1 To 0
        SetMemory(0x6647EC, Add, -16777216),# units:Shield Enable  index:63    from 1 To 0
        SetMemory(0x664804, Add, -1),# units:Shield Enable  index:84    from 1 To 0
        SetMemory(0x664810, Add, 16777216),# units:Shield Enable  index:99    from 0 To 1
        SetMemory(0x664814, Add, 1),# units:Shield Enable  index:100    from 0 To 1
        SetMemory(0x664814, Add, 65536),# units:Shield Enable  index:102    from 0 To 1
        SetMemory(0x664818, Add, 1),# units:Shield Enable  index:104    from 0 To 1
        SetMemory(0x664848, Add, 0),# units:Shield Enable  index:154    from 1 To 1
        SetMemory(0x664848, Add, -16777216),# units:Shield Enable  index:155    from 1 To 0
        SetMemory(0x66484C, Add, 0),# units:Shield Enable  index:156    from 1 To 1
        SetMemory(0x66484C, Add, -256),# units:Shield Enable  index:157    from 1 To 0
        SetMemory(0x66484C, Add, -16777216),# units:Shield Enable  index:159    from 1 To 0
        SetMemory(0x664850, Add, -1),# units:Shield Enable  index:160    from 1 To 0
        SetMemory(0x664850, Add, -65536),# units:Shield Enable  index:162    from 1 To 0
        SetMemory(0x664850, Add, -16777216),# units:Shield Enable  index:163    from 1 To 0
        SetMemory(0x664854, Add, -1),# units:Shield Enable  index:164    from 1 To 0
        SetMemory(0x664854, Add, -256),# units:Shield Enable  index:165    from 1 To 0
        SetMemory(0x664854, Add, -65536),# units:Shield Enable  index:166    from 1 To 0
        SetMemory(0x664854, Add, -16777216),# units:Shield Enable  index:167    from 1 To 0
        SetMemory(0x664858, Add, 1),# units:Shield Enable  index:168    from 0 To 1
        SetMemory(0x664858, Add, -256),# units:Shield Enable  index:169    from 1 To 0
        SetMemory(0x664858, Add, -65536),# units:Shield Enable  index:170    from 1 To 0
        SetMemory(0x664858, Add, -16777216),# units:Shield Enable  index:171    from 1 To 0
        SetMemory(0x66485C, Add, -1),# units:Shield Enable  index:172    from 1 To 0
        SetMemory(0x664880, Add, 256),# units:Shield Enable  index:209    from 0 To 1
        SetMemory(0x660E00, Add, 1),# units:Shield Amount  index:0    from 0 To 1
        SetMemory(0x660E00, Add, 65536),# units:Shield Amount  index:1    from 0 To 1
        SetMemory(0x660E04, Add, 1),# units:Shield Amount  index:2    from 0 To 1
        SetMemory(0x660E04, Add, 65536),# units:Shield Amount  index:3    from 0 To 1
        SetMemory(0x660E50, Add, 1),# units:Shield Amount  index:40    from 0 To 1
        SetMemory(0x660E94, Add, 840),# units:Shield Amount  index:74    from 80 To 920
        SetMemory(0x660F34, Add, 5750),# units:Shield Amount  index:154    from 750 To 6500
        SetMemory(0x660F38, Add, -299),# units:Shield Amount  index:156    from 300 To 1
        SetMemory(0x660F40, Add, -500),# units:Shield Amount  index:160    from 500 To 0
        SetMemory(0x660F50, Add, 6500),# units:Shield Amount  index:168    from 0 To 6500
        SetMemory(0x662350, Add, 413440),# units:Hit Points  index:0    from 10240 To 423680
        SetMemory(0x662354, Add, 308480),# units:Hit Points  index:1    from 11520 To 320000
        SetMemory(0x662358, Add, 462592),# units:Hit Points  index:2    from 20480 To 483072
        SetMemory(0x66235C, Add, 451072),# units:Hit Points  index:3    from 32000 To 483072
        SetMemory(0x662364, Add, 345600),# units:Hit Points  index:5    from 38400 To 384000
        SetMemory(0x6623C8, Add, 345600),# units:Hit Points  index:30    from 38400 To 384000
        SetMemory(0x6623D8, Add, 261120),# units:Hit Points  index:34    from 15360 To 276480
        SetMemory(0x6623F0, Add, 504320),# units:Hit Points  index:40    from 7680 To 512000
        SetMemory(0x662408, Add, 491520),# units:Hit Points  index:46    from 20480 To 512000
        SetMemory(0x662424, Add, 466432),# units:Hit Points  index:53    from 40960 To 507392
        SetMemory(0x662478, Add, 1141760),# units:Hit Points  index:74    from 10240 To 1152000
        SetMemory(0x6624DC, Add, 280320),# units:Hit Points  index:99    from 51200 To 331520
        SetMemory(0x6625B8, Add, 1472000),# units:Hit Points  index:154    from 192000 To 1664000
        SetMemory(0x6625C0, Add, 635392),# units:Hit Points  index:156    from 76800 To 712192
        SetMemory(0x6625D0, Add, 384000),# units:Hit Points  index:160    from 128000 To 512000
        SetMemory(0x6625F0, Add, 1152000),# units:Hit Points  index:168    from 512000 To 1664000
        SetMemory(0x662658, Add, -25344000),# units:Hit Points  index:194    from 25600000 To 256000
        SetMemory(0x663158, Add, -14),# units:Elevation Level  index:8    from 18 To 4
        SetMemory(0x663158, Add, -3072),# units:Elevation Level  index:9    from 16 To 4
        SetMemory(0x663158, Add, -201326592),# units:Elevation Level  index:11    from 16 To 4
        SetMemory(0x66315C, Add, -12),# units:Elevation Level  index:12    from 16 To 4
        SetMemory(0x663164, Add, -3584),# units:Elevation Level  index:21    from 18 To 4
        SetMemory(0x663164, Add, -786432),# units:Elevation Level  index:22    from 16 To 4
        SetMemory(0x66316C, Add, -12),# units:Elevation Level  index:28    from 16 To 4
        SetMemory(0x663178, Add, -234881024),# units:Elevation Level  index:43    from 18 To 4
        SetMemory(0x66317C, Add, -14),# units:Elevation Level  index:44    from 18 To 4
        SetMemory(0x66317C, Add, 786432),# units:Elevation Level  index:46    from 4 To 16
        SetMemory(0x663180, Add, 786432),# units:Elevation Level  index:50    from 4 To 16
        SetMemory(0x663184, Add, 14),# units:Elevation Level  index:52    from 4 To 18
        SetMemory(0x663184, Add, -234881024),# units:Elevation Level  index:55    from 18 To 4
        SetMemory(0x663188, Add, -14),# units:Elevation Level  index:56    from 18 To 4
        SetMemory(0x663188, Add, -786432),# units:Elevation Level  index:58    from 16 To 4
        SetMemory(0x66318C, Add, -917504),# units:Elevation Level  index:62    from 18 To 4
        SetMemory(0x663194, Add, -201326592),# units:Elevation Level  index:71    from 16 To 4
        SetMemory(0x663198, Add, -12),# units:Elevation Level  index:72    from 16 To 4
        SetMemory(0x66319C, Add, -16777216),# units:Elevation Level  index:79    from 4 To 3
        SetMemory(0x6631A0, Add, -14),# units:Elevation Level  index:80    from 18 To 4
        SetMemory(0x6631A0, Add, -786432),# units:Elevation Level  index:82    from 16 To 4
        SetMemory(0x6631A8, Add, -14),# units:Elevation Level  index:88    from 18 To 4
        SetMemory(0x6631A8, Add, 3072),# units:Elevation Level  index:89    from 4 To 16
        SetMemory(0x6631A8, Add, 786432),# units:Elevation Level  index:90    from 4 To 16
        SetMemory(0x6631AC, Add, 3072),# units:Elevation Level  index:93    from 4 To 16
        SetMemory(0x6631AC, Add, -917504),# units:Elevation Level  index:94    from 18 To 4
        SetMemory(0x6631AC, Add, 201326592),# units:Elevation Level  index:95    from 4 To 16
        SetMemory(0x6631B0, Add, -917504),# units:Elevation Level  index:98    from 18 To 4
        SetMemory(0x6631B4, Add, -786432),# units:Elevation Level  index:102    from 16 To 4
        SetMemory(0x6631B4, Add, 201326592),# units:Elevation Level  index:103    from 4 To 16
        SetMemory(0x6631DC, Add, 12),# units:Elevation Level  index:140    from 4 To 16
        SetMemory(0x6631E0, Add, 201326592),# units:Elevation Level  index:147    from 4 To 16
        SetMemory(0x6631E4, Add, 12),# units:Elevation Level  index:148    from 4 To 16
        SetMemory(0x663228, Add, 3072),# units:Elevation Level  index:217    from 4 To 16
        SetMemory(0x66322C, Add, 786432),# units:Elevation Level  index:222    from 4 To 16
        SetMemory(0x66322C, Add, 201326592),# units:Elevation Level  index:223    from 4 To 16
        SetMemory(0x663230, Add, 12),# units:Elevation Level  index:224    from 4 To 16
        SetMemory(0x663230, Add, 3072),# units:Elevation Level  index:225    from 4 To 16
        SetMemory(0x663230, Add, 786432),# units:Elevation Level  index:226    from 4 To 16
        SetMemory(0x663230, Add, 201326592),# units:Elevation Level  index:227    from 4 To 16
        SetMemory(0x660FDC, Add, -12910592),# units:Unknown (old Movement)  index:22    from 197 To 0
        SetMemory(0x661000, Add, -50432),# units:Unknown (old Movement)  index:57    from 197 To 0
        SetMemory(0x661018, Add, -132),# units:Unknown (old Movement)  index:80    from 197 To 65
        SetMemory(0x661084, Add, 1090519040),# units:Unknown (old Movement)  index:191    from 0 To 65
        SetMemory(0x661088, Add, 65),# units:Unknown (old Movement)  index:192    from 0 To 65
        SetMemory(0x661088, Add, 16640),# units:Unknown (old Movement)  index:193    from 0 To 65
        SetMemory(0x661098, Add, 12648448),# units:Unknown (old Movement)  index:210    from 0 To 193
        SetMemory(0x661098, Add, 3238002688),# units:Unknown (old Movement)  index:211    from 0 To 193
        SetMemory(0x66109C, Add, 193),# units:Unknown (old Movement)  index:212    from 0 To 193
        SetMemory(0x66109C, Add, 49408),# units:Unknown (old Movement)  index:213    from 0 To 193
        SetMemory(0x663DD0, Add, 1),# units:Rank/Sublabel  index:0    from 2 To 3
        SetMemory(0x663DD0, Add, -131072),# units:Rank/Sublabel  index:2    from 6 To 4
        SetMemory(0x663DD0, Add, -33554432),# units:Rank/Sublabel  index:3    from 7 To 5
        SetMemory(0x663DD4, Add, 67108864),# units:Rank/Sublabel  index:7    from 1 To 5
        SetMemory(0x663DD8, Add, -720896),# units:Rank/Sublabel  index:10    from 12 To 1
        SetMemory(0x663DD8, Add, -67108864),# units:Rank/Sublabel  index:11    from 9 To 5
        SetMemory(0x663DDC, Add, -13),# units:Rank/Sublabel  index:12    from 15 To 2
        SetMemory(0x663DE0, Add, -16),# units:Rank/Sublabel  index:16    from 18 To 2
        SetMemory(0x663DE0, Add, -2560),# units:Rank/Sublabel  index:17    from 13 To 3
        SetMemory(0x663DE0, Add, -218103808),# units:Rank/Sublabel  index:19    from 17 To 4
        SetMemory(0x663DE4, Add, 6),# units:Rank/Sublabel  index:20    from 17 To 23
        SetMemory(0x663DE4, Add, -983040),# units:Rank/Sublabel  index:22    from 15 To 0
        SetMemory(0x663DE4, Add, -234881024),# units:Rank/Sublabel  index:23    from 19 To 5
        SetMemory(0x663DE8, Add, -3584),# units:Rank/Sublabel  index:25    from 19 To 5
        SetMemory(0x663DEC, Add, -15),# units:Rank/Sublabel  index:28    from 20 To 5
        SetMemory(0x663DEC, Add, -4864),# units:Rank/Sublabel  index:29    from 21 To 2
        SetMemory(0x663DF0, Add, -1),# units:Rank/Sublabel  index:32    from 4 To 3
        SetMemory(0x663DF0, Add, 131072),# units:Rank/Sublabel  index:34    from 3 To 5
        SetMemory(0x663DF4, Add, -512),# units:Rank/Sublabel  index:37    from 5 To 3
        SetMemory(0x663DF8, Add, 256),# units:Rank/Sublabel  index:41    from 4 To 5
        SetMemory(0x663DF8, Add, -83886080),# units:Rank/Sublabel  index:43    from 10 To 5
        SetMemory(0x663DFC, Add, -16777216),# units:Rank/Sublabel  index:47    from 6 To 5
        SetMemory(0x663E00, Add, -8),# units:Rank/Sublabel  index:48    from 15 To 7
        SetMemory(0x663E00, Add, -3328),# units:Rank/Sublabel  index:49    from 15 To 2
        SetMemory(0x663E00, Add, -134217728),# units:Rank/Sublabel  index:51    from 16 To 8
        SetMemory(0x663E04, Add, -13),# units:Rank/Sublabel  index:52    from 15 To 2
        SetMemory(0x663E04, Add, -1536),# units:Rank/Sublabel  index:53    from 15 To 9
        SetMemory(0x663E04, Add, -327680),# units:Rank/Sublabel  index:54    from 15 To 10
        SetMemory(0x663E04, Add, -67108864),# units:Rank/Sublabel  index:55    from 15 To 11
        SetMemory(0x663E08, Add, -3840),# units:Rank/Sublabel  index:57    from 15 To 0
        SetMemory(0x663E08, Add, -720896),# units:Rank/Sublabel  index:58    from 16 To 5
        SetMemory(0x663E0C, Add, -1792),# units:Rank/Sublabel  index:61    from 12 To 5
        SetMemory(0x663E0C, Add, -655360),# units:Rank/Sublabel  index:62    from 12 To 2
        SetMemory(0x663E0C, Add, -100663296),# units:Rank/Sublabel  index:63    from 9 To 3
        SetMemory(0x663E10, Add, 5),# units:Rank/Sublabel  index:64    from 0 To 5
        SetMemory(0x663E10, Add, 2304),# units:Rank/Sublabel  index:65    from 3 To 12
        SetMemory(0x663E10, Add, 589824),# units:Rank/Sublabel  index:66    from 4 To 13
        SetMemory(0x663E10, Add, -100663296),# units:Rank/Sublabel  index:67    from 6 To 0
        SetMemory(0x663E14, Add, -7),# units:Rank/Sublabel  index:68    from 9 To 2
        SetMemory(0x663E14, Add, -1792),# units:Rank/Sublabel  index:69    from 7 To 0
        SetMemory(0x663E14, Add, -117440512),# units:Rank/Sublabel  index:71    from 10 To 3
        SetMemory(0x663E18, Add, -6),# units:Rank/Sublabel  index:72    from 11 To 5
        SetMemory(0x663E18, Add, 1024),# units:Rank/Sublabel  index:73    from 1 To 5
        SetMemory(0x663E18, Add, -720896),# units:Rank/Sublabel  index:74    from 12 To 1
        SetMemory(0x663E1C, Add, -3),# units:Rank/Sublabel  index:76    from 17 To 14
        SetMemory(0x663E1C, Add, 512),# units:Rank/Sublabel  index:77    from 13 To 15
        SetMemory(0x663E1C, Add, 131072),# units:Rank/Sublabel  index:78    from 14 To 16
        SetMemory(0x663E1C, Add, 16777216),# units:Rank/Sublabel  index:79    from 16 To 17
        SetMemory(0x663E20, Add, 12),# units:Rank/Sublabel  index:80    from 12 To 24
        SetMemory(0x663E20, Add, -1792),# units:Rank/Sublabel  index:81    from 12 To 5
        SetMemory(0x663E20, Add, -786432),# units:Rank/Sublabel  index:82    from 17 To 5
        SetMemory(0x663E20, Add, -50331648),# units:Rank/Sublabel  index:83    from 5 To 2
        SetMemory(0x663E24, Add, -458752),# units:Rank/Sublabel  index:86    from 12 To 5
        SetMemory(0x663E24, Add, 67108864),# units:Rank/Sublabel  index:87    from 16 To 20
        SetMemory(0x663E28, Add, 10),# units:Rank/Sublabel  index:88    from 12 To 22
        SetMemory(0x663E30, Add, -393216),# units:Rank/Sublabel  index:98    from 8 To 2
        SetMemory(0x663E34, Add, -3),# units:Rank/Sublabel  index:100    from 22 To 19
        SetMemory(0x663E34, Add, 1310720),# units:Rank/Sublabel  index:102    from 0 To 20
        SetMemory(0x663E38, Add, 6),# units:Rank/Sublabel  index:104    from 15 To 21
        SetMemory(0x663E38, Add, 327680),# units:Rank/Sublabel  index:106    from 0 To 5
        SetMemory(0x663E68, Add, 65536),# units:Rank/Sublabel  index:154    from 0 To 1
        SetMemory(0x663E7C, Add, 100663296),# units:Rank/Sublabel  index:175    from 0 To 6
        SetMemory(0x662EAC, Add, 34816),# units:Comp AI Idle  index:13    from 20 To 156
        SetMemory(0x662EB4, Add, 10092544),# units:Comp AI Idle  index:22    from 2 To 156
        SetMemory(0x662EBC, Add, 4096),# units:Comp AI Idle  index:29    from 2 To 18
        SetMemory(0x662EC8, Add, 105),# units:Comp AI Idle  index:40    from 2 To 107
        SetMemory(0x662ECC, Add, 1048576),# units:Comp AI Idle  index:46    from 2 To 18
        SetMemory(0x662ED4, Add, 0),# units:Comp AI Idle  index:52    from 2 To 2
        SetMemory(0x662EE4, Add, -2147483648),# units:Comp AI Idle  index:71    from 130 To 2
        SetMemory(0x662EF4, Add, -8388608),# units:Comp AI Idle  index:86    from 130 To 2
        SetMemory(0x662F80, Add, 59),# units:Comp AI Idle  index:224    from 97 To 156
        SetMemory(0x662274, Add, 768),# units:Human AI Idle  index:13    from 20 To 23
        SetMemory(0x66227C, Add, 1376256),# units:Human AI Idle  index:22    from 2 To 23
        SetMemory(0x662284, Add, 4096),# units:Human AI Idle  index:29    from 2 To 18
        SetMemory(0x662290, Add, 105),# units:Human AI Idle  index:40    from 2 To 107
        SetMemory(0x662294, Add, 1048576),# units:Human AI Idle  index:46    from 2 To 18
        SetMemory(0x66229C, Add, 0),# units:Human AI Idle  index:52    from 2 To 2
        SetMemory(0x6622A0, Add, -17920),# units:Human AI Idle  index:57    from 93 To 23
        SetMemory(0x6622AC, Add, -2147483648),# units:Human AI Idle  index:71    from 130 To 2
        SetMemory(0x6622BC, Add, -8388608),# units:Human AI Idle  index:86    from 130 To 2
        SetMemory(0x6622C4, Add, -10747904),# units:Human AI Idle  index:94    from 166 To 2
        SetMemory(0x662304, Add, -141),# units:Human AI Idle  index:156    from 164 To 23
        SetMemory(0x662348, Add, -74),# units:Human AI Idle  index:224    from 97 To 23
        SetMemory(0x6648A4, Add, 768),# units:Return to Idle  index:13    from 20 To 23
        SetMemory(0x6648AC, Add, 1376256),# units:Return to Idle  index:22    from 2 To 23
        SetMemory(0x6648B4, Add, 4096),# units:Return to Idle  index:29    from 2 To 18
        SetMemory(0x6648C0, Add, 105),# units:Return to Idle  index:40    from 2 To 107
        SetMemory(0x6648C4, Add, 1048576),# units:Return to Idle  index:46    from 2 To 18
        SetMemory(0x6648CC, Add, 0),# units:Return to Idle  index:52    from 2 To 2
        SetMemory(0x6648D0, Add, -17920),# units:Return to Idle  index:57    from 93 To 23
        SetMemory(0x6648F4, Add, -10747904),# units:Return to Idle  index:94    from 166 To 2
        SetMemory(0x664978, Add, -74),# units:Return to Idle  index:224    from 97 To 23
        SetMemory(0x663328, Add, 2816),# units:Attack Unit  index:9    from 10 To 21
        SetMemory(0x66332C, Add, 768),# units:Attack Unit  index:13    from 20 To 23
        SetMemory(0x663334, Add, 851968),# units:Attack Unit  index:22    from 10 To 23
        SetMemory(0x66333C, Add, 2304),# units:Attack Unit  index:29    from 10 To 19
        SetMemory(0x663348, Add, 9),# units:Attack Unit  index:40    from 10 To 19
        SetMemory(0x66334C, Add, 589824),# units:Attack Unit  index:46    from 10 To 19
        SetMemory(0x66334C, Add, -134217728),# units:Attack Unit  index:47    from 10 To 2
        SetMemory(0x663350, Add, -8650752),# units:Attack Unit  index:50    from 134 To 2
        SetMemory(0x663354, Add, 11),# units:Attack Unit  index:52    from 10 To 21
        SetMemory(0x663358, Add, 512),# units:Attack Unit  index:57    from 21 To 23
        SetMemory(0x66335C, Add, -184549376),# units:Attack Unit  index:63    from 21 To 10
        SetMemory(0x66337C, Add, -10944512),# units:Attack Unit  index:94    from 188 To 21
        SetMemory(0x663A5C, Add, -42240),# units:Attack Move  index:13    from 188 To 23
        SetMemory(0x663A64, Add, 1376256),# units:Attack Move  index:22    from 2 To 23
        SetMemory(0x663A6C, Add, 4096),# units:Attack Move  index:29    from 2 To 18
        SetMemory(0x663A78, Add, 0),# units:Attack Move  index:40    from 2 To 2
        SetMemory(0x663A7C, Add, 1441792),# units:Attack Move  index:46    from 2 To 24
        SetMemory(0x663A80, Add, -8716288),# units:Attack Move  index:50    from 135 To 2
        SetMemory(0x663A84, Add, 0),# units:Attack Move  index:52    from 2 To 2
        SetMemory(0x663A88, Add, 5376),# units:Attack Move  index:57    from 2 To 23
        SetMemory(0x663AAC, Add, -12189696),# units:Attack Move  index:94    from 188 To 2
        SetMemory(0x6636B8, Add, 0),# units:Ground Weapon  index:0    from 0 To 0
        SetMemory(0x6636BC, Add, 7798784),# units:Ground Weapon  index:6    from 11 To 130
        SetMemory(0x6636C4, Add, 31744),# units:Ground Weapon  index:13    from 6 To 130
        SetMemory(0x6636D0, Add, 118),# units:Ground Weapon  index:24    from 12 To 130
        SetMemory(0x6636E4, Add, -5242880),# units:Ground Weapon  index:46    from 130 To 50
        SetMemory(0x6636E8, Add, 4980736),# units:Ground Weapon  index:50    from 54 To 130
        SetMemory(0x6636F0, Add, -1769472),# units:Ground Weapon  index:58    from 130 To 103
        SetMemory(0x6636F4, Add, -1703936),# units:Ground Weapon  index:62    from 130 To 104
        SetMemory(0x6636F4, Add, -1090519040),# units:Ground Weapon  index:63    from 130 To 65
        SetMemory(0x6636F8, Add, -16777216),# units:Ground Weapon  index:67    from 130 To 129
        SetMemory(0x663708, Add, 43),# units:Ground Weapon  index:80    from 75 To 118
        SetMemory(0x66370C, Add, 2424832),# units:Ground Weapon  index:86    from 78 To 115
        SetMemory(0x66370C, Add, 805306368),# units:Ground Weapon  index:87    from 69 To 117
        SetMemory(0x663718, Add, -1966080),# units:Ground Weapon  index:98    from 130 To 100
        SetMemory(0x66371C, Add, 7012352),# units:Ground Weapon  index:102    from 21 To 128
        SetMemory(0x663724, Add, -262144),# units:Ground Weapon  index:110    from 130 To 126
        SetMemory(0x663728, Add, -8),# units:Ground Weapon  index:112    from 130 To 122
        SetMemory(0x663730, Add, -83886080),# units:Ground Weapon  index:123    from 130 To 125
        SetMemory(0x663734, Add, -101),# units:Ground Weapon  index:124    from 130 To 29
        SetMemory(0x663744, Add, -1792),# units:Ground Weapon  index:141    from 130 To 123
        SetMemory(0x66461C, Add, 256),# units:Max Ground Hits  index:61    from 1 To 2
        SetMemory(0x66461C, Add, 33554432),# units:Max Ground Hits  index:63    from 0 To 2
        SetMemory(0x6616E8, Add, 115),# units:Air Weapon  index:8    from 15 To 130
        SetMemory(0x6616F4, Add, 28928),# units:Air Weapon  index:21    from 17 To 130
        SetMemory(0x661708, Add, -89),# units:Air Weapon  index:40    from 130 To 41
        SetMemory(0x66170C, Add, -5242880),# units:Air Weapon  index:46    from 130 To 50
        SetMemory(0x66170C, Add, 1258291200),# units:Air Weapon  index:47    from 55 To 130
        SetMemory(0x661714, Add, 23296),# units:Air Weapon  index:53    from 39 To 130
        SetMemory(0x661718, Add, -5439488),# units:Air Weapon  index:58    from 103 To 20
        SetMemory(0x66171C, Add, 1703936),# units:Air Weapon  index:62    from 104 To 130
        SetMemory(0x661720, Add, -16777216),# units:Air Weapon  index:67    from 130 To 129
        SetMemory(0x661724, Add, 889192448),# units:Air Weapon  index:71    from 77 To 130
        SetMemory(0x66172C, Add, -1023410176),# units:Air Weapon  index:79    from 130 To 69
        SetMemory(0x661730, Add, 42),# units:Air Weapon  index:80    from 76 To 118
        SetMemory(0x661734, Add, -218103808),# units:Air Weapon  index:87    from 130 To 117
        SetMemory(0x661738, Add, -1),# units:Air Weapon  index:88    from 115 To 114
        SetMemory(0x661740, Add, -5242880),# units:Air Weapon  index:98    from 100 To 20
        SetMemory(0x661744, Add, 7012352),# units:Air Weapon  index:102    from 22 To 129
        SetMemory(0x660180, Add, -196608),# units:AI Internal  index:10    from 3 To 0
        SetMemory(0x660188, Add, -768),# units:AI Internal  index:17    from 3 To 0
        SetMemory(0x660188, Add, -50331648),# units:AI Internal  index:19    from 3 To 0
        SetMemory(0x66018C, Add, -3),# units:AI Internal  index:20    from 3 To 0
        SetMemory(0x660194, Add, -3),# units:AI Internal  index:28    from 3 To 0
        SetMemory(0x660194, Add, -768),# units:AI Internal  index:29    from 3 To 0
        SetMemory(0x660194, Add, 196608),# units:AI Internal  index:30    from 0 To 3
        SetMemory(0x6601A0, Add, 2),# units:AI Internal  index:40    from 0 To 2
        SetMemory(0x6601A8, Add, -3),# units:AI Internal  index:48    from 3 To 0
        SetMemory(0x6601A8, Add, 196608),# units:AI Internal  index:50    from 0 To 3
        SetMemory(0x6601A8, Add, -50331648),# units:AI Internal  index:51    from 3 To 0
        SetMemory(0x6601AC, Add, -768),# units:AI Internal  index:53    from 3 To 0
        SetMemory(0x6601AC, Add, -196608),# units:AI Internal  index:54    from 3 To 0
        SetMemory(0x6601AC, Add, -50331648),# units:AI Internal  index:55    from 3 To 0
        SetMemory(0x6601BC, Add, 768),# units:AI Internal  index:69    from 0 To 3
        SetMemory(0x6601C0, Add, -50331648),# units:AI Internal  index:75    from 3 To 0
        SetMemory(0x6601C4, Add, -3),# units:AI Internal  index:76    from 3 To 0
        SetMemory(0x6601C4, Add, -768),# units:AI Internal  index:77    from 3 To 0
        SetMemory(0x6601C4, Add, -196608),# units:AI Internal  index:78    from 3 To 0
        SetMemory(0x6601C4, Add, -50331648),# units:AI Internal  index:79    from 3 To 0
        SetMemory(0x6601CC, Add, -50331648),# units:AI Internal  index:87    from 3 To 0
        SetMemory(0x6601D0, Add, -3),# units:AI Internal  index:88    from 3 To 0
        SetMemory(0x6601D8, Add, -50331648),# units:AI Internal  index:99    from 3 To 0
        SetMemory(0x6601DC, Add, -3),# units:AI Internal  index:100    from 3 To 0
        SetMemory(0x6601DC, Add, -196608),# units:AI Internal  index:102    from 3 To 0
        SetMemory(0x6601E0, Add, -3),# units:AI Internal  index:104    from 3 To 0
        SetMemory(0x660258, Add, 0),# units:AI Internal  index:227    from 3 To 3
        SetMemory(0x664080, Add, 0),# units:Special Ability Flags  index:0    from 402718720 To 402718720
        SetMemory(0x664084, Add, -2097664),# units:Special Ability Flags  index:1    from 404816384 To 402718720
        SetMemory(0x66408C, Add, -1073676288),# units:Special Ability Flags  index:3    from 1476395008 To 402718720
        SetMemory(0x664094, Add, 65536),# units:Special Ability Flags  index:5    from 1509949440 To 1510014976
        SetMemory(0x66409C, Add, -8),# units:Special Ability Flags  index:7    from 1476460552 To 1476460544
        SetMemory(0x6640A0, Add, -2097540),# units:Special Ability Flags  index:8    from 1512047108 To 1509949568
        SetMemory(0x6640A4, Add, -1075806148),# units:Special Ability Flags  index:9    from 1512079620 To 436273472
        SetMemory(0x6640AC, Add, 124),# units:Special Ability Flags  index:11    from 1509949444 To 1509949568
        SetMemory(0x6640B0, Add, -2031492),# units:Special Ability Flags  index:12    from 1545601028 To 1543569536
        SetMemory(0x6640C0, Add, -2097664),# units:Special Ability Flags  index:16    from 404816448 To 402718784
        SetMemory(0x6640C4, Add, 65536),# units:Special Ability Flags  index:17    from 1476395072 To 1476460608
        SetMemory(0x6640CC, Add, 65536),# units:Special Ability Flags  index:19    from 1476395072 To 1476460608
        SetMemory(0x6640D4, Add, -1109328388),# units:Special Ability Flags  index:21    from 1512047172 To 402718784
        SetMemory(0x6640D8, Add, -975206724),# units:Special Ability Flags  index:22    from 1512079684 To 536872960
        SetMemory(0x6640DC, Add, -1073676288),# units:Special Ability Flags  index:23    from 1509949504 To 436273216
        SetMemory(0x6640E0, Add, 65536),# units:Special Ability Flags  index:24    from 805306384 To 805371920
        SetMemory(0x6640E4, Add, 65536),# units:Special Ability Flags  index:25    from 1107296320 To 1107361856
        SetMemory(0x6640F0, Add, -2031556),# units:Special Ability Flags  index:28    from 1545601092 To 1543569536
        SetMemory(0x6640F8, Add, 65728),# units:Special Ability Flags  index:30    from 1107296256 To 1107361984
        SetMemory(0x664100, Add, 64),# units:Special Ability Flags  index:32    from 402718720 To 402718784
        SetMemory(0x664108, Add, 0),# units:Special Ability Flags  index:34    from 404815872 To 404815872
        SetMemory(0x664114, Add, -1049664),# units:Special Ability Flags  index:37    from 403768448 To 402718784
        SetMemory(0x664118, Add, -1048640),# units:Special Ability Flags  index:38    from 403767424 To 402718784
        SetMemory(0x66411C, Add, -64),# units:Special Ability Flags  index:39    from 469827712 To 469827648
        SetMemory(0x664120, Add, 2112),# units:Special Ability Flags  index:40    from 402718848 To 402720960
        SetMemory(0x664124, Add, -136),# units:Special Ability Flags  index:41    from 403767432 To 403767296
        SetMemory(0x664128, Add, -32896),# units:Special Ability Flags  index:42    from 436306052 To 436273156
        SetMemory(0x66412C, Add, -132),# units:Special Ability Flags  index:43    from 436273284 To 436273152
        SetMemory(0x664130, Add, 1073676156),# units:Special Ability Flags  index:44    from 486604932 To 1560281088
        SetMemory(0x664138, Add, -36700156),# units:Special Ability Flags  index:46    from 439419008 To 402718852
        SetMemory(0x66413C, Add, 536870912),# units:Special Ability Flags  index:47    from 402719876 To 939590788
        SetMemory(0x664140, Add, -128),# units:Special Ability Flags  index:48    from 469827776 To 469827648
        SetMemory(0x664148, Add, 4),# units:Special Ability Flags  index:50    from 403767424 To 403767428
        SetMemory(0x66414C, Add, -2097792),# units:Special Ability Flags  index:51    from 404816576 To 402718784
        SetMemory(0x664150, Add, -34601084),# units:Special Ability Flags  index:52    from 439419072 To 404817988
        SetMemory(0x664154, Add, -1048704),# units:Special Ability Flags  index:53    from 403767488 To 402718784
        SetMemory(0x664158, Add, -1049728),# units:Special Ability Flags  index:54    from 403768512 To 402718784
        SetMemory(0x66415C, Add, -196),# units:Special Ability Flags  index:55    from 436273348 To 436273152
        SetMemory(0x664160, Add, -16777348),# units:Special Ability Flags  index:56    from 486604996 To 469827648
        SetMemory(0x664164, Add, 100566844),# units:Special Ability Flags  index:57    from 436306116 To 536872960
        SetMemory(0x664168, Add, 32892),# units:Special Ability Flags  index:58    from 1509949444 To 1509982336
        SetMemory(0x66416C, Add, 536872960),# units:Special Ability Flags  index:59    from 65540 To 536938500
        SetMemory(0x664174, Add, -4194240),# units:Special Ability Flags  index:61    from 406913024 To 402718784
        SetMemory(0x664178, Add, 1073676284),# units:Special Ability Flags  index:62    from 486604932 To 1560281216
        SetMemory(0x66417C, Add, -2031616),# units:Special Ability Flags  index:63    from 471859456 To 469827840
        SetMemory(0x664180, Add, 65592),# units:Special Ability Flags  index:64    from 1476411400 To 1476476992
        SetMemory(0x664184, Add, 64),# units:Special Ability Flags  index:65    from 402718720 To 402718784
        SetMemory(0x664188, Add, 65600),# units:Special Ability Flags  index:66    from 1509949440 To 1510015040
        SetMemory(0x66418C, Add, -2097152),# units:Special Ability Flags  index:67    from 404815872 To 402718720
        SetMemory(0x664190, Add, 65600),# units:Special Ability Flags  index:68    from 469762304 To 469827904
        SetMemory(0x664194, Add, -16192),# units:Special Ability Flags  index:69    from 1509965828 To 1509949636
        SetMemory(0x66419C, Add, -2097028),# units:Special Ability Flags  index:71    from 1512046596 To 1509949568
        SetMemory(0x6641A0, Add, -4),# units:Special Ability Flags  index:72    from 1543503876 To 1543503872
        SetMemory(0x6641A8, Add, -4194304),# units:Special Ability Flags  index:74    from 406913024 To 402718720
        SetMemory(0x6641AC, Add, -4194368),# units:Special Ability Flags  index:75    from 406913088 To 402718720
        SetMemory(0x6641B0, Add, 65536),# units:Special Ability Flags  index:76    from 469762368 To 469827904
        SetMemory(0x6641B8, Add, 65536),# units:Special Ability Flags  index:78    from 1509949504 To 1510015040
        SetMemory(0x6641BC, Add, -2097152),# units:Special Ability Flags  index:79    from 404815936 To 402718784
        SetMemory(0x6641C0, Add, -1107230724),# units:Special Ability Flags  index:80    from 1509949508 To 402718784
        SetMemory(0x6641C4, Add, 4194432),# units:Special Ability Flags  index:81    from 1543520320 To 1547714752
        SetMemory(0x6641C8, Add, 124),# units:Special Ability Flags  index:82    from 1543503940 To 1543504064
        SetMemory(0x6641CC, Add, 128),# units:Special Ability Flags  index:83    from 1543520256 To 1543520384
        SetMemory(0x6641D0, Add, -32768),# units:Special Ability Flags  index:84    from 1480638468 To 1480605700
        SetMemory(0x6641DC, Add, -2097152),# units:Special Ability Flags  index:87    from 404815936 To 402718784
        SetMemory(0x6641E0, Add, -1107230724),# units:Special Ability Flags  index:88    from 1509949508 To 402718784
        SetMemory(0x6641E4, Add, 4),# units:Special Ability Flags  index:89    from 402718720 To 402718724
        SetMemory(0x6641E8, Add, 4),# units:Special Ability Flags  index:90    from 402718720 To 402718724
        SetMemory(0x6641F4, Add, 4),# units:Special Ability Flags  index:93    from 402718720 To 402718724
        SetMemory(0x6641F8, Add, 188),# units:Special Ability Flags  index:94    from 402718724 To 402718912
        SetMemory(0x6641FC, Add, 4),# units:Special Ability Flags  index:95    from 402718720 To 402718724
        SetMemory(0x664208, Add, 32892),# units:Special Ability Flags  index:98    from 1512046660 To 1512079552
        SetMemory(0x66420C, Add, -2097664),# units:Special Ability Flags  index:99    from 404816448 To 402718784
        SetMemory(0x664210, Add, -2097152),# units:Special Ability Flags  index:100    from 404816448 To 402719296
        SetMemory(0x664218, Add, -2031492),# units:Special Ability Flags  index:102    from 1545601092 To 1543569600
        SetMemory(0x66421C, Add, 4),# units:Special Ability Flags  index:103    from 403767424 To 403767428
        SetMemory(0x664220, Add, -2097792),# units:Special Ability Flags  index:104    from 404816576 To 402718784
        SetMemory(0x664230, Add, -2),# units:Special Ability Flags  index:108    from 1140850691 To 1140850689
        SetMemory(0x664238, Add, -8192),# units:Special Ability Flags  index:110    from 1140858881 To 1140850689
        SetMemory(0x664240, Add, 524288),# units:Special Ability Flags  index:112    from 1140850689 To 1141374977
        SetMemory(0x664254, Add, -2),# units:Special Ability Flags  index:117    from 1140850691 To 1140850689
        SetMemory(0x664258, Add, -2),# units:Special Ability Flags  index:118    from 1140850691 To 1140850689
        SetMemory(0x66426C, Add, 524288),# units:Special Ability Flags  index:123    from 1140850689 To 1141374977
        SetMemory(0x66428C, Add, 524288),# units:Special Ability Flags  index:131    from 2231439489 To 2231963777
        SetMemory(0x6642B0, Add, 318636035),# units:Special Ability Flags  index:140    from 84082817 To 402718852
        SetMemory(0x6642BC, Add, 393216),# units:Special Ability Flags  index:143    from 84082817 To 84476033
        SetMemory(0x6642C8, Add, 536870912),# units:Special Ability Flags  index:146    from 352518273 To 889389185
        SetMemory(0x6642CC, Add, 452755331),# units:Special Ability Flags  index:147    from 84115585 To 536870916
        SetMemory(0x6642D0, Add, 452755331),# units:Special Ability Flags  index:148    from 84115585 To 536870916
        SetMemory(0x6642EC, Add, -524288),# units:Special Ability Flags  index:155    from 3288858625 To 3288334337
        SetMemory(0x6642F0, Add, 0),# units:Special Ability Flags  index:156    from 1140850689 To 1140850689
        SetMemory(0x6642FC, Add, 536346624),# units:Special Ability Flags  index:159    from 1141374977 To 1677721601
        SetMemory(0x664300, Add, -524288),# units:Special Ability Flags  index:160    from 3288858625 To 3288334337
        SetMemory(0x664308, Add, -524288),# units:Special Ability Flags  index:162    from 1409843201 To 1409318913
        SetMemory(0x66430C, Add, 2147483648),# units:Special Ability Flags  index:163    from 1141374977 To 3288858625
        SetMemory(0x664314, Add, -524288),# units:Special Ability Flags  index:165    from 1141374977 To 1140850689
        SetMemory(0x664318, Add, -524288),# units:Special Ability Flags  index:166    from 1141374977 To 1140850689
        SetMemory(0x66431C, Add, 536346624),# units:Special Ability Flags  index:167    from 1141374977 To 1677721601
        SetMemory(0x664320, Add, 2047),# units:Special Ability Flags  index:168    from 1140850689 To 1140852736
        SetMemory(0x664324, Add, -524288),# units:Special Ability Flags  index:169    from 1141374977 To 1140850689
        SetMemory(0x664328, Add, 2683830272),# units:Special Ability Flags  index:170    from 1141374977 To 3825205249
        SetMemory(0x66432C, Add, 2146959360),# units:Special Ability Flags  index:171    from 1141374977 To 3288334337
        SetMemory(0x664330, Add, 2147483648),# units:Special Ability Flags  index:172    from 1143472129 To 3290955777
        SetMemory(0x664338, Add, 3221749760),# units:Special Ability Flags  index:174    from 67108865 To 3288858625
        SetMemory(0x66434C, Add, -67117056),# units:Special Ability Flags  index:179    from 603987969 To 536870913
        SetMemory(0x664350, Add, -67117056),# units:Special Ability Flags  index:180    from 603987969 To 536870913
        SetMemory(0x664354, Add, -603979776),# units:Special Ability Flags  index:181    from 1140850689 To 536870913
        SetMemory(0x664358, Add, -603979776),# units:Special Ability Flags  index:182    from 1140850689 To 536870913
        SetMemory(0x664364, Add, 469762048),# units:Special Ability Flags  index:185    from 67108865 To 536870913
        SetMemory(0x664368, Add, 469762048),# units:Special Ability Flags  index:186    from 67108865 To 536870913
        SetMemory(0x66436C, Add, 469762048),# units:Special Ability Flags  index:187    from 67108865 To 536870913
        SetMemory(0x66437C, Add, -1),# units:Special Ability Flags  index:191    from 536870913 To 536870912
        SetMemory(0x664380, Add, -1),# units:Special Ability Flags  index:192    from 536870913 To 536870912
        SetMemory(0x664384, Add, -1),# units:Special Ability Flags  index:193    from 536870913 To 536870912
        SetMemory(0x664388, Add, 2147483648),# units:Special Ability Flags  index:194    from 536870913 To 2684354561
        SetMemory(0x6643B4, Add, 1),# units:Special Ability Flags  index:205    from 536870912 To 536870913
        SetMemory(0x6643B8, Add, 1),# units:Special Ability Flags  index:206    from 536870912 To 536870913
        SetMemory(0x6643BC, Add, 1),# units:Special Ability Flags  index:207    from 536870912 To 536870913
        SetMemory(0x6643C0, Add, 1),# units:Special Ability Flags  index:208    from 536870912 To 536870913
        SetMemory(0x6643C8, Add, 469729281),# units:Special Ability Flags  index:210    from 1140883456 To 1610612737
        SetMemory(0x6643CC, Add, 469729281),# units:Special Ability Flags  index:211    from 1140883456 To 1610612737
        SetMemory(0x6643D0, Add, 536838145),# units:Special Ability Flags  index:212    from 1140883456 To 1677721601
        SetMemory(0x6643D4, Add, 536838145),# units:Special Ability Flags  index:213    from 1140883456 To 1677721601
        SetMemory(0x6643E0, Add, -8388608),# units:Special Ability Flags  index:216    from 545261568 To 536872960
        SetMemory(0x6643E4, Add, -8388604),# units:Special Ability Flags  index:217    from 545261568 To 536872964
        SetMemory(0x6643E8, Add, -8388608),# units:Special Ability Flags  index:218    from 545261568 To 536872960
        SetMemory(0x6643EC, Add, -8388608),# units:Special Ability Flags  index:219    from 545261568 To 536872960
        SetMemory(0x6643F0, Add, 536870912),# units:Special Ability Flags  index:220    from 8390656 To 545261568
        SetMemory(0x6643F4, Add, 536870912),# units:Special Ability Flags  index:221    from 8390656 To 545261568
        SetMemory(0x6643F8, Add, 4),# units:Special Ability Flags  index:222    from 8390656 To 8390660
        SetMemory(0x6643FC, Add, 536870916),# units:Special Ability Flags  index:223    from 8390656 To 545261572
        SetMemory(0x664400, Add, -8388604),# units:Special Ability Flags  index:224    from 8390656 To 2052
        SetMemory(0x664404, Add, 536870916),# units:Special Ability Flags  index:225    from 8390656 To 545261572
        SetMemory(0x664408, Add, 4),# units:Special Ability Flags  index:226    from 8390656 To 8390660
        SetMemory(0x66440C, Add, 528482308),# units:Special Ability Flags  index:227    from 8390656 To 536872964
        SetMemory(0x662DB8, Add, 1),# units:Target Acquisition Range  index:0    from 4 To 5
        SetMemory(0x662DC4, Add, 1),# units:Target Acquisition Range  index:12    from 6 To 7
        SetMemory(0x662DC8, Add, 16777216),# units:Target Acquisition Range  index:19    from 5 To 6
        SetMemory(0x662DD0, Add, -327680),# units:Target Acquisition Range  index:26    from 12 To 7
        SetMemory(0x662DD4, Add, 1),# units:Target Acquisition Range  index:28    from 6 To 7
        SetMemory(0x662DD4, Add, 256),# units:Target Acquisition Range  index:29    from 6 To 7
        SetMemory(0x662DD4, Add, -67108864),# units:Target Acquisition Range  index:31    from 12 To 8
        SetMemory(0x662DDC, Add, 65536),# units:Target Acquisition Range  index:38    from 4 To 5
        SetMemory(0x662DE0, Add, 4),# units:Target Acquisition Range  index:40    from 3 To 7
        SetMemory(0x662DE0, Add, 50331648),# units:Target Acquisition Range  index:43    from 3 To 6
        SetMemory(0x662DE4, Add, -5),# units:Target Acquisition Range  index:44    from 8 To 3
        SetMemory(0x662DE4, Add, 458752),# units:Target Acquisition Range  index:46    from 0 To 7
        SetMemory(0x662DE4, Add, -50331648),# units:Target Acquisition Range  index:47    from 3 To 0
        SetMemory(0x662DEC, Add, 1),# units:Target Acquisition Range  index:52    from 0 To 1
        SetMemory(0x662DEC, Add, 50331648),# units:Target Acquisition Range  index:55    from 3 To 6
        SetMemory(0x662DF0, Add, -5),# units:Target Acquisition Range  index:56    from 8 To 3
        SetMemory(0x662DF0, Add, -65536),# units:Target Acquisition Range  index:58    from 6 To 5
        SetMemory(0x662DF4, Add, -131072),# units:Target Acquisition Range  index:62    from 7 To 5
        SetMemory(0x662DF4, Add, -67108864),# units:Target Acquisition Range  index:63    from 7 To 3
        SetMemory(0x662DF8, Add, 65536),# units:Target Acquisition Range  index:66    from 4 To 5
        SetMemory(0x662DF8, Add, 33554432),# units:Target Acquisition Range  index:67    from 3 To 5
        SetMemory(0x662E00, Add, 6),# units:Target Acquisition Range  index:72    from 8 To 14
        SetMemory(0x662E00, Add, 1024),# units:Target Acquisition Range  index:73    from 4 To 8
        SetMemory(0x662E04, Add, 65536),# units:Target Acquisition Range  index:78    from 4 To 5
        SetMemory(0x662E04, Add, 33554432),# units:Target Acquisition Range  index:79    from 3 To 5
        SetMemory(0x662E08, Add, 2),# units:Target Acquisition Range  index:80    from 4 To 6
        SetMemory(0x662E08, Add, -256),# units:Target Acquisition Range  index:81    from 8 To 7
        SetMemory(0x662E08, Add, 917504),# units:Target Acquisition Range  index:82    from 8 To 22
        SetMemory(0x662E08, Add, -16777216),# units:Target Acquisition Range  index:83    from 8 To 7
        SetMemory(0x662E0C, Add, 196608),# units:Target Acquisition Range  index:86    from 5 To 8
        SetMemory(0x662E0C, Add, 33554432),# units:Target Acquisition Range  index:87    from 3 To 5
        SetMemory(0x662E10, Add, 3),# units:Target Acquisition Range  index:88    from 4 To 7
        SetMemory(0x662E18, Add, -262144),# units:Target Acquisition Range  index:98    from 9 To 5
        SetMemory(0x662E18, Add, 16777216),# units:Target Acquisition Range  index:99    from 6 To 7
        SetMemory(0x662E1C, Add, 1),# units:Target Acquisition Range  index:100    from 6 To 7
        SetMemory(0x662E1C, Add, 131072),# units:Target Acquisition Range  index:102    from 6 To 8
        SetMemory(0x662E20, Add, 1),# units:Target Acquisition Range  index:104    from 6 To 7
        SetMemory(0x662E24, Add, 1),# units:Target Acquisition Range  index:108    from 0 To 1
        SetMemory(0x662E88, Add, -327680),# units:Target Acquisition Range  index:210    from 5 To 0
        SetMemory(0x662E88, Add, -33554432),# units:Target Acquisition Range  index:211    from 2 To 0
        SetMemory(0x662E8C, Add, -5),# units:Target Acquisition Range  index:212    from 5 To 0
        SetMemory(0x662E8C, Add, -512),# units:Target Acquisition Range  index:213    from 2 To 0
        SetMemory(0x66325C, Add, 131072),# units:Sight Range  index:38    from 6 To 8
        SetMemory(0x66325C, Add, 16777216),# units:Sight Range  index:39    from 7 To 8
        SetMemory(0x663260, Add, 3),# units:Sight Range  index:40    from 5 To 8
        SetMemory(0x663260, Add, -196608),# units:Sight Range  index:42    from 9 To 6
        SetMemory(0x663264, Add, -131072),# units:Sight Range  index:46    from 10 To 8
        SetMemory(0x663268, Add, 1),# units:Sight Range  index:48    from 7 To 8
        SetMemory(0x66326C, Add, -10),# units:Sight Range  index:52    from 10 To 0
        SetMemory(0x66326C, Add, 196608),# units:Sight Range  index:54    from 5 To 8
        SetMemory(0x663270, Add, -3),# units:Sight Range  index:56    from 11 To 8
        SetMemory(0x663270, Add, 67108864),# units:Sight Range  index:59    from 4 To 8
        SetMemory(0x663274, Add, -67108864),# units:Sight Range  index:63    from 10 To 6
        SetMemory(0x663278, Add, 33554432),# units:Sight Range  index:67    from 7 To 9
        SetMemory(0x663280, Add, -3),# units:Sight Range  index:72    from 11 To 8
        SetMemory(0x663288, Add, -1),# units:Sight Range  index:80    from 10 To 9
        SetMemory(0x663288, Add, -512),# units:Sight Range  index:81    from 10 To 8
        SetMemory(0x663288, Add, 131072),# units:Sight Range  index:82    from 9 To 11
        SetMemory(0x663288, Add, -33554432),# units:Sight Range  index:83    from 10 To 8
        SetMemory(0x66328C, Add, -8),# units:Sight Range  index:84    from 9 To 1
        SetMemory(0x66328C, Add, 65536),# units:Sight Range  index:86    from 9 To 10
        SetMemory(0x66328C, Add, 33554432),# units:Sight Range  index:87    from 7 To 9
        SetMemory(0x663290, Add, -1),# units:Sight Range  index:88    from 10 To 9
        SetMemory(0x663298, Add, -65536),# units:Sight Range  index:98    from 9 To 8
        SetMemory(0x66329C, Add, -2),# units:Sight Range  index:100    from 11 To 9
        SetMemory(0x6632B0, Add, -6),# units:Sight Range  index:120    from 8 To 2
        SetMemory(0x6632B0, Add, -393216),# units:Sight Range  index:122    from 8 To 2
        SetMemory(0x6632B4, Add, -524288),# units:Sight Range  index:126    from 10 To 2
        SetMemory(0x6632B4, Add, -100663296),# units:Sight Range  index:127    from 8 To 2
        SetMemory(0x6632BC, Add, -8),# units:Sight Range  index:132    from 10 To 2
        SetMemory(0x6632BC, Add, -2304),# units:Sight Range  index:133    from 11 To 2
        SetMemory(0x6632BC, Add, -100663296),# units:Sight Range  index:135    from 8 To 2
        SetMemory(0x6632C0, Add, -1536),# units:Sight Range  index:137    from 8 To 2
        SetMemory(0x6632C0, Add, -393216),# units:Sight Range  index:138    from 8 To 2
        SetMemory(0x6632C0, Add, -100663296),# units:Sight Range  index:139    from 8 To 2
        SetMemory(0x6632C4, Add, -6),# units:Sight Range  index:140    from 8 To 2
        SetMemory(0x6632C4, Add, -393216),# units:Sight Range  index:142    from 8 To 2
        SetMemory(0x6632C8, Add, -134217728),# units:Sight Range  index:147    from 8 To 0
        SetMemory(0x6632CC, Add, 3),# units:Sight Range  index:148    from 8 To 11
        SetMemory(0x6632CC, Add, -393216),# units:Sight Range  index:150    from 8 To 2
        SetMemory(0x6632D4, Add, 1),# units:Sight Range  index:156    from 8 To 9
        SetMemory(0x6632D4, Add, -1280),# units:Sight Range  index:157    from 10 To 5
        SetMemory(0x6632D8, Add, 0),# units:Sight Range  index:160    from 10 To 10
        SetMemory(0x6632D8, Add, -83886080),# units:Sight Range  index:163    from 10 To 5
        SetMemory(0x6632DC, Add, -8),# units:Sight Range  index:164    from 10 To 2
        SetMemory(0x6632DC, Add, -1280),# units:Sight Range  index:165    from 10 To 5
        SetMemory(0x6632DC, Add, -524288),# units:Sight Range  index:166    from 10 To 2
        SetMemory(0x6632DC, Add, 16777216),# units:Sight Range  index:167    from 10 To 11
        SetMemory(0x6632E0, Add, -7),# units:Sight Range  index:168    from 8 To 1
        SetMemory(0x6632E0, Add, -65536),# units:Sight Range  index:170    from 10 To 9
        SetMemory(0x6632E4, Add, -5),# units:Sight Range  index:172    from 10 To 5
        SetMemory(0x6632E8, Add, -150994944),# units:Sight Range  index:179    from 9 To 0
        SetMemory(0x6632EC, Add, -9),# units:Sight Range  index:180    from 9 To 0
        SetMemory(0x6632EC, Add, -2304),# units:Sight Range  index:181    from 9 To 0
        SetMemory(0x6632EC, Add, -589824),# units:Sight Range  index:182    from 9 To 0
        SetMemory(0x6632F0, Add, -2304),# units:Sight Range  index:185    from 9 To 0
        SetMemory(0x6632F0, Add, -589824),# units:Sight Range  index:186    from 9 To 0
        SetMemory(0x6632F0, Add, -150994944),# units:Sight Range  index:187    from 9 To 0
        SetMemory(0x6632F4, Add, -1536),# units:Sight Range  index:189    from 8 To 2
        SetMemory(0x663304, Add, -256),# units:Sight Range  index:205    from 1 To 0
        SetMemory(0x663304, Add, -65536),# units:Sight Range  index:206    from 1 To 0
        SetMemory(0x663304, Add, -16777216),# units:Sight Range  index:207    from 1 To 0
        SetMemory(0x663308, Add, -1),# units:Sight Range  index:208    from 1 To 0
        SetMemory(0x663308, Add, -393216),# units:Sight Range  index:210    from 6 To 0
        SetMemory(0x663308, Add, -50331648),# units:Sight Range  index:211    from 3 To 0
        SetMemory(0x66330C, Add, -6),# units:Sight Range  index:212    from 6 To 0
        SetMemory(0x66330C, Add, -768),# units:Sight Range  index:213    from 3 To 0
        SetMemory(0x663314, Add, -5),# units:Sight Range  index:220    from 5 To 0
        SetMemory(0x663314, Add, -1280),# units:Sight Range  index:221    from 5 To 0
        SetMemory(0x663314, Add, -83886080),# units:Sight Range  index:223    from 5 To 0
        SetMemory(0x663318, Add, -1280),# units:Sight Range  index:225    from 5 To 0
        SetMemory(0x6635D0, Add, 33554432),# units:Armor Upgrade  index:3    from 1 To 3
        SetMemory(0x6635D8, Add, 4),# units:Armor Upgrade  index:8    from 2 To 6
        SetMemory(0x6635D8, Add, 1024),# units:Armor Upgrade  index:9    from 2 To 6
        SetMemory(0x6635D8, Add, 67108864),# units:Armor Upgrade  index:11    from 2 To 6
        SetMemory(0x6635DC, Add, -2),# units:Armor Upgrade  index:12    from 2 To 0
        SetMemory(0x6635E0, Add, -256),# units:Armor Upgrade  index:17    from 1 To 0
        SetMemory(0x6635E4, Add, -512),# units:Armor Upgrade  index:21    from 2 To 0
        SetMemory(0x6635E4, Add, 83886080),# units:Armor Upgrade  index:23    from 1 To 6
        SetMemory(0x6635E8, Add, 1280),# units:Armor Upgrade  index:25    from 1 To 6
        SetMemory(0x6635EC, Add, 4),# units:Armor Upgrade  index:28    from 2 To 6
        SetMemory(0x6635EC, Add, 1024),# units:Armor Upgrade  index:29    from 2 To 6
        SetMemory(0x6635EC, Add, 0),# units:Armor Upgrade  index:30    from 1 To 1
        SetMemory(0x6635F0, Add, 5),# units:Armor Upgrade  index:32    from 0 To 5
        SetMemory(0x6635F4, Add, 57),# units:Armor Upgrade  index:36    from 3 To 60
        SetMemory(0x6635F4, Add, -768),# units:Armor Upgrade  index:37    from 3 To 0
        SetMemory(0x6635F4, Add, -131072),# units:Armor Upgrade  index:38    from 3 To 1
        SetMemory(0x6635F8, Add, 1),# units:Armor Upgrade  index:40    from 3 To 4
        SetMemory(0x6635F8, Add, -131072),# units:Armor Upgrade  index:42    from 4 To 2
        SetMemory(0x6635F8, Add, 33554432),# units:Armor Upgrade  index:43    from 4 To 6
        SetMemory(0x6635FC, Add, 65536),# units:Armor Upgrade  index:46    from 3 To 4
        SetMemory(0x6635FC, Add, -33554432),# units:Armor Upgrade  index:47    from 4 To 2
        SetMemory(0x663600, Add, -50331648),# units:Armor Upgrade  index:51    from 3 To 0
        SetMemory(0x663604, Add, -3),# units:Armor Upgrade  index:52    from 3 To 0
        SetMemory(0x663604, Add, -768),# units:Armor Upgrade  index:53    from 3 To 0
        SetMemory(0x663604, Add, -131072),# units:Armor Upgrade  index:54    from 3 To 1
        SetMemory(0x663604, Add, 33554432),# units:Armor Upgrade  index:55    from 4 To 6
        SetMemory(0x663608, Add, -1),# units:Armor Upgrade  index:56    from 4 To 3
        SetMemory(0x663608, Add, 956301312),# units:Armor Upgrade  index:59    from 3 To 60
        SetMemory(0x66360C, Add, -1280),# units:Armor Upgrade  index:61    from 5 To 0
        SetMemory(0x66360C, Add, 131072),# units:Armor Upgrade  index:62    from 4 To 6
        SetMemory(0x66360C, Add, -83886080),# units:Armor Upgrade  index:63    from 5 To 0
        SetMemory(0x663610, Add, -5),# units:Armor Upgrade  index:64    from 5 To 0
        SetMemory(0x663610, Add, -1280),# units:Armor Upgrade  index:65    from 5 To 0
        SetMemory(0x663610, Add, -262144),# units:Armor Upgrade  index:66    from 5 To 1
        SetMemory(0x663610, Add, -83886080),# units:Armor Upgrade  index:67    from 5 To 0
        SetMemory(0x663614, Add, -2),# units:Armor Upgrade  index:68    from 5 To 3
        SetMemory(0x663614, Add, 13824),# units:Armor Upgrade  index:69    from 6 To 60
        SetMemory(0x663614, Add, -100663296),# units:Armor Upgrade  index:71    from 6 To 0
        SetMemory(0x663618, Add, -83886080),# units:Armor Upgrade  index:75    from 5 To 0
        SetMemory(0x66361C, Add, -2),# units:Armor Upgrade  index:76    from 5 To 3
        SetMemory(0x66361C, Add, -1280),# units:Armor Upgrade  index:77    from 5 To 0
        SetMemory(0x66361C, Add, -262144),# units:Armor Upgrade  index:78    from 5 To 1
        SetMemory(0x66361C, Add, -83886080),# units:Armor Upgrade  index:79    from 5 To 0
        SetMemory(0x663620, Add, -6),# units:Armor Upgrade  index:80    from 6 To 0
        SetMemory(0x663620, Add, -50331648),# units:Armor Upgrade  index:83    from 5 To 2
        SetMemory(0x663624, Add, 54),# units:Armor Upgrade  index:84    from 6 To 60
        SetMemory(0x663624, Add, -83886080),# units:Armor Upgrade  index:87    from 5 To 0
        SetMemory(0x663628, Add, -6),# units:Armor Upgrade  index:88    from 6 To 0
        SetMemory(0x66362C, Add, -3538944),# units:Armor Upgrade  index:94    from 60 To 6
        SetMemory(0x663630, Add, 14592),# units:Armor Upgrade  index:97    from 3 To 60
        SetMemory(0x663634, Add, 262144),# units:Armor Upgrade  index:102    from 2 To 6
        SetMemory(0x663638, Add, -3),# units:Armor Upgrade  index:104    from 3 To 0
        SetMemory(0x66363C, Add, -13824),# units:Armor Upgrade  index:109    from 60 To 6
        SetMemory(0x66363C, Add, -3538944),# units:Armor Upgrade  index:110    from 60 To 6
        SetMemory(0x663640, Add, -54),# units:Armor Upgrade  index:112    from 60 To 6
        SetMemory(0x663640, Add, -3538944),# units:Armor Upgrade  index:114    from 60 To 6
        SetMemory(0x663648, Add, -905969664),# units:Armor Upgrade  index:123    from 60 To 6
        SetMemory(0x66364C, Add, -56),# units:Armor Upgrade  index:124    from 60 To 4
        SetMemory(0x663668, Add, -3670016),# units:Armor Upgrade  index:154    from 60 To 4
        SetMemory(0x663668, Add, -939524096),# units:Armor Upgrade  index:155    from 60 To 4
        SetMemory(0x66366C, Add, -13824),# units:Armor Upgrade  index:157    from 60 To 6
        SetMemory(0x66366C, Add, -905969664),# units:Armor Upgrade  index:159    from 60 To 6
        SetMemory(0x663670, Add, -56),# units:Armor Upgrade  index:160    from 60 To 4
        SetMemory(0x663670, Add, -3932160),# units:Armor Upgrade  index:162    from 60 To 0
        SetMemory(0x663670, Add, -905969664),# units:Armor Upgrade  index:163    from 60 To 6
        SetMemory(0x663674, Add, -56),# units:Armor Upgrade  index:164    from 60 To 4
        SetMemory(0x663674, Add, -13824),# units:Armor Upgrade  index:165    from 60 To 6
        SetMemory(0x663674, Add, -3670016),# units:Armor Upgrade  index:166    from 60 To 4
        SetMemory(0x663678, Add, -13824),# units:Armor Upgrade  index:169    from 60 To 6
        SetMemory(0x663678, Add, -939524096),# units:Armor Upgrade  index:171    from 60 To 4
        SetMemory(0x6636A0, Add, -13824),# units:Armor Upgrade  index:209    from 60 To 6
        SetMemory(0x662188, Add, -2),# units:Unit Size  index:8    from 3 To 1
        SetMemory(0x662190, Add, -256),# units:Unit Size  index:17    from 3 To 2
        SetMemory(0x662194, Add, -512),# units:Unit Size  index:21    from 3 To 1
        SetMemory(0x662194, Add, -33554432),# units:Unit Size  index:23    from 3 To 1
        SetMemory(0x662198, Add, -256),# units:Unit Size  index:25    from 3 To 2
        SetMemory(0x6621A8, Add, 0),# units:Unit Size  index:40    from 1 To 1
        SetMemory(0x6621A8, Add, 33554432),# units:Unit Size  index:43    from 1 To 3
        SetMemory(0x6621B4, Add, -256),# units:Unit Size  index:53    from 2 To 1
        SetMemory(0x6621B4, Add, 65536),# units:Unit Size  index:54    from 1 To 2
        SetMemory(0x6621B4, Add, 33554432),# units:Unit Size  index:55    from 1 To 3
        SetMemory(0x6621C0, Add, -65536),# units:Unit Size  index:66    from 3 To 2
        SetMemory(0x6621CC, Add, -65536),# units:Unit Size  index:78    from 3 To 2
        SetMemory(0x6621D0, Add, -2),# units:Unit Size  index:80    from 3 To 1
        SetMemory(0x6621D8, Add, -2),# units:Unit Size  index:88    from 3 To 1
        SetMemory(0x6621DC, Add, 65536),# units:Unit Size  index:94    from 1 To 2
        SetMemory(0x6621EC, Add, -2),# units:Unit Size  index:108    from 3 To 1
        SetMemory(0x6621FC, Add, -1),# units:Unit Size  index:124    from 3 To 2
        SetMemory(0x662218, Add, 0),# units:Unit Size  index:154    from 3 To 3
        SetMemory(0x662218, Add, -33554432),# units:Unit Size  index:155    from 3 To 1
        SetMemory(0x662220, Add, -1),# units:Unit Size  index:160    from 3 To 2
        SetMemory(0x662220, Add, -65536),# units:Unit Size  index:162    from 3 To 2
        SetMemory(0x662228, Add, -512),# units:Unit Size  index:169    from 3 To 1
        SetMemory(0x662228, Add, -16777216),# units:Unit Size  index:171    from 3 To 2
        SetMemory(0x65FEE8, Add, 589824),# units:Armor  index:34    from 1 To 10
        SetMemory(0x65FEEC, Add, 5120),# units:Armor  index:37    from 0 To 20
        SetMemory(0x65FEF4, Add, 1048576),# units:Armor  index:46    from 1 To 17
        SetMemory(0x65FEF8, Add, 402653184),# units:Armor  index:51    from 2 To 26
        SetMemory(0x65FEFC, Add, 5632),# units:Armor  index:53    from 2 To 24
        SetMemory(0x65FEFC, Add, 1441792),# units:Armor  index:54    from 3 To 25
        SetMemory(0x65FF08, Add, 5888),# units:Armor  index:65    from 1 To 24
        SetMemory(0x65FF14, Add, 5120),# units:Armor  index:77    from 2 To 22
        SetMemory(0x65FF68, Add, -1),# units:Armor  index:160    from 1 To 0
        SetMemory(0x6620AC, Add, -131072),# units:Right-click Action  index:22    from 2 To 0
        SetMemory(0x6620B4, Add, 1280),# units:Right-click Action  index:29    from 1 To 6
        SetMemory(0x6620C0, Add, 2),# units:Right-click Action  index:40    from 1 To 3
        SetMemory(0x6620C4, Add, 65536),# units:Right-click Action  index:46    from 2 To 3
        SetMemory(0x6620C4, Add, -16777216),# units:Right-click Action  index:47    from 1 To 0
        SetMemory(0x6620C8, Add, -65536),# units:Right-click Action  index:50    from 1 To 0
        SetMemory(0x6620CC, Add, 0),# units:Right-click Action  index:52    from 2 To 2
        SetMemory(0x6620D0, Add, -512),# units:Right-click Action  index:57    from 2 To 0
        SetMemory(0x6620D4, Add, -16777216),# units:Right-click Action  index:63    from 2 To 1
        SetMemory(0x6620D8, Add, -16777216),# units:Right-click Action  index:67    from 2 To 1
        SetMemory(0x662014, Add, -700),# units:Ready Sound  index:42    from 909 To 209
        SetMemory(0x662018, Add, -52232192),# units:Ready Sound  index:45    from 928 To 131
        SetMemory(0x66201C, Add, -50659328),# units:Ready Sound  index:47    from 775 To 2
        SetMemory(0x662028, Add, -814),# units:Ready Sound  index:52    from 814 To 0
        SetMemory(0x662028, Add, -13107200),# units:Ready Sound  index:53    from 866 To 666
        SetMemory(0x662030, Add, -59572224),# units:Ready Sound  index:57    from 909 To 0
        SetMemory(0x662038, Add, -47710208),# units:Ready Sound  index:61    from 728 To 0
        SetMemory(0x66203C, Add, -547),# units:Ready Sound  index:62    from 1096 To 549
        SetMemory(0x66203C, Add, -69795840),# units:Ready Sound  index:63    from 1065 To 0
        SetMemory(0x662044, Add, -40763392),# units:Ready Sound  index:67    from 622 To 0
        SetMemory(0x662054, Add, 51576832),# units:Ready Sound  index:75    from 0 To 787
        SetMemory(0x662060, Add, -534),# units:Ready Sound  index:80    from 534 To 0
        SetMemory(0x662060, Add, -24969216),# units:Ready Sound  index:81    from 637 To 256
        SetMemory(0x662064, Add, -24969216),# units:Ready Sound  index:83    from 637 To 256
        SetMemory(0x66206C, Add, 0),# units:Ready Sound  index:87    from 0 To 0
        SetMemory(0x660004, Add, -697),# units:What Sound Start  index:42    from 912 To 215
        SetMemory(0x66000C, Add, -44498944),# units:What Sound Start  index:47    from 781 To 102
        SetMemory(0x660018, Add, -806),# units:What Sound Start  index:52    from 821 To 15
        SetMemory(0x660018, Add, -13107200),# units:What Sound Start  index:53    from 870 To 670
        SetMemory(0x660020, Add, -58785792),# units:What Sound Start  index:57    from 912 To 15
        SetMemory(0x660028, Add, 851968),# units:What Sound Start  index:61    from 733 To 746
        SetMemory(0x66002C, Add, -542),# units:What Sound Start  index:62    from 1101 To 559
        SetMemory(0x66002C, Add, -24641536),# units:What Sound Start  index:63    from 1071 To 695
        SetMemory(0x660034, Add, -10813440),# units:What Sound Start  index:67    from 627 To 462
        SetMemory(0x660044, Add, 3014656),# units:What Sound Start  index:75    from 746 To 792
        SetMemory(0x660050, Add, -78),# units:What Sound Start  index:80    from 540 To 462
        SetMemory(0x660050, Add, -24707072),# units:What Sound Start  index:81    from 642 To 265
        SetMemory(0x660054, Add, -24707072),# units:What Sound Start  index:83    from 642 To 265
        SetMemory(0x66005C, Add, 30277632),# units:What Sound Start  index:87    from 0 To 462
        SetMemory(0x6600F0, Add, 10),# units:What Sound Start  index:160    from 479 To 489
        SetMemory(0x662C44, Add, -697),# units:What Sound End  index:42    from 915 To 218
        SetMemory(0x662C4C, Add, -44498944),# units:What Sound End  index:47    from 782 To 103
        SetMemory(0x662C58, Add, -808),# units:What Sound End  index:52    from 823 To 15
        SetMemory(0x662C58, Add, -13041664),# units:What Sound End  index:53    from 872 To 673
        SetMemory(0x662C60, Add, -58982400),# units:What Sound End  index:57    from 915 To 15
        SetMemory(0x662C68, Add, 851968),# units:What Sound End  index:61    from 736 To 749
        SetMemory(0x662C6C, Add, -541),# units:What Sound End  index:62    from 1103 To 562
        SetMemory(0x662C6C, Add, -24641536),# units:What Sound End  index:63    from 1074 To 698
        SetMemory(0x662C74, Add, -10813440),# units:What Sound End  index:67    from 630 To 465
        SetMemory(0x662C84, Add, 3014656),# units:What Sound End  index:75    from 749 To 795
        SetMemory(0x662C90, Add, -78),# units:What Sound End  index:80    from 543 To 465
        SetMemory(0x662C90, Add, -24707072),# units:What Sound End  index:81    from 645 To 268
        SetMemory(0x662C94, Add, -24707072),# units:What Sound End  index:83    from 645 To 268
        SetMemory(0x662C9C, Add, 30474240),# units:What Sound End  index:87    from 0 To 465
        SetMemory(0x662D30, Add, 10),# units:What Sound End  index:160    from 479 To 489
        SetMemory(0x663B8C, Add, -700),# units:Piss Sound Start  index:42    from 911 To 211
        SetMemory(0x663B94, Add, -44367872),# units:Piss Sound Start  index:47    from 779 To 102
        SetMemory(0x663BA0, Add, -818),# units:Piss Sound Start  index:52    from 818 To 0
        SetMemory(0x663BA0, Add, -13172736),# units:Piss Sound Start  index:53    from 868 To 667
        SetMemory(0x663BA8, Add, -59703296),# units:Piss Sound Start  index:57    from 911 To 0
        SetMemory(0x663BB0, Add, 851968),# units:Piss Sound Start  index:61    from 729 To 742
        SetMemory(0x663BB4, Add, -544),# units:Piss Sound Start  index:62    from 1098 To 554
        SetMemory(0x663BB4, Add, -24641536),# units:Piss Sound Start  index:63    from 1067 To 691
        SetMemory(0x663BBC, Add, -10878976),# units:Piss Sound Start  index:67    from 623 To 457
        SetMemory(0x663BCC, Add, 3014656),# units:Piss Sound Start  index:75    from 742 To 788
        SetMemory(0x663BD8, Add, -78),# units:Piss Sound Start  index:80    from 535 To 457
        SetMemory(0x663BD8, Add, -24969216),# units:Piss Sound Start  index:81    from 639 To 258
        SetMemory(0x663BDC, Add, -24969216),# units:Piss Sound Start  index:83    from 639 To 258
        SetMemory(0x663BE4, Add, 29949952),# units:Piss Sound Start  index:87    from 0 To 457
        SetMemory(0x661F3C, Add, -697),# units:Piss Sound End  index:42    from 911 To 214
        SetMemory(0x661F44, Add, -44367872),# units:Piss Sound End  index:47    from 780 To 103
        SetMemory(0x661F50, Add, -820),# units:Piss Sound End  index:52    from 820 To 0
        SetMemory(0x661F50, Add, -13107200),# units:Piss Sound End  index:53    from 869 To 669
        SetMemory(0x661F58, Add, -59703296),# units:Piss Sound End  index:57    from 911 To 0
        SetMemory(0x661F60, Add, 851968),# units:Piss Sound End  index:61    from 732 To 745
        SetMemory(0x661F64, Add, -542),# units:Piss Sound End  index:62    from 1100 To 558
        SetMemory(0x661F64, Add, -24641536),# units:Piss Sound End  index:63    from 1070 To 694
        SetMemory(0x661F6C, Add, -10813440),# units:Piss Sound End  index:67    from 626 To 461
        SetMemory(0x661F7C, Add, 3014656),# units:Piss Sound End  index:75    from 745 To 791
        SetMemory(0x661F88, Add, -78),# units:Piss Sound End  index:80    from 539 To 461
        SetMemory(0x661F88, Add, -24707072),# units:Piss Sound End  index:81    from 641 To 264
        SetMemory(0x661F8C, Add, -24707072),# units:Piss Sound End  index:83    from 641 To 264
        SetMemory(0x661F94, Add, 30212096),# units:Piss Sound End  index:87    from 0 To 461
        SetMemory(0x663C64, Add, -697),# units:Yes Sound Start  index:42    from 916 To 219
        SetMemory(0x663C6C, Add, -44630016),# units:Yes Sound Start  index:47    from 783 To 102
        SetMemory(0x663C78, Add, -824),# units:Yes Sound Start  index:52    from 824 To 0
        SetMemory(0x663C78, Add, -13041664),# units:Yes Sound Start  index:53    from 873 To 674
        SetMemory(0x663C80, Add, -60030976),# units:Yes Sound Start  index:57    from 916 To 0
        SetMemory(0x663C88, Add, 851968),# units:Yes Sound Start  index:61    from 737 To 750
        SetMemory(0x663C8C, Add, -541),# units:Yes Sound Start  index:62    from 1104 To 563
        SetMemory(0x663C8C, Add, -24641536),# units:Yes Sound Start  index:63    from 1075 To 699
        SetMemory(0x663C94, Add, -10813440),# units:Yes Sound Start  index:67    from 631 To 466
        SetMemory(0x663CA4, Add, 3014656),# units:Yes Sound Start  index:75    from 750 To 796
        SetMemory(0x663CB0, Add, -78),# units:Yes Sound Start  index:80    from 544 To 466
        SetMemory(0x663CB0, Add, -24707072),# units:Yes Sound Start  index:81    from 646 To 269
        SetMemory(0x663CB4, Add, -24707072),# units:Yes Sound Start  index:83    from 646 To 269
        SetMemory(0x663CBC, Add, 30539776),# units:Yes Sound Start  index:87    from 0 To 466
        SetMemory(0x661494, Add, -695),# units:Yes Sound End  index:42    from 919 To 224
        SetMemory(0x66149C, Add, -44630016),# units:Yes Sound End  index:47    from 784 To 103
        SetMemory(0x6614A8, Add, -826),# units:Yes Sound End  index:52    from 826 To 0
        SetMemory(0x6614A8, Add, -13041664),# units:Yes Sound End  index:53    from 876 To 677
        SetMemory(0x6614B0, Add, -60227584),# units:Yes Sound End  index:57    from 919 To 0
        SetMemory(0x6614B8, Add, 851968),# units:Yes Sound End  index:61    from 740 To 753
        SetMemory(0x6614BC, Add, -542),# units:Yes Sound End  index:62    from 1107 To 565
        SetMemory(0x6614BC, Add, -24641536),# units:Yes Sound End  index:63    from 1078 To 702
        SetMemory(0x6614C4, Add, -10813440),# units:Yes Sound End  index:67    from 634 To 469
        SetMemory(0x6614D4, Add, 3014656),# units:Yes Sound End  index:75    from 753 To 799
        SetMemory(0x6614E0, Add, -78),# units:Yes Sound End  index:80    from 547 To 469
        SetMemory(0x6614E0, Add, -24707072),# units:Yes Sound End  index:81    from 649 To 272
        SetMemory(0x6614E4, Add, -24707072),# units:Yes Sound End  index:83    from 649 To 272
        SetMemory(0x6614EC, Add, 30736384),# units:Yes Sound End  index:87    from 0 To 469
        SetMemory(0x662880, Add, -23),# units:StarEdit Placement Box Width  index:8    from 38 To 15
        SetMemory(0x662884, Add, -50),# units:StarEdit Placement Box Width  index:9    from 65 To 15
        SetMemory(0x662888, Add, -3),# units:StarEdit Placement Box Width  index:10    from 23 To 20
        SetMemory(0x66288C, Add, -20),# units:StarEdit Placement Box Width  index:11    from 49 To 29
        SetMemory(0x662890, Add, -55),# units:StarEdit Placement Box Width  index:12    from 80 To 25
        SetMemory(0x6628AC, Add, -7),# units:StarEdit Placement Box Width  index:19    from 32 To 25
        SetMemory(0x6628B0, Add, -1),# units:StarEdit Placement Box Width  index:20    from 18 To 17
        SetMemory(0x6628B4, Add, -21),# units:StarEdit Placement Box Width  index:21    from 38 To 17
        SetMemory(0x6628B8, Add, -64),# units:StarEdit Placement Box Width  index:22    from 65 To 1
        SetMemory(0x6628D0, Add, -50),# units:StarEdit Placement Box Width  index:28    from 75 To 25
        SetMemory(0x6628D8, Add, -31),# units:StarEdit Placement Box Width  index:30    from 32 To 1
        SetMemory(0x6628E0, Add, -3),# units:StarEdit Placement Box Width  index:32    from 23 To 20
        SetMemory(0x6628FC, Add, -8),# units:StarEdit Placement Box Width  index:39    from 38 To 30
        SetMemory(0x662900, Add, -9),# units:StarEdit Placement Box Width  index:40    from 19 To 10
        SetMemory(0x66290C, Add, -19),# units:StarEdit Placement Box Width  index:43    from 44 To 25
        SetMemory(0x662910, Add, -34),# units:StarEdit Placement Box Width  index:44    from 44 To 10
        SetMemory(0x662918, Add, -17),# units:StarEdit Placement Box Width  index:46    from 27 To 10
        SetMemory(0x66291C, Add, -24),# units:StarEdit Placement Box Width  index:47    from 24 To 0
        SetMemory(0x662920, Add, -8),# units:StarEdit Placement Box Width  index:48    from 38 To 30
        SetMemory(0x66292C, Add, 5),# units:StarEdit Placement Box Width  index:51    from 15 To 20
        SetMemory(0x662930, Add, -25),# units:StarEdit Placement Box Width  index:52    from 29 To 4
        SetMemory(0x662934, Add, 2),# units:StarEdit Placement Box Width  index:53    from 21 To 23
        SetMemory(0x662938, Add, 14),# units:StarEdit Placement Box Width  index:54    from 16 To 30
        SetMemory(0x66293C, Add, -19),# units:StarEdit Placement Box Width  index:55    from 44 To 25
        SetMemory(0x662940, Add, -14),# units:StarEdit Placement Box Width  index:56    from 44 To 30
        SetMemory(0x662944, Add, -49),# units:StarEdit Placement Box Width  index:57    from 50 To 1
        SetMemory(0x662948, Add, -21),# units:StarEdit Placement Box Width  index:58    from 50 To 29
        SetMemory(0x662954, Add, -4),# units:StarEdit Placement Box Width  index:61    from 24 To 20
        SetMemory(0x662958, Add, -19),# units:StarEdit Placement Box Width  index:62    from 44 To 25
        SetMemory(0x66295C, Add, -9),# units:StarEdit Placement Box Width  index:63    from 32 To 23
        SetMemory(0x662960, Add, -13),# units:StarEdit Placement Box Width  index:64    from 23 To 10
        SetMemory(0x662964, Add, -3),# units:StarEdit Placement Box Width  index:65    from 23 To 20
        SetMemory(0x66296C, Add, -9),# units:StarEdit Placement Box Width  index:67    from 24 To 15
        SetMemory(0x662970, Add, -2),# units:StarEdit Placement Box Width  index:68    from 32 To 30
        SetMemory(0x662974, Add, -25),# units:StarEdit Placement Box Width  index:69    from 40 To 15
        SetMemory(0x66297C, Add, -19),# units:StarEdit Placement Box Width  index:71    from 44 To 25
        SetMemory(0x662980, Add, -35),# units:StarEdit Placement Box Width  index:72    from 64 To 29
        SetMemory(0x66298C, Add, -4),# units:StarEdit Placement Box Width  index:75    from 24 To 20
        SetMemory(0x662990, Add, -2),# units:StarEdit Placement Box Width  index:76    from 32 To 30
        SetMemory(0x662994, Add, -4),# units:StarEdit Placement Box Width  index:77    from 24 To 20
        SetMemory(0x6629A0, Add, -21),# units:StarEdit Placement Box Width  index:80    from 36 To 15
        SetMemory(0x6629A4, Add, -7),# units:StarEdit Placement Box Width  index:81    from 32 To 25
        SetMemory(0x6629A8, Add, -35),# units:StarEdit Placement Box Width  index:82    from 64 To 29
        SetMemory(0x6629AC, Add, -7),# units:StarEdit Placement Box Width  index:83    from 32 To 25
        SetMemory(0x6629B8, Add, -11),# units:StarEdit Placement Box Width  index:86    from 44 To 33
        SetMemory(0x6629BC, Add, -9),# units:StarEdit Placement Box Width  index:87    from 24 To 15
        SetMemory(0x6629C0, Add, -21),# units:StarEdit Placement Box Width  index:88    from 36 To 15
        SetMemory(0x6629D8, Add, -17),# units:StarEdit Placement Box Width  index:94    from 32 To 15
        SetMemory(0x6629E0, Add, -31),# units:StarEdit Placement Box Width  index:96    from 32 To 1
        SetMemory(0x6629E8, Add, -16),# units:StarEdit Placement Box Width  index:98    from 49 To 33
        SetMemory(0x6629F8, Add, -50),# units:StarEdit Placement Box Width  index:102    from 75 To 25
        SetMemory(0x662A14, Add, -51),# units:StarEdit Placement Box Width  index:109    from 96 To 45
        SetMemory(0x662A20, Add, -51),# units:StarEdit Placement Box Width  index:112    from 96 To 45
        SetMemory(0x662A28, Add, -83),# units:StarEdit Placement Box Width  index:114    from 128 To 45
        SetMemory(0x662A4C, Add, -51),# units:StarEdit Placement Box Width  index:123    from 96 To 45
        SetMemory(0x662A60, Add, -28),# units:StarEdit Placement Box Width  index:128    from 32 To 4
        SetMemory(0x662A64, Add, -28),# units:StarEdit Placement Box Width  index:129    from 32 To 4
        SetMemory(0x662A90, Add, -91),# units:StarEdit Placement Box Width  index:140    from 96 To 5
        SetMemory(0x662A9C, Add, -29),# units:StarEdit Placement Box Width  index:143    from 64 To 35
        SetMemory(0x662AAC, Add, -160),# units:StarEdit Placement Box Width  index:147    from 160 To 0
        SetMemory(0x662AB0, Add, -160),# units:StarEdit Placement Box Width  index:148    from 160 To 0
        SetMemory(0x662ACC, Add, -56),# units:StarEdit Placement Box Width  index:155    from 96 To 40
        SetMemory(0x662AD0, Add, -63),# units:StarEdit Placement Box Width  index:156    from 64 To 1
        SetMemory(0x662ADC, Add, -95),# units:StarEdit Placement Box Width  index:159    from 96 To 1
        SetMemory(0x662AE0, Add, -88),# units:StarEdit Placement Box Width  index:160    from 128 To 40
        SetMemory(0x662AE8, Add, -16),# units:StarEdit Placement Box Width  index:162    from 64 To 48
        SetMemory(0x662AEC, Add, -51),# units:StarEdit Placement Box Width  index:163    from 96 To 45
        SetMemory(0x662AF0, Add, -48),# units:StarEdit Placement Box Width  index:164    from 96 To 48
        SetMemory(0x662AF4, Add, -51),# units:StarEdit Placement Box Width  index:165    from 96 To 45
        SetMemory(0x662AF8, Add, -48),# units:StarEdit Placement Box Width  index:166    from 96 To 48
        SetMemory(0x662AFC, Add, -113),# units:StarEdit Placement Box Width  index:167    from 128 To 15
        SetMemory(0x662B04, Add, -95),# units:StarEdit Placement Box Width  index:169    from 96 To 1
        SetMemory(0x662B08, Add, -95),# units:StarEdit Placement Box Width  index:170    from 96 To 1
        SetMemory(0x662B0C, Add, -56),# units:StarEdit Placement Box Width  index:171    from 96 To 40
        SetMemory(0x662B10, Add, -51),# units:StarEdit Placement Box Width  index:172    from 96 To 45
        SetMemory(0x662B18, Add, -179),# units:StarEdit Placement Box Width  index:174    from 224 To 45
        SetMemory(0x662B2C, Add, -64),# units:StarEdit Placement Box Width  index:179    from 64 To 0
        SetMemory(0x662B30, Add, -64),# units:StarEdit Placement Box Width  index:180    from 64 To 0
        SetMemory(0x662B34, Add, -64),# units:StarEdit Placement Box Width  index:181    from 64 To 0
        SetMemory(0x662B38, Add, -32),# units:StarEdit Placement Box Width  index:182    from 32 To 0
        SetMemory(0x662B44, Add, -32),# units:StarEdit Placement Box Width  index:185    from 32 To 0
        SetMemory(0x662B48, Add, -32),# units:StarEdit Placement Box Width  index:186    from 32 To 0
        SetMemory(0x662B4C, Add, -32),# units:StarEdit Placement Box Width  index:187    from 32 To 0
        SetMemory(0x662B54, Add, -61),# units:StarEdit Placement Box Width  index:189    from 96 To 35
        SetMemory(0x662B5C, Add, -95),# units:StarEdit Placement Box Width  index:191    from 96 To 1
        SetMemory(0x662B60, Add, -95),# units:StarEdit Placement Box Width  index:192    from 96 To 1
        SetMemory(0x662B64, Add, -95),# units:StarEdit Placement Box Width  index:193    from 96 To 1
        SetMemory(0x662B94, Add, -136),# units:StarEdit Placement Box Width  index:205    from 136 To 0
        SetMemory(0x662B98, Add, -136),# units:StarEdit Placement Box Width  index:206    from 136 To 0
        SetMemory(0x662B9C, Add, -148),# units:StarEdit Placement Box Width  index:207    from 148 To 0
        SetMemory(0x662BA0, Add, -148),# units:StarEdit Placement Box Width  index:208    from 148 To 0
        SetMemory(0x662BA8, Add, -64),# units:StarEdit Placement Box Width  index:210    from 64 To 0
        SetMemory(0x662BAC, Add, -64),# units:StarEdit Placement Box Width  index:211    from 64 To 0
        SetMemory(0x662BB0, Add, -64),# units:StarEdit Placement Box Width  index:212    from 64 To 0
        SetMemory(0x662BB4, Add, -64),# units:StarEdit Placement Box Width  index:213    from 64 To 0
        SetMemory(0x662BBC, Add, -28),# units:StarEdit Placement Box Width  index:215    from 32 To 4
        SetMemory(0x662BC0, Add, -28),# units:StarEdit Placement Box Width  index:216    from 32 To 4
        SetMemory(0x662BC4, Add, -28),# units:StarEdit Placement Box Width  index:217    from 32 To 4
        SetMemory(0x662BC8, Add, -28),# units:StarEdit Placement Box Width  index:218    from 32 To 4
        SetMemory(0x662BCC, Add, -28),# units:StarEdit Placement Box Width  index:219    from 32 To 4
        SetMemory(0x662BD0, Add, -32),# units:StarEdit Placement Box Width  index:220    from 32 To 0
        SetMemory(0x662BD4, Add, -32),# units:StarEdit Placement Box Width  index:221    from 32 To 0
        SetMemory(0x662BD8, Add, -30),# units:StarEdit Placement Box Width  index:222    from 32 To 2
        SetMemory(0x662BDC, Add, -32),# units:StarEdit Placement Box Width  index:223    from 32 To 0
        SetMemory(0x662BE0, Add, -32),# units:StarEdit Placement Box Width  index:224    from 32 To 0
        SetMemory(0x662BE4, Add, -32),# units:StarEdit Placement Box Width  index:225    from 32 To 0
        SetMemory(0x662BE8, Add, -32),# units:StarEdit Placement Box Width  index:226    from 32 To 0
        SetMemory(0x662BEC, Add, -32),# units:StarEdit Placement Box Width  index:227    from 32 To 0
        SetMemory(0x662880, Add, -983040),# units:StarEdit Placement Box Height  index:8    from 30 To 15
        SetMemory(0x662884, Add, -2293760),# units:StarEdit Placement Box Height  index:9    from 50 To 15
        SetMemory(0x662888, Add, -524288),# units:StarEdit Placement Box Height  index:10    from 28 To 20
        SetMemory(0x66288C, Add, -524288),# units:StarEdit Placement Box Height  index:11    from 37 To 29
        SetMemory(0x662890, Add, -2555904),# units:StarEdit Placement Box Height  index:12    from 64 To 25
        SetMemory(0x6628AC, Add, -458752),# units:StarEdit Placement Box Height  index:19    from 32 To 25
        SetMemory(0x6628B0, Add, -131072),# units:StarEdit Placement Box Height  index:20    from 22 To 20
        SetMemory(0x6628B4, Add, -655360),# units:StarEdit Placement Box Height  index:21    from 30 To 20
        SetMemory(0x6628B8, Add, -3211264),# units:StarEdit Placement Box Height  index:22    from 50 To 1
        SetMemory(0x6628D0, Add, -2228224),# units:StarEdit Placement Box Height  index:28    from 59 To 25
        SetMemory(0x6628D8, Add, -2031616),# units:StarEdit Placement Box Height  index:30    from 32 To 1
        SetMemory(0x6628E0, Add, -524288),# units:StarEdit Placement Box Height  index:32    from 28 To 20
        SetMemory(0x6628FC, Add, -131072),# units:StarEdit Placement Box Height  index:39    from 32 To 30
        SetMemory(0x662900, Add, -589824),# units:StarEdit Placement Box Height  index:40    from 19 To 10
        SetMemory(0x66290C, Add, -1245184),# units:StarEdit Placement Box Height  index:43    from 44 To 25
        SetMemory(0x662910, Add, -2228224),# units:StarEdit Placement Box Height  index:44    from 44 To 10
        SetMemory(0x662918, Add, -983040),# units:StarEdit Placement Box Height  index:46    from 25 To 10
        SetMemory(0x66291C, Add, -1572864),# units:StarEdit Placement Box Height  index:47    from 24 To 0
        SetMemory(0x662920, Add, -131072),# units:StarEdit Placement Box Height  index:48    from 32 To 30
        SetMemory(0x66292C, Add, -131072),# units:StarEdit Placement Box Height  index:51    from 22 To 20
        SetMemory(0x662930, Add, -1638400),# units:StarEdit Placement Box Height  index:52    from 29 To 4
        SetMemory(0x662938, Add, 917504),# units:StarEdit Placement Box Height  index:54    from 16 To 30
        SetMemory(0x66293C, Add, -1245184),# units:StarEdit Placement Box Height  index:55    from 44 To 25
        SetMemory(0x662940, Add, -917504),# units:StarEdit Placement Box Height  index:56    from 44 To 30
        SetMemory(0x662944, Add, -3211264),# units:StarEdit Placement Box Height  index:57    from 50 To 1
        SetMemory(0x662948, Add, -1376256),# units:StarEdit Placement Box Height  index:58    from 50 To 29
        SetMemory(0x662954, Add, -655360),# units:StarEdit Placement Box Height  index:61    from 30 To 20
        SetMemory(0x662958, Add, -1245184),# units:StarEdit Placement Box Height  index:62    from 44 To 25
        SetMemory(0x66295C, Add, -589824),# units:StarEdit Placement Box Height  index:63    from 32 To 23
        SetMemory(0x662964, Add, -458752),# units:StarEdit Placement Box Height  index:65    from 27 To 20
        SetMemory(0x66296C, Add, -393216),# units:StarEdit Placement Box Height  index:67    from 28 To 22
        SetMemory(0x662970, Add, -131072),# units:StarEdit Placement Box Height  index:68    from 32 To 30
        SetMemory(0x662974, Add, -1114112),# units:StarEdit Placement Box Height  index:69    from 32 To 15
        SetMemory(0x66297C, Add, -1245184),# units:StarEdit Placement Box Height  index:71    from 44 To 25
        SetMemory(0x662980, Add, -2293760),# units:StarEdit Placement Box Height  index:72    from 64 To 29
        SetMemory(0x66298C, Add, -655360),# units:StarEdit Placement Box Height  index:75    from 30 To 20
        SetMemory(0x662990, Add, -131072),# units:StarEdit Placement Box Height  index:76    from 32 To 30
        SetMemory(0x662994, Add, -655360),# units:StarEdit Placement Box Height  index:77    from 30 To 20
        SetMemory(0x66299C, Add, -131072),# units:StarEdit Placement Box Height  index:79    from 28 To 26
        SetMemory(0x6629A0, Add, -524288),# units:StarEdit Placement Box Height  index:80    from 32 To 24
        SetMemory(0x6629A4, Add, -458752),# units:StarEdit Placement Box Height  index:81    from 32 To 25
        SetMemory(0x6629A8, Add, -2293760),# units:StarEdit Placement Box Height  index:82    from 64 To 29
        SetMemory(0x6629AC, Add, -458752),# units:StarEdit Placement Box Height  index:83    from 32 To 25
        SetMemory(0x6629B8, Add, -720896),# units:StarEdit Placement Box Height  index:86    from 44 To 33
        SetMemory(0x6629BC, Add, -393216),# units:StarEdit Placement Box Height  index:87    from 28 To 22
        SetMemory(0x6629C0, Add, -655360),# units:StarEdit Placement Box Height  index:88    from 32 To 22
        SetMemory(0x6629D8, Add, -1114112),# units:StarEdit Placement Box Height  index:94    from 32 To 15
        SetMemory(0x6629E0, Add, -2031616),# units:StarEdit Placement Box Height  index:96    from 32 To 1
        SetMemory(0x6629E8, Add, -262144),# units:StarEdit Placement Box Height  index:98    from 37 To 33
        SetMemory(0x6629F8, Add, -2228224),# units:StarEdit Placement Box Height  index:102    from 59 To 25
        SetMemory(0x662A14, Add, -1245184),# units:StarEdit Placement Box Height  index:109    from 64 To 45
        SetMemory(0x662A20, Add, -1245184),# units:StarEdit Placement Box Height  index:112    from 64 To 45
        SetMemory(0x662A28, Add, -3342336),# units:StarEdit Placement Box Height  index:114    from 96 To 45
        SetMemory(0x662A4C, Add, -1245184),# units:StarEdit Placement Box Height  index:123    from 64 To 45
        SetMemory(0x662A60, Add, -1835008),# units:StarEdit Placement Box Height  index:128    from 32 To 4
        SetMemory(0x662A64, Add, -1835008),# units:StarEdit Placement Box Height  index:129    from 32 To 4
        SetMemory(0x662A90, Add, -3866624),# units:StarEdit Placement Box Height  index:140    from 64 To 5
        SetMemory(0x662A9C, Add, -1900544),# units:StarEdit Placement Box Height  index:143    from 64 To 35
        SetMemory(0x662AAC, Add, -6291456),# units:StarEdit Placement Box Height  index:147    from 96 To 0
        SetMemory(0x662AB0, Add, -6291456),# units:StarEdit Placement Box Height  index:148    from 96 To 0
        SetMemory(0x662ACC, Add, -1572864),# units:StarEdit Placement Box Height  index:155    from 64 To 40
        SetMemory(0x662AD0, Add, -4128768),# units:StarEdit Placement Box Height  index:156    from 64 To 1
        SetMemory(0x662ADC, Add, -4128768),# units:StarEdit Placement Box Height  index:159    from 64 To 1
        SetMemory(0x662AE0, Add, -3670016),# units:StarEdit Placement Box Height  index:160    from 96 To 40
        SetMemory(0x662AE8, Add, -1048576),# units:StarEdit Placement Box Height  index:162    from 64 To 48
        SetMemory(0x662AEC, Add, -1245184),# units:StarEdit Placement Box Height  index:163    from 64 To 45
        SetMemory(0x662AF0, Add, -1048576),# units:StarEdit Placement Box Height  index:164    from 64 To 48
        SetMemory(0x662AF4, Add, -1245184),# units:StarEdit Placement Box Height  index:165    from 64 To 45
        SetMemory(0x662AF8, Add, -1048576),# units:StarEdit Placement Box Height  index:166    from 64 To 48
        SetMemory(0x662AFC, Add, -5308416),# units:StarEdit Placement Box Height  index:167    from 96 To 15
        SetMemory(0x662B04, Add, -4128768),# units:StarEdit Placement Box Height  index:169    from 64 To 1
        SetMemory(0x662B08, Add, -4128768),# units:StarEdit Placement Box Height  index:170    from 64 To 1
        SetMemory(0x662B0C, Add, -1572864),# units:StarEdit Placement Box Height  index:171    from 64 To 40
        SetMemory(0x662B10, Add, -1245184),# units:StarEdit Placement Box Height  index:172    from 64 To 45
        SetMemory(0x662B18, Add, -3342336),# units:StarEdit Placement Box Height  index:174    from 96 To 45
        SetMemory(0x662B2C, Add, -4194304),# units:StarEdit Placement Box Height  index:179    from 64 To 0
        SetMemory(0x662B30, Add, -4194304),# units:StarEdit Placement Box Height  index:180    from 64 To 0
        SetMemory(0x662B34, Add, -4194304),# units:StarEdit Placement Box Height  index:181    from 64 To 0
        SetMemory(0x662B38, Add, -2097152),# units:StarEdit Placement Box Height  index:182    from 32 To 0
        SetMemory(0x662B44, Add, -2097152),# units:StarEdit Placement Box Height  index:185    from 32 To 0
        SetMemory(0x662B48, Add, -2097152),# units:StarEdit Placement Box Height  index:186    from 32 To 0
        SetMemory(0x662B4C, Add, -2097152),# units:StarEdit Placement Box Height  index:187    from 32 To 0
        SetMemory(0x662B54, Add, -1900544),# units:StarEdit Placement Box Height  index:189    from 64 To 35
        SetMemory(0x662B5C, Add, -4128768),# units:StarEdit Placement Box Height  index:191    from 64 To 1
        SetMemory(0x662B60, Add, -4128768),# units:StarEdit Placement Box Height  index:192    from 64 To 1
        SetMemory(0x662B64, Add, -4128768),# units:StarEdit Placement Box Height  index:193    from 64 To 1
        SetMemory(0x662B94, Add, -8912896),# units:StarEdit Placement Box Height  index:205    from 136 To 0
        SetMemory(0x662B98, Add, -8912896),# units:StarEdit Placement Box Height  index:206    from 136 To 0
        SetMemory(0x662B9C, Add, -6553600),# units:StarEdit Placement Box Height  index:207    from 100 To 0
        SetMemory(0x662BA0, Add, -6553600),# units:StarEdit Placement Box Height  index:208    from 100 To 0
        SetMemory(0x662BA8, Add, -4194304),# units:StarEdit Placement Box Height  index:210    from 64 To 0
        SetMemory(0x662BAC, Add, -4194304),# units:StarEdit Placement Box Height  index:211    from 64 To 0
        SetMemory(0x662BB0, Add, -4194304),# units:StarEdit Placement Box Height  index:212    from 64 To 0
        SetMemory(0x662BB4, Add, -4194304),# units:StarEdit Placement Box Height  index:213    from 64 To 0
        SetMemory(0x662BBC, Add, -1835008),# units:StarEdit Placement Box Height  index:215    from 32 To 4
        SetMemory(0x662BC0, Add, -1835008),# units:StarEdit Placement Box Height  index:216    from 32 To 4
        SetMemory(0x662BC4, Add, -1835008),# units:StarEdit Placement Box Height  index:217    from 32 To 4
        SetMemory(0x662BC8, Add, -1835008),# units:StarEdit Placement Box Height  index:218    from 32 To 4
        SetMemory(0x662BCC, Add, -1835008),# units:StarEdit Placement Box Height  index:219    from 32 To 4
        SetMemory(0x662BD0, Add, -2097152),# units:StarEdit Placement Box Height  index:220    from 32 To 0
        SetMemory(0x662BD4, Add, -2097152),# units:StarEdit Placement Box Height  index:221    from 32 To 0
        SetMemory(0x662BD8, Add, -1966080),# units:StarEdit Placement Box Height  index:222    from 32 To 2
        SetMemory(0x662BDC, Add, -2097152),# units:StarEdit Placement Box Height  index:223    from 32 To 0
        SetMemory(0x662BE0, Add, -2097152),# units:StarEdit Placement Box Height  index:224    from 32 To 0
        SetMemory(0x662BE4, Add, -2097152),# units:StarEdit Placement Box Height  index:225    from 32 To 0
        SetMemory(0x662BE8, Add, -2097152),# units:StarEdit Placement Box Height  index:226    from 32 To 0
        SetMemory(0x662BEC, Add, -2097152),# units:StarEdit Placement Box Height  index:227    from 32 To 0
        SetMemory(0x6617C8, Add, -1),# units:Unit Size Left  index:0    from 8 To 7
        SetMemory(0x6617D0, Add, 3),# units:Unit Size Left  index:1    from 7 To 10
        SetMemory(0x6617E0, Add, -1),# units:Unit Size Left  index:3    from 16 To 15
        SetMemory(0x661800, Add, -5),# units:Unit Size Left  index:7    from 11 To 6
        SetMemory(0x661808, Add, -12),# units:Unit Size Left  index:8    from 19 To 7
        SetMemory(0x661810, Add, -29),# units:Unit Size Left  index:9    from 32 To 3
        SetMemory(0x661818, Add, -2),# units:Unit Size Left  index:10    from 11 To 9
        SetMemory(0x661820, Add, -13),# units:Unit Size Left  index:11    from 24 To 11
        SetMemory(0x661828, Add, -30),# units:Unit Size Left  index:12    from 37 To 7
        SetMemory(0x661848, Add, 3),# units:Unit Size Left  index:16    from 7 To 10
        SetMemory(0x661850, Add, -4),# units:Unit Size Left  index:17    from 16 To 12
        SetMemory(0x661860, Add, -5),# units:Unit Size Left  index:19    from 16 To 11
        SetMemory(0x661868, Add, -1),# units:Unit Size Left  index:20    from 8 To 7
        SetMemory(0x661870, Add, -12),# units:Unit Size Left  index:21    from 19 To 7
        SetMemory(0x661878, Add, -31),# units:Unit Size Left  index:22    from 32 To 1
        SetMemory(0x6618A8, Add, -30),# units:Unit Size Left  index:28    from 37 To 7
        SetMemory(0x6618B8, Add, -15),# units:Unit Size Left  index:30    from 16 To 1
        SetMemory(0x6618C8, Add, -2),# units:Unit Size Left  index:32    from 11 To 9
        SetMemory(0x6618F8, Add, 1),# units:Unit Size Left  index:38    from 10 To 11
        SetMemory(0x661900, Add, -6),# units:Unit Size Left  index:39    from 19 To 13
        SetMemory(0x661908, Add, -4),# units:Unit Size Left  index:40    from 9 To 5
        SetMemory(0x661920, Add, -16),# units:Unit Size Left  index:43    from 22 To 6
        SetMemory(0x661928, Add, -19),# units:Unit Size Left  index:44    from 22 To 3
        SetMemory(0x661938, Add, -8),# units:Unit Size Left  index:46    from 13 To 5
        SetMemory(0x661940, Add, -12),# units:Unit Size Left  index:47    from 12 To 0
        SetMemory(0x661948, Add, -6),# units:Unit Size Left  index:48    from 19 To 13
        SetMemory(0x661960, Add, 2),# units:Unit Size Left  index:51    from 7 To 9
        SetMemory(0x661968, Add, -10),# units:Unit Size Left  index:52    from 14 To 4
        SetMemory(0x661970, Add, -1),# units:Unit Size Left  index:53    from 10 To 9
        SetMemory(0x661978, Add, 3),# units:Unit Size Left  index:54    from 8 To 11
        SetMemory(0x661980, Add, -16),# units:Unit Size Left  index:55    from 22 To 6
        SetMemory(0x661988, Add, -9),# units:Unit Size Left  index:56    from 22 To 13
        SetMemory(0x661990, Add, -24),# units:Unit Size Left  index:57    from 25 To 1
        SetMemory(0x661998, Add, -13),# units:Unit Size Left  index:58    from 24 To 11
        SetMemory(0x6619B0, Add, -3),# units:Unit Size Left  index:61    from 12 To 9
        SetMemory(0x6619B8, Add, -12),# units:Unit Size Left  index:62    from 22 To 10
        SetMemory(0x6619C0, Add, -7),# units:Unit Size Left  index:63    from 16 To 9
        SetMemory(0x6619C8, Add, -5),# units:Unit Size Left  index:64    from 11 To 6
        SetMemory(0x6619D8, Add, -3),# units:Unit Size Left  index:66    from 15 To 12
        SetMemory(0x6619E0, Add, -3),# units:Unit Size Left  index:67    from 12 To 9
        SetMemory(0x6619E8, Add, -3),# units:Unit Size Left  index:68    from 16 To 13
        SetMemory(0x6619F0, Add, -15),# units:Unit Size Left  index:69    from 20 To 5
        SetMemory(0x661A00, Add, -12),# units:Unit Size Left  index:71    from 22 To 10
        SetMemory(0x661A08, Add, -21),# units:Unit Size Left  index:72    from 32 To 11
        SetMemory(0x661A20, Add, -5),# units:Unit Size Left  index:75    from 12 To 7
        SetMemory(0x661A28, Add, -3),# units:Unit Size Left  index:76    from 16 To 13
        SetMemory(0x661A30, Add, -2),# units:Unit Size Left  index:77    from 11 To 9
        SetMemory(0x661A38, Add, -3),# units:Unit Size Left  index:78    from 15 To 12
        SetMemory(0x661A40, Add, -3),# units:Unit Size Left  index:79    from 12 To 9
        SetMemory(0x661A48, Add, -9),# units:Unit Size Left  index:80    from 18 To 9
        SetMemory(0x661A50, Add, -6),# units:Unit Size Left  index:81    from 16 To 10
        SetMemory(0x661A58, Add, -21),# units:Unit Size Left  index:82    from 32 To 11
        SetMemory(0x661A60, Add, -6),# units:Unit Size Left  index:83    from 16 To 10
        SetMemory(0x661A78, Add, -9),# units:Unit Size Left  index:86    from 22 To 13
        SetMemory(0x661A80, Add, -3),# units:Unit Size Left  index:87    from 12 To 9
        SetMemory(0x661A88, Add, -8),# units:Unit Size Left  index:88    from 18 To 10
        SetMemory(0x661AB8, Add, -13),# units:Unit Size Left  index:94    from 16 To 3
        SetMemory(0x661AC8, Add, -15),# units:Unit Size Left  index:96    from 16 To 1
        SetMemory(0x661AD8, Add, -13),# units:Unit Size Left  index:98    from 24 To 11
        SetMemory(0x661AE0, Add, 3),# units:Unit Size Left  index:99    from 7 To 10
        SetMemory(0x661AE8, Add, 3),# units:Unit Size Left  index:100    from 7 To 10
        SetMemory(0x661AF8, Add, -30),# units:Unit Size Left  index:102    from 37 To 7
        SetMemory(0x661B08, Add, 3),# units:Unit Size Left  index:104    from 7 To 10
        SetMemory(0x661B30, Add, -18),# units:Unit Size Left  index:109    from 38 To 20
        SetMemory(0x661B48, Add, -20),# units:Unit Size Left  index:112    from 40 To 20
        SetMemory(0x661B58, Add, -28),# units:Unit Size Left  index:114    from 48 To 20
        SetMemory(0x661BA0, Add, -28),# units:Unit Size Left  index:123    from 48 To 20
        SetMemory(0x661BC8, Add, -15),# units:Unit Size Left  index:128    from 16 To 1
        SetMemory(0x661BD0, Add, -15),# units:Unit Size Left  index:129    from 16 To 1
        SetMemory(0x661C28, Add, -39),# units:Unit Size Left  index:140    from 40 To 1
        SetMemory(0x661C40, Add, -4),# units:Unit Size Left  index:143    from 24 To 20
        SetMemory(0x661C60, Add, -80),# units:Unit Size Left  index:147    from 80 To 0
        SetMemory(0x661C68, Add, -80),# units:Unit Size Left  index:148    from 80 To 0
        SetMemory(0x661CA0, Add, -20),# units:Unit Size Left  index:155    from 36 To 16
        SetMemory(0x661CA8, Add, -15),# units:Unit Size Left  index:156    from 16 To 1
        SetMemory(0x661CC0, Add, -43),# units:Unit Size Left  index:159    from 44 To 1
        SetMemory(0x661CC8, Add, -32),# units:Unit Size Left  index:160    from 48 To 16
        SetMemory(0x661CD8, Add, -5),# units:Unit Size Left  index:162    from 20 To 15
        SetMemory(0x661CE0, Add, -4),# units:Unit Size Left  index:163    from 24 To 20
        SetMemory(0x661CE8, Add, -24),# units:Unit Size Left  index:164    from 40 To 16
        SetMemory(0x661CF0, Add, -12),# units:Unit Size Left  index:165    from 32 To 20
        SetMemory(0x661CF8, Add, -20),# units:Unit Size Left  index:166    from 36 To 16
        SetMemory(0x661D00, Add, -43),# units:Unit Size Left  index:167    from 48 To 5
        SetMemory(0x661D10, Add, -39),# units:Unit Size Left  index:169    from 40 To 1
        SetMemory(0x661D18, Add, -43),# units:Unit Size Left  index:170    from 44 To 1
        SetMemory(0x661D20, Add, -16),# units:Unit Size Left  index:171    from 32 To 16
        SetMemory(0x661D28, Add, -12),# units:Unit Size Left  index:172    from 32 To 20
        SetMemory(0x661D38, Add, -92),# units:Unit Size Left  index:174    from 112 To 20
        SetMemory(0x661D60, Add, -32),# units:Unit Size Left  index:179    from 32 To 0
        SetMemory(0x661D68, Add, -32),# units:Unit Size Left  index:180    from 32 To 0
        SetMemory(0x661D70, Add, -32),# units:Unit Size Left  index:181    from 32 To 0
        SetMemory(0x661D78, Add, -16),# units:Unit Size Left  index:182    from 16 To 0
        SetMemory(0x661D90, Add, -16),# units:Unit Size Left  index:185    from 16 To 0
        SetMemory(0x661D98, Add, -16),# units:Unit Size Left  index:186    from 16 To 0
        SetMemory(0x661DA0, Add, -16),# units:Unit Size Left  index:187    from 16 To 0
        SetMemory(0x661DB0, Add, -28),# units:Unit Size Left  index:189    from 48 To 20
        SetMemory(0x661DC0, Add, -47),# units:Unit Size Left  index:191    from 48 To 1
        SetMemory(0x661DC8, Add, -47),# units:Unit Size Left  index:192    from 48 To 1
        SetMemory(0x661DD0, Add, -47),# units:Unit Size Left  index:193    from 48 To 1
        SetMemory(0x661E30, Add, -25),# units:Unit Size Left  index:205    from 25 To 0
        SetMemory(0x661E38, Add, -44),# units:Unit Size Left  index:206    from 44 To 0
        SetMemory(0x661E40, Add, -41),# units:Unit Size Left  index:207    from 41 To 0
        SetMemory(0x661E48, Add, -28),# units:Unit Size Left  index:208    from 28 To 0
        SetMemory(0x661E58, Add, -16),# units:Unit Size Left  index:210    from 16 To 0
        SetMemory(0x661E60, Add, -16),# units:Unit Size Left  index:211    from 16 To 0
        SetMemory(0x661E68, Add, -16),# units:Unit Size Left  index:212    from 16 To 0
        SetMemory(0x661E70, Add, -16),# units:Unit Size Left  index:213    from 16 To 0
        SetMemory(0x661E80, Add, -15),# units:Unit Size Left  index:215    from 16 To 1
        SetMemory(0x661E88, Add, -15),# units:Unit Size Left  index:216    from 16 To 1
        SetMemory(0x661E90, Add, -12),# units:Unit Size Left  index:217    from 16 To 4
        SetMemory(0x661E98, Add, -15),# units:Unit Size Left  index:218    from 16 To 1
        SetMemory(0x661EA0, Add, -15),# units:Unit Size Left  index:219    from 16 To 1
        SetMemory(0x661EA8, Add, -16),# units:Unit Size Left  index:220    from 16 To 0
        SetMemory(0x661EB0, Add, -16),# units:Unit Size Left  index:221    from 16 To 0
        SetMemory(0x661EB8, Add, -15),# units:Unit Size Left  index:222    from 16 To 1
        SetMemory(0x661EC0, Add, -16),# units:Unit Size Left  index:223    from 16 To 0
        SetMemory(0x661EC8, Add, -16),# units:Unit Size Left  index:224    from 16 To 0
        SetMemory(0x661ED0, Add, -16),# units:Unit Size Left  index:225    from 16 To 0
        SetMemory(0x661ED8, Add, -16),# units:Unit Size Left  index:226    from 16 To 0
        SetMemory(0x661EE0, Add, -16),# units:Unit Size Left  index:227    from 16 To 0
        SetMemory(0x6617C8, Add, -131072),# units:Unit Size Up  index:0    from 9 To 7
        SetMemory(0x6617E0, Add, -65536),# units:Unit Size Up  index:3    from 16 To 15
        SetMemory(0x661800, Add, -327680),# units:Unit Size Up  index:7    from 11 To 6
        SetMemory(0x661808, Add, -524288),# units:Unit Size Up  index:8    from 15 To 7
        SetMemory(0x661810, Add, -1966080),# units:Unit Size Up  index:9    from 33 To 3
        SetMemory(0x661818, Add, -262144),# units:Unit Size Up  index:10    from 13 To 9
        SetMemory(0x661820, Add, -327680),# units:Unit Size Up  index:11    from 16 To 11
        SetMemory(0x661828, Add, -1441792),# units:Unit Size Up  index:12    from 29 To 7
        SetMemory(0x661850, Add, -262144),# units:Unit Size Up  index:17    from 16 To 12
        SetMemory(0x661860, Add, -327680),# units:Unit Size Up  index:19    from 16 To 11
        SetMemory(0x661868, Add, -131072),# units:Unit Size Up  index:20    from 9 To 7
        SetMemory(0x661870, Add, -524288),# units:Unit Size Up  index:21    from 15 To 7
        SetMemory(0x661878, Add, -2097152),# units:Unit Size Up  index:22    from 33 To 1
        SetMemory(0x6618A8, Add, -1441792),# units:Unit Size Up  index:28    from 29 To 7
        SetMemory(0x6618B8, Add, -983040),# units:Unit Size Up  index:30    from 16 To 1
        SetMemory(0x6618C8, Add, 131072),# units:Unit Size Up  index:32    from 7 To 9
        SetMemory(0x6618F0, Add, 262144),# units:Unit Size Up  index:37    from 4 To 8
        SetMemory(0x6618F8, Add, 65536),# units:Unit Size Up  index:38    from 10 To 11
        SetMemory(0x661900, Add, -196608),# units:Unit Size Up  index:39    from 16 To 13
        SetMemory(0x661908, Add, -262144),# units:Unit Size Up  index:40    from 9 To 5
        SetMemory(0x661920, Add, -1048576),# units:Unit Size Up  index:43    from 22 To 6
        SetMemory(0x661928, Add, -1245184),# units:Unit Size Up  index:44    from 22 To 3
        SetMemory(0x661938, Add, -458752),# units:Unit Size Up  index:46    from 12 To 5
        SetMemory(0x661940, Add, -786432),# units:Unit Size Up  index:47    from 12 To 0
        SetMemory(0x661948, Add, -196608),# units:Unit Size Up  index:48    from 16 To 13
        SetMemory(0x661960, Add, -65536),# units:Unit Size Up  index:51    from 10 To 9
        SetMemory(0x661968, Add, -655360),# units:Unit Size Up  index:52    from 14 To 4
        SetMemory(0x661970, Add, -65536),# units:Unit Size Up  index:53    from 10 To 9
        SetMemory(0x661978, Add, 458752),# units:Unit Size Up  index:54    from 4 To 11
        SetMemory(0x661980, Add, -1048576),# units:Unit Size Up  index:55    from 22 To 6
        SetMemory(0x661988, Add, -589824),# units:Unit Size Up  index:56    from 22 To 13
        SetMemory(0x661990, Add, -1572864),# units:Unit Size Up  index:57    from 25 To 1
        SetMemory(0x661998, Add, -327680),# units:Unit Size Up  index:58    from 16 To 11
        SetMemory(0x6619B0, Add, 196608),# units:Unit Size Up  index:61    from 6 To 9
        SetMemory(0x6619B8, Add, -786432),# units:Unit Size Up  index:62    from 22 To 10
        SetMemory(0x6619C0, Add, -458752),# units:Unit Size Up  index:63    from 16 To 9
        SetMemory(0x6619C8, Add, -327680),# units:Unit Size Up  index:64    from 11 To 6
        SetMemory(0x6619D0, Add, 393216),# units:Unit Size Up  index:65    from 5 To 11
        SetMemory(0x6619D8, Add, -196608),# units:Unit Size Up  index:66    from 15 To 12
        SetMemory(0x6619E0, Add, -65536),# units:Unit Size Up  index:67    from 10 To 9
        SetMemory(0x6619E8, Add, -196608),# units:Unit Size Up  index:68    from 16 To 13
        SetMemory(0x6619F0, Add, -720896),# units:Unit Size Up  index:69    from 16 To 5
        SetMemory(0x661A00, Add, -786432),# units:Unit Size Up  index:71    from 22 To 10
        SetMemory(0x661A08, Add, -1376256),# units:Unit Size Up  index:72    from 32 To 11
        SetMemory(0x661A20, Add, 65536),# units:Unit Size Up  index:75    from 6 To 7
        SetMemory(0x661A28, Add, -196608),# units:Unit Size Up  index:76    from 16 To 13
        SetMemory(0x661A30, Add, 262144),# units:Unit Size Up  index:77    from 5 To 9
        SetMemory(0x661A38, Add, -196608),# units:Unit Size Up  index:78    from 15 To 12
        SetMemory(0x661A40, Add, -65536),# units:Unit Size Up  index:79    from 10 To 9
        SetMemory(0x661A48, Add, -458752),# units:Unit Size Up  index:80    from 16 To 9
        SetMemory(0x661A50, Add, -393216),# units:Unit Size Up  index:81    from 16 To 10
        SetMemory(0x661A58, Add, -1376256),# units:Unit Size Up  index:82    from 32 To 11
        SetMemory(0x661A60, Add, -393216),# units:Unit Size Up  index:83    from 16 To 10
        SetMemory(0x661A78, Add, -589824),# units:Unit Size Up  index:86    from 22 To 13
        SetMemory(0x661A80, Add, -327680),# units:Unit Size Up  index:87    from 14 To 9
        SetMemory(0x661A88, Add, -393216),# units:Unit Size Up  index:88    from 16 To 10
        SetMemory(0x661AB8, Add, -851968),# units:Unit Size Up  index:94    from 16 To 3
        SetMemory(0x661AC8, Add, -983040),# units:Unit Size Up  index:96    from 16 To 1
        SetMemory(0x661AD8, Add, -327680),# units:Unit Size Up  index:98    from 16 To 11
        SetMemory(0x661AF8, Add, -1441792),# units:Unit Size Up  index:102    from 29 To 7
        SetMemory(0x661B30, Add, -131072),# units:Unit Size Up  index:109    from 22 To 20
        SetMemory(0x661B48, Add, -786432),# units:Unit Size Up  index:112    from 32 To 20
        SetMemory(0x661B58, Add, -1310720),# units:Unit Size Up  index:114    from 40 To 20
        SetMemory(0x661BA0, Add, -786432),# units:Unit Size Up  index:123    from 32 To 20
        SetMemory(0x661BC8, Add, -983040),# units:Unit Size Up  index:128    from 16 To 1
        SetMemory(0x661BD0, Add, -983040),# units:Unit Size Up  index:129    from 16 To 1
        SetMemory(0x661C28, Add, -2031616),# units:Unit Size Up  index:140    from 32 To 1
        SetMemory(0x661C40, Add, -262144),# units:Unit Size Up  index:143    from 24 To 20
        SetMemory(0x661C60, Add, -2097152),# units:Unit Size Up  index:147    from 32 To 0
        SetMemory(0x661C68, Add, -2097152),# units:Unit Size Up  index:148    from 32 To 0
        SetMemory(0x661CA8, Add, -720896),# units:Unit Size Up  index:156    from 12 To 1
        SetMemory(0x661CC0, Add, -983040),# units:Unit Size Up  index:159    from 16 To 1
        SetMemory(0x661CC8, Add, -1048576),# units:Unit Size Up  index:160    from 32 To 16
        SetMemory(0x661CD8, Add, -65536),# units:Unit Size Up  index:162    from 16 To 15
        SetMemory(0x661CE0, Add, -262144),# units:Unit Size Up  index:163    from 24 To 20
        SetMemory(0x661CE8, Add, -524288),# units:Unit Size Up  index:164    from 24 To 16
        SetMemory(0x661CF0, Add, -262144),# units:Unit Size Up  index:165    from 24 To 20
        SetMemory(0x661CF8, Add, -524288),# units:Unit Size Up  index:166    from 24 To 16
        SetMemory(0x661D00, Add, -2293760),# units:Unit Size Up  index:167    from 40 To 5
        SetMemory(0x661D10, Add, -2031616),# units:Unit Size Up  index:169    from 32 To 1
        SetMemory(0x661D18, Add, -1769472),# units:Unit Size Up  index:170    from 28 To 1
        SetMemory(0x661D20, Add, -1048576),# units:Unit Size Up  index:171    from 32 To 16
        SetMemory(0x661D28, Add, 262144),# units:Unit Size Up  index:172    from 16 To 20
        SetMemory(0x661D38, Add, -1835008),# units:Unit Size Up  index:174    from 48 To 20
        SetMemory(0x661D60, Add, -2097152),# units:Unit Size Up  index:179    from 32 To 0
        SetMemory(0x661D68, Add, -2097152),# units:Unit Size Up  index:180    from 32 To 0
        SetMemory(0x661D70, Add, -2097152),# units:Unit Size Up  index:181    from 32 To 0
        SetMemory(0x661D78, Add, -1048576),# units:Unit Size Up  index:182    from 16 To 0
        SetMemory(0x661D90, Add, -1048576),# units:Unit Size Up  index:185    from 16 To 0
        SetMemory(0x661D98, Add, -1048576),# units:Unit Size Up  index:186    from 16 To 0
        SetMemory(0x661DA0, Add, -1048576),# units:Unit Size Up  index:187    from 16 To 0
        SetMemory(0x661DB0, Add, -786432),# units:Unit Size Up  index:189    from 32 To 20
        SetMemory(0x661DC0, Add, -2031616),# units:Unit Size Up  index:191    from 32 To 1
        SetMemory(0x661DC8, Add, -2031616),# units:Unit Size Up  index:192    from 32 To 1
        SetMemory(0x661DD0, Add, -2031616),# units:Unit Size Up  index:193    from 32 To 1
        SetMemory(0x661E30, Add, -1114112),# units:Unit Size Up  index:205    from 17 To 0
        SetMemory(0x661E38, Add, -1114112),# units:Unit Size Up  index:206    from 17 To 0
        SetMemory(0x661E40, Add, -1114112),# units:Unit Size Up  index:207    from 17 To 0
        SetMemory(0x661E48, Add, -1114112),# units:Unit Size Up  index:208    from 17 To 0
        SetMemory(0x661E58, Add, -1048576),# units:Unit Size Up  index:210    from 16 To 0
        SetMemory(0x661E60, Add, -1048576),# units:Unit Size Up  index:211    from 16 To 0
        SetMemory(0x661E68, Add, -1048576),# units:Unit Size Up  index:212    from 16 To 0
        SetMemory(0x661E70, Add, -1048576),# units:Unit Size Up  index:213    from 16 To 0
        SetMemory(0x661E80, Add, -983040),# units:Unit Size Up  index:215    from 16 To 1
        SetMemory(0x661E88, Add, -983040),# units:Unit Size Up  index:216    from 16 To 1
        SetMemory(0x661E90, Add, -786432),# units:Unit Size Up  index:217    from 16 To 4
        SetMemory(0x661E98, Add, -983040),# units:Unit Size Up  index:218    from 16 To 1
        SetMemory(0x661EA0, Add, -983040),# units:Unit Size Up  index:219    from 16 To 1
        SetMemory(0x661EA8, Add, -1048576),# units:Unit Size Up  index:220    from 16 To 0
        SetMemory(0x661EB0, Add, -1048576),# units:Unit Size Up  index:221    from 16 To 0
        SetMemory(0x661EB8, Add, -983040),# units:Unit Size Up  index:222    from 16 To 1
        SetMemory(0x661EC0, Add, -1048576),# units:Unit Size Up  index:223    from 16 To 0
        SetMemory(0x661EC8, Add, -1048576),# units:Unit Size Up  index:224    from 16 To 0
        SetMemory(0x661ED0, Add, -1048576),# units:Unit Size Up  index:225    from 16 To 0
        SetMemory(0x661ED8, Add, -1048576),# units:Unit Size Up  index:226    from 16 To 0
        SetMemory(0x661EE0, Add, -1048576),# units:Unit Size Up  index:227    from 16 To 0
        SetMemory(0x6617CC, Add, -1),# units:Unit Size Right  index:0    from 8 To 7
        SetMemory(0x6617D4, Add, 3),# units:Unit Size Right  index:1    from 7 To 10
        SetMemory(0x661804, Add, -5),# units:Unit Size Right  index:7    from 11 To 6
        SetMemory(0x66180C, Add, -11),# units:Unit Size Right  index:8    from 18 To 7
        SetMemory(0x661814, Add, -29),# units:Unit Size Right  index:9    from 32 To 3
        SetMemory(0x66181C, Add, -2),# units:Unit Size Right  index:10    from 11 To 9
        SetMemory(0x661824, Add, -13),# units:Unit Size Right  index:11    from 24 To 11
        SetMemory(0x66182C, Add, -30),# units:Unit Size Right  index:12    from 37 To 7
        SetMemory(0x66184C, Add, 3),# units:Unit Size Right  index:16    from 7 To 10
        SetMemory(0x661854, Add, -3),# units:Unit Size Right  index:17    from 15 To 12
        SetMemory(0x661864, Add, -4),# units:Unit Size Right  index:19    from 15 To 11
        SetMemory(0x66186C, Add, -1),# units:Unit Size Right  index:20    from 8 To 7
        SetMemory(0x661874, Add, -11),# units:Unit Size Right  index:21    from 18 To 7
        SetMemory(0x66187C, Add, -31),# units:Unit Size Right  index:22    from 32 To 1
        SetMemory(0x6618AC, Add, -30),# units:Unit Size Right  index:28    from 37 To 7
        SetMemory(0x6618BC, Add, -14),# units:Unit Size Right  index:30    from 15 To 1
        SetMemory(0x6618CC, Add, -2),# units:Unit Size Right  index:32    from 11 To 9
        SetMemory(0x6618F4, Add, 1),# units:Unit Size Right  index:37    from 7 To 8
        SetMemory(0x6618FC, Add, 1),# units:Unit Size Right  index:38    from 10 To 11
        SetMemory(0x661904, Add, -5),# units:Unit Size Right  index:39    from 18 To 13
        SetMemory(0x66190C, Add, -4),# units:Unit Size Right  index:40    from 9 To 5
        SetMemory(0x661924, Add, -15),# units:Unit Size Right  index:43    from 21 To 6
        SetMemory(0x66192C, Add, -18),# units:Unit Size Right  index:44    from 21 To 3
        SetMemory(0x66193C, Add, -8),# units:Unit Size Right  index:46    from 13 To 5
        SetMemory(0x661944, Add, -11),# units:Unit Size Right  index:47    from 11 To 0
        SetMemory(0x66194C, Add, -5),# units:Unit Size Right  index:48    from 18 To 13
        SetMemory(0x661964, Add, 2),# units:Unit Size Right  index:51    from 7 To 9
        SetMemory(0x66196C, Add, -10),# units:Unit Size Right  index:52    from 14 To 4
        SetMemory(0x661974, Add, -1),# units:Unit Size Right  index:53    from 10 To 9
        SetMemory(0x66197C, Add, 4),# units:Unit Size Right  index:54    from 7 To 11
        SetMemory(0x661984, Add, -15),# units:Unit Size Right  index:55    from 21 To 6
        SetMemory(0x66198C, Add, -8),# units:Unit Size Right  index:56    from 21 To 13
        SetMemory(0x661994, Add, -23),# units:Unit Size Right  index:57    from 24 To 1
        SetMemory(0x66199C, Add, -13),# units:Unit Size Right  index:58    from 24 To 11
        SetMemory(0x6619B4, Add, -2),# units:Unit Size Right  index:61    from 11 To 9
        SetMemory(0x6619BC, Add, -11),# units:Unit Size Right  index:62    from 21 To 10
        SetMemory(0x6619C4, Add, -6),# units:Unit Size Right  index:63    from 15 To 9
        SetMemory(0x6619CC, Add, -5),# units:Unit Size Right  index:64    from 11 To 6
        SetMemory(0x6619DC, Add, -4),# units:Unit Size Right  index:66    from 16 To 12
        SetMemory(0x6619E4, Add, -2),# units:Unit Size Right  index:67    from 11 To 9
        SetMemory(0x6619EC, Add, -2),# units:Unit Size Right  index:68    from 15 To 13
        SetMemory(0x6619F4, Add, -14),# units:Unit Size Right  index:69    from 19 To 5
        SetMemory(0x661A04, Add, -11),# units:Unit Size Right  index:71    from 21 To 10
        SetMemory(0x661A0C, Add, -20),# units:Unit Size Right  index:72    from 31 To 11
        SetMemory(0x661A24, Add, -4),# units:Unit Size Right  index:75    from 11 To 7
        SetMemory(0x661A2C, Add, -2),# units:Unit Size Right  index:76    from 15 To 13
        SetMemory(0x661A34, Add, -2),# units:Unit Size Right  index:77    from 11 To 9
        SetMemory(0x661A3C, Add, -4),# units:Unit Size Right  index:78    from 16 To 12
        SetMemory(0x661A44, Add, -2),# units:Unit Size Right  index:79    from 11 To 9
        SetMemory(0x661A4C, Add, -8),# units:Unit Size Right  index:80    from 17 To 9
        SetMemory(0x661A54, Add, -5),# units:Unit Size Right  index:81    from 15 To 10
        SetMemory(0x661A5C, Add, -20),# units:Unit Size Right  index:82    from 31 To 11
        SetMemory(0x661A64, Add, -5),# units:Unit Size Right  index:83    from 15 To 10
        SetMemory(0x661A7C, Add, -8),# units:Unit Size Right  index:86    from 21 To 13
        SetMemory(0x661A84, Add, -2),# units:Unit Size Right  index:87    from 11 To 9
        SetMemory(0x661A8C, Add, -7),# units:Unit Size Right  index:88    from 17 To 10
        SetMemory(0x661ABC, Add, -12),# units:Unit Size Right  index:94    from 15 To 3
        SetMemory(0x661ACC, Add, -14),# units:Unit Size Right  index:96    from 15 To 1
        SetMemory(0x661ADC, Add, -13),# units:Unit Size Right  index:98    from 24 To 11
        SetMemory(0x661AE4, Add, 3),# units:Unit Size Right  index:99    from 7 To 10
        SetMemory(0x661AEC, Add, 3),# units:Unit Size Right  index:100    from 7 To 10
        SetMemory(0x661AFC, Add, -30),# units:Unit Size Right  index:102    from 37 To 7
        SetMemory(0x661B0C, Add, 3),# units:Unit Size Right  index:104    from 7 To 10
        SetMemory(0x661B34, Add, -18),# units:Unit Size Right  index:109    from 38 To 20
        SetMemory(0x661B4C, Add, -24),# units:Unit Size Right  index:112    from 44 To 20
        SetMemory(0x661B5C, Add, -28),# units:Unit Size Right  index:114    from 48 To 20
        SetMemory(0x661BA4, Add, -27),# units:Unit Size Right  index:123    from 47 To 20
        SetMemory(0x661BCC, Add, -14),# units:Unit Size Right  index:128    from 15 To 1
        SetMemory(0x661BD4, Add, -14),# units:Unit Size Right  index:129    from 15 To 1
        SetMemory(0x661C2C, Add, -31),# units:Unit Size Right  index:140    from 32 To 1
        SetMemory(0x661C44, Add, -3),# units:Unit Size Right  index:143    from 23 To 20
        SetMemory(0x661C64, Add, -78),# units:Unit Size Right  index:147    from 79 To 1
        SetMemory(0x661C6C, Add, -78),# units:Unit Size Right  index:148    from 79 To 1
        SetMemory(0x661CA4, Add, -24),# units:Unit Size Right  index:155    from 40 To 16
        SetMemory(0x661CAC, Add, -15),# units:Unit Size Right  index:156    from 16 To 1
        SetMemory(0x661CC4, Add, -43),# units:Unit Size Right  index:159    from 44 To 1
        SetMemory(0x661CCC, Add, -32),# units:Unit Size Right  index:160    from 48 To 16
        SetMemory(0x661CDC, Add, -5),# units:Unit Size Right  index:162    from 20 To 15
        SetMemory(0x661CE4, Add, -20),# units:Unit Size Right  index:163    from 40 To 20
        SetMemory(0x661CEC, Add, -24),# units:Unit Size Right  index:164    from 40 To 16
        SetMemory(0x661CF4, Add, -12),# units:Unit Size Right  index:165    from 32 To 20
        SetMemory(0x661CFC, Add, -20),# units:Unit Size Right  index:166    from 36 To 16
        SetMemory(0x661D04, Add, -43),# units:Unit Size Right  index:167    from 48 To 5
        SetMemory(0x661D14, Add, -46),# units:Unit Size Right  index:169    from 47 To 1
        SetMemory(0x661D1C, Add, -43),# units:Unit Size Right  index:170    from 44 To 1
        SetMemory(0x661D24, Add, -16),# units:Unit Size Right  index:171    from 32 To 16
        SetMemory(0x661D2C, Add, -12),# units:Unit Size Right  index:172    from 32 To 20
        SetMemory(0x661D3C, Add, -91),# units:Unit Size Right  index:174    from 111 To 20
        SetMemory(0x661D64, Add, -30),# units:Unit Size Right  index:179    from 31 To 1
        SetMemory(0x661D6C, Add, -30),# units:Unit Size Right  index:180    from 31 To 1
        SetMemory(0x661D74, Add, -30),# units:Unit Size Right  index:181    from 31 To 1
        SetMemory(0x661D7C, Add, -14),# units:Unit Size Right  index:182    from 15 To 1
        SetMemory(0x661D94, Add, -14),# units:Unit Size Right  index:185    from 15 To 1
        SetMemory(0x661D9C, Add, -14),# units:Unit Size Right  index:186    from 15 To 1
        SetMemory(0x661DA4, Add, -14),# units:Unit Size Right  index:187    from 15 To 1
        SetMemory(0x661DB4, Add, -27),# units:Unit Size Right  index:189    from 47 To 20
        SetMemory(0x661DC4, Add, -46),# units:Unit Size Right  index:191    from 47 To 1
        SetMemory(0x661DCC, Add, -46),# units:Unit Size Right  index:192    from 47 To 1
        SetMemory(0x661DD4, Add, -46),# units:Unit Size Right  index:193    from 47 To 1
        SetMemory(0x661E34, Add, -43),# units:Unit Size Right  index:205    from 44 To 1
        SetMemory(0x661E3C, Add, -24),# units:Unit Size Right  index:206    from 25 To 1
        SetMemory(0x661E44, Add, -27),# units:Unit Size Right  index:207    from 28 To 1
        SetMemory(0x661E4C, Add, -40),# units:Unit Size Right  index:208    from 41 To 1
        SetMemory(0x661E5C, Add, -14),# units:Unit Size Right  index:210    from 15 To 1
        SetMemory(0x661E64, Add, -14),# units:Unit Size Right  index:211    from 15 To 1
        SetMemory(0x661E6C, Add, -14),# units:Unit Size Right  index:212    from 15 To 1
        SetMemory(0x661E74, Add, -14),# units:Unit Size Right  index:213    from 15 To 1
        SetMemory(0x661E84, Add, -14),# units:Unit Size Right  index:215    from 15 To 1
        SetMemory(0x661E8C, Add, -14),# units:Unit Size Right  index:216    from 15 To 1
        SetMemory(0x661E94, Add, -11),# units:Unit Size Right  index:217    from 15 To 4
        SetMemory(0x661E9C, Add, -14),# units:Unit Size Right  index:218    from 15 To 1
        SetMemory(0x661EA4, Add, -14),# units:Unit Size Right  index:219    from 15 To 1
        SetMemory(0x661EAC, Add, -14),# units:Unit Size Right  index:220    from 15 To 1
        SetMemory(0x661EB4, Add, -14),# units:Unit Size Right  index:221    from 15 To 1
        SetMemory(0x661EBC, Add, -14),# units:Unit Size Right  index:222    from 15 To 1
        SetMemory(0x661EC4, Add, -14),# units:Unit Size Right  index:223    from 15 To 1
        SetMemory(0x661ECC, Add, -14),# units:Unit Size Right  index:224    from 15 To 1
        SetMemory(0x661ED4, Add, -14),# units:Unit Size Right  index:225    from 15 To 1
        SetMemory(0x661EDC, Add, -14),# units:Unit Size Right  index:226    from 15 To 1
        SetMemory(0x661EE4, Add, -14),# units:Unit Size Right  index:227    from 15 To 1
        SetMemory(0x6617CC, Add, -196608),# units:Unit Size Down  index:0    from 10 To 7
        SetMemory(0x6617D4, Add, -65536),# units:Unit Size Down  index:1    from 11 To 10
        SetMemory(0x661804, Add, -327680),# units:Unit Size Down  index:7    from 11 To 6
        SetMemory(0x66180C, Add, -458752),# units:Unit Size Down  index:8    from 14 To 7
        SetMemory(0x661814, Add, -851968),# units:Unit Size Down  index:9    from 16 To 3
        SetMemory(0x66181C, Add, -327680),# units:Unit Size Down  index:10    from 14 To 9
        SetMemory(0x661824, Add, -589824),# units:Unit Size Down  index:11    from 20 To 11
        SetMemory(0x66182C, Add, -1441792),# units:Unit Size Down  index:12    from 29 To 7
        SetMemory(0x66184C, Add, -65536),# units:Unit Size Down  index:16    from 11 To 10
        SetMemory(0x661854, Add, -196608),# units:Unit Size Down  index:17    from 15 To 12
        SetMemory(0x661864, Add, -262144),# units:Unit Size Down  index:19    from 15 To 11
        SetMemory(0x66186C, Add, -196608),# units:Unit Size Down  index:20    from 10 To 7
        SetMemory(0x661874, Add, -458752),# units:Unit Size Down  index:21    from 14 To 7
        SetMemory(0x66187C, Add, -983040),# units:Unit Size Down  index:22    from 16 To 1
        SetMemory(0x6618AC, Add, -1441792),# units:Unit Size Down  index:28    from 29 To 7
        SetMemory(0x6618BC, Add, -917504),# units:Unit Size Down  index:30    from 15 To 1
        SetMemory(0x6618CC, Add, -327680),# units:Unit Size Down  index:32    from 14 To 9
        SetMemory(0x6618F4, Add, -196608),# units:Unit Size Down  index:37    from 11 To 8
        SetMemory(0x6618FC, Add, -65536),# units:Unit Size Down  index:38    from 12 To 11
        SetMemory(0x661904, Add, -131072),# units:Unit Size Down  index:39    from 15 To 13
        SetMemory(0x66190C, Add, -262144),# units:Unit Size Down  index:40    from 9 To 5
        SetMemory(0x661924, Add, -983040),# units:Unit Size Down  index:43    from 21 To 6
        SetMemory(0x66192C, Add, -1179648),# units:Unit Size Down  index:44    from 21 To 3
        SetMemory(0x66193C, Add, -458752),# units:Unit Size Down  index:46    from 12 To 5
        SetMemory(0x661944, Add, -720896),# units:Unit Size Down  index:47    from 11 To 0
        SetMemory(0x66194C, Add, -131072),# units:Unit Size Down  index:48    from 15 To 13
        SetMemory(0x661964, Add, -131072),# units:Unit Size Down  index:51    from 11 To 9
        SetMemory(0x66196C, Add, -655360),# units:Unit Size Down  index:52    from 14 To 4
        SetMemory(0x661974, Add, -196608),# units:Unit Size Down  index:53    from 12 To 9
        SetMemory(0x661984, Add, -983040),# units:Unit Size Down  index:55    from 21 To 6
        SetMemory(0x66198C, Add, -524288),# units:Unit Size Down  index:56    from 21 To 13
        SetMemory(0x661994, Add, -1507328),# units:Unit Size Down  index:57    from 24 To 1
        SetMemory(0x66199C, Add, -589824),# units:Unit Size Down  index:58    from 20 To 11
        SetMemory(0x6619B4, Add, -655360),# units:Unit Size Down  index:61    from 19 To 9
        SetMemory(0x6619BC, Add, -720896),# units:Unit Size Down  index:62    from 21 To 10
        SetMemory(0x6619C4, Add, -393216),# units:Unit Size Down  index:63    from 15 To 9
        SetMemory(0x6619CC, Add, -327680),# units:Unit Size Down  index:64    from 11 To 6
        SetMemory(0x6619D4, Add, -131072),# units:Unit Size Down  index:65    from 13 To 11
        SetMemory(0x6619DC, Add, -262144),# units:Unit Size Down  index:66    from 16 To 12
        SetMemory(0x6619E4, Add, -262144),# units:Unit Size Down  index:67    from 13 To 9
        SetMemory(0x6619EC, Add, -131072),# units:Unit Size Down  index:68    from 15 To 13
        SetMemory(0x6619F4, Add, -655360),# units:Unit Size Down  index:69    from 15 To 5
        SetMemory(0x661A04, Add, -720896),# units:Unit Size Down  index:71    from 21 To 10
        SetMemory(0x661A0C, Add, -1310720),# units:Unit Size Down  index:72    from 31 To 11
        SetMemory(0x661A24, Add, -786432),# units:Unit Size Down  index:75    from 19 To 7
        SetMemory(0x661A2C, Add, -131072),# units:Unit Size Down  index:76    from 15 To 13
        SetMemory(0x661A34, Add, -262144),# units:Unit Size Down  index:77    from 13 To 9
        SetMemory(0x661A3C, Add, -262144),# units:Unit Size Down  index:78    from 16 To 12
        SetMemory(0x661A44, Add, -262144),# units:Unit Size Down  index:79    from 13 To 9
        SetMemory(0x661A4C, Add, -393216),# units:Unit Size Down  index:80    from 15 To 9
        SetMemory(0x661A54, Add, -327680),# units:Unit Size Down  index:81    from 15 To 10
        SetMemory(0x661A5C, Add, -1310720),# units:Unit Size Down  index:82    from 31 To 11
        SetMemory(0x661A64, Add, -327680),# units:Unit Size Down  index:83    from 15 To 10
        SetMemory(0x661A7C, Add, -524288),# units:Unit Size Down  index:86    from 21 To 13
        SetMemory(0x661A84, Add, -262144),# units:Unit Size Down  index:87    from 13 To 9
        SetMemory(0x661A8C, Add, -327680),# units:Unit Size Down  index:88    from 15 To 10
        SetMemory(0x661ABC, Add, -786432),# units:Unit Size Down  index:94    from 15 To 3
        SetMemory(0x661ACC, Add, -917504),# units:Unit Size Down  index:96    from 15 To 1
        SetMemory(0x661ADC, Add, -589824),# units:Unit Size Down  index:98    from 20 To 11
        SetMemory(0x661AE4, Add, -65536),# units:Unit Size Down  index:99    from 11 To 10
        SetMemory(0x661AEC, Add, -65536),# units:Unit Size Down  index:100    from 11 To 10
        SetMemory(0x661AFC, Add, -1441792),# units:Unit Size Down  index:102    from 29 To 7
        SetMemory(0x661B0C, Add, -65536),# units:Unit Size Down  index:104    from 11 To 10
        SetMemory(0x661B34, Add, -393216),# units:Unit Size Down  index:109    from 26 To 20
        SetMemory(0x661B4C, Add, -262144),# units:Unit Size Down  index:112    from 24 To 20
        SetMemory(0x661B5C, Add, -1179648),# units:Unit Size Down  index:114    from 38 To 20
        SetMemory(0x661BA4, Add, -131072),# units:Unit Size Down  index:123    from 22 To 20
        SetMemory(0x661BCC, Add, -917504),# units:Unit Size Down  index:128    from 15 To 1
        SetMemory(0x661BD4, Add, -917504),# units:Unit Size Down  index:129    from 15 To 1
        SetMemory(0x661C2C, Add, -1966080),# units:Unit Size Down  index:140    from 31 To 1
        SetMemory(0x661C44, Add, -196608),# units:Unit Size Down  index:143    from 23 To 20
        SetMemory(0x661C64, Add, -2555904),# units:Unit Size Down  index:147    from 40 To 1
        SetMemory(0x661C6C, Add, -2555904),# units:Unit Size Down  index:148    from 40 To 1
        SetMemory(0x661CA4, Add, -262144),# units:Unit Size Down  index:155    from 20 To 16
        SetMemory(0x661CAC, Add, -1245184),# units:Unit Size Down  index:156    from 20 To 1
        SetMemory(0x661CC4, Add, -1769472),# units:Unit Size Down  index:159    from 28 To 1
        SetMemory(0x661CCC, Add, -1572864),# units:Unit Size Down  index:160    from 40 To 16
        SetMemory(0x661CDC, Add, -65536),# units:Unit Size Down  index:162    from 16 To 15
        SetMemory(0x661CE4, Add, -262144),# units:Unit Size Down  index:163    from 24 To 20
        SetMemory(0x661CEC, Add, -524288),# units:Unit Size Down  index:164    from 24 To 16
        SetMemory(0x661CF4, Add, -262144),# units:Unit Size Down  index:165    from 24 To 20
        SetMemory(0x661CFC, Add, -262144),# units:Unit Size Down  index:166    from 20 To 16
        SetMemory(0x661D04, Add, -1769472),# units:Unit Size Down  index:167    from 32 To 5
        SetMemory(0x661D14, Add, -1507328),# units:Unit Size Down  index:169    from 24 To 1
        SetMemory(0x661D1C, Add, -1769472),# units:Unit Size Down  index:170    from 28 To 1
        SetMemory(0x661D24, Add, -262144),# units:Unit Size Down  index:171    from 20 To 16
        SetMemory(0x661D2C, Add, 262144),# units:Unit Size Down  index:172    from 16 To 20
        SetMemory(0x661D3C, Add, -1769472),# units:Unit Size Down  index:174    from 47 To 20
        SetMemory(0x661D64, Add, -1966080),# units:Unit Size Down  index:179    from 31 To 1
        SetMemory(0x661D6C, Add, -1966080),# units:Unit Size Down  index:180    from 31 To 1
        SetMemory(0x661D74, Add, -1966080),# units:Unit Size Down  index:181    from 31 To 1
        SetMemory(0x661D7C, Add, -917504),# units:Unit Size Down  index:182    from 15 To 1
        SetMemory(0x661D94, Add, -917504),# units:Unit Size Down  index:185    from 15 To 1
        SetMemory(0x661D9C, Add, -917504),# units:Unit Size Down  index:186    from 15 To 1
        SetMemory(0x661DA4, Add, -917504),# units:Unit Size Down  index:187    from 15 To 1
        SetMemory(0x661DB4, Add, -720896),# units:Unit Size Down  index:189    from 31 To 20
        SetMemory(0x661DC4, Add, -1966080),# units:Unit Size Down  index:191    from 31 To 1
        SetMemory(0x661DCC, Add, -1966080),# units:Unit Size Down  index:192    from 31 To 1
        SetMemory(0x661DD4, Add, -1966080),# units:Unit Size Down  index:193    from 31 To 1
        SetMemory(0x661E34, Add, -1245184),# units:Unit Size Down  index:205    from 20 To 1
        SetMemory(0x661E3C, Add, -1245184),# units:Unit Size Down  index:206    from 20 To 1
        SetMemory(0x661E44, Add, -1245184),# units:Unit Size Down  index:207    from 20 To 1
        SetMemory(0x661E4C, Add, -1245184),# units:Unit Size Down  index:208    from 20 To 1
        SetMemory(0x661E5C, Add, -917504),# units:Unit Size Down  index:210    from 15 To 1
        SetMemory(0x661E64, Add, -917504),# units:Unit Size Down  index:211    from 15 To 1
        SetMemory(0x661E6C, Add, -917504),# units:Unit Size Down  index:212    from 15 To 1
        SetMemory(0x661E74, Add, -917504),# units:Unit Size Down  index:213    from 15 To 1
        SetMemory(0x661E84, Add, -917504),# units:Unit Size Down  index:215    from 15 To 1
        SetMemory(0x661E8C, Add, -917504),# units:Unit Size Down  index:216    from 15 To 1
        SetMemory(0x661E94, Add, -720896),# units:Unit Size Down  index:217    from 15 To 4
        SetMemory(0x661E9C, Add, -917504),# units:Unit Size Down  index:218    from 15 To 1
        SetMemory(0x661EA4, Add, -917504),# units:Unit Size Down  index:219    from 15 To 1
        SetMemory(0x661EAC, Add, -917504),# units:Unit Size Down  index:220    from 15 To 1
        SetMemory(0x661EB4, Add, -917504),# units:Unit Size Down  index:221    from 15 To 1
        SetMemory(0x661EBC, Add, -917504),# units:Unit Size Down  index:222    from 15 To 1
        SetMemory(0x661EC4, Add, -917504),# units:Unit Size Down  index:223    from 15 To 1
        SetMemory(0x661ECC, Add, -917504),# units:Unit Size Down  index:224    from 15 To 1
        SetMemory(0x661ED4, Add, -917504),# units:Unit Size Down  index:225    from 15 To 1
        SetMemory(0x661EDC, Add, -917504),# units:Unit Size Down  index:226    from 15 To 1
        SetMemory(0x661EE4, Add, -917504),# units:Unit Size Down  index:227    from 15 To 1
        SetMemory(0x662FB4, Add, 70),# units:Portrait  index:22    from 9 To 79
        SetMemory(0x662FD4, Add, 16),# units:Portrait  index:38    from 21 To 37
        SetMemory(0x662FDC, Add, -15),# units:Portrait  index:42    from 25 To 10
        SetMemory(0x662FE4, Add, -29),# units:Portrait  index:46    from 29 To 0
        SetMemory(0x662FE4, Add, 3211264),# units:Portrait  index:47    from 30 To 79
        SetMemory(0x662FF0, Add, 53),# units:Portrait  index:52    from 29 To 82
        SetMemory(0x662FF0, Add, 851968),# units:Portrait  index:53    from 37 To 50
        SetMemory(0x662FF8, Add, -5),# units:Portrait  index:56    from 27 To 22
        SetMemory(0x662FF8, Add, 3538944),# units:Portrait  index:57    from 25 To 79
        SetMemory(0x663000, Add, 196608),# units:Portrait  index:61    from 49 To 52
        SetMemory(0x663004, Add, -51),# units:Portrait  index:62    from 97 To 46
        SetMemory(0x663004, Add, -3211264),# units:Portrait  index:63    from 99 To 50
        SetMemory(0x663008, Add, 655360),# units:Portrait  index:65    from 40 To 50
        SetMemory(0x66300C, Add, -1966080),# units:Portrait  index:67    from 42 To 12
        SetMemory(0x66301C, Add, -1900544),# units:Portrait  index:75    from 52 To 23
        SetMemory(0x663028, Add, -3145728),# units:Portrait  index:81    from 56 To 8
        SetMemory(0x66302C, Add, -3145728),# units:Portrait  index:83    from 56 To 8
        SetMemory(0x663034, Add, 49),# units:Portrait  index:86    from 46 To 95
        SetMemory(0x663034, Add, -3080192),# units:Portrait  index:87    from 59 To 12
        SetMemory(0x663044, Add, -46),# units:Portrait  index:94    from 102 To 56
        SetMemory(0x6630D8, Add, 19),# units:Portrait  index:168    from 41 To 60
        SetMemory(0x663888, Add, -25),# units:Mineral Cost  index:0    from 50 To 25
        SetMemory(0x66388C, Add, -25),# units:Mineral Cost  index:2    from 75 To 50
        SetMemory(0x66388C, Add, -1638400),# units:Mineral Cost  index:3    from 100 To 75
        SetMemory(0x663890, Add, -3276800),# units:Mineral Cost  index:5    from 150 To 100
        SetMemory(0x663894, Add, -3276800),# units:Mineral Cost  index:7    from 50 To 0
        SetMemory(0x663898, Add, -150),# units:Mineral Cost  index:8    from 150 To 0
        SetMemory(0x6638CC, Add, -37),# units:Mineral Cost  index:34    from 50 To 13
        SetMemory(0x66391C, Add, -5242880),# units:Mineral Cost  index:75    from 100 To 20
        SetMemory(0x663944, Add, -1),# units:Mineral Cost  index:94    from 1 To 0
        SetMemory(0x663948, Add, -1),# units:Mineral Cost  index:96    from 1 To 0
        SetMemory(0x663954, Add, -3014656),# units:Mineral Cost  index:103    from 50 To 4
        SetMemory(0x6639BC, Add, -400),# units:Mineral Cost  index:154    from 400 To 0
        SetMemory(0x6639C0, Add, 300),# units:Mineral Cost  index:156    from 100 To 400
        SetMemory(0x6639C8, Add, -50),# units:Mineral Cost  index:160    from 150 To 100
        SetMemory(0x6639D8, Add, -150),# units:Mineral Cost  index:168    from 150 To 0
        SetMemory(0x65FD00, Add, -4915200),# units:Vespene Cost  index:1    from 75 To 0
        SetMemory(0x65FD04, Add, -3276800),# units:Vespene Cost  index:3    from 50 To 0
        SetMemory(0x65FD08, Add, -6553600),# units:Vespene Cost  index:5    from 100 To 0
        SetMemory(0x65FD10, Add, -100),# units:Vespene Cost  index:8    from 100 To 0
        SetMemory(0x660428, Add, -22937600),# units:Build Time  index:1    from 750 To 400
        SetMemory(0x660430, Add, -22937600),# units:Build Time  index:5    from 750 To 400
        SetMemory(0x6604BC, Add, -74711040),# units:Build Time  index:75    from 1500 To 360
        SetMemory(0x66055C, Add, -1750),# units:Build Time  index:154    from 1800 To 50
        SetMemory(0x660568, Add, -450),# units:Build Time  index:160    from 900 To 450
        SetMemory(0x6637A0, Add, 2),# units:Staredit Group Flags  index:0    from 10 To 12
        SetMemory(0x6637A0, Add, 512),# units:Staredit Group Flags  index:1    from 10 To 12
        SetMemory(0x6637A0, Add, 131072),# units:Staredit Group Flags  index:2    from 10 To 12
        SetMemory(0x6637A0, Add, 33554432),# units:Staredit Group Flags  index:3    from 10 To 12
        SetMemory(0x6637A8, Add, 2),# units:Staredit Group Flags  index:8    from 10 To 12
        SetMemory(0x6637A8, Add, 512),# units:Staredit Group Flags  index:9    from 10 To 12
        SetMemory(0x6637A8, Add, 2097152),# units:Staredit Group Flags  index:10    from 10 To 42
        SetMemory(0x6637AC, Add, 2),# units:Staredit Group Flags  index:12    from 10 To 12
        SetMemory(0x6637B0, Add, 32),# units:Staredit Group Flags  index:16    from 10 To 42
        SetMemory(0x6637B0, Add, 536870912),# units:Staredit Group Flags  index:19    from 10 To 42
        SetMemory(0x6637B4, Add, 32),# units:Staredit Group Flags  index:20    from 10 To 42
        SetMemory(0x6637B4, Add, 8704),# units:Staredit Group Flags  index:21    from 10 To 44
        SetMemory(0x6637B4, Add, 7864320),# units:Staredit Group Flags  index:22    from 10 To 130
        SetMemory(0x6637BC, Add, 131072),# units:Staredit Group Flags  index:30    from 10 To 12
        SetMemory(0x6637C0, Add, 131072),# units:Staredit Group Flags  index:34    from 10 To 12
        SetMemory(0x6637C4, Add, 8448),# units:Staredit Group Flags  index:37    from 9 To 42
        SetMemory(0x6637C4, Add, 2097152),# units:Staredit Group Flags  index:38    from 9 To 41
        SetMemory(0x6637C8, Add, 256),# units:Staredit Group Flags  index:41    from 9 To 10
        SetMemory(0x6637C8, Add, 65536),# units:Staredit Group Flags  index:42    from 9 To 10
        SetMemory(0x6637D0, Add, 33),# units:Staredit Group Flags  index:48    from 9 To 42
        SetMemory(0x6637D0, Add, 256),# units:Staredit Group Flags  index:49    from 9 To 10
        SetMemory(0x6637D0, Add, 553648128),# units:Staredit Group Flags  index:51    from 9 To 42
        SetMemory(0x6637D4, Add, -7),# units:Staredit Group Flags  index:52    from 9 To 2
        SetMemory(0x6637D4, Add, 8448),# units:Staredit Group Flags  index:53    from 9 To 42
        SetMemory(0x6637D4, Add, 2162688),# units:Staredit Group Flags  index:54    from 9 To 42
        SetMemory(0x6637D4, Add, 16777216),# units:Staredit Group Flags  index:55    from 9 To 10
        SetMemory(0x6637D8, Add, 32),# units:Staredit Group Flags  index:56    from 9 To 41
        SetMemory(0x6637D8, Add, 2304),# units:Staredit Group Flags  index:57    from 9 To 18
        SetMemory(0x6637DC, Add, 8192),# units:Staredit Group Flags  index:61    from 12 To 44
        SetMemory(0x6637DC, Add, 65536),# units:Staredit Group Flags  index:62    from 9 To 10
        SetMemory(0x6637DC, Add, -33554432),# units:Staredit Group Flags  index:63    from 12 To 10
        SetMemory(0x6637E0, Add, 7680),# units:Staredit Group Flags  index:65    from 12 To 42
        SetMemory(0x6637E0, Add, 1966080),# units:Staredit Group Flags  index:66    from 12 To 42
        SetMemory(0x6637E0, Add, 536870912),# units:Staredit Group Flags  index:67    from 12 To 44
        SetMemory(0x6637E4, Add, 30),# units:Staredit Group Flags  index:68    from 12 To 42
        SetMemory(0x6637E4, Add, 8192),# units:Staredit Group Flags  index:69    from 12 To 44
        SetMemory(0x6637E4, Add, -33554432),# units:Staredit Group Flags  index:71    from 12 To 10
        SetMemory(0x6637E8, Add, -2),# units:Staredit Group Flags  index:72    from 12 To 10
        SetMemory(0x6637E8, Add, -512),# units:Staredit Group Flags  index:73    from 12 To 10
        SetMemory(0x6637E8, Add, -131072),# units:Staredit Group Flags  index:74    from 12 To 10
        SetMemory(0x6637EC, Add, 30),# units:Staredit Group Flags  index:76    from 12 To 42
        SetMemory(0x6637EC, Add, 7680),# units:Staredit Group Flags  index:77    from 12 To 42
        SetMemory(0x6637EC, Add, 1966080),# units:Staredit Group Flags  index:78    from 12 To 42
        SetMemory(0x6637EC, Add, 503316480),# units:Staredit Group Flags  index:79    from 12 To 42
        SetMemory(0x6637F0, Add, 30),# units:Staredit Group Flags  index:80    from 12 To 42
        SetMemory(0x6637F0, Add, -512),# units:Staredit Group Flags  index:81    from 12 To 10
        SetMemory(0x6637F0, Add, -131072),# units:Staredit Group Flags  index:82    from 12 To 10
        SetMemory(0x6637F0, Add, -33554432),# units:Staredit Group Flags  index:83    from 12 To 10
        SetMemory(0x6637F4, Add, 116),# units:Staredit Group Flags  index:84    from 12 To 128
        SetMemory(0x6637F4, Add, -131072),# units:Staredit Group Flags  index:86    from 12 To 10
        SetMemory(0x6637F4, Add, 503316480),# units:Staredit Group Flags  index:87    from 12 To 42
        SetMemory(0x6637F8, Add, 30),# units:Staredit Group Flags  index:88    from 12 To 42
        SetMemory(0x663800, Add, -131072),# units:Staredit Group Flags  index:98    from 12 To 10
        SetMemory(0x663800, Add, 536870912),# units:Staredit Group Flags  index:99    from 10 To 42
        SetMemory(0x663804, Add, 32),# units:Staredit Group Flags  index:100    from 10 To 42
        SetMemory(0x663808, Add, 33),# units:Staredit Group Flags  index:104    from 9 To 42
        SetMemory(0x663820, Add, -30720),# units:Staredit Group Flags  index:129    from 128 To 8
        SetMemory(0x66382C, Add, -8),# units:Staredit Group Flags  index:140    from 17 To 9
        SetMemory(0x663830, Add, -268435456),# units:Staredit Group Flags  index:147    from 17 To 1
        SetMemory(0x663834, Add, -16),# units:Staredit Group Flags  index:148    from 17 To 1
        SetMemory(0x663838, Add, 0),# units:Staredit Group Flags  index:154    from 52 To 52
        SetMemory(0x663838, Add, -570425344),# units:Staredit Group Flags  index:155    from 52 To 18
        SetMemory(0x66383C, Add, 0),# units:Staredit Group Flags  index:156    from 20 To 20
        SetMemory(0x66383C, Add, -512),# units:Staredit Group Flags  index:157    from 20 To 18
        SetMemory(0x663840, Add, 0),# units:Staredit Group Flags  index:160    from 52 To 52
        SetMemory(0x663840, Add, -131072),# units:Staredit Group Flags  index:162    from 20 To 18
        SetMemory(0x663840, Add, -33554432),# units:Staredit Group Flags  index:163    from 20 To 18
        SetMemory(0x663844, Add, -2),# units:Staredit Group Flags  index:164    from 20 To 18
        SetMemory(0x663844, Add, -512),# units:Staredit Group Flags  index:165    from 20 To 18
        SetMemory(0x663844, Add, -131072),# units:Staredit Group Flags  index:166    from 20 To 18
        SetMemory(0x663844, Add, -536870912),# units:Staredit Group Flags  index:167    from 52 To 20
        SetMemory(0x663848, Add, 0),# units:Staredit Group Flags  index:168    from 20 To 20
        SetMemory(0x663848, Add, -512),# units:Staredit Group Flags  index:169    from 20 To 18
        SetMemory(0x663848, Add, 8126464),# units:Staredit Group Flags  index:170    from 20 To 144
        SetMemory(0x663848, Add, -33554432),# units:Staredit Group Flags  index:171    from 20 To 18
        SetMemory(0x663850, Add, -2080374784),# units:Staredit Group Flags  index:179    from 144 To 20
        SetMemory(0x663854, Add, -124),# units:Staredit Group Flags  index:180    from 144 To 20
        SetMemory(0x663854, Add, -31744),# units:Staredit Group Flags  index:181    from 144 To 20
        SetMemory(0x663854, Add, -8126464),# units:Staredit Group Flags  index:182    from 144 To 20
        SetMemory(0x663858, Add, -31744),# units:Staredit Group Flags  index:185    from 144 To 20
        SetMemory(0x663858, Add, -8126464),# units:Staredit Group Flags  index:186    from 144 To 20
        SetMemory(0x663858, Add, -2080374784),# units:Staredit Group Flags  index:187    from 144 To 20
        SetMemory(0x66385C, Add, 134217728),# units:Staredit Group Flags  index:191    from 1 To 9
        SetMemory(0x663860, Add, 8),# units:Staredit Group Flags  index:192    from 2 To 10
        SetMemory(0x663860, Add, 2048),# units:Staredit Group Flags  index:193    from 4 To 12
        SetMemory(0x663860, Add, 3145728),# units:Staredit Group Flags  index:194    from 1 To 49
        SetMemory(0x663864, Add, 16),# units:Staredit Group Flags  index:196    from 4 To 20
        SetMemory(0x663864, Add, 4096),# units:Staredit Group Flags  index:197    from 1 To 17
        SetMemory(0x663864, Add, 1048576),# units:Staredit Group Flags  index:198    from 2 To 18
        SetMemory(0x663864, Add, 268435456),# units:Staredit Group Flags  index:199    from 4 To 20
        SetMemory(0x66386C, Add, -27648),# units:Staredit Group Flags  index:205    from 128 To 20
        SetMemory(0x66386C, Add, -7077888),# units:Staredit Group Flags  index:206    from 128 To 20
        SetMemory(0x66386C, Add, -1811939328),# units:Staredit Group Flags  index:207    from 128 To 20
        SetMemory(0x663870, Add, -108),# units:Staredit Group Flags  index:208    from 128 To 20
        SetMemory(0x663870, Add, -7077888),# units:Staredit Group Flags  index:210    from 128 To 20
        SetMemory(0x663870, Add, -1811939328),# units:Staredit Group Flags  index:211    from 128 To 20
        SetMemory(0x663874, Add, -108),# units:Staredit Group Flags  index:212    from 128 To 20
        SetMemory(0x663874, Add, -27648),# units:Staredit Group Flags  index:213    from 128 To 20
        SetMemory(0x664764, Add, -16),# units:Supply Provided  index:156    from 16 To 0
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663CE8, Add, -262144),# units:Supply Required  index:2    from 4 To 0
        SetMemory(0x663CE8, Add, -67108864),# units:Supply Required  index:3    from 4 To 0
        SetMemory(0x663CEC, Add, -1024),# units:Supply Required  index:5    from 4 To 0
        SetMemory(0x663CEC, Add, -33554432),# units:Supply Required  index:7    from 2 To 0
        SetMemory(0x663CF0, Add, -4),# units:Supply Required  index:8    from 4 To 0
        SetMemory(0x663CF0, Add, -1024),# units:Supply Required  index:9    from 4 To 0
        SetMemory(0x663CF0, Add, -67108864),# units:Supply Required  index:11    from 4 To 0
        SetMemory(0x663CF4, Add, -12),# units:Supply Required  index:12    from 12 To 0
        SetMemory(0x663D04, Add, -262144),# units:Supply Required  index:30    from 4 To 0
        SetMemory(0x663D08, Add, -2),# units:Supply Required  index:32    from 2 To 0
        SetMemory(0x663D08, Add, -131072),# units:Supply Required  index:34    from 2 To 0
        SetMemory(0x663D0C, Add, -256),# units:Supply Required  index:37    from 1 To 0
        SetMemory(0x663D0C, Add, -131072),# units:Supply Required  index:38    from 2 To 0
        SetMemory(0x663D0C, Add, -134217728),# units:Supply Required  index:39    from 8 To 0
        SetMemory(0x663D10, Add, -512),# units:Supply Required  index:41    from 2 To 0
        SetMemory(0x663D10, Add, -67108864),# units:Supply Required  index:43    from 4 To 0
        SetMemory(0x663D14, Add, -4),# units:Supply Required  index:44    from 4 To 0
        SetMemory(0x663D14, Add, -1024),# units:Supply Required  index:45    from 4 To 0
        SetMemory(0x663D14, Add, -262144),# units:Supply Required  index:46    from 4 To 0
        SetMemory(0x663D14, Add, -16777216),# units:Supply Required  index:47    from 1 To 0
        SetMemory(0x663D18, Add, -131072),# units:Supply Required  index:50    from 2 To 0
        SetMemory(0x663D20, Add, -393216),# units:Supply Required  index:58    from 6 To 0
        SetMemory(0x663D24, Add, -4),# units:Supply Required  index:60    from 4 To 0
        SetMemory(0x663D24, Add, -1024),# units:Supply Required  index:61    from 4 To 0
        SetMemory(0x663D24, Add, -262144),# units:Supply Required  index:62    from 4 To 0
        SetMemory(0x663D24, Add, -134217728),# units:Supply Required  index:63    from 8 To 0
        SetMemory(0x663D28, Add, -2),# units:Supply Required  index:64    from 2 To 0
        SetMemory(0x663D28, Add, -1024),# units:Supply Required  index:65    from 4 To 0
        SetMemory(0x663D28, Add, -262144),# units:Supply Required  index:66    from 4 To 0
        SetMemory(0x663D28, Add, -67108864),# units:Supply Required  index:67    from 4 To 0
        SetMemory(0x663D2C, Add, -8),# units:Supply Required  index:68    from 8 To 0
        SetMemory(0x663D2C, Add, -1024),# units:Supply Required  index:69    from 4 To 0
        SetMemory(0x663D2C, Add, -134217728),# units:Supply Required  index:71    from 8 To 0
        SetMemory(0x663D30, Add, -12),# units:Supply Required  index:72    from 12 To 0
        SetMemory(0x663D30, Add, -131072),# units:Supply Required  index:74    from 2 To 0
        SetMemory(0x663D38, Add, -134217728),# units:Supply Required  index:83    from 8 To 0
        SetMemory(0x663D3C, Add, -2),# units:Supply Required  index:84    from 2 To 0
        SetMemory(0x663D4C, Add, -67108864),# units:Supply Required  index:103    from 4 To 0
        SetMemory(0x664410, Add, 16580608),# units:Space Required  index:2    from 2 To 255
        SetMemory(0x664410, Add, 4244635648),# units:Space Required  index:3    from 2 To 255
        SetMemory(0x664414, Add, 64256),# units:Space Required  index:5    from 4 To 255
        SetMemory(0x66441C, Add, 16777216),# units:Space Required  index:15    from 1 To 2
        SetMemory(0x664420, Add, -256),# units:Space Required  index:17    from 2 To 1
        SetMemory(0x664420, Add, -16777216),# units:Space Required  index:19    from 2 To 1
        SetMemory(0x664424, Add, -65024),# units:Space Required  index:21    from 255 To 1
        SetMemory(0x664434, Add, -65536),# units:Space Required  index:38    from 2 To 1
        SetMemory(0x664434, Add, -33554432),# units:Space Required  index:39    from 4 To 2
        SetMemory(0x664438, Add, 254),# units:Space Required  index:40    from 1 To 255
        SetMemory(0x664440, Add, -2),# units:Space Required  index:48    from 4 To 2
        SetMemory(0x664444, Add, -256),# units:Space Required  index:53    from 2 To 1
        SetMemory(0x664448, Add, -253),# units:Space Required  index:56    from 255 To 2
        SetMemory(0x66444C, Add, -256),# units:Space Required  index:61    from 2 To 1
        SetMemory(0x66444C, Add, -33554432),# units:Space Required  index:63    from 4 To 2
        SetMemory(0x664450, Add, -256),# units:Space Required  index:65    from 2 To 1
        SetMemory(0x664450, Add, -196608),# units:Space Required  index:66    from 4 To 1
        SetMemory(0x664450, Add, -16777216),# units:Space Required  index:67    from 2 To 1
        SetMemory(0x664454, Add, -2),# units:Space Required  index:68    from 4 To 2
        SetMemory(0x664458, Add, -65536),# units:Space Required  index:74    from 2 To 1
        SetMemory(0x664458, Add, -16777216),# units:Space Required  index:75    from 2 To 1
        SetMemory(0x66445C, Add, -2),# units:Space Required  index:76    from 4 To 2
        SetMemory(0x66445C, Add, -256),# units:Space Required  index:77    from 2 To 1
        SetMemory(0x66445C, Add, -196608),# units:Space Required  index:78    from 4 To 1
        SetMemory(0x66445C, Add, -16777216),# units:Space Required  index:79    from 2 To 1
        SetMemory(0x664460, Add, -254),# units:Space Required  index:80    from 255 To 1
        SetMemory(0x664464, Add, -16777216),# units:Space Required  index:87    from 2 To 1
        SetMemory(0x664468, Add, -254),# units:Space Required  index:88    from 255 To 1
        SetMemory(0x660990, Add, -134217728),# units:Space Provided  index:11    from 8 To 0
        SetMemory(0x6609C0, Add, -2048),# units:Space Provided  index:57    from 8 To 0
        SetMemory(0x663408, Add, -50),# units:Build Score  index:0    from 50 To 0
        SetMemory(0x663408, Add, -11468800),# units:Build Score  index:1    from 175 To 0
        SetMemory(0x663420, Add, -1200),# units:Build Score  index:12    from 1200 To 0
        SetMemory(0x663448, Add, -100),# units:Build Score  index:32    from 100 To 0
        SetMemory(0x66344C, Add, -125),# units:Build Score  index:34    from 125 To 0
        SetMemory(0x663450, Add, -1638400),# units:Build Score  index:37    from 25 To 0
        SetMemory(0x663454, Add, -125),# units:Build Score  index:38    from 125 To 0
        SetMemory(0x663454, Add, -42598400),# units:Build Score  index:39    from 650 To 0
        SetMemory(0x66345C, Add, -19660800),# units:Build Score  index:43    from 300 To 0
        SetMemory(0x663464, Add, -225),# units:Build Score  index:46    from 225 To 0
        SetMemory(0x663480, Add, -21299200),# units:Build Score  index:61    from 325 To 0
        SetMemory(0x663488, Add, -50),# units:Build Score  index:64    from 50 To 0
        SetMemory(0x663488, Add, -6553600),# units:Build Score  index:65    from 100 To 0
        SetMemory(0x66348C, Add, -250),# units:Build Score  index:66    from 250 To 0
        SetMemory(0x66348C, Add, -22937600),# units:Build Score  index:67    from 350 To 0
        SetMemory(0x663490, Add, -700),# units:Build Score  index:68    from 700 To 0
        SetMemory(0x663490, Add, -13107200),# units:Build Score  index:69    from 200 To 0
        SetMemory(0x66352C, Add, -40),# units:Build Score  index:146    from 40 To 0
        SetMemory(0x66353C, Add, -400),# units:Build Score  index:154    from 400 To 0
        SetMemory(0x66353C, Add, -19660800),# units:Build Score  index:155    from 300 To 0
        SetMemory(0x663540, Add, -50),# units:Build Score  index:156    from 50 To 0
        SetMemory(0x663548, Add, -75),# units:Build Score  index:160    from 75 To 0
        SetMemory(0x66354C, Add, -100),# units:Build Score  index:162    from 100 To 0
        SetMemory(0x663550, Add, -100),# units:Build Score  index:164    from 100 To 0
        SetMemory(0x663554, Add, -100),# units:Build Score  index:166    from 100 To 0
        SetMemory(0x663554, Add, -19660800),# units:Build Score  index:167    from 300 To 0
        SetMemory(0x663558, Add, -22937600),# units:Build Score  index:169    from 350 To 0
        SetMemory(0x66355C, Add, -450),# units:Build Score  index:170    from 450 To 0
        SetMemory(0x66355C, Add, -8192000),# units:Build Score  index:171    from 125 To 0
        SetMemory(0x663560, Add, -50),# units:Build Score  index:172    from 50 To 0
        SetMemory(0x663EB8, Add, -96),# units:Destroy Score  index:0    from 100 To 4
        SetMemory(0x663EB8, Add, -22675456),# units:Destroy Score  index:1    from 350 To 4
        SetMemory(0x663EBC, Add, -26214400),# units:Destroy Score  index:3    from 400 To 0
        SetMemory(0x663EC0, Add, -45875200),# units:Destroy Score  index:5    from 700 To 0
        SetMemory(0x663EC4, Add, -6553600),# units:Destroy Score  index:7    from 100 To 0
        SetMemory(0x663EC8, Add, -800),# units:Destroy Score  index:8    from 800 To 0
        SetMemory(0x663EC8, Add, -81920000),# units:Destroy Score  index:9    from 1250 To 0
        SetMemory(0x663ECC, Add, -395),# units:Destroy Score  index:10    from 400 To 5
        SetMemory(0x663ECC, Add, -39321600),# units:Destroy Score  index:11    from 600 To 0
        SetMemory(0x663ED0, Add, -2380),# units:Destroy Score  index:12    from 2400 To 20
        SetMemory(0x663ED0, Add, -1638400),# units:Destroy Score  index:13    from 25 To 0
        SetMemory(0x663ED4, Add, -655360),# units:Destroy Score  index:15    from 10 To 0
        SetMemory(0x663ED8, Add, -696),# units:Destroy Score  index:16    from 700 To 4
        SetMemory(0x663ED8, Add, -51904512),# units:Destroy Score  index:17    from 800 To 8
        SetMemory(0x663EDC, Add, -19136512),# units:Destroy Score  index:19    from 300 To 8
        SetMemory(0x663EE0, Add, -196),# units:Destroy Score  index:20    from 200 To 4
        SetMemory(0x663EE0, Add, -104595456),# units:Destroy Score  index:21    from 1600 To 4
        SetMemory(0x663EE4, Add, -2500),# units:Destroy Score  index:22    from 2500 To 0
        SetMemory(0x663EE4, Add, -91750400),# units:Destroy Score  index:23    from 1400 To 0
        SetMemory(0x663EE8, Add, -91750400),# units:Destroy Score  index:25    from 1400 To 0
        SetMemory(0x663EEC, Add, -314572800),# units:Destroy Score  index:27    from 4800 To 0
        SetMemory(0x663EF0, Add, -4780),# units:Destroy Score  index:28    from 4800 To 20
        SetMemory(0x663EF0, Add, -313262080),# units:Destroy Score  index:29    from 4800 To 20
        SetMemory(0x663EF4, Add, -700),# units:Destroy Score  index:30    from 700 To 0
        SetMemory(0x663EF8, Add, -195),# units:Destroy Score  index:32    from 200 To 5
        SetMemory(0x663EFC, Add, -246),# units:Destroy Score  index:34    from 250 To 4
        SetMemory(0x663F00, Add, -2949120),# units:Destroy Score  index:37    from 50 To 5
        SetMemory(0x663F04, Add, -342),# units:Destroy Score  index:38    from 350 To 8
        SetMemory(0x663F04, Add, -84475904),# units:Destroy Score  index:39    from 1300 To 11
        SetMemory(0x663F08, Add, -25),# units:Destroy Score  index:40    from 25 To 0
        SetMemory(0x663F08, Add, -6553600),# units:Destroy Score  index:41    from 100 To 0
        SetMemory(0x663F0C, Add, -200),# units:Destroy Score  index:42    from 200 To 0
        SetMemory(0x663F0C, Add, -38404096),# units:Destroy Score  index:43    from 600 To 14
        SetMemory(0x663F10, Add, -1000),# units:Destroy Score  index:44    from 1100 To 100
        SetMemory(0x663F10, Add, -52428800),# units:Destroy Score  index:45    from 800 To 0
        SetMemory(0x663F14, Add, -450),# units:Destroy Score  index:46    from 450 To 0
        SetMemory(0x663F14, Add, -13107200),# units:Destroy Score  index:47    from 200 To 0
        SetMemory(0x663F18, Add, -2589),# units:Destroy Score  index:48    from 2600 To 11
        SetMemory(0x663F1C, Add, -400),# units:Destroy Score  index:50    from 400 To 0
        SetMemory(0x663F1C, Add, -261816320),# units:Destroy Score  index:51    from 4000 To 5
        SetMemory(0x663F20, Add, -900),# units:Destroy Score  index:52    from 900 To 0
        SetMemory(0x663F20, Add, -32505856),# units:Destroy Score  index:53    from 500 To 4
        SetMemory(0x663F24, Add, -92),# units:Destroy Score  index:54    from 100 To 8
        SetMemory(0x663F24, Add, -77725696),# units:Destroy Score  index:55    from 1200 To 14
        SetMemory(0x663F28, Add, -2189),# units:Destroy Score  index:56    from 2200 To 11
        SetMemory(0x663F28, Add, -26214400),# units:Destroy Score  index:57    from 400 To 0
        SetMemory(0x663F2C, Add, -800),# units:Destroy Score  index:58    from 800 To 0
        SetMemory(0x663F2C, Add, -72089600),# units:Destroy Score  index:59    from 1100 To 0
        SetMemory(0x663F30, Add, -700),# units:Destroy Score  index:60    from 700 To 0
        SetMemory(0x663F30, Add, -42270720),# units:Destroy Score  index:61    from 650 To 5
        SetMemory(0x663F34, Add, -1100),# units:Destroy Score  index:62    from 1100 To 0
        SetMemory(0x663F34, Add, -85196800),# units:Destroy Score  index:63    from 1300 To 0
        SetMemory(0x663F38, Add, -99),# units:Destroy Score  index:64    from 100 To 1
        SetMemory(0x663F38, Add, -12779520),# units:Destroy Score  index:65    from 200 To 5
        SetMemory(0x663F3C, Add, -492),# units:Destroy Score  index:66    from 500 To 8
        SetMemory(0x663F3C, Add, -45613056),# units:Destroy Score  index:67    from 700 To 4
        SetMemory(0x663F40, Add, -1389),# units:Destroy Score  index:68    from 1400 To 11
        SetMemory(0x663F40, Add, -26017792),# units:Destroy Score  index:69    from 400 To 3
        SetMemory(0x663F44, Add, -134348800),# units:Destroy Score  index:71    from 2050 To 0
        SetMemory(0x663F48, Add, -1900),# units:Destroy Score  index:72    from 1900 To 0
        SetMemory(0x663F48, Add, -3932160),# units:Destroy Score  index:73    from 60 To 0
        SetMemory(0x663F4C, Add, -400),# units:Destroy Score  index:74    from 400 To 0
        SetMemory(0x663F4C, Add, -52101120),# units:Destroy Score  index:75    from 800 To 5
        SetMemory(0x663F50, Add, -2789),# units:Destroy Score  index:76    from 2800 To 11
        SetMemory(0x663F50, Add, -25886720),# units:Destroy Score  index:77    from 400 To 5
        SetMemory(0x663F54, Add, -992),# units:Destroy Score  index:78    from 1000 To 8
        SetMemory(0x663F54, Add, -91488256),# units:Destroy Score  index:79    from 1400 To 4
        SetMemory(0x663F58, Add, -2596),# units:Destroy Score  index:80    from 2600 To 4
        SetMemory(0x663F58, Add, -104857600),# units:Destroy Score  index:81    from 1600 To 0
        SetMemory(0x663F5C, Add, -3800),# units:Destroy Score  index:82    from 3800 To 0
        SetMemory(0x663F5C, Add, -52428800),# units:Destroy Score  index:83    from 800 To 0
        SetMemory(0x663F60, Add, -450),# units:Destroy Score  index:84    from 450 To 0
        SetMemory(0x663F64, Add, -4100),# units:Destroy Score  index:86    from 4100 To 0
        SetMemory(0x663F64, Add, -91488256),# units:Destroy Score  index:87    from 1400 To 4
        SetMemory(0x663F68, Add, -2396),# units:Destroy Score  index:88    from 2400 To 4
        SetMemory(0x663F74, Add, -7),# units:Destroy Score  index:94    from 10 To 3
        SetMemory(0x663F78, Add, -10),# units:Destroy Score  index:96    from 10 To 0
        SetMemory(0x663F7C, Add, -1300),# units:Destroy Score  index:98    from 1300 To 0
        SetMemory(0x663F7C, Add, -45613056),# units:Destroy Score  index:99    from 700 To 4
        SetMemory(0x663F80, Add, -696),# units:Destroy Score  index:100    from 700 To 4
        SetMemory(0x663F84, Add, -4780),# units:Destroy Score  index:102    from 4800 To 20
        SetMemory(0x663F84, Add, -32768000),# units:Destroy Score  index:103    from 500 To 0
        SetMemory(0x663F88, Add, -696),# units:Destroy Score  index:104    from 700 To 4
        SetMemory(0x663F90, Add, -225),# units:Destroy Score  index:108    from 225 To 0
        SetMemory(0x663F90, Add, -9830400),# units:Destroy Score  index:109    from 150 To 0
        SetMemory(0x663F94, Add, -150),# units:Destroy Score  index:110    from 150 To 0
        SetMemory(0x663F98, Add, -300),# units:Destroy Score  index:112    from 300 To 0
        SetMemory(0x663F9C, Add, -600),# units:Destroy Score  index:114    from 600 To 0
        SetMemory(0x663FA0, Add, -14745600),# units:Destroy Score  index:117    from 225 To 0
        SetMemory(0x663FA4, Add, -225),# units:Destroy Score  index:118    from 225 To 0
        SetMemory(0x663FA8, Add, -225),# units:Destroy Score  index:120    from 225 To 0
        SetMemory(0x663FAC, Add, -195),# units:Destroy Score  index:122    from 195 To 0
        SetMemory(0x663FAC, Add, -19660800),# units:Destroy Score  index:123    from 300 To 0
        SetMemory(0x663FB0, Add, -150),# units:Destroy Score  index:124    from 150 To 0
        SetMemory(0x663FB4, Add, -5000),# units:Destroy Score  index:126    from 5000 To 0
        SetMemory(0x663FB4, Add, -327680000),# units:Destroy Score  index:127    from 5000 To 0
        SetMemory(0x663FC0, Add, -1200),# units:Destroy Score  index:132    from 1200 To 0
        SetMemory(0x663FC0, Add, -98304000),# units:Destroy Score  index:133    from 1500 To 0
        SetMemory(0x663FC4, Add, -19660800),# units:Destroy Score  index:135    from 300 To 0
        SetMemory(0x663FC8, Add, -450),# units:Destroy Score  index:136    from 450 To 0
        SetMemory(0x663FC8, Add, -88473600),# units:Destroy Score  index:137    from 1350 To 0
        SetMemory(0x663FCC, Add, -525),# units:Destroy Score  index:138    from 525 To 0
        SetMemory(0x663FCC, Add, -7864320),# units:Destroy Score  index:139    from 120 To 0
        SetMemory(0x663FD0, Add, -825),# units:Destroy Score  index:140    from 825 To 0
        SetMemory(0x663FD0, Add, -49152000),# units:Destroy Score  index:141    from 750 To 0
        SetMemory(0x663FD4, Add, -225),# units:Destroy Score  index:142    from 225 To 0
        SetMemory(0x663FD4, Add, -7864320),# units:Destroy Score  index:143    from 120 To 0
        SetMemory(0x663FDC, Add, -240),# units:Destroy Score  index:146    from 240 To 0
        SetMemory(0x663FDC, Add, -655360000),# units:Destroy Score  index:147    from 10000 To 0
        SetMemory(0x663FE0, Add, -10000),# units:Destroy Score  index:148    from 10000 To 0
        SetMemory(0x663FE4, Add, -5000),# units:Destroy Score  index:150    from 5000 To 0
        SetMemory(0x663FEC, Add, -1200),# units:Destroy Score  index:154    from 1200 To 0
        SetMemory(0x663FEC, Add, -58327040),# units:Destroy Score  index:155    from 900 To 10
        SetMemory(0x663FF0, Add, -150),# units:Destroy Score  index:156    from 150 To 0
        SetMemory(0x663FF0, Add, -9830400),# units:Destroy Score  index:157    from 150 To 0
        SetMemory(0x663FF4, Add, -34406400),# units:Destroy Score  index:159    from 525 To 0
        SetMemory(0x663FF8, Add, -200),# units:Destroy Score  index:160    from 225 To 25
        SetMemory(0x663FFC, Add, -272),# units:Destroy Score  index:162    from 300 To 28
        SetMemory(0x663FFC, Add, -39321600),# units:Destroy Score  index:163    from 600 To 0
        SetMemory(0x664000, Add, -300),# units:Destroy Score  index:164    from 300 To 0
        SetMemory(0x664000, Add, -49152000),# units:Destroy Score  index:165    from 750 To 0
        SetMemory(0x664004, Add, -278),# units:Destroy Score  index:166    from 300 To 22
        SetMemory(0x664004, Add, -58982400),# units:Destroy Score  index:167    from 900 To 0
        SetMemory(0x664008, Add, -5000),# units:Destroy Score  index:168    from 5000 To 0
        SetMemory(0x664008, Add, -67502080),# units:Destroy Score  index:169    from 1050 To 20
        SetMemory(0x66400C, Add, -1350),# units:Destroy Score  index:170    from 1350 To 0
        SetMemory(0x66400C, Add, -22937600),# units:Destroy Score  index:171    from 375 To 25
        SetMemory(0x664010, Add, -150),# units:Destroy Score  index:172    from 150 To 0
        SetMemory(0x664010, Add, -163840000),# units:Destroy Score  index:173    from 2500 To 0
        SetMemory(0x664014, Add, -5000),# units:Destroy Score  index:174    from 5000 To 0
        SetMemory(0x664030, Add, -131072000),# units:Destroy Score  index:189    from 2000 To 0
        SetMemory(0x664058, Add, -6553600),# units:Destroy Score  index:209    from 100 To 0
        SetMemory(0x66405C, Add, -100),# units:Destroy Score  index:210    from 100 To 0
        SetMemory(0x66405C, Add, -6553600),# units:Destroy Score  index:211    from 100 To 0
        SetMemory(0x664060, Add, -100),# units:Destroy Score  index:212    from 100 To 0
        SetMemory(0x664060, Add, -6553600),# units:Destroy Score  index:213    from 100 To 0
        SetMemory(0x6606D8, Add, 0),# units:Broodwar Unit Flag  index:2    from 0 To 0
        SetMemory(0x661534, Add, 335),# units:Staredit Availability Flags  index:14    from 128 To 463
        SetMemory(0x661544, Add, 8),# units:Staredit Availability Flags  index:22    from 455 To 463
        SetMemory(0x66154C, Add, 29556736),# units:Staredit Availability Flags  index:27    from 4 To 455
        SetMemory(0x661588, Add, 524288),# units:Staredit Availability Flags  index:57    from 455 To 463
        SetMemory(0x6615C4, Add, 30081024),# units:Staredit Availability Flags  index:87    from 4 To 463
        SetMemory(0x6615C8, Add, 589824),# units:Staredit Availability Flags  index:89    from 454 To 463
        SetMemory(0x6615CC, Add, 9),# units:Staredit Availability Flags  index:90    from 454 To 463
        SetMemory(0x6615D0, Add, 589824),# units:Staredit Availability Flags  index:93    from 966 To 975
        SetMemory(0x6615D4, Add, 9),# units:Staredit Availability Flags  index:94    from 966 To 975
        SetMemory(0x6615D4, Add, 589824),# units:Staredit Availability Flags  index:95    from 454 To 463
        SetMemory(0x6615D8, Add, 9),# units:Staredit Availability Flags  index:96    from 966 To 975
        SetMemory(0x6615DC, Add, 459),# units:Staredit Availability Flags  index:98    from 4 To 463
        SetMemory(0x6615E4, Add, 459),# units:Staredit Availability Flags  index:102    from 4 To 463
        SetMemory(0x6615E4, Add, 524288),# units:Staredit Availability Flags  index:103    from 967 To 975
        SetMemory(0x661618, Add, -25690112),# units:Staredit Availability Flags  index:129    from 855 To 463
        SetMemory(0x661670, Add, 36175872),# units:Staredit Availability Flags  index:173    from 455 To 1007
        SetMemory(0x66167C, Add, 30343168),# units:Staredit Availability Flags  index:179    from 0 To 463
        SetMemory(0x661680, Add, 463),# units:Staredit Availability Flags  index:180    from 0 To 463
        SetMemory(0x661680, Add, 30343168),# units:Staredit Availability Flags  index:181    from 0 To 463
        SetMemory(0x661684, Add, 463),# units:Staredit Availability Flags  index:182    from 0 To 463
        SetMemory(0x661688, Add, 30343168),# units:Staredit Availability Flags  index:185    from 0 To 463
        SetMemory(0x66168C, Add, 463),# units:Staredit Availability Flags  index:186    from 0 To 463
        SetMemory(0x66168C, Add, 30343168),# units:Staredit Availability Flags  index:187    from 0 To 463
        SetMemory(0x661694, Add, 63897600),# units:Staredit Availability Flags  index:191    from 0 To 975
        SetMemory(0x661698, Add, 975),# units:Staredit Availability Flags  index:192    from 0 To 975
        SetMemory(0x661698, Add, 63897600),# units:Staredit Availability Flags  index:193    from 0 To 975
        SetMemory(0x6616B0, Add, 28246016),# units:Staredit Availability Flags  index:205    from 32 To 463
        SetMemory(0x6616B4, Add, 431),# units:Staredit Availability Flags  index:206    from 32 To 463
        SetMemory(0x6616B4, Add, 28246016),# units:Staredit Availability Flags  index:207    from 32 To 463
        SetMemory(0x6616B8, Add, 431),# units:Staredit Availability Flags  index:208    from 32 To 463
        SetMemory(0x6616BC, Add, 431),# units:Staredit Availability Flags  index:210    from 32 To 463
        SetMemory(0x6616BC, Add, 28246016),# units:Staredit Availability Flags  index:211    from 32 To 463
        SetMemory(0x6616C0, Add, 431),# units:Staredit Availability Flags  index:212    from 32 To 463
        SetMemory(0x6616C0, Add, 28246016),# units:Staredit Availability Flags  index:213    from 32 To 463
        SetMemory(0x6616C4, Add, 7864320),# units:Staredit Availability Flags  index:215    from 343 To 463
        SetMemory(0x6616C8, Add, 120),# units:Staredit Availability Flags  index:216    from 343 To 463
        SetMemory(0x6616C8, Add, 7864320),# units:Staredit Availability Flags  index:217    from 343 To 463
        SetMemory(0x6616CC, Add, 120),# units:Staredit Availability Flags  index:218    from 343 To 463
        SetMemory(0x6616CC, Add, 7864320),# units:Staredit Availability Flags  index:219    from 343 To 463
        SetMemory(0x6616D0, Add, 455),# units:Staredit Availability Flags  index:220    from 0 To 455
        SetMemory(0x6616D0, Add, 29818880),# units:Staredit Availability Flags  index:221    from 0 To 455
        SetMemory(0x6616D4, Add, 343),# units:Staredit Availability Flags  index:222    from 0 To 343
        SetMemory(0x6616D4, Add, 30343168),# units:Staredit Availability Flags  index:223    from 0 To 463
        SetMemory(0x6616D8, Add, 343),# units:Staredit Availability Flags  index:224    from 0 To 343
        SetMemory(0x6616D8, Add, 63897600),# units:Staredit Availability Flags  index:225    from 0 To 975
        SetMemory(0x6616DC, Add, 463),# units:Staredit Availability Flags  index:226    from 0 To 463
        SetMemory(0x6616DC, Add, 30343168),# units:Staredit Availability Flags  index:227    from 0 To 463
        SetMemory(0x6572E0, Add, 2),# weapons:Label  index:0    from 229 To 231
        SetMemory(0x6572E0, Add, 65536),# weapons:Label  index:1    from 230 To 231
        SetMemory(0x6572E4, Add, -65536),# weapons:Label  index:3    from 232 To 231
        SetMemory(0x6572E8, Add, -2),# weapons:Label  index:4    from 233 To 231
        SetMemory(0x6572E8, Add, -196608),# weapons:Label  index:5    from 234 To 231
        SetMemory(0x6572EC, Add, -86),# weapons:Label  index:6    from 316 To 230
        SetMemory(0x6572EC, Add, -327680),# weapons:Label  index:7    from 235 To 230
        SetMemory(0x6572F0, Add, -4),# weapons:Label  index:8    from 236 To 232
        SetMemory(0x6572F0, Add, -458752),# weapons:Label  index:9    from 237 To 230
        SetMemory(0x6572F4, Add, -6),# weapons:Label  index:10    from 238 To 232
        SetMemory(0x6572F4, Add, -458752),# weapons:Label  index:11    from 239 To 232
        SetMemory(0x6572F8, Add, -8),# weapons:Label  index:12    from 240 To 232
        SetMemory(0x6572F8, Add, -720896),# weapons:Label  index:13    from 241 To 230
        SetMemory(0x6572FC, Add, -720896),# weapons:Label  index:15    from 243 To 232
        SetMemory(0x657300, Add, -14),# weapons:Label  index:16    from 244 To 230
        SetMemory(0x657300, Add, -851968),# weapons:Label  index:17    from 245 To 232
        SetMemory(0x657304, Add, -15),# weapons:Label  index:18    from 246 To 231
        SetMemory(0x657304, Add, -1114112),# weapons:Label  index:19    from 247 To 230
        SetMemory(0x657308, Add, -18),# weapons:Label  index:20    from 248 To 230
        SetMemory(0x657308, Add, -1245184),# weapons:Label  index:21    from 249 To 230
        SetMemory(0x65730C, Add, -20),# weapons:Label  index:22    from 250 To 230
        SetMemory(0x65730C, Add, -1376256),# weapons:Label  index:23    from 251 To 230
        SetMemory(0x657310, Add, -22),# weapons:Label  index:24    from 252 To 230
        SetMemory(0x657310, Add, -1441792),# weapons:Label  index:25    from 253 To 231
        SetMemory(0x657314, Add, -24),# weapons:Label  index:26    from 254 To 230
        SetMemory(0x657314, Add, -1638400),# weapons:Label  index:27    from 255 To 230
        SetMemory(0x657318, Add, -1769472),# weapons:Label  index:29    from 257 To 230
        SetMemory(0x657324, Add, -1966080),# weapons:Label  index:35    from 260 To 230
        SetMemory(0x657328, Add, -30),# weapons:Label  index:36    from 261 To 231
        SetMemory(0x657328, Add, -2097152),# weapons:Label  index:37    from 262 To 230
        SetMemory(0x65732C, Add, -31),# weapons:Label  index:38    from 263 To 232
        SetMemory(0x65732C, Add, -2228224),# weapons:Label  index:39    from 264 To 230
        SetMemory(0x657330, Add, -35),# weapons:Label  index:40    from 265 To 230
        SetMemory(0x657330, Add, -2359296),# weapons:Label  index:41    from 266 To 230
        SetMemory(0x657334, Add, -37),# weapons:Label  index:42    from 267 To 230
        SetMemory(0x65733C, Add, -2752512),# weapons:Label  index:47    from 272 To 230
        SetMemory(0x657340, Add, -41),# weapons:Label  index:48    from 273 To 232
        SetMemory(0x657340, Add, -2752512),# weapons:Label  index:49    from 274 To 232
        SetMemory(0x657344, Add, -45),# weapons:Label  index:50    from 275 To 230
        SetMemory(0x657348, Add, -3080192),# weapons:Label  index:53    from 279 To 232
        SetMemory(0x657350, Add, 1638400),# weapons:Label  index:57    from 375 To 400
        SetMemory(0x65735C, Add, -51),# weapons:Label  index:62    from 281 To 230
        SetMemory(0x657360, Add, -52),# weapons:Label  index:64    from 282 To 230
        SetMemory(0x657360, Add, -3407872),# weapons:Label  index:65    from 283 To 231
        SetMemory(0x657364, Add, -54),# weapons:Label  index:66    from 286 To 232
        SetMemory(0x657364, Add, -3604480),# weapons:Label  index:67    from 287 To 232
        SetMemory(0x657368, Add, -58),# weapons:Label  index:68    from 288 To 230
        SetMemory(0x657368, Add, -3801088),# weapons:Label  index:69    from 289 To 231
        SetMemory(0x65736C, Add, -60),# weapons:Label  index:70    from 290 To 230
        SetMemory(0x65736C, Add, -3997696),# weapons:Label  index:71    from 291 To 230
        SetMemory(0x657370, Add, -4063232),# weapons:Label  index:73    from 293 To 231
        SetMemory(0x657374, Add, -1),# weapons:Label  index:74    from 294 To 293
        SetMemory(0x657380, Add, -70),# weapons:Label  index:80    from 300 To 230
        SetMemory(0x657380, Add, -4653056),# weapons:Label  index:81    from 301 To 230
        SetMemory(0x657388, Add, -3604480),# weapons:Label  index:85    from 285 To 230
        SetMemory(0x6573A8, Add, -954),# weapons:Label  index:100    from 1240 To 286
        SetMemory(0x6573BC, Add, -3538944),# weapons:Label  index:111    from 284 To 230
        SetMemory(0x6573C0, Add, -65536),# weapons:Label  index:113    from 231 To 230
        SetMemory(0x6573C4, Add, -63),# weapons:Label  index:114    from 293 To 230
        SetMemory(0x6573C8, Add, 0),# weapons:Label  index:116    from 231 To 231
        SetMemory(0x6573C8, Add, 196608),# weapons:Label  index:117    from 229 To 232
        SetMemory(0x6573CC, Add, 3),# weapons:Label  index:118    from 229 To 232
        SetMemory(0x6573D4, Add, 1260),# weapons:Label  index:122    from 229 To 1489
        SetMemory(0x6573D8, Add, 1262),# weapons:Label  index:124    from 229 To 1491
        SetMemory(0x6573D8, Add, 82771968),# weapons:Label  index:125    from 229 To 1492
        SetMemory(0x6573DC, Add, 1264),# weapons:Label  index:126    from 229 To 1493
        SetMemory(0x6573DC, Add, 83623936),# weapons:Label  index:127    from 229 To 1505
        SetMemory(0x6573E0, Add, 1),# weapons:Label  index:128    from 229 To 230
        SetMemory(0x6573E0, Add, 196608),# weapons:Label  index:129    from 229 To 232
        SetMemory(0x656CF0, Add, -7),# weapons:Graphics  index:18    from 149 To 142
        SetMemory(0x656D14, Add, -2),# weapons:Graphics  index:27    from 150 To 148
        SetMemory(0x656D28, Add, 4),# weapons:Graphics  index:32    from 146 To 150
        SetMemory(0x656D44, Add, -171),# weapons:Graphics  index:39    from 171 To 0
        SetMemory(0x656D50, Add, 142),# weapons:Graphics  index:42    from 0 To 142
        SetMemory(0x656D64, Add, -163),# weapons:Graphics  index:47    from 163 To 0
        SetMemory(0x656D70, Add, -20),# weapons:Graphics  index:50    from 162 To 142
        SetMemory(0x656D84, Add, -21),# weapons:Graphics  index:55    from 172 To 151
        SetMemory(0x656D88, Add, 35),# weapons:Graphics  index:56    from 167 To 202
        SetMemory(0x656D8C, Add, 35),# weapons:Graphics  index:57    from 167 To 202
        SetMemory(0x656DBC, Add, -1),# weapons:Graphics  index:69    from 143 To 142
        SetMemory(0x656DC0, Add, 4),# weapons:Graphics  index:70    from 156 To 160
        SetMemory(0x656DCC, Add, -9),# weapons:Graphics  index:73    from 152 To 143
        SetMemory(0x656DE0, Add, 43),# weapons:Graphics  index:78    from 159 To 202
        SetMemory(0x656DF4, Add, -18),# weapons:Graphics  index:83    from 172 To 154
        SetMemory(0x656DF8, Add, 45),# weapons:Graphics  index:84    from 157 To 202
        SetMemory(0x656E38, Add, -47),# weapons:Graphics  index:100    from 206 To 159
        SetMemory(0x656E44, Add, -43),# weapons:Graphics  index:103    from 202 To 159
        SetMemory(0x656E48, Add, -45),# weapons:Graphics  index:104    from 204 To 159
        SetMemory(0x656E70, Add, 19),# weapons:Graphics  index:114    from 152 To 171
        SetMemory(0x656E74, Add, -2),# weapons:Graphics  index:115    from 154 To 152
        SetMemory(0x656E78, Add, 6),# weapons:Graphics  index:116    from 143 To 149
        SetMemory(0x656E7C, Add, 4),# weapons:Graphics  index:117    from 142 To 146
        SetMemory(0x656E80, Add, 4),# weapons:Graphics  index:118    from 142 To 146
        SetMemory(0x656EA8, Add, 6),# weapons:Graphics  index:128    from 142 To 148
        SetMemory(0x656EAC, Add, 4),# weapons:Graphics  index:129    from 142 To 146
        SetMemory(0x6579BC, Add, 1),# weapons:Target Flags  index:18    from 2 To 3
        SetMemory(0x6579D0, Add, 131072),# weapons:Target Flags  index:29    from 1 To 3
        SetMemory(0x6579D4, Add, -1),# weapons:Target Flags  index:30    from 3 To 2
        SetMemory(0x6579D8, Add, -21),# weapons:Target Flags  index:32    from 23 To 2
        SetMemory(0x6579E4, Add, -65536),# weapons:Target Flags  index:39    from 3 To 2
        SetMemory(0x6579EC, Add, 1),# weapons:Target Flags  index:42    from 2 To 3
        SetMemory(0x6579FC, Add, 1),# weapons:Target Flags  index:50    from 2 To 3
        SetMemory(0x657A04, Add, 131072),# weapons:Target Flags  index:55    from 1 To 3
        SetMemory(0x657A08, Add, -16),# weapons:Target Flags  index:56    from 19 To 3
        SetMemory(0x657A08, Add, -3211264),# weapons:Target Flags  index:57    from 178 To 129
        SetMemory(0x657A20, Add, 65536),# weapons:Target Flags  index:69    from 2 To 3
        SetMemory(0x657A24, Add, 0),# weapons:Target Flags  index:70    from 3 To 3
        SetMemory(0x657A28, Add, 65536),# weapons:Target Flags  index:73    from 2 To 3
        SetMemory(0x657A2C, Add, 2),# weapons:Target Flags  index:74    from 1 To 3
        SetMemory(0x657A30, Add, -65536),# weapons:Target Flags  index:77    from 3 To 2
        SetMemory(0x657A34, Add, -2),# weapons:Target Flags  index:78    from 3 To 1
        SetMemory(0x657A3C, Add, -4194304),# weapons:Target Flags  index:83    from 67 To 3
        SetMemory(0x657A40, Add, -82),# weapons:Target Flags  index:84    from 83 To 1
        SetMemory(0x657A60, Add, 1),# weapons:Target Flags  index:100    from 1 To 2
        SetMemory(0x657A64, Add, 65536),# weapons:Target Flags  index:103    from 1 To 2
        SetMemory(0x657A68, Add, 1),# weapons:Target Flags  index:104    from 1 To 2
        SetMemory(0x657A7C, Add, 1),# weapons:Target Flags  index:114    from 2 To 3
        SetMemory(0x657A7C, Add, 65536),# weapons:Target Flags  index:115    from 1 To 2
        SetMemory(0x657A94, Add, -196608),# weapons:Target Flags  index:127    from 3 To 0
        SetMemory(0x657A98, Add, -1),# weapons:Target Flags  index:128    from 3 To 2
        SetMemory(0x656A84, Add, -64),# weapons:Minimum Range  index:27    from 64 To 0
        SetMemory(0x656A88, Add, -32),# weapons:Minimum Range  index:28    from 64 To 32
        SetMemory(0x657474, Add, -32),# weapons:Maximum Range  index:1    from 160 To 128
        SetMemory(0x657478, Add, -16),# weapons:Maximum Range  index:2    from 224 To 208
        SetMemory(0x65747C, Add, 32),# weapons:Maximum Range  index:3    from 192 To 224
        SetMemory(0x657480, Add, 32),# weapons:Maximum Range  index:4    from 160 To 192
        SetMemory(0x657484, Add, 16),# weapons:Maximum Range  index:5    from 160 To 176
        SetMemory(0x657490, Add, 64),# weapons:Maximum Range  index:8    from 160 To 224
        SetMemory(0x657494, Add, 16),# weapons:Maximum Range  index:9    from 160 To 176
        SetMemory(0x657498, Add, 64),# weapons:Maximum Range  index:10    from 160 To 224
        SetMemory(0x6574B8, Add, -32),# weapons:Maximum Range  index:18    from 160 To 128
        SetMemory(0x6574BC, Add, 32),# weapons:Maximum Range  index:19    from 192 To 224
        SetMemory(0x6574C0, Add, 32),# weapons:Maximum Range  index:20    from 192 To 224
        SetMemory(0x6574C4, Add, 32),# weapons:Maximum Range  index:21    from 192 To 224
        SetMemory(0x6574C8, Add, 32),# weapons:Maximum Range  index:22    from 192 To 224
        SetMemory(0x6574CC, Add, 32),# weapons:Maximum Range  index:23    from 192 To 224
        SetMemory(0x6574DC, Add, -128),# weapons:Maximum Range  index:27    from 384 To 256
        SetMemory(0x6574E0, Add, -160),# weapons:Maximum Range  index:28    from 384 To 224
        SetMemory(0x6574E8, Add, -128),# weapons:Maximum Range  index:30    from 320 To 192
        SetMemory(0x6574F0, Add, -96),# weapons:Maximum Range  index:32    from 256 To 160
        SetMemory(0x65750C, Add, -145),# weapons:Maximum Range  index:39    from 160 To 15
        SetMemory(0x657518, Add, 222),# weapons:Maximum Range  index:42    from 2 To 224
        SetMemory(0x657528, Add, -128),# weapons:Maximum Range  index:46    from 256 To 128
        SetMemory(0x65752C, Add, -231),# weapons:Maximum Range  index:47    from 256 To 25
        SetMemory(0x657530, Add, 64),# weapons:Maximum Range  index:48    from 96 To 160
        SetMemory(0x657534, Add, 64),# weapons:Maximum Range  index:49    from 96 To 160
        SetMemory(0x657538, Add, 96),# weapons:Maximum Range  index:50    from 128 To 224
        SetMemory(0x657550, Add, 160),# weapons:Maximum Range  index:56    from 384 To 544
        SetMemory(0x657554, Add, 480),# weapons:Maximum Range  index:57    from 288 To 768
        SetMemory(0x657578, Add, 16),# weapons:Maximum Range  index:66    from 128 To 144
        SetMemory(0x657584, Add, 32),# weapons:Maximum Range  index:69    from 96 To 128
        SetMemory(0x657594, Add, 96),# weapons:Maximum Range  index:73    from 128 To 224
        SetMemory(0x657598, Add, 128),# weapons:Maximum Range  index:74    from 128 To 256
        SetMemory(0x6575A8, Add, 32),# weapons:Maximum Range  index:78    from 160 To 192
        SetMemory(0x6575AC, Add, 128),# weapons:Maximum Range  index:79    from 128 To 256
        SetMemory(0x6575BC, Add, 128),# weapons:Maximum Range  index:83    from 288 To 416
        SetMemory(0x6575C0, Add, 352),# weapons:Maximum Range  index:84    from 288 To 640
        SetMemory(0x65760C, Add, -32),# weapons:Maximum Range  index:103    from 192 To 160
        SetMemory(0x657610, Add, -64),# weapons:Maximum Range  index:104    from 192 To 128
        SetMemory(0x657630, Add, 32),# weapons:Maximum Range  index:112    from 192 To 224
        SetMemory(0x657634, Add, 16),# weapons:Maximum Range  index:113    from 192 To 208
        SetMemory(0x657638, Add, 80),# weapons:Maximum Range  index:114    from 128 To 208
        SetMemory(0x65763C, Add, -64),# weapons:Maximum Range  index:115    from 128 To 64
        SetMemory(0x657640, Add, 16),# weapons:Maximum Range  index:116    from 192 To 208
        SetMemory(0x657648, Add, 16),# weapons:Maximum Range  index:118    from 128 To 144
        SetMemory(0x657670, Add, 112),# weapons:Maximum Range  index:128    from 128 To 240
        SetMemory(0x6571D4, Add, -1),# weapons:Damage Upgrade  index:4    from 8 To 7
        SetMemory(0x6571D4, Add, -256),# weapons:Damage Upgrade  index:5    from 8 To 7
        SetMemory(0x6571D4, Add, -16777216),# weapons:Damage Upgrade  index:7    from 8 To 7
        SetMemory(0x6571D8, Add, -1),# weapons:Damage Upgrade  index:8    from 8 To 7
        SetMemory(0x6571D8, Add, -256),# weapons:Damage Upgrade  index:9    from 8 To 7
        SetMemory(0x6571D8, Add, -65536),# weapons:Damage Upgrade  index:10    from 8 To 7
        SetMemory(0x6571D8, Add, -16777216),# weapons:Damage Upgrade  index:11    from 8 To 7
        SetMemory(0x6571DC, Add, -1),# weapons:Damage Upgrade  index:12    from 8 To 7
        SetMemory(0x6571DC, Add, -33554432),# weapons:Damage Upgrade  index:15    from 9 To 7
        SetMemory(0x6571E0, Add, -2),# weapons:Damage Upgrade  index:16    from 9 To 7
        SetMemory(0x6571E0, Add, -512),# weapons:Damage Upgrade  index:17    from 9 To 7
        SetMemory(0x6571E0, Add, -131072),# weapons:Damage Upgrade  index:18    from 9 To 7
        SetMemory(0x6571E0, Add, -33554432),# weapons:Damage Upgrade  index:19    from 9 To 7
        SetMemory(0x6571E4, Add, -2),# weapons:Damage Upgrade  index:20    from 9 To 7
        SetMemory(0x6571E4, Add, 1280),# weapons:Damage Upgrade  index:21    from 9 To 14
        SetMemory(0x6571E4, Add, 327680),# weapons:Damage Upgrade  index:22    from 9 To 14
        SetMemory(0x6571E4, Add, 83886080),# weapons:Damage Upgrade  index:23    from 9 To 14
        SetMemory(0x6571E8, Add, 5),# weapons:Damage Upgrade  index:24    from 9 To 14
        SetMemory(0x6571E8, Add, 67108864),# weapons:Damage Upgrade  index:27    from 8 To 12
        SetMemory(0x6571EC, Add, 6),# weapons:Damage Upgrade  index:28    from 8 To 14
        SetMemory(0x6571EC, Add, -12288),# weapons:Damage Upgrade  index:29    from 60 To 12
        SetMemory(0x6571F0, Add, -46),# weapons:Damage Upgrade  index:32    from 60 To 14
        SetMemory(0x6571F0, Add, -50331648),# weapons:Damage Upgrade  index:35    from 10 To 7
        SetMemory(0x6571F4, Add, -3),# weapons:Damage Upgrade  index:36    from 10 To 7
        SetMemory(0x6571F4, Add, -768),# weapons:Damage Upgrade  index:37    from 10 To 7
        SetMemory(0x6571F4, Add, -262144),# weapons:Damage Upgrade  index:38    from 11 To 7
        SetMemory(0x6571F4, Add, -67108864),# weapons:Damage Upgrade  index:39    from 11 To 7
        SetMemory(0x6571F8, Add, -3),# weapons:Damage Upgrade  index:40    from 10 To 7
        SetMemory(0x6571F8, Add, -768),# weapons:Damage Upgrade  index:41    from 10 To 7
        SetMemory(0x6571F8, Add, 131072),# weapons:Damage Upgrade  index:42    from 10 To 12
        SetMemory(0x6571FC, Add, -327680),# weapons:Damage Upgrade  index:46    from 12 To 7
        SetMemory(0x6571FC, Add, -83886080),# weapons:Damage Upgrade  index:47    from 12 To 7
        SetMemory(0x657200, Add, 2),# weapons:Damage Upgrade  index:48    from 12 To 14
        SetMemory(0x657200, Add, 512),# weapons:Damage Upgrade  index:49    from 12 To 14
        SetMemory(0x657200, Add, 65536),# weapons:Damage Upgrade  index:50    from 11 To 12
        SetMemory(0x657200, Add, -67108864),# weapons:Damage Upgrade  index:51    from 11 To 7
        SetMemory(0x657204, Add, -12288),# weapons:Damage Upgrade  index:53    from 60 To 12
        SetMemory(0x657210, Add, -6),# weapons:Damage Upgrade  index:64    from 13 To 7
        SetMemory(0x657210, Add, -1536),# weapons:Damage Upgrade  index:65    from 13 To 7
        SetMemory(0x657210, Add, -393216),# weapons:Damage Upgrade  index:66    from 13 To 7
        SetMemory(0x657210, Add, -100663296),# weapons:Damage Upgrade  index:67    from 13 To 7
        SetMemory(0x657214, Add, -6),# weapons:Damage Upgrade  index:68    from 13 To 7
        SetMemory(0x657214, Add, -1536),# weapons:Damage Upgrade  index:69    from 13 To 7
        SetMemory(0x657214, Add, -393216),# weapons:Damage Upgrade  index:70    from 13 To 7
        SetMemory(0x657214, Add, -100663296),# weapons:Damage Upgrade  index:71    from 13 To 7
        SetMemory(0x657218, Add, -1792),# weapons:Damage Upgrade  index:73    from 14 To 7
        SetMemory(0x657220, Add, -53),# weapons:Damage Upgrade  index:80    from 60 To 7
        SetMemory(0x657220, Add, -12288),# weapons:Damage Upgrade  index:81    from 60 To 12
        SetMemory(0x657224, Add, -1536),# weapons:Damage Upgrade  index:85    from 13 To 7
        SetMemory(0x657234, Add, 83886080),# weapons:Damage Upgrade  index:103    from 9 To 14
        SetMemory(0x65723C, Add, -100663296),# weapons:Damage Upgrade  index:111    from 13 To 7
        SetMemory(0x657240, Add, -458752),# weapons:Damage Upgrade  index:114    from 14 To 7
        SetMemory(0x657250, Add, 7),# weapons:Damage Upgrade  index:128    from 7 To 14
        SetMemory(0x657258, Add, -1),# weapons:Weapon Type  index:0    from 3 To 2
        SetMemory(0x657258, Add, -256),# weapons:Weapon Type  index:1    from 3 To 2
        SetMemory(0x657268, Add, -65536),# weapons:Weapon Type  index:18    from 3 To 2
        SetMemory(0x657270, Add, 65536),# weapons:Weapon Type  index:26    from 2 To 3
        SetMemory(0x657270, Add, 33554432),# weapons:Weapon Type  index:27    from 1 To 3
        SetMemory(0x657274, Add, 2),# weapons:Weapon Type  index:28    from 1 To 3
        SetMemory(0x657274, Add, 512),# weapons:Weapon Type  index:29    from 1 To 3
        SetMemory(0x657274, Add, 131072),# weapons:Weapon Type  index:30    from 1 To 3
        SetMemory(0x657278, Add, -1),# weapons:Weapon Type  index:32    from 2 To 1
        SetMemory(0x65727C, Add, -1),# weapons:Weapon Type  index:36    from 3 To 2
        SetMemory(0x65727C, Add, 33554432),# weapons:Weapon Type  index:39    from 1 To 3
        SetMemory(0x657288, Add, -2),# weapons:Weapon Type  index:48    from 3 To 1
        SetMemory(0x657288, Add, -512),# weapons:Weapon Type  index:49    from 3 To 1
        SetMemory(0x657288, Add, 65536),# weapons:Weapon Type  index:50    from 2 To 3
        SetMemory(0x657290, Add, 3),# weapons:Weapon Type  index:56    from 0 To 3
        SetMemory(0x657290, Add, 768),# weapons:Weapon Type  index:57    from 0 To 3
        SetMemory(0x657298, Add, -256),# weapons:Weapon Type  index:65    from 3 To 2
        SetMemory(0x65729C, Add, -256),# weapons:Weapon Type  index:69    from 3 To 2
        SetMemory(0x6572A0, Add, -256),# weapons:Weapon Type  index:73    from 3 To 2
        SetMemory(0x6572A0, Add, 131072),# weapons:Weapon Type  index:74    from 1 To 3
        SetMemory(0x6572A4, Add, 512),# weapons:Weapon Type  index:77    from 1 To 3
        SetMemory(0x6572A4, Add, 131072),# weapons:Weapon Type  index:78    from 1 To 3
        SetMemory(0x6572A8, Add, 50331648),# weapons:Weapon Type  index:83    from 0 To 3
        SetMemory(0x6572AC, Add, -1),# weapons:Weapon Type  index:84    from 4 To 3
        SetMemory(0x6572BC, Add, 2),# weapons:Weapon Type  index:100    from 1 To 3
        SetMemory(0x6572BC, Add, 33554432),# weapons:Weapon Type  index:103    from 1 To 3
        SetMemory(0x6572C0, Add, 2),# weapons:Weapon Type  index:104    from 1 To 3
        SetMemory(0x6572C8, Add, 33554432),# weapons:Weapon Type  index:115    from 1 To 3
        SetMemory(0x6572CC, Add, 0),# weapons:Weapon Type  index:116    from 2 To 2
        SetMemory(0x6572CC, Add, -512),# weapons:Weapon Type  index:117    from 3 To 1
        SetMemory(0x6572CC, Add, -131072),# weapons:Weapon Type  index:118    from 3 To 1
        SetMemory(0x6572D8, Add, -512),# weapons:Weapon Type  index:129    from 3 To 1
        SetMemory(0x656680, Add, 8),# weapons:Weapon Behavior  index:16    from 0 To 8
        SetMemory(0x656680, Add, 131072),# weapons:Weapon Behavior  index:18    from 0 To 2
        SetMemory(0x656688, Add, -33554432),# weapons:Weapon Behavior  index:27    from 2 To 0
        SetMemory(0x656690, Add, 1),# weapons:Weapon Behavior  index:32    from 1 To 2
        SetMemory(0x656694, Add, 50331648),# weapons:Weapon Behavior  index:39    from 2 To 5
        SetMemory(0x656698, Add, -196608),# weapons:Weapon Behavior  index:42    from 5 To 2
        SetMemory(0x65669C, Add, 67108864),# weapons:Weapon Behavior  index:47    from 1 To 5
        SetMemory(0x6566A0, Add, -6),# weapons:Weapon Behavior  index:48    from 7 To 1
        SetMemory(0x6566A0, Add, -1536),# weapons:Weapon Behavior  index:49    from 7 To 1
        SetMemory(0x6566A0, Add, 131072),# weapons:Weapon Behavior  index:50    from 0 To 2
        SetMemory(0x6566B4, Add, -65536),# weapons:Weapon Behavior  index:70    from 2 To 1
        SetMemory(0x6566C0, Add, -67108864),# weapons:Weapon Behavior  index:83    from 5 To 1
        SetMemory(0x6566C4, Add, -2),# weapons:Weapon Behavior  index:84    from 3 To 1
        SetMemory(0x6566D4, Add, -1),# weapons:Weapon Behavior  index:100    from 2 To 1
        SetMemory(0x6566D4, Add, -117440512),# weapons:Weapon Behavior  index:103    from 8 To 1
        SetMemory(0x6566D8, Add, 1),# weapons:Weapon Behavior  index:104    from 0 To 1
        SetMemory(0x6566E0, Add, 16777216),# weapons:Weapon Behavior  index:115    from 1 To 2
        SetMemory(0x6566E4, Add, -1),# weapons:Weapon Behavior  index:116    from 2 To 1
        SetMemory(0x6566E4, Add, -512),# weapons:Weapon Behavior  index:117    from 2 To 0
        SetMemory(0x6566E4, Add, -131072),# weapons:Weapon Behavior  index:118    from 2 To 0
        SetMemory(0x6566F0, Add, -2),# weapons:Weapon Behavior  index:128    from 2 To 0
        SetMemory(0x6566F0, Add, -512),# weapons:Weapon Behavior  index:129    from 2 To 0
        SetMemory(0x65704C, Add, -256),# weapons:Remove After  index:13    from 255 To 254
        SetMemory(0x657088, Add, -57600),# weapons:Remove After  index:73    from 255 To 30
        SetMemory(0x656708, Add, 33554432),# weapons:Explosion Type  index:19    from 1 To 3
        SetMemory(0x65670C, Add, 512),# weapons:Explosion Type  index:21    from 1 To 3
        SetMemory(0x65670C, Add, 33554432),# weapons:Explosion Type  index:23    from 1 To 3
        SetMemory(0x656710, Add, -16777216),# weapons:Explosion Type  index:27    from 2 To 1
        SetMemory(0x656718, Add, -1),# weapons:Explosion Type  index:32    from 4 To 3
        SetMemory(0x656728, Add, 2),# weapons:Explosion Type  index:48    from 1 To 3
        SetMemory(0x656728, Add, 512),# weapons:Explosion Type  index:49    from 1 To 3
        SetMemory(0x656728, Add, -65536),# weapons:Explosion Type  index:50    from 2 To 1
        SetMemory(0x65672C, Add, 16777216),# weapons:Explosion Type  index:55    from 1 To 2
        SetMemory(0x656730, Add, -5),# weapons:Explosion Type  index:56    from 6 To 1
        SetMemory(0x656730, Add, -1536),# weapons:Explosion Type  index:57    from 7 To 1
        SetMemory(0x65673C, Add, -131072),# weapons:Explosion Type  index:70    from 3 To 1
        SetMemory(0x656748, Add, -131072),# weapons:Explosion Type  index:82    from 3 To 1
        SetMemory(0x656748, Add, -184549376),# weapons:Explosion Type  index:83    from 12 To 1
        SetMemory(0x65674C, Add, -1),# weapons:Explosion Type  index:84    from 2 To 1
        SetMemory(0x65675C, Add, -23),# weapons:Explosion Type  index:100    from 24 To 1
        SetMemory(0x65675C, Add, -385875968),# weapons:Explosion Type  index:103    from 24 To 1
        SetMemory(0x656760, Add, -15),# weapons:Explosion Type  index:104    from 18 To 3
        SetMemory(0x656778, Add, 2),# weapons:Explosion Type  index:128    from 1 To 3
        SetMemory(0x6568A8, Add, 10),# weapons:Inner Splash Range  index:16    from 0 To 10
        SetMemory(0x6568AC, Add, 655360),# weapons:Inner Splash Range  index:19    from 0 To 10
        SetMemory(0x6568B0, Add, 655360),# weapons:Inner Splash Range  index:21    from 0 To 10
        SetMemory(0x6568B4, Add, 655360),# weapons:Inner Splash Range  index:23    from 0 To 10
        SetMemory(0x6568B8, Add, -327680),# weapons:Inner Splash Range  index:25    from 15 To 10
        SetMemory(0x6568BC, Add, -5),# weapons:Inner Splash Range  index:26    from 15 To 10
        SetMemory(0x6568BC, Add, -655360),# weapons:Inner Splash Range  index:27    from 10 To 0
        SetMemory(0x6568E8, Add, 10),# weapons:Inner Splash Range  index:48    from 0 To 10
        SetMemory(0x6568E8, Add, 655360),# weapons:Inner Splash Range  index:49    from 0 To 10
        SetMemory(0x6568EC, Add, -10),# weapons:Inner Splash Range  index:50    from 10 To 0
        SetMemory(0x6568F4, Add, 3145728),# weapons:Inner Splash Range  index:55    from 0 To 48
        SetMemory(0x656914, Add, -3),# weapons:Inner Splash Range  index:70    from 3 To 0
        SetMemory(0x65691C, Add, 10),# weapons:Inner Splash Range  index:74    from 0 To 10
        SetMemory(0x656920, Add, 1638400),# weapons:Inner Splash Range  index:77    from 0 To 25
        SetMemory(0x65692C, Add, -20),# weapons:Inner Splash Range  index:82    from 20 To 0
        SetMemory(0x656930, Add, -48),# weapons:Inner Splash Range  index:84    from 48 To 0
        SetMemory(0x656950, Add, -5),# weapons:Inner Splash Range  index:100    from 5 To 0
        SetMemory(0x656954, Add, -327680),# weapons:Inner Splash Range  index:103    from 5 To 0
        SetMemory(0x656958, Add, 25),# weapons:Inner Splash Range  index:104    from 0 To 25
        SetMemory(0x656988, Add, 10),# weapons:Inner Splash Range  index:128    from 0 To 10
        SetMemory(0x6570E8, Add, 10),# weapons:Medium Splash Range  index:16    from 0 To 10
        SetMemory(0x6570EC, Add, 655360),# weapons:Medium Splash Range  index:19    from 0 To 10
        SetMemory(0x6570F0, Add, 655360),# weapons:Medium Splash Range  index:21    from 0 To 10
        SetMemory(0x6570F4, Add, 655360),# weapons:Medium Splash Range  index:23    from 0 To 10
        SetMemory(0x6570F8, Add, -327680),# weapons:Medium Splash Range  index:25    from 20 To 15
        SetMemory(0x6570FC, Add, -5),# weapons:Medium Splash Range  index:26    from 20 To 15
        SetMemory(0x6570FC, Add, -1638400),# weapons:Medium Splash Range  index:27    from 25 To 0
        SetMemory(0x657128, Add, 10),# weapons:Medium Splash Range  index:48    from 0 To 10
        SetMemory(0x657128, Add, 655360),# weapons:Medium Splash Range  index:49    from 0 To 10
        SetMemory(0x65712C, Add, -20),# weapons:Medium Splash Range  index:50    from 20 To 0
        SetMemory(0x657134, Add, 3145728),# weapons:Medium Splash Range  index:55    from 0 To 48
        SetMemory(0x657154, Add, -15),# weapons:Medium Splash Range  index:70    from 15 To 0
        SetMemory(0x65715C, Add, 10),# weapons:Medium Splash Range  index:74    from 0 To 10
        SetMemory(0x657160, Add, 1638400),# weapons:Medium Splash Range  index:77    from 0 To 25
        SetMemory(0x65716C, Add, -40),# weapons:Medium Splash Range  index:82    from 40 To 0
        SetMemory(0x657170, Add, -48),# weapons:Medium Splash Range  index:84    from 48 To 0
        SetMemory(0x657190, Add, -50),# weapons:Medium Splash Range  index:100    from 50 To 0
        SetMemory(0x657194, Add, -3276800),# weapons:Medium Splash Range  index:103    from 50 To 0
        SetMemory(0x657198, Add, 25),# weapons:Medium Splash Range  index:104    from 0 To 25
        SetMemory(0x6571C8, Add, 10),# weapons:Medium Splash Range  index:128    from 0 To 10
        SetMemory(0x6577A0, Add, 10),# weapons:Outer Splash Range  index:16    from 0 To 10
        SetMemory(0x6577A4, Add, 655360),# weapons:Outer Splash Range  index:19    from 0 To 10
        SetMemory(0x6577A8, Add, 655360),# weapons:Outer Splash Range  index:21    from 0 To 10
        SetMemory(0x6577AC, Add, 655360),# weapons:Outer Splash Range  index:23    from 0 To 10
        SetMemory(0x6577B0, Add, -327680),# weapons:Outer Splash Range  index:25    from 25 To 20
        SetMemory(0x6577B4, Add, -5),# weapons:Outer Splash Range  index:26    from 25 To 20
        SetMemory(0x6577B4, Add, -2621440),# weapons:Outer Splash Range  index:27    from 40 To 0
        SetMemory(0x6577E0, Add, 10),# weapons:Outer Splash Range  index:48    from 0 To 10
        SetMemory(0x6577E0, Add, 655360),# weapons:Outer Splash Range  index:49    from 0 To 10
        SetMemory(0x6577E4, Add, -30),# weapons:Outer Splash Range  index:50    from 30 To 0
        SetMemory(0x6577EC, Add, 3145728),# weapons:Outer Splash Range  index:55    from 0 To 48
        SetMemory(0x65780C, Add, -30),# weapons:Outer Splash Range  index:70    from 30 To 0
        SetMemory(0x657814, Add, 10),# weapons:Outer Splash Range  index:74    from 0 To 10
        SetMemory(0x657818, Add, 1638400),# weapons:Outer Splash Range  index:77    from 0 To 25
        SetMemory(0x657824, Add, -60),# weapons:Outer Splash Range  index:82    from 60 To 0
        SetMemory(0x657828, Add, -48),# weapons:Outer Splash Range  index:84    from 48 To 0
        SetMemory(0x657848, Add, -100),# weapons:Outer Splash Range  index:100    from 100 To 0
        SetMemory(0x65784C, Add, -6553600),# weapons:Outer Splash Range  index:103    from 100 To 0
        SetMemory(0x657850, Add, 25),# weapons:Outer Splash Range  index:104    from 0 To 25
        SetMemory(0x657880, Add, 10),# weapons:Outer Splash Range  index:128    from 0 To 10
        SetMemory(0x656EB0, Add, 26),# weapons:Damage Amount  index:0    from 6 To 32
        SetMemory(0x656EB0, Add, 1114112),# weapons:Damage Amount  index:1    from 18 To 35
        SetMemory(0x656ED4, Add, 48),# weapons:Damage Amount  index:18    from 16 To 64
        SetMemory(0x656EE4, Add, 26),# weapons:Damage Amount  index:26    from 16 To 42
        SetMemory(0x656EEC, Add, -70),# weapons:Damage Amount  index:30    from 260 To 190
        SetMemory(0x656EF0, Add, 155),# weapons:Damage Amount  index:32    from 0 To 155
        SetMemory(0x656EF4, Add, 2031616),# weapons:Damage Amount  index:35    from 5 To 36
        SetMemory(0x656EF8, Add, 42),# weapons:Damage Amount  index:36    from 10 To 52
        SetMemory(0x656EFC, Add, 2162688),# weapons:Damage Amount  index:39    from 20 To 53
        SetMemory(0x656F14, Add, 75),# weapons:Damage Amount  index:50    from 5 To 80
        SetMemory(0x656F20, Add, 600),# weapons:Damage Amount  index:56    from 0 To 600
        SetMemory(0x656F20, Add, 39321600),# weapons:Damage Amount  index:57    from 0 To 600
        SetMemory(0x656F30, Add, 43),# weapons:Damage Amount  index:64    from 8 To 51
        SetMemory(0x656F30, Add, 2359296),# weapons:Damage Amount  index:65    from 20 To 56
        SetMemory(0x656F38, Add, 1114112),# weapons:Damage Amount  index:69    from 20 To 37
        SetMemory(0x656F54, Add, 26214400),# weapons:Damage Amount  index:83    from 0 To 400
        SetMemory(0x656F58, Add, 586),# weapons:Damage Amount  index:84    from 14 To 600
        SetMemory(0x656F90, Add, 1769472),# weapons:Damage Amount  index:113    from 25 To 52
        SetMemory(0x656F98, Add, 22),# weapons:Damage Amount  index:116    from 30 To 52
        SetMemory(0x656F98, Add, 3801088),# weapons:Damage Amount  index:117    from 6 To 64
        SetMemory(0x656F9C, Add, 53),# weapons:Damage Amount  index:118    from 6 To 59
        SetMemory(0x656FA4, Add, 1494),# weapons:Damage Amount  index:122    from 6 To 1500
        SetMemory(0x656FA4, Add, 12713984),# weapons:Damage Amount  index:123    from 6 To 200
        SetMemory(0x656FA8, Add, 994),# weapons:Damage Amount  index:124    from 6 To 1000
        SetMemory(0x656FA8, Add, 56950784),# weapons:Damage Amount  index:125    from 6 To 875
        SetMemory(0x656FAC, Add, 294),# weapons:Damage Amount  index:126    from 6 To 300
        SetMemory(0x656FAC, Add, 19267584),# weapons:Damage Amount  index:127    from 6 To 300
        SetMemory(0x656FB0, Add, 93),# weapons:Damage Amount  index:128    from 6 To 99
        SetMemory(0x656FB0, Add, 3604480),# weapons:Damage Amount  index:129    from 6 To 61
        SetMemory(0x6576DC, Add, 2),# weapons:Damage Bonus  index:50    from 1 To 3
        SetMemory(0x656FB8, Add, -4),# weapons:Weapon Cooldown  index:0    from 15 To 11
        SetMemory(0x656FB8, Add, -1024),# weapons:Weapon Cooldown  index:1    from 15 To 11
        SetMemory(0x656FBC, Add, -8),# weapons:Weapon Cooldown  index:4    from 30 To 22
        SetMemory(0x656FC8, Add, -1245184),# weapons:Weapon Cooldown  index:18    from 30 To 11
        SetMemory(0x656FC8, Add, -67108864),# weapons:Weapon Cooldown  index:19    from 30 To 26
        SetMemory(0x656FCC, Add, -4),# weapons:Weapon Cooldown  index:20    from 30 To 26
        SetMemory(0x656FCC, Add, -1024),# weapons:Weapon Cooldown  index:21    from 30 To 26
        SetMemory(0x656FCC, Add, -262144),# weapons:Weapon Cooldown  index:22    from 30 To 26
        SetMemory(0x656FCC, Add, -16777216),# weapons:Weapon Cooldown  index:23    from 22 To 21
        SetMemory(0x656FD0, Add, -1),# weapons:Weapon Cooldown  index:24    from 22 To 21
        SetMemory(0x656FD0, Add, -1073741824),# weapons:Weapon Cooldown  index:27    from 75 To 11
        SetMemory(0x656FD4, Add, -60),# weapons:Weapon Cooldown  index:28    from 75 To 15
        SetMemory(0x656FD8, Add, 79),# weapons:Weapon Cooldown  index:32    from 1 To 80
        SetMemory(0x656FDC, Add, 117440512),# weapons:Weapon Cooldown  index:39    from 15 To 22
        SetMemory(0x656FE4, Add, -251658240),# weapons:Weapon Cooldown  index:47    from 30 To 15
        SetMemory(0x656FE8, Add, -458752),# weapons:Weapon Cooldown  index:50    from 22 To 15
        SetMemory(0x656FEC, Add, -5376),# weapons:Weapon Cooldown  index:53    from 32 To 11
        SetMemory(0x656FF8, Add, -655360),# weapons:Weapon Cooldown  index:66    from 30 To 20
        SetMemory(0x656FF8, Add, -33554432),# weapons:Weapon Cooldown  index:67    from 22 To 20
        SetMemory(0x656FFC, Add, -2816),# weapons:Weapon Cooldown  index:69    from 22 To 11
        SetMemory(0x656FFC, Add, -327680),# weapons:Weapon Cooldown  index:70    from 20 To 15
        SetMemory(0x657000, Add, -2048),# weapons:Weapon Cooldown  index:73    from 30 To 22
        SetMemory(0x657000, Add, -385875968),# weapons:Weapon Cooldown  index:75    from 30 To 7
        SetMemory(0x657004, Add, 2560),# weapons:Weapon Cooldown  index:77    from 45 To 55
        SetMemory(0x657004, Add, -983040),# weapons:Weapon Cooldown  index:78    from 45 To 30
        SetMemory(0x657018, Add, 8),# weapons:Weapon Cooldown  index:96    from 22 To 30
        SetMemory(0x65701C, Add, 12),# weapons:Weapon Cooldown  index:100    from 8 To 20
        SetMemory(0x65701C, Add, -738197504),# weapons:Weapon Cooldown  index:103    from 64 To 20
        SetMemory(0x657020, Add, -70),# weapons:Weapon Cooldown  index:104    from 100 To 30
        SetMemory(0x657028, Add, 0),# weapons:Weapon Cooldown  index:113    from 22 To 22
        SetMemory(0x657028, Add, -524288),# weapons:Weapon Cooldown  index:114    from 30 To 22
        SetMemory(0x657028, Add, 134217728),# weapons:Weapon Cooldown  index:115    from 22 To 30
        SetMemory(0x65702C, Add, 1792),# weapons:Weapon Cooldown  index:117    from 15 To 22
        SetMemory(0x65702C, Add, 458752),# weapons:Weapon Cooldown  index:118    from 15 To 22
        SetMemory(0x657038, Add, 11),# weapons:Weapon Cooldown  index:128    from 15 To 26
        SetMemory(0x657038, Add, 1792),# weapons:Weapon Cooldown  index:129    from 15 To 22
        SetMemory(0x656504, Add, 16777216),# weapons:Damage Factor  index:39    from 1 To 2
        SetMemory(0x656544, Add, -16777216),# weapons:Damage Factor  index:103    from 2 To 1
        SetMemory(0x656550, Add, -16777216),# weapons:Damage Factor  index:115    from 2 To 1
        SetMemory(0x6569F4, Add, 112),# weapons:Attack Angle  index:100    from 16 To 128
        SetMemory(0x6569F4, Add, 1610612736),# weapons:Attack Angle  index:103    from 32 To 128
        SetMemory(0x657920, Add, -2949120),# weapons:Forward Offset  index:18    from 45 To 0
        SetMemory(0x657940, Add, -1310720),# weapons:Forward Offset  index:50    from 25 To 5
        SetMemory(0x657990, Add, 75),# weapons:Forward Offset  index:128    from 0 To 75
        SetMemory(0x6565D8, Add, -458752),# weapons:Target Error Message  index:57    from 886 To 879
        SetMemory(0x656668, Add, -262144),# weapons:Target Error Message  index:129    from 879 To 875
        SetMemory(0x6567A4, Add, -9),# weapons:Icon  index:18    from 332 To 323
        SetMemory(0x6567B4, Add, -196608),# weapons:Icon  index:27    from 336 To 333
        SetMemory(0x6567C0, Add, 94),# weapons:Icon  index:32    from 240 To 334
        SetMemory(0x6567CC, Add, 917504),# weapons:Icon  index:39    from 339 To 353
        SetMemory(0x6567D4, Add, -18),# weapons:Icon  index:42    from 341 To 323
        SetMemory(0x6567DC, Add, -262144),# weapons:Icon  index:47    from 344 To 340
        SetMemory(0x6567E4, Add, -23),# weapons:Icon  index:50    from 346 To 323
        SetMemory(0x6567EC, Add, -2555904),# weapons:Icon  index:55    from 350 To 311
        SetMemory(0x6567F0, Add, 60),# weapons:Icon  index:56    from 271 To 331
        SetMemory(0x6567F0, Add, 19070976),# weapons:Icon  index:57    from 40 To 331
        SetMemory(0x656808, Add, -2097152),# weapons:Icon  index:69    from 355 To 323
        SetMemory(0x65680C, Add, 6),# weapons:Icon  index:70    from 356 To 362
        SetMemory(0x656810, Add, -2228224),# weapons:Icon  index:73    from 358 To 324
        SetMemory(0x65681C, Add, -29),# weapons:Icon  index:78    from 360 To 331
        SetMemory(0x656824, Add, 3211264),# weapons:Icon  index:83    from 278 To 327
        SetMemory(0x656828, Add, 53),# weapons:Icon  index:84    from 278 To 331
        SetMemory(0x656828, Add, -3538944),# weapons:Icon  index:85    from 353 To 299
        SetMemory(0x656848, Add, 22),# weapons:Icon  index:100    from 332 To 354
        SetMemory(0x65684C, Add, 1507328),# weapons:Icon  index:103    from 331 To 354
        SetMemory(0x656850, Add, 10),# weapons:Icon  index:104    from 344 To 354
        SetMemory(0x656864, Add, -19),# weapons:Icon  index:114    from 358 To 339
        SetMemory(0x656864, Add, -65536),# weapons:Icon  index:115    from 359 To 358
        SetMemory(0x656868, Add, 0),# weapons:Icon  index:116    from 324 To 324
        SetMemory(0x656868, Add, 917504),# weapons:Icon  index:117    from 323 To 337
        SetMemory(0x65686C, Add, 14),# weapons:Icon  index:118    from 323 To 337
        SetMemory(0x656874, Add, -211),# weapons:Icon  index:122    from 323 To 112
        SetMemory(0x656874, Add, -13959168),# weapons:Icon  index:123    from 323 To 110
        SetMemory(0x656878, Add, -147),# weapons:Icon  index:124    from 323 To 176
        SetMemory(0x656878, Add, -13565952),# weapons:Icon  index:125    from 323 To 116
        SetMemory(0x65687C, Add, -146),# weapons:Icon  index:126    from 323 To 177
        SetMemory(0x65687C, Add, -9830400),# weapons:Icon  index:127    from 323 To 173
        SetMemory(0x656880, Add, 10),# weapons:Icon  index:128    from 323 To 333
        SetMemory(0x656880, Add, 917504),# weapons:Icon  index:129    from 323 To 337
        SetMemory(0x6CA414, Add, -52),# flingy:Sprite  index:126    from 287 To 235
        SetMemory(0x6C9FAC, Add, 200),# flingy:Speed  index:45    from 853 To 1053
        SetMemory(0x6C9FC0, Add, 2547),# flingy:Speed  index:50    from 853 To 3400
        SetMemory(0x6CA040, Add, 52),# flingy:Speed  index:82    from 1 To 53
        SetMemory(0x6CA050, Add, -1067),# flingy:Speed  index:86    from 1280 To 213
        SetMemory(0x6CA058, Add, 3293),# flingy:Speed  index:88    from 1707 To 5000
        SetMemory(0x6CA0AC, Add, -7070),# flingy:Speed  index:109    from 8533 To 1463
        SetMemory(0x6CA0F0, Add, 0),# flingy:Speed  index:126    from 0 To 0
        SetMemory(0x6C9CD0, Add, 393216),# flingy:Acceleration  index:45    from 27 To 33
        SetMemory(0x6C9CDC, Add, 80),# flingy:Acceleration  index:50    from 27 To 107
        SetMemory(0x6C9D1C, Add, 26),# flingy:Acceleration  index:82    from 1 To 27
        SetMemory(0x6C9D24, Add, -23),# flingy:Acceleration  index:86    from 50 To 27
        SetMemory(0x6C9D28, Add, 200),# flingy:Acceleration  index:88    from 100 To 300
        SetMemory(0x6C9D50, Add, -589824),# flingy:Acceleration  index:109    from 33 To 24
        SetMemory(0x6C9D74, Add, 0),# flingy:Acceleration  index:126    from 0 To 0
        SetMemory(0x6C9A78, Add, 499),# flingy:Halt Distance  index:82    from 1 To 500
        SetMemory(0x6C9A88, Add, -4280),# flingy:Halt Distance  index:86    from 5120 To 840
        SetMemory(0x6C9AE4, Add, -1067213),# flingy:Halt Distance  index:109    from 1103213 To 36000
        SetMemory(0x6C9B28, Add, 0),# flingy:Halt Distance  index:126    from 0 To 0
        SetMemory(0x6C9E70, Add, 7471104),# flingy:Turn Radius  index:82    from 13 To 127
        SetMemory(0x6C9E9C, Add, 8323072),# flingy:Turn Radius  index:126    from 0 To 127
        SetMemory(0x6C98A8, Add, -131072),# flingy:Movement Control  index:82    from 2 To 0
        SetMemory(0x6C98D4, Add, -131072),# flingy:Movement Control  index:126    from 2 To 0
        SetMemory(0x66EC48, Add, 133),# images:Iscript ID  index:0    from 0 To 133
        SetMemory(0x66F138, Add, -49),# images:Iscript ID  index:316    from 131 To 82
        SetMemory(0x6559D8, Add, -3276800),# upgrades:Mineral Cost Factor  index:13    from 50 To 0
        SetMemory(0x655858, Add, -6422528),# upgrades:Vespene Cost Base  index:13    from 100 To 2
        SetMemory(0x655B80, Add, -1600),# upgrades:Research Time Base  index:0    from 4000 To 2400
        SetMemory(0x655B98, Add, 180224000),# upgrades:Research Time Base  index:13    from 4000 To 6750
        SetMemory(0x655958, Add, -31457280),# upgrades:Research Time Factor  index:13    from 480 To 0
        SetMemory(0x655A44, Add, -2),# upgrades:Label  index:2    from 413 To 411
        SetMemory(0x655A44, Add, -65536),# upgrades:Label  index:3    from 414 To 413
        SetMemory(0x655A48, Add, -3),# upgrades:Label  index:4    from 415 To 412
        SetMemory(0x655A48, Add, -327680),# upgrades:Label  index:5    from 416 To 411
        SetMemory(0x655A4C, Add, -4),# upgrades:Label  index:6    from 417 To 413
        SetMemory(0x655700, Add, 252),# upgrades:Max. Repeats  index:0    from 3 To 255
        SetMemory(0x655700, Add, 64512),# upgrades:Max. Repeats  index:1    from 3 To 255
        SetMemory(0x655700, Add, 16515072),# upgrades:Max. Repeats  index:2    from 3 To 255
        SetMemory(0x655700, Add, 4227858432),# upgrades:Max. Repeats  index:3    from 3 To 255
        SetMemory(0x655704, Add, 252),# upgrades:Max. Repeats  index:4    from 3 To 255
        SetMemory(0x655704, Add, 64512),# upgrades:Max. Repeats  index:5    from 3 To 255
        SetMemory(0x655704, Add, 16515072),# upgrades:Max. Repeats  index:6    from 3 To 255
        SetMemory(0x655704, Add, 4227858432),# upgrades:Max. Repeats  index:7    from 3 To 255
        SetMemory(0x655708, Add, 252),# upgrades:Max. Repeats  index:8    from 3 To 255
        SetMemory(0x655708, Add, 64512),# upgrades:Max. Repeats  index:9    from 3 To 255
        SetMemory(0x655708, Add, 16515072),# upgrades:Max. Repeats  index:10    from 3 To 255
        SetMemory(0x65570C, Add, 252),# upgrades:Max. Repeats  index:12    from 3 To 255
        SetMemory(0x65570C, Add, 16515072),# upgrades:Max. Repeats  index:14    from 3 To 255
    ])

