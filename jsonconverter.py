import csv,json
import codecs
from collections import OrderedDict


class Foo(object):
    def __init__(self):
        self.x = 1
        self.y = 2



fields=("ID","Adikaram","Agapporul","Athigaram","Thurai","Thuraivilakkam","Kolu","Thelivurai","Moolam1","Moolam2","Moolam3","Moolam4","Patham1","Patham2","Patham3","Patham4")

f = codecs.open('utils\input.csv', encoding='utf-8')
first_line = f.readline()

#f=open("utils\input.csv","r")
reader = csv.DictReader( f, fieldnames = fields)
data_list = list()
kovairecord=[]
for row in reader:
    #data_list.append(entry)
    record={
        "Id":row["ID"],
        "Ilakkiyam": {
					"அகப்பொருள்": row["Agapporul"],
					"அதிகாரம்": row["Athigaram"],
					"துறை": row["Thurai"],
					"துறை விளக்கம்": row["Thuraivilakkam"]
				},  
            "padal": {
					"மூலம்": [
					row["Moolam1"],
			    	row["Moolam2"],
                    row["Moolam3"],
                    row["Moolam4"]
					],
					"பதம் பிரித்து": [
						row["Patham1"],
			    	row["Patham2"],
                    row["Patham3"],
                    row["Patham4"]
					]
				},
                "Porul": {
					"சேர்க்கப்படவேண்டியுள்ளது": "சேர்க்கப்படவேண்டியுள்ளது"
				},
				"Info": {
					"விளக்கம்": row["Thelivurai"],
					"கொளு": row["Kolu"],                    
					"ஒப்புமை": "சேர்க்கப்படவேண்டியுள்ளது"
				}
    }
    kovairecord.append(record)

with codecs.open('file.json', 'w', encoding='utf8') as json_file:
    # unicode(data) auto-decodes data to unicode if str
        json_file.write(json.dumps(kovairecord, ensure_ascii=False))

