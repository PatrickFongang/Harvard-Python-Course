def main():
    file=input("File name: ").strip().lower()
    print(mime(ex(file)))

def ex(file):
    index=file.rfind(".")
    return file[index:]

def mime(extension):
    match extension:
        case ".gif":
            return "image/gif"
        case ".jpg"|".jpeg":
            return "image/jpeg"
        case ".png":
            return "image/png"
        case ".pdf":
            return "application/pdf"
        case ".txt":
            return "text/plain"
        case ".zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()
