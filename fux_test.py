from fux import Voice

voice = Voice()

voice.note(0, 4, 'C', 1)
voice.note(1, 4, 'C', 1)
voice.note(2, 4, 'G')
voice.note(3, 4, 'G')

print(voice.display_all())

voice.type_notes()