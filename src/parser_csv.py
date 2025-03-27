import csv

class ParserStudents:
    def __init__(self, path):
        self.data = []
        self.parse_csv(path)

    def parse_csv(self, path: str) -> None:
        if not path:
            raise ValueError("Path cannot be empty")
        try:
            with open(path, "r", newline="") as file:
              
                reader = csv.DictReader(file)
                if not self.check_csv_header(reader.fieldnames):
                    raise ValueError("Invalid CSV header")
                
                self.data = [dict(row) for row in reader if self.check_row(row)]
        except IOError as e:
            raise IOError(f"Error reading {path}: {e}") from e
        
    def check_csv_header(self, header):

        excepted_header = [
            "gender",
            "race/ethnicity",
            "parental level of education",
            "lunch",
            "test preparation course",
            'math score',
            'reading score',
            'writing score'
            ]
        return header == excepted_header  
    
    def check_row(self, row: dict) -> bool:
        valid_types = {
        "gender": lambda x: isinstance(x, str) and x in ("male", "female"),
        "race/ethnicity": lambda x: isinstance(x, str) and x.startswith("group "),
        "parental level of education": lambda x: isinstance(x, str) and len(x) <= 50,
        "lunch": lambda x: isinstance(x, str) and x in ("standard", "free/reduced"),
        "test preparation course": lambda x: isinstance(x, str) and x in ("none", "completed"),
        "math score": lambda x: x.isdigit() and 0 <= int(x) <= 100,
        "reading score": lambda x: x.isdigit() and 0 <= int(x) <= 100,
        "writing score": lambda x: x.isdigit() and 0 <= int(x) <= 100,
        }
        for key, value_type in valid_types.items():
            value = row[key]

            if not value_type(value):
                raise ValueError(f"{value} doesn't match the criteria for {key}\nLine: {row}")
        return True
    