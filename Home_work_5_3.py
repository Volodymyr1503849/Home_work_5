import sys
from pathlib import PurePath , Path

def parse_log_line(full_text: str):
    list_of_dict = []
    for lines in full_text:
        dict_of_log = {}
        dict_of_log["date"] = lines.split()[0]
        dict_of_log["time"] = lines.split()[1]
        dict_of_log["info"] = lines.split()[2]
        dict_of_log["message"] = " ".join(lines.split()[3:] )
        list_of_dict.append(dict_of_log)
    return count_logs_by_level(list_of_dict)
    
def load_logs(file_path: str):
    with open (file_path,"r") as ph:
        full_text = ph.readlines()
        return parse_log_line(full_text)
    
def count_logs_by_level(list_of_dict: list):
    count_of_info = {}
    for dict in list_of_dict:
        num = count_of_info.get(dict["info"])
        if num:
            count_of_info[dict["info"]] = num + 1
        else:
            count_of_info[dict["info"]] = 1
    return display_log_counts(count_of_info)

def display_log_counts(counts: dict):
    header = "|{:^15}|{:^15}|".format("Рівень логування","Кількість")
    separator = "-" * len(header)
    body = " "
    for keys,values in counts.items():
        body += "|{:^15}|{:^15}|\n".format(keys,values)
    table = "\n".join([separator,header,separator,body])
    return table

def main():
        try:
            file = Path(sys.argv[1])
            return load_logs(file)
        except UnicodeDecodeError:
            return f"Put correct file" 
if __name__ == "__main__":
   print( main())