import os
import re

def clean_filename(title):
    """Làm sạch tên file, loại bỏ ký tự không hợp lệ"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        title = title.replace(char, '')
    return title.replace(' ', '_')

def get_difficulty_badge(difficulty):
    """Tạo badge màu sắc cho độ khó"""
    colors = {
        'Basic': '⚪',
        'Easy': '🟢',
        'Medium': '🟡', 
        'Hard': '🔴'
    }
    return f"{colors.get(difficulty, '⚪')} **{difficulty}**"

def clean_html_content(html_content):
    """Làm sạch HTML tags và format lại content"""
    if not html_content:
        return ""
    
    # Remove HTML tags
    clean = re.compile('<.*?>')
    text = re.sub(clean, '', html_content)
    
    # Replace HTML entities - bao gồm cả numeric entities
    import html
    text = html.unescape(text)  # Converts &#39; -> ', &lt; -> <, etc.
    
    # Additional manual replacements for common cases
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&quot;', '"')
    
    # Clean up extra whitespace but preserve line breaks for better formatting
    text = re.sub(r'[ \t]+', ' ', text)  # Multiple spaces/tabs -> single space
    text = re.sub(r'\n\s*\n', '\n\n', text)  # Multiple newlines -> double newline
    text = text.strip()
    
    return text

def format_problem_description_html(problem_question):
    """Format problem description giữ nguyên HTML formatting"""
    if not problem_question:
        return ""
    
    # Split content để lấy phần description (trước Examples:)
    sections = problem_question.split('Examples:')
    description_part = sections[0] if sections else problem_question
    
    # Chỉ clean các HTML entities cơ bản, giữ nguyên tags
    import html
    formatted_desc = html.unescape(description_part)
    
    # Clean up một số whitespace thừa nhưng giữ structure
    formatted_desc = re.sub(r'\n\s*\n\s*\n+', '\n\n', formatted_desc)
    formatted_desc = formatted_desc.strip()
    
    return formatted_desc

def extract_examples_from_html(problem_question):
    """Trích xuất examples từ HTML content, giữ nguyên format"""
    examples = []
    
    # Tìm phần Examples (có thể là "Examples:" hoặc nằm trong content)
    # Pattern phức tạp hơn để handle GFG format
    
    # Tìm tất cả các Input/Output blocks trong content
    input_output_pattern = r'<strong[^>]*>Input[:\s]*</strong[^>]*>(.*?)(?:<strong[^>]*>Output[:\s]*</strong[^>]*>(.*?)(?:<strong[^>]*>Explanation[:\s]*</strong[^>]*>(.*?))?)?(?=<strong[^>]*>Input|<strong[^>]*>Constraints|</p>|$)'
    matches = re.findall(input_output_pattern, problem_question, re.DOTALL | re.IGNORECASE)
    
    for i, match in enumerate(matches):
        input_part, output_part, explanation_part = match
        
        # Clean HTML từ content nhưng giữ format cơ bản
        import html
        input_clean = html.unescape(re.sub(r'<[^>]+>', '', input_part)).strip()
        output_clean = html.unescape(re.sub(r'<[^>]+>', '', output_part)).strip()
        explanation_clean = html.unescape(re.sub(r'<[^>]+>', '', explanation_part)).strip() if explanation_part else ""
        
        if input_clean and output_clean:
            # Tạo example block với HTML format giống LeetCode
            example_html = f'<p><strong class="example">Example {i+1}:</strong></p>\n<pre>\n<strong>Input:</strong> {input_clean}\n<strong>Output:</strong> {output_clean}'
            if explanation_clean:
                example_html += f'\n<strong>Explanation:</strong> {explanation_clean}'
            example_html += '\n</pre>'
            
            examples.append(example_html)
    
    return examples

def extract_constraints_from_html(problem_question):
    """Trích xuất constraints từ HTML, giữ nguyên format"""
    # Tìm phần Constraints với pattern linh hoạt hơn
    constraints_match = re.search(r'<strong[^>]*>Constraints[:\s]*</strong[^>]*>(.*?)(?:<strong[^>]*>(?:Example|Note|Your Task|Follow up)|$)', problem_question, re.DOTALL | re.IGNORECASE)
    
    if not constraints_match:
        # Fallback: tìm text "Constraints:" không có HTML tags
        constraints_match = re.search(r'Constraints[:\s]+(.*?)(?:Example|Note|Your Task|Follow up|$)', problem_question, re.DOTALL | re.IGNORECASE)
    
    if not constraints_match:
        return ""
    
    constraints_section = constraints_match.group(1).strip()
    
    # Chỉ unescape HTML entities, giữ nguyên structure
    import html
    constraints_formatted = html.unescape(constraints_section)
    
    # Nếu đã có HTML structure thì giữ nguyên
    if '<' in constraints_formatted and '>' in constraints_formatted:
        return f"<p><strong>Constraints:</strong></p>\n{constraints_formatted}"
    
    # Nếu là plain text, convert thành HTML list
    lines = [line.strip() for line in constraints_formatted.split('\n') if line.strip()]
    if lines:
        constraints_html = '<p><strong>Constraints:</strong></p>\n<ul>\n'
        for line in lines:
            constraints_html += f'\t<li><code>{line}</code></li>\n'
        constraints_html += '</ul>'
        return constraints_html
    
    return ""

def extract_examples_and_constraints(problem_question):
    """Trích xuất examples và constraints từ problem question"""
    examples = []
    constraints = ""
    
    # Clean toàn bộ content trước
    clean_content = clean_html_content(problem_question)
    
    # Split by common patterns
    sections = clean_content.split('Examples:')
    if len(sections) > 1:
        example_section = sections[1]
        
        # Find constraints section
        constraint_split = example_section.split('Constraints:')
        if len(constraint_split) > 1:
            example_section = constraint_split[0]
            constraints = constraint_split[1].strip()
        
        # Extract individual examples - cải thiện pattern matching
        # Tìm Input: ... Output: ... blocks
        example_pattern = r'Input[:\s]*([^O]*?)(?:Output[:\s]*([^I]*?)(?=Input|Constraints|Note|$))'
        matches = re.findall(example_pattern, example_section, re.DOTALL | re.IGNORECASE)
        
        for i, (input_part, output_part) in enumerate(matches):
            input_clean = input_part.strip()
            output_clean = output_part.strip()
            
            if input_clean or output_clean:
                example = f"Input: {input_clean}\nOutput: {output_clean}"
                
                # Tìm explanation nếu có
                explanation_pattern = rf'Output[:\s]*{re.escape(output_clean)}[^\n]*(?:Explanation[:\s]*([^I]*?)(?=Input|Constraints|Note|$))'
                exp_match = re.search(explanation_pattern, example_section, re.DOTALL | re.IGNORECASE)
                if exp_match:
                    explanation = exp_match.group(1).strip()
                    if explanation:
                        example += f"\nExplanation: {explanation}"
                
                examples.append(example)
    
    return examples, constraints

def generate_gfg_problems_files(data, base_folder, base_name):
    """Tạo các file solution cho từng bài toán GeeksforGeeks"""
    
    for item in data:
        problem_id = item["id"]
        problem_name = item["problem_name"]
        clean_name = clean_filename(problem_name)
        difficulty = item.get("difficulty", "Basic")
        slug = item.get("slug", "")
        accuracy = item.get("accuracy", "N/A")
        
        # Tạo folder theo difficulty
        diff_folder = os.path.join(base_folder, difficulty)
        os.makedirs(diff_folder, exist_ok=True)
        
        filename = f"{problem_id}_{clean_name}.md"
        filepath = os.path.join(diff_folder, filename)
        
        # Tạo URL cho GeeksforGeeks problem
        gfg_url = f"https://www.geeksforgeeks.org/problems/{slug}/"
        
        # Lấy problem question từ JSON data
        problem_question = item.get("problem_question", "")
        
        # Trích xuất examples và constraints với HTML format
        examples_html = extract_examples_from_html(problem_question)
        constraints_html = extract_constraints_from_html(problem_question)
        
        with open(filepath, "w", encoding="utf-8") as f:
            # Header với styling đẹp
            f.write(f"<div align=\"center\">\n\n")
            f.write(f"# 🧠 [{problem_name}]({gfg_url})\n\n")
            f.write(f"[![GeeksforGeeks](<https://img.shields.io/badge/GeeksforGeeks-Problem-0F9D58?style=for-the-badge&logo=geeksforgeeks&logoColor=white>)]({gfg_url})/1\n\n")
            f.write(f"</div>\n\n")
            f.write("---\n\n")
            
            # Problem Overview
            f.write("## 📋 Problem Overview\n\n")
            f.write("| Property | Value |\n")
            f.write("|----------|-------|\n")
            f.write(f"| **Problem ID** | `{problem_id}` |\n")
            f.write(f"| **Difficulty** | {get_difficulty_badge(difficulty)} |\n")
            f.write(f"| **Accuracy** | `{accuracy}` |\n")
            f.write(f"| **Problem Link** | [Open in GeeksforGeeks]({gfg_url})/1 |\n")
            
            # Tags
            tags = item.get("tags", {})
            topic_tags = tags.get("topic_tags", [])
            if topic_tags:
                f.write(f"| **Topic Tags** | ")
                tag_badges = [f"![{tag}](https://img.shields.io/badge/-{tag.replace(' ', '%20')}-blue?style=flat-square)" for tag in topic_tags]
                f.write(" ".join(tag_badges))
                f.write(" |\n")
            
            company_tags = tags.get("company_tags", [])
            if company_tags:
                f.write(f"| **Company Tags** | ")
                comp_badges = [f"![{comp}](https://img.shields.io/badge/-{comp.replace(' ', '%20')}-orange?style=flat-square)" for comp in company_tags]
                f.write(" ".join(comp_badges))
                f.write(" |\n")
            f.write("\n")
            
            # Problem Description - Giữ nguyên HTML format
            f.write("## Description\n")
            f.write("<!-- description:start -->\n")
            
            # Sử dụng HTML format thay vì clean text
            html_description = format_problem_description_html(problem_question)
            f.write(f"{html_description}\n")
            f.write("<!-- description:end -->\n\n")
            
            # Examples - HTML format
            if examples_html:
                f.write("## Examples\n\n")
                for i, example in enumerate(examples_html, 1):
                    f.write(f"{example}\n\n")
            
            # Constraints - HTML format
            if constraints_html:
                f.write("## Constraints\n\n")
                f.write(f"{constraints_html}\n\n")
            
            # Progress Tracking Section
            f.write("## ⏰ Progress Tracking\n\n")
            f.write("| Status | Date | Notes |\n")
            f.write("|--------|------|-------|\n")
            f.write("| 🎯 **Attempted** | `DD-MM-YYYY` | First attempt, understanding the problem |\n")
            f.write("| ✅ **Solved** | `DD-MM-YYYY` | Successfully implemented solution |\n")
            f.write("| 🔄 **Review 1** | `DD-MM-YYYY` | First review, optimization |\n")
            f.write("| 🔄 **Review 2** | `DD-MM-YYYY` | Second review, different approaches |\n")
            f.write("| 🔄 **Review 3** | `DD-MM-YYYY` | Final review, mastery |\n\n")
            
            # Related Articles
            article_list = item.get("article_list", [])
            if article_list:
                f.write("## 📚 Related Articles\n\n")
                for i, article in enumerate(article_list, 1):
                    f.write(f"{i}. [GeeksforGeeks Article {i}]({article})\n")
                f.write("\n")
            
            # Solution template
            f.write("---\n\n")
            f.write("## 💡 Solutions\n\n")
            
            # Approach 1 - Brute Force
            f.write("### 🥉 Approach 1: Brute Force\n\n")
            f.write("#### 📝 Intuition\n")
            f.write("> Mô tả ý tưởng đơn giản nhất để giải quyết bài toán\n\n")
            
            f.write("#### 🔍 Algorithm\n")
            f.write("```pseudo\n")
            f.write("// Write your pseudocode here\n")
            f.write("```\n\n")
            
            f.write("#### 💻 Implementation\n\n")
            
            # C++ Implementation
            f.write("**C++:**\n")
            f.write("```cpp\n")
            f.write("class Solution {\n")
            f.write("public:\n")
            f.write("    int solutionBruteForce() {\n")
            f.write("        // Implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("};\n")
            f.write("```\n\n")
            
            # Python Implementation
            f.write("**Python:**\n")
            f.write("```python\n")
            f.write("class Solution:\n")
            f.write("    def solutionBruteForce(self):\n")
            f.write("        # Implementation here\n")
            f.write("        return 0\n")
            f.write("```\n\n")
            
            # Java Implementation  
            f.write("**Java:**\n")
            f.write("```java\n")
            f.write("class Solution {\n")
            f.write("    public int solutionBruteForce() {\n")
            f.write("        // Implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("}\n")
            f.write("```\n\n")
            
            # Approach 2 - Optimized
            f.write("### 🥈 Approach 2: Optimized Solution\n\n")
            f.write("#### 📝 Intuition\n")
            f.write("> Mô tả cách tối ưu hóa từ approach đầu tiên\n\n")
            
            f.write("#### 🔍 Algorithm\n")
            f.write("```pseudo\n")
            f.write("// Write your pseudocode here\n")
            f.write("```\n\n")
            
            f.write("#### 💻 Implementation\n\n")
            
            # Multiple language implementations for optimized solution
            f.write("**C++:**\n")
            f.write("```cpp\n")
            f.write("class Solution {\n")
            f.write("public:\n")
            f.write("    int solutionOptimized() {\n")
            f.write("        // Optimized implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("};\n")
            f.write("```\n\n")
            
            # Approach 3 - Best Solution  
            f.write("### 🥇 Approach 3: Optimal Solution ⭐\n\n")
            f.write("#### 📝 Intuition\n")
            f.write("> Mô tả giải pháp tốt nhất, elegant nhất\n\n")
            
            f.write("#### 🔍 Algorithm\n")
            f.write("```pseudo\n")
            f.write("// Write your pseudocode here\n")
            f.write("```\n\n")
            
            f.write("#### 💻 Implementation\n\n")
            f.write("**C++:**\n")
            f.write("```cpp\n")
            f.write("class Solution {\n")
            f.write("public:\n")
            f.write("    int solutionOptimal() {\n")
            f.write("        // Optimal implementation here\n")
            f.write("        return 0;\n")
            f.write("    }\n")
            f.write("};\n")
            f.write("```\n\n")
            
            # Comparison table
            f.write("## 📊 Comparison of Approaches\n\n")
            f.write("| Approach | Time Complexity | Space Complexity | Pros | Cons |\n")
            f.write("|----------|-----------------|------------------|------|------|\n")
            f.write("| 🥉 Brute Force | O(?) | O(?) | Simple to implement | High complexity |\n")
            f.write("| 🥈 Optimized   | O(?) | O(?) | Better performance | More complex |\n")
            f.write("| 🥇 Optimal ⭐  | O(?) | O(?) | Best performance | Requires insight |\n\n")
            
            # Footer
            f.write("---\n\n")
            f.write("<div align=\"center\">\n\n")
            f.write(f"**🎯 Problem {problem_id} Completed!**\n\n")
            f.write("*Happy Coding! 🚀*\n\n")
            f.write("</div>\n")
    
    print(f"✅ Generated {len(data)} GeeksforGeeks solution files in: {base_folder}")