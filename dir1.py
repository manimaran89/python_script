# -*- coding: utf-8 -*-
class Path:
    def __init__(self, path):
	self.current_path = path

    def cd(self, new_path):
	abc = new_path.split("/")
	final_path = self.current_path.split("/")
	if self.current_path.startswith("/"):
	    self.current_path = "/"
	else:
	    self.current_path = ""
	for i in abc:
	    if i == "..":
		final_path.pop()
		self.current_path = "/".join(final_path)
            else:
		final_path.append(i)
		self.current_path = "/".join(final_path)
        return self.current_path
