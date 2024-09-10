import subprocess
import os

def remove_bg(input_path, output_path):
    # Garante que o arquivo de saída tenha a extensão .png
    if not output_path.lower().endswith('.png'):
        output_path = os.path.splitext(output_path)[0] + '.png'
    
    # Executa o comando da ferramenta image-background-remove-tool corretamente
    subprocess.run([
        "python", 
        "-m", "carvekit",  # Comando para o módulo carvekit
        "-i", input_path,  # Caminho da imagem de entrada
        "-o", output_path,  # Caminho da imagem de saída
        "--device", "cpu"  # Use "cpu" ou "cuda" dependendo do seu setup
    ])
