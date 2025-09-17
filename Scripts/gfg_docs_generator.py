import os
from datetime import datetime

def get_difficulty_badge(difficulty):
    """Tạo badge màu sắc cho độ khó"""
    colors = {
        'Basic': '⚪',
        'Easy': '🟢',
        'Medium': '🟡', 
        'Hard': '🔴'
    }
    return f"{colors.get(difficulty, '⚪')} **{difficulty}**"

def clean_filename(title):
    """Làm sạch tên file, loại bỏ ký tự không hợp lệ"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    return title.replace(' ', '_')

def generate_gfg_docs_file(data, docs_file, base_name, json_file):
    """Tạo file documentation tổng hợp cho GeeksforGeeks"""
    
    current_date = datetime.now().strftime("%d-%m-%Y")
    format_date = current_date.replace("-", "--")
    
    with open(docs_file, "w", encoding="utf-8") as f:
        f.write("<div align=\"center\">\n\n")
        f.write(f"# 📊 {base_name} - GeeksforGeeks Progress Tracker\n\n")
        f.write(f"![Problems](https://img.shields.io/badge/Total%20Problems-{len(data)}-0F9D58?style=for-the-badge&logo=geeksforgeeks)\n")
        f.write(f"![Progress](https://img.shields.io/badge/Completed-0%2F{len(data)}-critical?style=for-the-badge&logo=github)\n")
        f.write(f"![Last Updated](https://img.shields.io/badge/Last%20Updated-{format_date}-success?style=for-the-badge&logo=git)\n\n")
        f.write("</div>\n\n")
        f.write("---\n\n")
        
        # Table of Contents
        f.write("## 📑 Table of Contents\n\n")
        f.write("1. [📈 Progress Statistics](#-progress-statistics)\n")
        f.write("2. [🏷️ Top Topics by Question Frequency](#️-top-topics-by-question-frequency)\n")
        f.write("3. [🏢 Companies](#-companies)\n")
        f.write("4. [📋 Problems List](#-problems-list)\n\n")
        
        # Statistics
        difficulty_stats = {}
        for item in data:
            diff = item['difficulty']
            difficulty_stats[diff] = difficulty_stats.get(diff, 0) + 1
        
        f.write("## 📈 Progress Statistics\n\n")
        f.write("| Difficulty | Total | Solved | Remaining | Progress |\n")
        f.write("|------------|-------|--------|-----------|----------|\n")
        for diff in ['Basic', 'Easy', 'Medium', 'Hard']:
            if diff in difficulty_stats:
                count = difficulty_stats[diff]
                badge = get_difficulty_badge(diff)
                f.write(f"| {badge} | `{count}` | `0` | `{count}` | ![Progress Bar](https://progress-bar.xyz/0/?title=Progress&width=150&color=green) |\n")
        f.write("\n")
        
        # Topic frequency analysis
        f.write("## 🏷️ Top Topics by Question Frequency\n\n")
        topic_freq = {}
        for item in data:
            tags = item.get("tags", {})
            topic_tags = tags.get("topic_tags", [])
            for topic in topic_tags:
                topic_freq[topic] = topic_freq.get(topic, 0) + 1
        
        sorted_topics = sorted(topic_freq.items(), key=lambda x: x[1], reverse=True)[:15]
        
        f.write("| Rank | Topic | Questions | Percentage |\n")
        f.write("|------|-------|-----------|------------|\n")
        for i, (topic, count) in enumerate(sorted_topics, 1):
            percentage = (count / len(data)) * 100
            f.write(f"| {i} | **{topic}** | `{count}` | `{percentage:.1f}%` |\n")
        f.write("\n")
        
        # Company analysis
        f.write("## 🏢 Companies\n\n")
        company_freq = {}
        for item in data:
            tags = item.get("tags", {})
            company_tags = tags.get("company_tags", [])
            for company in company_tags:
                company_freq[company] = company_freq.get(company, 0) + 1
        
        if company_freq:
            sorted_companies = sorted(company_freq.items(), key=lambda x: x[1], reverse=True)[:10]
            
            f.write("| Rank | Company | Questions | Percentage |\n")
            f.write("|------|---------|-----------|------------|\n")
            for i, (company, count) in enumerate(sorted_companies, 1):
                percentage = (count / len(data)) * 100
                f.write(f"| {i} | **{company}** | `{count}` | `{percentage:.1f}%` |\n")
        else:
            f.write("*No company tags found in this dataset.*\n")
        f.write("\n")
        
        # Problems tracking table
        f.write("## 📋 Problems List\n\n")
        #f.write("| # | Problem | Difficulty | Accuracy | Topics | Status |\n")
        #f.write("|---|---------|------------|----------|--------|--------|\n")
        
        for i, item in enumerate(data, 1):
            problem_id = item["id"]
            problem_name = item["problem_name"]
            slug = item.get("slug", "")
            gfg_url = f"https://www.geeksforgeeks.org/problems/{slug}/"
            difficulty_badge = get_difficulty_badge(item['difficulty'])
            accuracy = item.get("accuracy", "N/A")
            
            # Create link to solution file  
            clean_name = clean_filename(problem_name)
            solution_file = f"{problem_id}_{clean_name}.md"
            # Extract base name without _GFG suffix for folder structure
            folder_base = base_name.replace('_GFG', '')
            solution_link = f"../Problems/{folder_base}/GFG/{item['difficulty']}/{solution_file}"
            
            # Get topic tags
            tags = item.get("tags", {})
            topic_tags = tags.get("topic_tags", [])
            topics_str = ", ".join(topic_tags[:3])  # Show first 3 topics
            if len(topic_tags) > 3:
                topics_str += "..."
            
            #f.write(f"| {i} | [{problem_name}]({solution_link}) | {difficulty_badge} | `{accuracy}` | {topics_str} | ⏳ |\n")
            f.write(f" - [{problem_name}]({solution_link})\n")

        f.write("\n")
        
        # Legend
        f.write("### 📝 Status Legend\n\n")
        f.write("| Symbol | Meaning |\n")
        f.write("|--------|----------|\n")
        f.write("| ⏳ | Not Started |\n")
        f.write("| 🎯 | Attempted |\n")
        f.write("| ✅ | Solved |\n")
        f.write("| 🔄 | Under Review |\n")
        f.write("| 🏆 | Mastered |\n\n")
        
        # Difficulty Distribution Chart
        f.write("## 📊 Difficulty Distribution\n\n")
        f.write("```mermaid\n")
        f.write("pie title Difficulty Distribution\n")
        for diff, count in difficulty_stats.items():
            f.write(f'    "{diff}" : {count}\n')
        f.write("```\n\n")
        
        # Footer
        f.write("---\n\n")
        f.write("<div align=\"center\">\n\n")
        f.write(f"*Generated on {format_date} from `{os.path.basename(json_file)}`*\n\n")
        f.write("**Happy Coding! 🚀 Learn from Mistakes! 📈 Keep Going! 💪**\n\n")
        f.write("</div>\n")
    
    print(f"✅ Generated GeeksforGeeks documentation file: {docs_file}")