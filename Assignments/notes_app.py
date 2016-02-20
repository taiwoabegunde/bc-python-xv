class NotesApplication(object):

	def __init__(self, author):
		self.author = author
		self.notes_list = [ ]

	def create(self, note_content):
		self.notes_list.append(note_content)
		return self

	def list(self):
		list_notes = ""
		for i in range(len(self.notes_list)):
			content = "Note ID: %s /n %s n/ By Author %s /n" % (i, self.notes_list[i], self.author)
			list_notes +=content
		return  list_notes
	
	def get(self, note_id):
		return self.notes_list[note_id]
	
	def search(self, search_text):
		list_notes = "Showing result for search [%s]" % search_text
		for i in range(len(self.notes_list)):
			if self.notes_list[i].find(search_text) > -1:
				content = "Note ID: %s /n %s n/ By Author %s /n" % (i, self.notes_list[i], self.author)
				notes_list += content
		return list_notes
	
	def delete(self, note_id):
		for i in range(len(self.notes_list)):
			if i == note_id :
				del self.notes_list[note_id]
	def edit(self, note_id, new_content):
		for i in range(len(self.notes_list)):
			if i == note_id :
				if new_content == "":
					return "New content can not be empty"
					edit()
				else:
					self.notes_list[note_id] = new_content"""


testing = NotesApplication('James')
print (testing.create('Is a great to be in Andela!'))
