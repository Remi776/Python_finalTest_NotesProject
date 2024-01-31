import Python_finalTest_NotesProject.models.Note


def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Python_finalTest_NotesProject.models.Note.Note.to_string(notes))
        file.write('\n')
    file.close