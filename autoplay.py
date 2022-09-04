import pyautogui
import time

def press(key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)

#起风了
QiFengLe="(VJ)Q(AW)ED TE B S G/\
(CJ)Q(MW)ED TE (NW)E(AQ)W(DJ)QG/\
(VJ)Q(AW)ED TE B S G/\
(CJ)Q(MW)ED TE (NDW)EQW(BSJ)QG/\
(VJ)Q(AW)ED (AT)EB S G S/\
(CJ)Q(MW)ED (MT)E (NW)E(AQ)W(DJ)QG/\
(VJ)Q(AW)ED (AT)EB S G/\
(NDWY)EWH DNSDN/\
(ZS) CA(BS) XA(CS)D G D/\
(ZS) BA(XS) CA(BS) DSA N/\
(CS) XA(CS) BA(NS)D G D/\
(VS) XD(VS) (BA)S (NS)/\
(XS) VA(NS) VA (BS)(XD)(VG)D/\
(NS) XD(CS)(BA)N/\
DSAS (VA) Z (XD)SAS (BA) X/\
(VD)SAS Z (BA) X C (NA)S (BAD)A/\
(VH) (AG)HD A (BJ) (SH)JG S/\
(CJ) (BH)JMDB  (NQ) W(AQ)J(DH)(AG)/\
(VH) (AG)HD G(AH)G (BH)(MG)(AS)(MG)/\
Z (BD) X C (NA)S (BAD)A/\
(VH) (AG)HD A (BJ) (SH)JG S/\
(CJ) (BH)JMDB  (NQ) W(AQ)J(DH)(AG)/\
(VH) (AE)E DGA (BH) (ME)E SGMH/\
(CNH) C (NM) C (NA)/\
Q W (VQE) (AY)TD (AY)TB (SY)TGWS/\
(CE) (MY)TD (MY)TN (DY)THED W/\
(VW) (AQ)HD AQ (BW) (SQ)HGQS/\
(ZQE) B A R(SE)W (DE)W (BQ) W/\
(VQE) (AY)TD (AY)TB (SY)TGWS/\
(CE) (MY)TD (MY)TN (DY)THED W/\
(VW) (AQ)HDEA W(BW) (SQ)HGQS/\
(NQ) C N M A/\
H E (VAW) QH E (BSW) QH Q Q/\
(VJ)Q(AW)ED (AT)EB S G S/\
(CJ)Q(MW)ED (MT)E (NW)E(AQ)W(DJ)QG/\
(VJ)Q(AW)ED (AT)EB S G/\
(NDWY)EWH DNSDN"


#小城夏天
XiaoChengXiaTian="(VE) A /(DR) (VE) /A (DW)Q/(VJ) A /\
(BQ) (AJ) /S (BQ) /(AD) S /B A /\
(ZE) A /(DR) (ZE) /A (DW)Q/(ZJ) A /\
(NQ) (AJ) /S (NQ) /(AD) S /(NG) A /\
(VE) A /(DR) (VE) /A (DW)Q/(VJ) A /\
(BQ) (AJ) /S (BQ) /(AD) S /B A /\
(ZE) A /(DR) (ZE) /A (DW)Q/(ZJ) A /\
B  /B  /B  /B  /\
(VQ) Q /(ADW) (VQ) /Q (VQ) /(ADQ) (VQ) /\
(BJ) Q /(MSJ) B /G B /(MS) B /\
(ZQ) Q /(ADW) (ZQ) /Q (ZQ) /(ADQ) (ZQ) /\
(NT) Q /(ADJ) N /Q N /(ADT) N /\
(VT)  /(ADQ) V /Q (VQ) /(ADQ) (VQ) /\
(BQ)  /(MSJ) B /G B /(MS) (BG) /\
(ZQ) Q /(ADW) (ZQ) /Q (ZQ) /(ADQ) Z /\
(NE)  /(ADJ) N /Q N /(AD) N /\
(VQ) Q /(ADW) (VQ) /Q (VQ) /(ADQ) (VQ) /\
(BJ) Q /(MSJ) B /G B /(MS) B /\
(ZQ) Q /(ADW) (ZQ) /Q (ZQ) /(ADQ) (ZQ) /\
(NT) Q /(ADJ) N /Q N /(ADT) N /\
(VT)  /(ADQ) V /Q V /(ADQ) (VQ) /\
(BJ) Q /(MSJ) B /G B /(MS) (BG) /\
(ZR) E /(ADE) (ZR) /T (ZQ) /(ADQ) (ZT) /\
N T /(AD) N /E (NW) /(ADE) (NW)"


#红色高跟鞋
REDGaoGenXie="(VNA) /(NAT) (VW) /(BMS) J /(MSG) (BJ)/\
(NAD) Q /(AD) N /(MT) (AE) /(BMQ) (AY)/\
(VNA) /(NAT) (VY) /(BMS) T /(MSE) (BE)/\
(NAD)WQ /(AD) (NQ) /(MT) (AE) /(BMQ) (AQ)/\
(VNA)  /(NAT) (VW) /(BMS)  /(MSJ) (BJ)/\
(NAD) Q /(AD) NQ/(NADT) EE/(BMS)W Q/\
(VNA) /(VNA) /(VNA) /(VNAW)EW /\
(BMS)   /   G/J Q /G J /\
(VNAH) /(NAH)(VQ) /(BMSY) /(MST)(BT)/\
(NAD) E /(AD) N /M A /(BM) A/\
(VNA) /(NAH)(VQ) /(BMSY) /(MST) (BT)/\
(NAD) E /(AD) N /M A /(BM) A/\
(VNA) /(NAE)E(VE)E /(BMSW) J /(MS) (BQ)/\
(NAD) Q /(ADH) (NQ) /M A /(BM) A/\
(VNA) /(NAE)E(VE)E /(BMSW) T /(MS) (BJ)/\
(NAD) Q /(ADG) (NJ) /M (AQ) /(BMH) A/\
(VNA) /(NAE)W(VQ)W /(BMSW) G/(MS) (BG)/\
(NAD) /(ADE)W(NQ) /(NADW) J/(BMS) Q/\
(VNA) /(VNA) /(VNA) H /(VNAE) W/\
(BMS) T /(BMS) /(BMST) E /(BMSQ) H"

#================Add music here=============================









#=====================change the music=======================
toPlay=REDGaoGenXie
#============================================================

print("Preparing,please wait 5 seconds!")

steps=toPlay.split('/')

notes=[]
notesNum=0

for i in range(len(steps)):
    step=steps[i].split()
    for j in range(len(step)):
        step[j]=step[j].replace('(',' ')
        step[j]=step[j].replace(')',' ')
        unit=step[j].split()
        for k in range(len(unit)):
            notes.append(unit[k])
            notesNum+=1
        notes.append(" ")
        notesNum+=1
    notes.append("/")
    notesNum+=1

time.sleep(5)
print("Begin!")

#===========change the rhythm====================================
for i in range(notesNum):
    if notes[i]==" ":
        time.sleep(0.04)
        continue
    if notes[i]=='/':
        time.sleep(0.06)
        continue
    pyautogui.write(notes[i],0.02)
#================================================================

print("End!")