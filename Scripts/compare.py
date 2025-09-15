def map_files_to_links(list_a: str, list_b: str) -> str:
    """
    Chèn link từ list_b vào vị trí file trong list_a.
    :param list_a: chuỗi nội dung danh sách A (chưa link)
    :param list_b: chuỗi nội dung danh sách B (đã link)
    :return: chuỗi mới đã được chèn link
    """
    # Tạo dict từ list_b: {filename: full_link}
    mapping = {}
    for line in list_b.splitlines():
        if ".md" in line:
            # Lấy tên file .md trong dấu ()
            start = line.find("(") + 1
            end = line.find(")")
            filepath = line[start:end]
            filename = filepath.split("/")[-1]
            mapping[filename] = line  # lưu nguyên dòng link
    
    # Xử lý list_a
    output_lines = []
    for line in list_a.splitlines():
        if ".md" in line:
            filename = line.strip()
            if filename in mapping:
                # thay bằng link đúng từ list_b
                output_lines.append(mapping[filename])
            else:
                # nếu ko tìm thấy thì giữ nguyên
                output_lines.append(line)
        else:
            # giữ nguyên dòng không chứa file
            output_lines.append(line)
    
    return "\n".join(output_lines)


# ----------------- Demo -----------------
list_a = """Prime & Divisibility:

1175_Prime_Arrangements.md
2198_Number_of_Single_Divisor_Triplets.md
263_Ugly_Number.md
"""

list_b = """- [Prime Arrangements](../Problems/1-Math/Medium/1175_Prime_Arrangements.md)
- [Number of Single Divisor Triplets](../Problems/1-Math/Medium/2198_Number_of_Single_Divisor_Triplets.md)
- [Ugly Number](../Problems/1-Math/Easy/263_Ugly_Number.md)
"""

print(map_files_to_links(list_a, list_b))
