import  wave
import struct
import pyaudio


class Play:


        def __init__(self, arreglo):
            self.Array = arreglo


        def generar(self):

            output = wave.open("Nombre.wav", 'w')
            Set_Bits = 16/8
            output.setparams((1, Set_Bits, 44100, 0, 'NONE', 'not compressed'))
            values = []
            for i in range(0, len(self.Array)):
                    packed_value = struct.pack('<h', self.Array[i])
                    values.append(packed_value)
            value_str = ''.join(values)
            output.writeframes(value_str)
            output.close()
            rf = wave.open("Nombre.wav", 'rb')
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

        #def graficar(self,array):
                #plt.plot(array, color="red", linewidth=1.0, linestyle="-")
                #plt.show()