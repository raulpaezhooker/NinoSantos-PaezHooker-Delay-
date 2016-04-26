import  wave
import struct
import pyaudio
import  math


class delay:


        def __init__(self, sampling, bits,Audio,tiempo,nr):

            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.tiempo=tiempo
            self.repeticiones=nr
            self.Audio=Audio


        def generar(self):
            wavearray=[]
            b=[]
            d=[]
            b=[]
            v=[]
            d=[]
            f=[]
            print "Audio", self.Audio

            frames=int(self.tiempo*44100)
            peaklevel = max(abs(self.Audio))
            print peaklevel
            for j in range (0, self.repeticiones):
                b=[]
                valueAdjust = (2000-(j*(800))) / float(peaklevel)
                print "valueadjust",valueAdjust
                datosAjustados = self.Audio * valueAdjust
                print max(datosAjustados)
                fram=(frames*self.repeticiones+44100)-(44100*j)


                for i in range (frames*j,len(self.Audio)):

                    c=(self.Audio[i]+datosAjustados[i-(frames*j)])
                    b.append(c)
                print "len de audio",len(self.Audio)
                print "Len de b",len(b)

                if len(self.Audio)==len(b):
                        for k in range (0,len(b)):
                            l=b[k]
                            f.append(l)

                elif len(self.Audio)>=len(b):
                        for o in range (0,(len(self.Audio)-len(b))):
                            m=0
                            d.append(m)
                        for o in range (0,len(b)):
                            m=b[o]
                            d.append(m)
                        for o in range (0,len(d)):
                            n=d[o]
                            f.append(n)


            for p in range (0,len(self.Audio)):
                w=f[p]+f[p+len(self.Audio)]+f[p+(2*len(self.Audio))]
                v.append(w)

            FinalData=v

            output = wave.open("delay.wav", 'w')
            Set_Bits = 16/8
            output.setparams((1, Set_Bits, 44100, 0, 'NONE', 'not compressed'))
            values = []
            for i in range(0, len(b)):
                    packed_value = struct.pack('<h', FinalData[i])
                    values.append(packed_value)
            value_str = ''.join(values)
            output.writeframes(value_str)
            output.close()
            rf = wave.open("delay.wav", 'rb')
            prof = rf.getsampwidth()
            channels = rf.getnchannels()
            rate = rf.getframerate()
            print rate
            frame=rf.getnframes()
            print frame
            audioN = pyaudio.PyAudio()
            streamN = audioN.open(format=audioN.get_format_from_width(prof), channels=channels, rate=rate, output=True)
            datos = rf.readframes(1024)
            while datos != '':
                streamN.write(datos)
                datos = rf.readframes(1024)
            rf.close()
            streamN.stop_stream()
            streamN.close()
            audioN.terminate()

