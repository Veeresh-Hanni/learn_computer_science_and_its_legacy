
from Advance_Exception import check_age


try:
    pass
except:
    pass


def open_file(file_name):
    try:
        file = open(file_name, "r")
    except Exception as e:
        print("Error Occured:", e)
    finally:
        try:
            file.close()
        except Exception as e:
            pass

def read_and_print(file_path):
    # file_handles = None
    try:
        with open(file_path) as file_handles:
            content = file_handles.read()
            # print(content)
    except FileNotFoundError as f:
        print(f"File {file_path} deosn't exists. ")
    except PermissionError as p:
        print("Permission denied")
    finally:
        print("Clean up")
        try:
            # if file_handles is not None:
            file_handles.close()
        except:
            pass
# open_file("file-ede.txt")
read_and_print("file-ede.txt")

def check_voting():
    try:
        check_age(16)
    except Exception as e:
        print("Error: ", e)

check_voting()