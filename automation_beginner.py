import pathlib

desktop  = pathlib.Path('/Users/91763/Desktop')

new_path = pathlib.Path('/Users/91763/Desktop/Screenshots')
new_path.mkdir(exist_ok=True)

for filepath in desktop.iterdir():
    if filepath.suffix == '.png':
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)