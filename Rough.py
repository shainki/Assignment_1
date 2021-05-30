from flask import Flask, request, render_template, abort
import chardet

app = Flask(__name__, template_folder='templates')

@app.route("/", defaults={"optional_parameter": "file1.txt"})
@app.route("/<optional_parameter>")
def route(optional_parameter="file1.txt"):
    start_line = request.args.get('start_line')
    end_line = request.args.get('end_line')

    if optional_parameter not in ["file1.txt","file2.txt","file3.txt","file4.txt"]:
        return abort(404, "Resource not found!")
    else:
        with open(optional_parameter, 'rb') as opened_file:
            bytes_file = opened_file.read()
            chardet_data = chardet.detect(bytes_file)
            file_encoding = (chardet_data['encoding'])

        with open(optional_parameter,"r",encoding=file_encoding) as f:
            file_content = f.readlines()

        if start_line and end_line and start_line <= end_line:
            file_content=file_content[int(start_line):int(end_line)]

        return render_template("index.html", file_content=file_content )


if __name__ == "__main__":
    app.run()