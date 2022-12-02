# fux
 A counterpoint helper and generator.

 # Todo
 - [x] implement a stave
 - [x] implement rythm
 - [x] implement voices
   - [x] this includes notation for pitches
 - [ ] implement a way by which you can find distance between voices
 - [ ] check for direction of motion
 - [ ] check for leaps and steps
 - [ ] find a way to encode counterpoint rules
 - [ ] implement recommendations for voices once there is a cantus firmus
   - [ ] 1st species
   - [ ] 2nd species
   - [ ] 3rd species
   - [ ] 4th species
   - [ ] 5th species
 - [ ] midi / sheet music support
 - [ ] GUI
 - [ ] web interface

# Brain dump
* we have the object 'note'
* the 'note' objects are organised into a 'voice', which has a timeline and notes inserted into it
  * current problem I see is that time values are too short and that is not ideal
  * also it is a bit clumsy (the way I implemented time is not ideal)
* the 'voice' objects are organised into a Stave, but this should really be a Composition
* lets start from the beginning!