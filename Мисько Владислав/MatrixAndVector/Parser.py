def ParseRow(thelist):
        array = []
        thelist = thelist.strip()
        array = thelist.split(' ')
        array = list(filter((' ').__ne__, array))
        array = list(filter(('').__ne__, array))
        return array
