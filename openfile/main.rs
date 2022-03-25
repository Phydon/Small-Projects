use std::process::Command;

fn main() {
    let file_path: &str = "/home/phydon/main/test/testfile.txt";

    open_file(file_path);
}

fn open_file(file: &str) {
    Command::new("vim").arg(file).status().unwrap();
}
