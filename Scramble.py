import base64
import os

def encode_html_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(directory, f'encoded_{filename}')

            with open(input_file, 'rb') as file:
                encoded_html = base64.b64encode(file.read()).decode('utf-8')

            wrapped_html = '''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Encoded HTML</title>
                </head>
                <body>
                    <script>
                        var encodedHTML = '{}';
                        var decodedHTML = atob(encodedHTML);
                        document.write(decodedHTML);
                    </script>
                </body>
                </html>
            '''.format(encoded_md)

            with open(output_file, 'w') as file:
                file.write(wrapped_html)


directory = 'content/glist.md'
encode_html_files(directory)
