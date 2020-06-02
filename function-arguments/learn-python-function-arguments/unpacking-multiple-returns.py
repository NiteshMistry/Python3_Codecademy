def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("Nitesh")
print(the_scream) # prints NITESH
print(the_whisper) # prints nitesh
