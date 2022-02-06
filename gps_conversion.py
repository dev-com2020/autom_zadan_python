import re


def tuple_to_decimal(gps_tuple):
    '''
    Definicja krotki:
    stopnie, minuty, sekundy

    Dla każdego elementu podawane są wartość i skala. 
    Na przykład sekundy mogą być zapisane tak:

    (3456, 1000)

    To oznacza, że wartość należy podzielić przez skalę.
    '''
    degrees_info, minutes_info, seconds_info = gps_tuple

    degrees = degrees_info[0] / degrees_info[1]
    minutes = minutes_info[0] / minutes_info[1]
    seconds = seconds_info[0] / seconds_info[1]

    return degrees + minutes / 60 + seconds / 3600


def ddm_to_decimal(gps_ddm):
    '''
    W formacie DDM używany jest łańcuch znaków, który obejmuje
    referencję i rozdzielone przecinkiem stopnie oraz minuty.
    Minuty sa definiowane z częścią dziesiętną, na przykład tak:
    
    DD,MMM.MMMMR

    R to referencja.

    Sekundy są pomijane, ponieważ minuty podaje się z 
    częścią dziesiętną.
    '''
    match = re.match(r'(\d+),([\d.]+)(N|S|E|W)', gps_ddm)
    degrees, dminutes, ref = match.groups()

    decimal = float(degrees) + float(dminutes) / 60
    return f'{ref}{decimal}'


def exif_to_decimal(exif_info):
    latitude = tuple_to_decimal(exif_info['GPSLatitude'])
    latref = exif_info['GPSLatitudeRef']
    longitude = tuple_to_decimal(exif_info['GPSLongitude'])
    longref = exif_info['GPSLongitudeRef']

    return f'{latref}{latitude}', f'{longref}{longitude}'


def rdf_to_decimal(rdf_info):
    latitude = ddm_to_decimal(rdf_info['exif:GPSLatitude'])
    longitude = ddm_to_decimal(rdf_info['exif:GPSLongitude'])

    return latitude, longitude
