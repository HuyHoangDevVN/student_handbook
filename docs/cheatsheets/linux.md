# Linux Cheat Sheet

> Copy-paste nhanh các lệnh Linux thường dùng.

---

## Di chuyển & File

```bash
pwd                           # Thư mục hiện tại
ls -la                        # Liệt kê chi tiết + file ẩn
cd /path/to/dir               # Di chuyển
cd ..                         # Lên 1 cấp
cd ~                          # Về home
cd -                          # Quay lại thư mục trước

mkdir -p dir/subdir            # Tạo folder lồng nhau
touch file.txt                 # Tạo file rỗng
cp -r src/ dest/               # Copy folder
mv old new                     # Di chuyển / đổi tên
rm -rf folder/                 # Xoá folder (â ï¸ cẩn thận!)
```

## Xem & Tìm kiếm

```bash
cat file.txt                   # In nội dung file
head -20 file.txt              # 20 dòng đầu
tail -f app.log                # Follow log realtime
less file.txt                  # Xem từng trang
wc -l file.txt                 # Đếm dòng

grep -rn "pattern" .           # Tìm text trong file
find . -name "*.py" -type f    # Tìm file theo tên
```

## Quyền (Permissions)

```bash
chmod +x script.sh             # Cấp quyền thực thi
chmod 755 file                 # rwxr-xr-x
chmod 644 file                 # rw-r--r--
chown user:group file          # Đổi owner
```

## Process

```bash
ps aux                         # Liệt kê process
ps aux | grep node             # Tìm process
kill PID                       # Dừng process
kill -9 PID                    # Force kill
pkill -f "pattern"             # Kill theo tên
htop                           # Monitor realtime
```

## Network

```bash
ip addr show                   # Xem IP
ss -tulnp                      # Xem port đang mở
lsof -i :8080                  # Ai dùng port 8080
curl -I http://localhost:3000   # Test HTTP
ping google.com -c 4           # Test connectivity
wget URL                       # Tải file
```

## Pipe & Redirect

```bash
cmd1 | cmd2                    # Pipe output
echo "text" > file             # Ghi đè file
echo "text" >> file            # Ghi thêm cuối file
cmd 2> error.log               # Redirect stderr
cmd > all.log 2>&1             # Redirect cả stdout + stderr
```

## Package (Ubuntu/Debian)

```bash
sudo apt update                # Cập nhật danh sách
sudo apt install -y pkg        # Cài package
sudo apt remove pkg            # Gỡ package
apt search keyword             # Tìm package
```

## Disk & System

```bash
df -h                          # Disk usage
du -sh folder/                 # Kích thước folder
free -h                        # RAM usage
uname -a                       # Thông tin hệ thống
whoami                         # User hiện tại
history | grep cmd             # Lịch sử lệnh
```

## Biến môi trường

```bash
echo $PATH                     # Xem PATH
export MY_VAR="value"          # Set biến (session)
echo 'export VAR="val"' >> ~/.bashrc  # Set cố định
source ~/.bashrc               # Reload config
```

## Nén & Giải nén

```bash
tar -czf archive.tar.gz dir/   # Nén
tar -xzf archive.tar.gz        # Giải nén
zip -r archive.zip dir/        # Nén zip
unzip archive.zip              # Giải nén zip
```
