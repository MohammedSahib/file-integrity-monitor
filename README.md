# File Integrity Monitor

A simple Python command-line tool that uses SHA-256 hashing to detect changes to files by comparing their current state against previously saved snapshots.

## Features

- Create SHA-256 hash snapshots of files.
- Store snapshots in a JSON file.
- Detect file modifications.
- Update snapshots after intentional changes.
- Monitor multiple files.
- Basic error handling.


## Usage

**1. Create a snapshot**

```bash
python monitor.py init testing.txt
```

Saves the file's original SHA-256 hash to `destination.json`.

**2. Check file integrity**

```bash
python monitor.py check testing.txt
```

Compares the current file hash against the stored snapshot and reports whether the file has changed.

**3. Update a snapshot**

```bash
python monitor.py update testing.txt
```

Updates the stored hash after an intentional modification.

## How It Works

The program calculates a SHA-256 hash of the file's contents and stores it in `destination.json`, using the file's absolute path as the key.

When checking integrity, it recalculates the hash and compares it with the stored value. A mismatch indicates that the file's contents have changed.

## Limitations

- Currently supports individual files, not recursive directory monitoring.
- Detects changes to file contents, not metadata or permissions.
- The JSON baseline is not protected against tampering.