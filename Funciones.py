def ListarPelis(doc):
    return {"titulos":doc.xpath("/movies/movie/title/text()"),"años":"/movies/movie/year/text()","genero":doc.xpath("/movies/movie/genre/text()")}

def NPeliculas_por_año(doc,fechaini,fechafin):
    return len(doc.xpath("/movies/movie[year/text()>='%i' and year/text()<='%i']/year/text()" % (int(fechaini),int(fechafin))))

def ListarPelis_por_pais(doc,pais):
    return doc.xpath("/movies/movie[country/text() = '%s']" % pais)

def ListarPeliculasyActores_por_Director(doc,director):
    resultado=[]
    peliculas=doc.xpath("/movies/movie[director/first_name = '%s']/title/text()" % director)
    for pelicula in peliculas:
        resultado.append({"titulo":peliculas,"Actores":doc.xpath("/movies/movie[title/text() = '%s']/actor/first_name/text()" % pelicula)})
    return resultado

