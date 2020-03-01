def ListarPelis(doc):
    return {"titulos":doc.xpath("/movies/movie/title/text()"),"años":"/movies/movie/year/text()","genero":doc.xpath("/movies/movie/genre/text()")}

def NPeliculas_por_año(doc,fechaino,fechafin):
    return len(doc.xpath("/movies/movie[year/text()>=%i and year/text()<=%i]/year/text()"))