# Python & Anaconda

Trang nĂ y hÆ°á»›ng dáº«n cĂ¡ch **quáº£n lĂ½ mĂ´i trÆ°á»ng Python vĂ  package dependencies**.

Python projects thÆ°á»ng sá»­ dá»¥ng **virtual environments** Ä‘á»ƒ:

- trĂ¡nh conflict package
- quáº£n lĂ½ dependency theo project
- Ä‘áº£m báº£o reproducible environment

---

## Má»¥c tiĂªu

Sau bĂ i nĂ y báº¡n cĂ³ thá»ƒ:

- táº¡o **virtual environment**
- quáº£n lĂ½ package báº±ng **pip** hoáº·c **conda**
- cháº¡y **Jupyter Notebook**
- xá»­ lĂ½ lá»—i phá»• biáº¿n khi cĂ i package

---

## YĂªu cáº§u

Báº¡n cáº§n cĂ i:

- **Python 3.9+**
- hoáº·c **Anaconda**

Náº¿u chÆ°a cĂ i mĂ´i trÆ°á»ng, xem:

```text
Quickstart
```

---

## pip vs conda

|             | pip               | conda                     |
| ----------- | ----------------- | ------------------------- |
| Quáº£n lĂ½     | Python packages   | Python + system libraries |
| Nguá»“n       | PyPI              | Anaconda / conda-forge    |
| Environment | venv / virtualenv | conda env                 |
| Lock file   | requirements.txt  | environment.yml           |

---

!!! tip "Quy táº¯c quan trá»ng"
Trong má»™t environment nĂªn **chá»‰ dĂ¹ng pip hoáº·c conda lĂ m package manager chĂ­nh** Ä‘á»ƒ trĂ¡nh conflict.

---

## Virtual Environment

Virtual environment giĂºp má»—i project cĂ³ **dependencies riĂªng biá»‡t**.

---

## Táº¡o environment vá»›i conda

---

### Táº¡o env

```bash
conda create -n myproject python=3.11 -y
```

---

### KĂ­ch hoáº¡t

```bash
conda activate myproject
```

---

### Xem danh sĂ¡ch env

```bash
conda env list
```

---

### CĂ i package

```bash
conda install numpy pandas flask
```

---

### Export environment

```bash
conda env export > environment.yml
```

---

### Táº¡o env tá»« file

```bash
conda env create -f environment.yml
```

---

### XoĂ¡ env

```bash
conda env remove -n myproject
```

---

## Virtual Environment vá»›i venv

Python tĂ­ch há»£p sáºµn **venv**.

---

### Táº¡o environment

```bash
python -m venv .venv
```

---

### KĂ­ch hoáº¡t env

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

---

### CĂ i package

```bash
pip install flask sqlalchemy
```

---

### Export dependencies

```bash
pip freeze > requirements.txt
```

---

### CĂ i tá»« file

```bash
pip install -r requirements.txt
```

---

### ThoĂ¡t environment

```bash
deactivate
```

---

## Cáº¥u trĂºc project Python

Má»™t project Python thÆ°á»ng cĂ³ cáº¥u trĂºc:

```text
myproject/
â”œâ”€â”€ .venv/
â”œâ”€â”€ src/
â”‚   â””â”€â”€ myproject/
â”‚       â”œâ”€â”€ __init__.py
â”‚       â”œâ”€â”€ main.py
â”‚       â””â”€â”€ utils.py
â”œâ”€â”€ tests/
â”‚   â””â”€â”€ test_utils.py
â”œâ”€â”€ requirements.txt
â”œâ”€â”€ pyproject.toml
â””â”€â”€ README.md
```

---

## Jupyter Notebook

Jupyter cho phĂ©p cháº¡y code Python **tá»«ng cell**.

---

### CĂ i Jupyter

```bash
pip install jupyter
```

hoáº·c:

```bash
conda install jupyter
```

---

### Cháº¡y Jupyter

```bash
jupyter notebook
```

---

### JupyterLab (giao diá»‡n má»›i)

```bash
pip install jupyterlab
jupyter lab
```

---

## Kernel cho virtual environment

Äá»ƒ Jupyter nháº­n environment:

---

### CĂ i ipykernel

```bash
pip install ipykernel
```

---

### ÄÄƒng kĂ½ kernel

```bash
python -m ipykernel install --user --name myproject --display-name "Python (myproject)"
```

---

### Xem danh sĂ¡ch kernel

```bash
jupyter kernelspec list
```

---

### XoĂ¡ kernel

```bash
jupyter kernelspec remove myproject
```

---

## `.gitignore` cho Python

```gitignore
__pycache__/
*.pyc
*.pyo

.venv/

*.egg-info/
dist/
build/

.pytest_cache/
.mypy_cache/

.ipynb_checkpoints/

.env
```

---

!!! danger "Quan trá»ng"
KhĂ´ng commit:

```text
.env
.venv
API keys
password
```

---

## Lá»—i thÆ°á»ng gáº·p

| Lá»—i                         | NguyĂªn nhĂ¢n           | CĂ¡ch sá»­a            |
| --------------------------- | --------------------- | ------------------- |
| ModuleNotFoundError         | package chÆ°a cĂ i      | kiá»ƒm tra env        |
| conda: command not found    | chÆ°a init conda       | cháº¡y `conda init`   |
| Could not build wheels      | thiáº¿u build tools     | cĂ i build-essential |
| Solving environment ráº¥t lĂ¢u | conflict dependencies | dĂ¹ng conda-forge    |
| Jupyter kernel sai          | env chÆ°a Ä‘Äƒng kĂ½      | cĂ i ipykernel       |

---

## BĂ i táº­p

### BĂ i 1

Táº¡o conda env:

```text
practice
```

CĂ i:

```text
pandas
requests
```

Export:

```text
environment.yml
```

---

### BĂ i 2

Viáº¿t script Python:

- Ä‘á»c file CSV
- in 5 dĂ²ng Ä‘áº§u

---

### BĂ i 3

Táº¡o Jupyter Notebook:

- import `matplotlib`
- váº½ biá»ƒu Ä‘á»“ Ä‘Æ¡n giáº£n

---

## TĂ i liá»‡u tham kháº£o

```text
https://packaging.python.org/
```

```text
https://docs.conda.io/projects/conda/en/latest/
```
