use std::{io, time::Duration, thread::sleep};
use std::process::Command;

fn main() {
    let cmd_clear: &str = "clear";

    exec(cmd_clear).expect("Failed to execute command");
    println!("FOO");
    sleep(Duration::from_secs(2));
    exec(cmd_clear).expect("Failed to execute command");
    println!("BAR");
    sleep(Duration::from_secs(2));
    exec(cmd_clear).expect("Failed to execute command");
    println!("END");
}

 fn exec(cmd: &str) -> io::Result<()> {
    if cfg!(target_os = "windows") {
        Command::new("cmd").args(["/C", cmd]).status()?;
        Ok(())
    } else {
        Command::new(cmd).status()?;
        Ok(())
    }
 }
