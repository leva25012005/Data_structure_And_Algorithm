import os
import json
from datetime import datetime
from problems_generator import generate_problems_files
from docs_generator import generate_docs_file
import sys

def main():
    # Đường dẫn file JSON
    if len(sys.argv) < 2:
        print("❌ Please provide the path to JSON file!")
        return
    json_file = sys.argv[1]
    
    # Đọc dữ liệu JSON (danh sách các bài toán)
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Tên folder từ tên file json
    base_name = os.path.splitext(os.path.basename(json_file))[0]
    
    # Tạo Solutions folder
    solutions_folder = os.path.join(r"E:\Github\Data_structure_And_Algorithm\Problems", base_name)
    os.makedirs(solutions_folder, exist_ok=True)
    
    # Tạo file Docs .md
    docs_folder = r"E:\Github\Data_structure_And_Algorithm\Docs"
    os.makedirs(docs_folder, exist_ok=True)
    docs_file = os.path.join(docs_folder, f"{base_name}.md")
    
    print("🚀 Starting file generation...")
    
    # Tạo các file solution
    print("📝 Generating solution files...")
    generate_problems_files(data, solutions_folder, base_name)
    
    # Tạo file documentation
    print("📚 Generating documentation file...")
    generate_docs_file(data, docs_file, base_name, json_file)
    
    print(f"✅ Successfully generated {len(data)} problem files!")
    print(f"📄 Documentation file: {docs_file}")
    print(f"📁 Solutions folder: {solutions_folder}")
    print(f"🎯 Total problems processed: {len(data)}")
    print(f"📊 Difficulty breakdown:")
    
    difficulty_count = {}
    for item in data:
        diff = item['difficulty']
        difficulty_count[diff] = difficulty_count.get(diff, 0) + 1
    
    for diff in ['Easy', 'Medium', 'Hard']:
        if diff in difficulty_count:
            colors = {'Easy': '🟢', 'Medium': '🟡', 'Hard': '🔴'}
            print(f"   {colors[diff]} **{diff}**: {difficulty_count[diff]} problems")
    
    print("\n🚀 Ready to start your coding journey!")

if __name__ == "__main__":
    main()