import os
import jinja2

def check_templates():
    env = jinja2.Environment()
    encodings = ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin-1']
    
    for root, dirs, files in os.walk('templates'):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                content = None
                successful_encoding = None
                
                for enc in encodings:
                    try:
                        with open(path, 'r', encoding=enc) as fh:
                            content = fh.read()
                        successful_encoding = enc
                        break
                    except Exception:
                        continue
                
                if content is None:
                    print(f"ERROR: Could not read {path} with any known encoding.")
                    continue
                
                try:
                    env.parse(content)
                    print(f"OK: {path} (Parsed successfully using {successful_encoding})")
                except jinja2.TemplateSyntaxError as e:
                    print(f"JINJA ERROR in {path} (encoding {successful_encoding}): line {e.lineno} - {e.message}")
                except Exception as e:
                    print(f"ERROR in {path}: {e}")

if __name__ == '__main__':
    check_templates()
