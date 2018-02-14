def binInc(bin):
 carry="1"
 out=["0"]*len(bin)
 for i in range(len(bin)-1,-1,-1):
  if(carry!=bin[i]):
   out[i]="1"
  if(carry=="1" and bin[i]=="1"):
   carry="1"
  else:
   carry="0"
 return out
def binDec(bin):
 carry="1"
 out=["0"]*len(bin)
 for i in range(len(bin)-1,-1,-1):
  if(carry!=bin[i]):
   out[i]="1"
  if(carry=="1" and bin[i]=="0"):
   carry="1"
  else:
   carry="0"
 return out

def netcalc(ip,cidr):
 ipstr=""
 mskstr=""
 idstr=""
 brdcststr=""
 rngstr=["",""]
 quaddot=[]
 ipstr=ip+"/"+str(cidr)
 for num in ip.split('.'):
  quaddot.append(int(num))
 clss="Unknown"
 clssranges=[(1,126,"A"),(128,191,"B"),(192,223,"C"),(224,239,"D"),(240,254,"E")]
 for low,high,res in clssranges:
  if(int(quaddot[0])>=low and int(quaddot[0])<=high):
   clss=res
 ipbin=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
 for quadind in range(4):
  for bit in range(8):
   ipbin[(8*quadind)+bit]=str(quaddot[quadind]//(2**(7-bit)))
   quaddot[quadind]%=2**(7-bit)
 submsk=["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
 for i in range(cidr):
  submsk[i]="1"
 submskint=[0,0,0,0]
 for i in range(4):
  for j in range(8):
   submskint[i]+=(int(submsk[(8*i)+j]))*(2**(7-j))
  if i>0:
   mskstr+="."
  mskstr+=str(submskint[i])
 netidbin=["0"]*32
 for i in range(32):
  if ipbin[i]=="1" and submsk[i]=="1":
   netidbin[i]="1"
 netid=[0,0,0,0]
 for i in range(32):
  netid[i//8]+=(int(netidbin[i]))*(2**(7-(i%8)))
 for i in range(4):
  if i>0:
   idstr+="."
  idstr+=str(netid[i])
 brdbin=["0"]*32
 for i in range(32):
  if ipbin[i]=="1" or submsk[i]=="0":
   brdbin[i]="1"
 brdcst=[0,0,0,0]
 for i in range(32):
  brdcst[i//8]+=(int(brdbin[i]))*(2**(7-(i%8)))
 for i in range(4):
  if i>0:
   brdcststr+="."
  brdcststr+=str(brdcst[i])
 rngmaxbin=binDec(brdbin)
 rngminbin=binInc(netidbin)
 rngmax=[0,0,0,0]
 rngmin=[0,0,0,0]
 for i in range(32):
  rngmax[i//8]+=(int(rngmaxbin[i]))*(2**(7-(i%8)))
  rngmin[i//8]+=(int(rngminbin[i]))*(2**(7-(i%8)))
 for i in range(4):
  if i>0:
   rngstr[0]+="."
   rngstr[1]+="."
  rngstr[0]+=str(rngmin[i])
  rngstr[1]+=str(rngmax[i])
 return ipstr,clss,mskstr,idstr,brdcststr,rngstr

if __name__=='__main__':
 import sys
 fullip=sys.argv[1]
 arrfullip=fullip.split('/')
 ipstr,clss,mskstr,idstr,brdcststr,rngstr=netcalc(arrfullip[0],int(arrfullip[1]))
 print("IP: ",ipstr,"\nClass: ",clss,"\nNet-Mask: ",mskstr,"\nNet-ID: ",idstr,"\nBroadcast-Address: ",brdcststr,"\nRange: ",rngstr[0],"-",rngstr[1],sep="")
