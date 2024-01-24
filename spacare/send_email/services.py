import os
from datetime import datetime

from pyhtml2pdf import converter


def create_pdf(name, phone_number, lich_hen, products, tong_tien):
    html_template_path = os.path.abspath("pdf.html")

    # Đọc nội dung từ file HTML mẫu
    with open(html_template_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Thay thế các biến trong HTML
    html_content = html_content.replace("{{name}}", name)
    html_content = html_content.replace("{{lich_hen}}", lich_hen)
    html_content = html_content.replace("{{phone_number}}", phone_number)
    html_content = html_content.replace("{{tong_tien}}", tong_tien)

    # Chuyển danh sách sản phẩm thành chuỗi HTML
    products_html = ""
    for product in products:
        products_html += (
            f"<tr><td>{product['stt']}</td><td>{product['dich_vu']}</td>"
            f"<td>{product['trang_thai']}</td><td>{product['ghi_chu']}</td></tr>"
        )

    # Thay thế placeholder cho danh sách sản phẩm
    html_content = html_content.replace("{{products}}", products_html)

    # Tạo một tệp HTML tạm thời với các giá trị được thay thế
    temp_html_path = "temp.html"
    with open(temp_html_path, "w", encoding="utf-8") as temp_file:
        temp_file.write(html_content)

    # Chuyển đổi tệp HTML tạm thời thành PDF
    pdf_filename = "sample.pdf"
    converter.convert(
        f"file:///{os.path.abspath(temp_html_path)}", pdf_filename  # noqa: E231
    )

    # Xóa tệp HTML tạm thời sau khi chuyển đổi
    os.remove(temp_html_path)  # noqa

    return pdf_filename


def convert_datetime(input_string):
    try:
        # Chuyển đổi thành đối tượng datetime
        datetime_object = datetime.strptime(input_string, "%Y-%m-%dT%H:%M:%SZ")

        # Định dạng lại theo yêu cầu
        output_string = datetime_object.strftime("%H:%M %d-%m-%Y")

        return output_string
    except ValueError:
        return "Invalid datetime format"


def format_number(number):
    formatted_number = "{:,}".format(number)
    return formatted_number
