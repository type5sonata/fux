


class Note:
    
    def __init__(self, octave=4, pitch='C', length=0.25) -> None:
        
        #class attribute
        pitch_names = {
                'C' : 1,
                
                'C#' : 2,
                'Db' : 2,
                
                'D' : 3,
                
                'D#' : 4,
                'Eb' : 4,
                
                'E' : 5,
                'Fb' : 5,
                
                'F' : 6,
                
                'F#' : 7,
                'Gb' : 7,
                
                'G' : 8,
                
                'G#' : 9,
                'Ab' : 9,
                
                'A' : 10,
                
                'A#' : 11,
                'Bb' : 11,
                
                'B' : 12,
                'H' : 12,
                'Cb' : 12
                }
        
        # note attributes
        self.octave = octave
        self.pitch = pitch
        self.pitch_numeric = self.pitch_names(self.pitch)
        self.length = length
    
    def display(self):
        return self.name

class Voice:
    
    def __init__(self, name, cantus_firmus=False, notes=[]) -> None:
        self.name = name
        self.cantus_firnmus = cantus_firmus
        self.notes = notes
    
    def display(self):
        for note in self.notes:
            print(note.display(), '')
            
class Composition:
    
    def __init__(self, name, time='4/4', voices=[], length=8):
        self.name = name
        self.voices = voices
        self.time = time
        self.length = 8
    
    def 
    