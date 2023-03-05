import pynecone as pc

class ToDo(pc.Model, table=True):
	title: str
	done: bool