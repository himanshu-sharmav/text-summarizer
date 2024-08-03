import click
import requests
import json

def send_prompt(content):
    url = "http://localhost:11434/api/chat"  

    data = {
        "model": "qwen2:0.5b", 
        "messages": [
            {
                "role": "user",
                "content": f"{content}"
            },
        ],
        "stream": True  
    }

    response = requests.post(url, json=data, stream=True)
    print(response.status_code)
    if response.status_code == 200:
        full_response = ''
        for line in response.iter_lines():
            if line:
                try:
                    json_object = json.loads(line)
                    if 'message' in json_object and 'content' in json_object['message']:
                        chunk = json_object['message']['content']
                        full_response += chunk
                        # print(chunk, end='', flush=True)
                except json.JSONDecodeError:
                    pass
        print()
        return full_response
    else:
        print(f"Error: {response.status_code}")
        return response.text

@click.command()
@click.option('-t', '--text', 'input_text', type=click.STRING, required=False, help='Text to summarize')
@click.option('-f', '--file', 'file_path', type=click.Path(exists=True), required=False, help='Path to the text file to summarize')
def summarize(input_text, file_path):
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
        summary = send_prompt(text)
        click.echo(f"Summary of {file_path}:\n{summary}")
    elif input_text:
        summary = send_prompt(input_text)
        click.echo(f"Summary of provided text:\n{summary}")
    else:
        click.echo("Please provide either text or a file path.")

if __name__ == "__main__":
    summarize()
