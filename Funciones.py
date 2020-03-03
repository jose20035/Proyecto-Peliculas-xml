def ListarPelis(doc):
    respuesta=[]
    for titulo in doc.xpath("//title/text()"):
        respuesta.append({"titulo":titulo,"año":doc.xpath("//movie[title = '%s']/year/text()" % titulo),"genero":doc.xpath("//movie[title = '%s']/genre/text()" % titulo)}) 
    return respuesta

def NPeliculas_por_año(doc,fechaini,fechafin):
    return len(doc.xpath("/movies/movie[year/text()>='%i' and year/text()<='%i']/year/text()" % (int(fechaini),int(fechafin))))

def ListarPelis_por_pais(doc,pais):
    return doc.xpath("/movies/movie[country/text() = '%s']/title/text()" % pais)

def ListarPeliculasyActores_por_Director(doc,director):
    resultado=[]
    peliculas=doc.xpath("/movies/movie[director/first_name = '%s']/title/text()" % director)
    for pelicula in peliculas:
        resultado.append({"titulo":peliculas,"actores":doc.xpath("/movies/movie[title/text() = '%s']/actor/first_name/text()" % pelicula)})
    return resultado

def ListarDirecetoresyPeliculasEntreDosAños(doc,fechaini,fechafin):
    resultado=[]
    directores=doc.xpath("/movies/movie/director[birth_date/text()>='%i' AND birth_date/text()<='%i']/first_name/text()" % (int(fechaini),int(fechafin)))
    for director in directores:
        resultado.append({"directores":director,"pelis":doc.xpath("//movie[director/first_name/text() = '%s']/title/text()" % director)})
    return resultado
