import os
import pdb

def rename_images(folder_path):
    # Verifica se o diretório existe
    if not os.path.exists(folder_path):
        print("O diretório não existe.")
        return

    # Lista de arquivos no diretório
    files = os.listdir(folder_path)
    
    # Filtrar apenas os arquivos de imagem (supondo que são arquivos com extensões comuns)
    image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Ordenar os arquivos
    image_files.sort()

    # Renomear os arquivos em ordem numérica
    for i, filename in enumerate(image_files, start=1):
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, str(i) + os.path.splitext(filename)[1])
        os.rename(src, dst)
        print(f"Renomeando {filename} para {str(i) + os.path.splitext(filename)[1]}")

if __name__ == "__main__":
    #folder_path = "data/images/train"
    folder_path = "data/masks"
    rename_images(folder_path)
