use std::path::Path;
use std::{fs, io};

fn main() {
    let src_path: &str = "/home/phydon/main/testfile.txt";
    let dst_path: &str = "/home/phydon/main/test/testfile.txt";

    copy_file(src_path, dst_path).unwrap();
}

fn copy_file(src: &str, dst: &str) -> io::Result<()> {
    // create destination file if it doesn`t exist
    if file_missing(dst) {
        fs::File::create(dst).unwrap();
    }

    // copy src to dst
    fs::copy(src, dst)?;
    Ok(())
}

fn file_missing(path: &str) -> bool {
    let file = Path::new(path);
    if file.exists() {
        return false;
    }
    true
}
