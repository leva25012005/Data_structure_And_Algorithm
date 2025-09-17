import os
import json
from datetime import datetime
from problems_generator import generate_problems_files
from docs_generator import generate_docs_file
from gfg_problems_generator import generate_gfg_problems_files
from gfg_docs_generator import generate_gfg_docs_file
import sys

def detect_platform(data):
    """Detect if data is from LeetCode or GeeksforGeeks"""
    if isinstance(data, list) and len(data) > 0:
        sample = data[0]
        if 'questionFrontendId' in sample and 'titleSlug' in sample:
            return 'LC'
        elif 'problem_name' in sample and 'slug' in sample and 'id' in sample:
            return 'GFG'
    return 'UNKNOWN'

def main():
    # Đường dẫn file JSON
    if len(sys.argv) < 2:
        print("❌ Please provide the path to JSON file!")
        return
    
    json_file = sys.argv[1]
    
    # Đọc dữ liệu JSON
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Tên file gốc và platform
    base_filename = os.path.splitext(os.path.basename(json_file))[0]
    platform = detect_platform(data)
    
    if platform == 'UNKNOWN':
        print("❌ Cannot detect platform! Please check your JSON format.")
        return
    
    print(f"🔍 Detected platform: {'LeetCode' if platform == 'LC' else 'GeeksforGeeks'}")
    
    # Xử lý tên folder
    # Ví dụ: 1-Math_LC.json -> base_name = "1-Math", suffix = "LC"
    if '_' in base_filename:
        base_name, suffix = base_filename.rsplit('_', 1)
        if suffix not in ['LC', 'GFG']:
            # Nếu không có suffix hợp lệ, dùng detection
            base_name = base_filename
            suffix = platform
    else:
        base_name = base_filename  
        suffix = platform
    
    # Tạo Solutions folder: Problems/1-Math/LC hoặc Problems/1-Math/GFG
    problems_base_folder = os.path.join(r"E:\Github\Data_structure_And_Algorithm\Problems", base_name)
    solutions_folder = os.path.join(problems_base_folder, suffix)
    os.makedirs(solutions_folder, exist_ok=True)
    
    # Tạo file Docs với suffix: 1-Math_LC.md hoặc 1-Math_GFG.md
    docs_folder = r"E:\Github\Data_structure_And_Algorithm\Docs"
    os.makedirs(docs_folder, exist_ok=True)
    docs_file = os.path.join(docs_folder, f"{base_name}_{suffix}.md")
    
    print("🚀 Starting file generation...")
    
    # Tạo các file solution và documentation theo platform
    if platform == 'LC':
        print("📝 Generating LeetCode solution files...")
        generate_problems_files(data, solutions_folder, base_name)
        
        print("📚 Generating LeetCode documentation file...")
        generate_docs_file(data, docs_file, f"{base_name}_{suffix}", json_file)
        
    elif platform == 'GFG':
        print("📝 Generating GeeksforGeeks solution files...")
        generate_gfg_problems_files(data, solutions_folder, base_name)
        
        print("📚 Generating GeeksforGeeks documentation file...")
        generate_gfg_docs_file(data, docs_file, f"{base_name}_{suffix}", json_file)
    
    print(f"✅ Successfully generated {len(data)} problem files!")
    print(f"📄 Documentation file: {docs_file}")
    print(f"📁 Solutions folder: {solutions_folder}")
    print(f"🎯 Total problems processed: {len(data)}")
    print(f"🏢 Platform: {'LeetCode' if platform == 'LC' else 'GeeksforGeeks'}")
    
    # Thống kê difficulty
    print(f"📊 Difficulty breakdown:")
    difficulty_count = {}
    
    if platform == 'LC':
        for item in data:
            diff = item['difficulty']
            difficulty_count[diff] = difficulty_count.get(diff, 0) + 1
        
        for diff in ['Easy', 'Medium', 'Hard']:
            if diff in difficulty_count:
                colors = {'Easy': '🟢', 'Medium': '🟡', 'Hard': '🔴'}
                print(f"   {colors[diff]} **{diff}**: {difficulty_count[diff]} problems")
                
    elif platform == 'GFG':
        for item in data:
            diff = item['difficulty']
            difficulty_count[diff] = difficulty_count.get(diff, 0) + 1
        
        for diff in ['Basic', 'Easy', 'Medium', 'Hard']:
            if diff in difficulty_count:
                colors = {'Basic': '⚪', 'Easy': '🟢', 'Medium': '🟡', 'Hard': '🔴'}
                print(f"   {colors.get(diff, '⚪')} **{diff}**: {difficulty_count[diff]} problems")
    
    print("\n🚀 Ready to start your coding journey!")

if __name__ == "__main__":
    main()