from lxml import etree
from collections import defaultdict


class CoraStructure():
	def __init__(self, publication_id, author, title, venue):
		self.publication_id = publication_id
		self.author = author
		self.title = title
		self.venue = venue

class ParseXML():
	def __init__(self):
		self.parse()

	def parse(self):
		tree = etree.parse('cora-all-id.xml')
		root = tree.getroot()

		self.Cora = []
		self.publication_id = ''
		self.author = {}
		self.title = []
		self.venue = {}
		i=0
		for child in root:
			self.publication_id = child.get("id")
			for subchild in child:
				if subchild.tag=="author":
					self.author[subchild.get("id")] = subchild.text
				if subchild.tag=="title":
					self.title.append(subchild.text)
				for subsubchild in subchild:
					print(subsubchild.get("id"))
					self.venue[subsubchild.get("id")]={}
					for subsubsubchild in subsubchild:
						self.venue[subsubchild.get("id")]['pubid'] = subsubchild.get("pubid")
						self.venue[subsubchild.get("id")][subsubsubchild.tag] = subsubsubchild.text
			cora = CoraStructure(self.publication_id, self.author, self.title, self.venue)
			self.Cora.append(cora)
			self.publication_id = ''
			self.author = {}
			self.title = []
			self.venue = {}
		for item in self.Cora:
			print(item.publication_id)
			print(item.author)
			print(item.title)
			print(item.venue)

if __name__ == "__main__":
	ParseXML()