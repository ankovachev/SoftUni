from pathlib import Path
home = Path('.')
if home.parent.exists():
    print('has parent')
