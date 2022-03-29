use std::process::Command;

fn main() {
    let file_path: &str = "/home/phydon/main/test/testfile.txt";

    open_file(file_path);
}

fn open_file(file: &str) {
    // change the tool to whatever is needed
    if cfg!(target_os = "windows") {
        Command::new("cmd").args(["/C", file]).status().unwrap();
    } else {
        Command::new("vim").arg(file).status().unwrap();
    }
}
