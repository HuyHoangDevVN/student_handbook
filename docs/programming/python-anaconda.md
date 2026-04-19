# Python & Anaconda

Trang này hướng dẫn cách **quản lý môi trường Python và package dependencies**.

Python projects thường sử dụng **virtual environments** để:

- tránh conflict package
- quản lý dependency theo project
- đảm bảo reproducible environment

---

## Mục tiêu

Sau bài này bạn có thể:

- tạo **virtual environment**
- quản lý package bằng **pip** hoặc **conda**
- chạy **Jupyter Notebook**
- xử lý lỗi phổ biến khi cài package

---

## Yêu cầu

Bạn cần cài:

- **Python 3.9+**
- hoặc **Anaconda**

Nếu chưa cài môi trường, xem:

```text
Quickstart
```

---

## pip vs conda

|             | pip               | conda                     |
| ----------- | ----------------- | ------------------------- |
| Quản lý     | Python packages   | Python + system libraries |
| Nguồn       | PyPI              | Anaconda / conda-forge    |
| Environment | venv / virtualenv | conda env                 |
| Lock file   | requirements.txt  | environment.yml           |

---

!!! tip "Quy tắc quan trọng"
Trong một environment nên **chỉ dùng pip hoặc conda làm package manager chính** để tránh conflict.

---

## Virtual Environment

Virtual environment giúp mỗi project có **dependencies riêng biệt**.

---

## Tạo environment với conda

---

### Tạo env

```bash
conda create -n myproject python=3.11 -y
```

---

### Kích hoạt

```bash
conda activate myproject
```

---

### Xem danh sách env

```bash
conda env list
```

---

### Cài package

```bash
conda install numpy pandas flask
```

---

### Export environment

```bash
conda env export > environment.yml
```

---

### Tạo env từ file

```bash
conda env create -f environment.yml
```

---

### Xoá env

```bash
conda env remove -n myproject
```

---

## Virtual Environment với venv

Python tích hợp sẵn **venv**.

---

### Tạo environment

```bash
python -m venv .venv
```

---

### Kích hoạt env

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.\.venv\Scripts\Activate.ps1
```

---

### Cài package

```bash
pip install flask sqlalchemy
```

---

### Export dependencies

```bash
pip freeze > requirements.txt
```

---

### Cài từ file

```bash
pip install -r requirements.txt
```

---

### Thoát environment

```bash
deactivate
```

---

## Cấu trúc project Python

Một project Python thường có cấu trúc:

```text
myproject/
├── .venv/
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   └── test_utils.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## Jupyter Notebook

Jupyter cho phép chạy code Python **từng cell**.

---

### Cài Jupyter

```bash
pip install jupyter
```

hoặc:

```bash
conda install jupyter
```

---

### Chạy Jupyter

```bash
jupyter notebook
```

---

### JupyterLab (giao diện mới)

```bash
pip install jupyterlab
jupyter lab
```

---

## Kernel cho virtual environment

Để Jupyter nhận environment:

---

### Cài ipykernel

```bash
pip install ipykernel
```

---

### Đăng ký kernel

```bash
python -m ipykernel install --user --name myproject --display-name "Python (myproject)"
```

---

### Xem danh sách kernel

```bash
jupyter kernelspec list
```

---

### Xoá kernel

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

!!! danger "Quan trọng"
Không commit:

```text
.env
.venv
API keys
password
```

---

## Lỗi thường gặp

| Lỗi                         | Nguyên nhân           | Cách sửa            |
| --------------------------- | --------------------- | ------------------- |
| ModuleNotFoundError         | package chưa cài      | kiểm tra env        |
| conda: command not found    | chưa init conda       | chạy `conda init`   |
| Could not build wheels      | thiếu build tools     | cài build-essential |
| Solving environment rất lâu | conflict dependencies | dùng conda-forge    |
| Jupyter kernel sai          | env chưa đăng ký      | cài ipykernel       |

---

## Bài tập

### Bài 1

Tạo conda env:

```text
practice
```

Cài:

```text
pandas
requests
```

Export:

```text
environment.yml
```

---

### Bài 2

Viết script Python:

- đọc file CSV
- in 5 dòng đầu

---

### Bài 3

Tạo Jupyter Notebook:

- import `matplotlib`
- vẽ biểu đồ đơn giản

---

## Tài liệu tham khảo

```text
https://packaging.python.org/
```

```text
https://docs.conda.io/projects/conda/en/latest/
```
