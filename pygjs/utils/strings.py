from browser import window

gamejs = window.gamejs

def get_common_prefix(str1, str2):
    return gamejs.utils.strings.getCommonPrefix(str1, str2)
