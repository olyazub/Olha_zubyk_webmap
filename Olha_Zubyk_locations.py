
def read_file(path):
    """
    (str) -> (list)
    Reads a file and returns a list of lines needed
    :param path: file name/ path to file
    """
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lst = f.readlines()[14:]
        return lst

def films_year(film_list, year):
    """
    (list, int) -> (list)
    Finds films of a given year and
    writes their name and shooting location into a list of lists
    """
    year1 = "({})".format(str(year))
    lst = []
    for el in film_list:
        if year1 in el:
            f = el.split("\t")
            film = [x for x in f if x]
            film[0] = film[0].split(year1)[0]
            if film[-1].startswith("("):
                film.remove(film[-1])
            film[-1] = film[-1].strip("\n")
            if "'" in film[0]:
                film[0] = film[0].replace("'", '*')
            lst.append(film)
    return lst


def find_location(adress):
    """
    (str) -> (tuple)
    :return: latitude and longitude of a location
    """
    from geopy.geocoders import ArcGIS
    try:
        geolocator = ArcGIS(timeout=20)
        location = geolocator.geocode(adress)
        coord = (location.latitude, location.longitude)
    except:
        coord = find_location(adress)
    return coord



