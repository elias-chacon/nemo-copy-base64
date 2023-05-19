# Nemo copy base64 from a file

Copy base64 from a file in Nemo

It adds a context menu called "Copy base64"

You will be able to copy the file content and paste the base64 



# How to install:

Clone this repository:

```bash
git clone https://github.com/elias-chacon/nemo-copy-base64.git
cd nemo-copy-base64
chmod +x install.sh
```



Run the **install.sh** file.

Ex:

```bash
# go to this reporitory directory 
./install.sh
```

It will create a directory into **~/.local/share** and will copy the file to there.

* Notice: your nemo instance will be restarted.



# Manual installation:

Follow the manual installation:

```bash
mkdir -p ~/.local/share/nemo-python/extensions
cp -f ./nemo-base64-copy.py ~/.local/share/nemo-python/extensions
nemo -q
```

# After all

Whenever you installed the script. You will be able to copy base64.
