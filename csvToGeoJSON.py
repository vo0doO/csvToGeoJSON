import csv

# Чтение необработанных данных из csv
rawData = csv.reader(open('sample.csv', 'rb'), dialect='excel')

# шаблон. где данные из csv будут отформатированы к geojson
template = \
    ''' \
    { "type" : "Feature",
        "id" : %s,
            "geometry" : {
                "type" : "Point",
                "coordinates" : ["%s","%s"]},
        "properties" : { "name" : "%s", "value" : "%s"}
        },
    '''

# голова geojson файла
output = \
    ''' \
{ "type" : "Feature Collection",
    {"features" : [
    '''

# цикл через csv строкой, пропускающий первое
iter = 0
for row in rawData:
    iter += 1
    if iter >= 2:
        id = row[0]
        lat = row[1]
        lon = row[2]
        name = row[3]
        pop = row[4]
        output += template % (row[0], row[1], row[2], row[3], row[4])

# хвост geojson файла
output += \
    ''' \
    ]
}
    '''

# открывает файл geoJSON, чтобы записать вывод в файл output.geojson
outFileHandle = open("output.geojson", "w")
outFileHandle.write(output)
outFileHandle.close()
