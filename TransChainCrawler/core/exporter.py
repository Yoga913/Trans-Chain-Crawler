"secara keseluruhan # program ini digunakan untuk mengekspor data graf dalam dua format yang berbeda: GraphML dan JSON."

import json

def exporter(filename, jsoned):
    # Memeriksa apakah ekstensi berkas adalah '.graphml'
	if filename.endswith('.graphml'):
		graphml = '''<?xml version="1.0" encoding="UTF-8"?><graphml xmlns="http://graphml.graphdrawing.org/xmlns">
<key attr.name="label" attr.type="string" for="node" id="label"/>
<key attr.name="weight" attr.type="double" for="edge" id="weight"/>
<key attr.name="size" attr.type="float" for="node" id="size"/>
<graph edgedefault="undirected">
		'''
        # Menambahkan node ke dalam format GraphML
		num = 0
		for node in jsoned['nodes']:
			graphml += '<node id="%i">\n<data key="label">%s</data>\n<data key="size">%s</data>\n</node>' % (num, node['label'], float(node['size']))
			num += 1
        # Menambahkan edge ke dalam format GraphML
		num = 0
		for edge in jsoned['edges']:
			graphml += '<edge id="%i" source="%s" target="%s">\n<data key="weight">%s</data>\n</edge>\n' % (num, edge['source'].lstrip('id='), edge['target'].lstrip('id='), float(edge['size']))
			num += 1
        # Menutup tag GraphML
		graphml += '</graph>\n</graphml>'
		return graphml
	else:
        # Jika bukan ekstensi '.graphml', mengembalikan JSON dalam format string
		return json.dumps(jsoned, indent=4)


