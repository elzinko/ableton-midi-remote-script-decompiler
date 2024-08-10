import os
import uncompyle6
from pathlib import Path
import sys

def decompile_ableton_scripts(source_dir, output_dir):
    """
    Décompile tous les fichiers .pyc ou .pyo dans le répertoire source
    et les place dans le répertoire de sortie.
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Le répertoire source {source_dir} n'existe pas.")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.pyc', '.pyo')):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_dir)
                output_file_dir = os.path.join(output_dir, relative_path)
                
                Path(output_file_dir).mkdir(parents=True, exist_ok=True)
                
                output_file_path = os.path.join(output_file_dir, file[:-1] + "py")
                
                try:
                    with open(output_file_path, 'w') as output_file:
                        uncompyle6.decompile_file(source_file_path, outstream=output_file)
                    print(f"Décompilé : {source_file_path} -> {output_file_path}")
                except Exception as e:
                    print(f"Erreur lors de la décompilation de {source_file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python decompile.py <source_directory> <output_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    output_directory = sys.argv[2]
    
    decompile_ableton_scripts(source_directory, output_directory)
