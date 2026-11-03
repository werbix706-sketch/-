import codecs
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with open(html_file, 'r', encoding='utf-8') as file:
           html = file.read()

      clean_text = ''
      inside_tag = False

      for i in html:
          if i == '<':
               inside_tag = True
          elif i == '>':
               inside_tag = False
          elif not inside_tag:
               clean_text += i

      with open(result_file, 'w', encoding='utf-8') as file:
          file.write(clean_text)

delete_html_tags('draft.html')

delete_html_tags('test.html', 'test_cleaned.txt')

