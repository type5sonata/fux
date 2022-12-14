'''
Welcome to Fux!

Named after Joseph Johann Fux, Fux provides an API and later hopefully other functions for writing traditional species counterpoint
as laid out in the seminal work Gradus ad Parnassum.
'''

#just a dictionary for pitch classes for translation
pitch_classes = {
    0 : 'C',
    1 : 'C#',
    2 : 'D',
    3 : 'Eb',
    4 : 'E',
    5 : 'F',
    6 : 'F#',
    7 : 'G',
    8 : 'G#',
    9 : 'A',
    10 : 'Bb',
    11 : 'B'
}

#define note class, defined by octave, pitch class, duration
class Note:
    def __init__(self, octave=4, pitch_class=0, length=1):
        
        assert octave in range(0, 9), 'Octaves are numbered 0-8'
        assert pitch_class in range(0, 12), 'There are 12 pitch classes in traditional counterpoint, numbered 0-11.'
        
        self.octave = octave
        self.pitch_class = pitch_class
        self.letter = pitch_classes[self.pitch_class]
        self.length = length
        pass
    
    #displays pitch class and octave in standard notation
    def display(self):
        return f'{self.letter}{self.octave}'

#we define a Slur class, which will sit in place of a note
#allowing it to carry over to the next time unit
class Slur:
    def __init__(self, follows: Note):
        self.previous_note = follows
        self.octave = follows.octave
        self.pitch_class = follows.pitch_class
        self.length = 1 #it is always one, it fills one space
        pass
    
    def display(self):
        return f'({self.previous_note.display()})'
        
#define Voice as a class, it has a length (in time units)
#by default it fills up each time unit with a note

class Voice:
    def __init__(self, length=8):
        self.length = length
        self.notes = []
        for note in range(self.length):
            self.notes.append(Note(0,0))
        pass
    
    #displays the entire voice for all times
    def display_all(self):
        display_version = []
        for note in self.notes:
            display_version.append(note.display())
        return display_version
    
    def display(self, time):
        return self.notes[time].display()
    
    def set_single_note(self, time: int, octave, pitch, length=1):
        if length != 1:
            # self.notes[time] = Note(octave, pitch)
            for i in range(length):
                self.notes[time+i] = Slur(self.notes[time])
        self.notes[time] = Note(octave, pitch, length)
        
    def set_notes(self, source):
        #one input type should be a list of touples
        if type(source) == list:
            #todo! slurs
            for time, note in enumerate(source):
                self.notes[time] = Note(note[0], note[1])
        print (f'Notes successfully set from {source}!')

#finally, define a Stave, which will include Voices
#for now, Voices will all start at 0     
class Stave:
    def __init__(self, length=8):
        self.length = length
        self.voices = {}
        self.number_of_voices = 0
        self.cantus_firmus = None
        
        pass
    
    #add a voice
    def add_voice(self, name=None):
        if not name:
            name = f'Voice {self.number_of_voices}'
        
        self.voices[name] = (Voice(self.length))
        
        print(f'Voice {name} added!')
        self.number_of_voices += 1
        pass
    
    #set cantus firmus to one of the existing voices
    def set_cantus_firmus(self, voice: str):
        assert voice in self.voices
        self.cantus_firmus = self.voices[voice]
        print(f'Cantus firmus set to {voice}.')
    
    def display(self):
        for moment in range(self.length):
            print(f'Time {moment}')
            for voice in self.voices:
                if self.voices[voice] != self.cantus_firmus:
                    print(f'\t{voice}: {self.voices[voice].display(moment)}')
                else:
                    print(f'*\t{voice}: {self.voices[voice].display(moment)}')
        pass