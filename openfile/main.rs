use std::io;
use std::process::Command;

fn main() {
    let file_path: &str = "/home/phydon/main/test/testfile.txt";

    open_file(file_path).expect("Failed to execute command");
}

fn open_file(file: &str) -> io::Result<()> {
    // change the tool to whatever is needed
    if cfg!(target_os = "windows") {
        Command::new("cmd").args(["/C", file]).status()?;
        Ok(())
    } else {
        Command::new("vim").arg(file).status()?;
        Ok(())
    }
}
