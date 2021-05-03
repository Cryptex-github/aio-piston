
class PistonResponse:

    def __init__(self, data: dict):

        self.ran = data.get("ran")
        self.language = data.get("language")
        self.version  = data.get("version")
        self.stdout   = data.get("stdout")
        self.stderr   = data.get("stderr")
        self.output   = data.get("output")

    def __repr__(self):
        return f"<PistonResponse language='{self.language}' version='{self.version}' ran={self.ran}>"

    def __str__(self):
        return self.output

    def __eq__(self, o):
        if isinstance(o, PistonResponse):
            return self.output == o.output
        else:
            return self.output == o.output
    
    def __ne__(self, o):
        return not self.__eq__(o)