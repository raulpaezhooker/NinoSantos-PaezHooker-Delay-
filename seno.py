
import math

class Seno:



        def __init__(self, sampling, bits,f1,fram):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.tono=f1
            self.frames=fram

        def generar(self):
            b=[]
            d=[]
            wavearray=[]
            wavearray1=[]

            duracion=int(44100*5)
            for i in range(0, duracion):

                    datos = math.sin((2*math.pi*(self.tono)*i)/44100)*1000
                    wavearray.append(datos)

            print len(wavearray)

            for i in range (self.frames,len(wavearray)):

                c=(wavearray[i]+wavearray[i-(self.frames)])
                b.append(c)

            for i in range (0,(len(wavearray)-len(b))):
                k= wavearray[i]
                d.append(k)

            for i in range (0,len(b)):
                k=b[i]
                d.append(k)


            FinalData = d
            print len(FinalData)

            return FinalData



