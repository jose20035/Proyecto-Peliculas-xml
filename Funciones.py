def ListarPelis(doc):
    return {"titulos":doc.xpath("/movies/movie/title/text()"),"años":"/movies/movie/year/text()","genero":doc.xpath("/movies/movie/genre/text()")}

def NPeliculas_por_año(doc,fechaini,fechafin):
    return len(doc.xpath("/movies/movie[year/text()>='%i' and year/text()<='%i']/year/text()" % (int(fechaini),int(fechafin))))

def ListarPelis_por_pais(doc,pais):
    return doc.xpath("/movies/movie[country/text() = '%s']" % pais)

