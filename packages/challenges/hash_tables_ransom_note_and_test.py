import datetime

def checkMagazine_dict(magazine, note):
    mag_dict = {}
    for w in magazine:
        mag_dict[w] = mag_dict.get(w, 0) + 1
    note_dict = {}
    for w in note:
        note_dict[w] = note_dict.get(w, 0) + 1
    
    ret = "Yes"
    for w in note_dict:
        if w in mag_dict:
            if note_dict[w] > mag_dict[w]:
                ret = "No"
                break
        else:
            ret = "No"
            break
    return ret


def checkMagazine_list(magazine, note):
    yes = True
    for note_word in note:
        if note_word in magazine:
            i = magazine.index(note_word)
            magazine.pop(i)
        else:
            yes = False
            ret = "No"
            break
    if yes:
        ret = "Yes"
    return ret


m = "o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x o l x imjaw bee khmla v o v o imjaw l khmla imjaw x"
n = "imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o"

 
magazine = m.split()
note = n.split()

def test_checkMagazine():
    start = datetime.datetime.now()
    result_dict = checkMagazine_dict(magazine, note)
    end = datetime.datetime.now()
    time_diff = end-start
    execution_time_dict = time_diff.total_seconds() * 1000

    start = datetime.datetime.now()
    result_list = checkMagazine_list(magazine, note)
    end = datetime.datetime.now()
    time_diff = end-start
    execution_time_list = time_diff.total_seconds() * 1000

    assert execution_time_dict < execution_time_list
    assert result_dict =="No"
    assert result_list == "No"
    
