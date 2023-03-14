from xml.etree import ElementTree as ET


def get_movie_description():
    tree = ET.parse("movies.xml")
    root = tree.getroot()

    for movie in root.iter("movie"):
        if movie.attrib['title'] == "Ferris Bueller's Day Off":
            description = movie.find("description").text
            return description


movie = get_movie_description()
print(movie)
