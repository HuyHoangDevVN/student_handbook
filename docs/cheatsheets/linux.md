# Linux Cheat Sheet

> Copy-paste nhanh cĂ¡c lá»‡nh Linux thÆ°á»ng dĂ¹ng.

---

## Di chuyá»ƒn & File

```bash
pwd                           # ThÆ° má»¥c hiá»‡n táº¡i
ls -la                        # Liá»‡t kĂª chi tiáº¿t + file áº©n
cd /path/to/dir               # Di chuyá»ƒn
cd ..                         # LĂªn 1 cáº¥p
cd ~                          # Vá» home
cd -                          # Quay láº¡i thÆ° má»¥c trÆ°á»›c

mkdir -p dir/subdir            # Táº¡o folder lá»“ng nhau
touch file.txt                 # Táº¡o file rá»—ng
cp -r src/ dest/               # Copy folder
mv old new                     # Di chuyá»ƒn / Ä‘á»•i tĂªn
rm -rf folder/                 # XoĂ¡ folder (â ï¸ cáº©n tháº­n!)
```

## Xem & TĂ¬m kiáº¿m

```bash
cat file.txt                   # In ná»™i dung file
head -20 file.txt              # 20 dĂ²ng Ä‘áº§u
tail -f app.log                # Follow log realtime
less file.txt                  # Xem tá»«ng trang
wc -l file.txt                 # Äáº¿m dĂ²ng

grep -rn "pattern" .           # TĂ¬m text trong file
find . -name "*.py" -type f    # TĂ¬m file theo tĂªn
```

## Quyá»n (Permissions)

```bash
chmod +x script.sh             # Cáº¥p quyá»n thá»±c thi
chmod 755 file                 # rwxr-xr-x
chmod 644 file                 # rw-r--r--
chown user:group file          # Äá»•i owner
```

## Process

```bash
ps aux                         # Liá»‡t kĂª process
ps aux | grep node             # TĂ¬m process
kill PID                       # Dá»«ng process
kill -9 PID                    # Force kill
pkill -f "pattern"             # Kill theo tĂªn
htop                           # Monitor realtime
```

## Network

```bash
ip addr show                   # Xem IP
ss -tulnp                      # Xem port Ä‘ang má»Ÿ
lsof -i :8080                  # Ai dĂ¹ng port 8080
curl -I http://localhost:3000   # Test HTTP
ping google.com -c 4           # Test connectivity
wget URL                       # Táº£i file
```

## Pipe & Redirect

```bash
cmd1 | cmd2                    # Pipe output
echo "text" > file             # Ghi Ä‘Ă¨ file
echo "text" >> file            # Ghi thĂªm cuá»‘i file
cmd 2> error.log               # Redirect stderr
cmd > all.log 2>&1             # Redirect cáº£ stdout + stderr
```

## Package (Ubuntu/Debian)

```bash
sudo apt update                # Cáº­p nháº­t danh sĂ¡ch
sudo apt install -y pkg        # CĂ i package
sudo apt remove pkg            # Gá»¡ package
apt search keyword             # TĂ¬m package
```

## Disk & System

```bash
df -h                          # Disk usage
du -sh folder/                 # KĂ­ch thÆ°á»›c folder
free -h                        # RAM usage
uname -a                       # ThĂ´ng tin há»‡ thá»‘ng
whoami                         # User hiá»‡n táº¡i
history | grep cmd             # Lá»‹ch sá»­ lá»‡nh
```

## Biáº¿n mĂ´i trÆ°á»ng

```bash
echo $PATH                     # Xem PATH
export MY_VAR="value"          # Set biáº¿n (session)
echo 'export VAR="val"' >> ~/.bashrc  # Set cá»‘ Ä‘á»‹nh
source ~/.bashrc               # Reload config
```

## NĂ©n & Giáº£i nĂ©n

```bash
tar -czf archive.tar.gz dir/   # NĂ©n
tar -xzf archive.tar.gz        # Giáº£i nĂ©n
zip -r archive.zip dir/        # NĂ©n zip
unzip archive.zip              # Giáº£i nĂ©n zip
```
