use std::fs;
use chrono::Local;
use std::collections::BTreeMap;
use std::io::Write;

fn main() {
    let file_path = "/home/phydon/main/simple_logging/logfile.txt";

    let mut file = fs::OpenOptions::new()
        .read(true)
        .append(true)
        .create(true) // if file doesn`t exist already
        .open(file_path)
        .unwrap();

    // Hashmap -> unsorted
    // BTreeMap -> sorted
    let mut container: BTreeMap<_,_> = BTreeMap::new();

    // log the current date and time as key and some random values
    // change to whatever should be logged
    for i in 1..=10 {
        let datetime = Local::now().to_string();
        container.insert(datetime, i * i);
    }

    for (key, value) in &container {
        match writeln!(file, "{}: {}", key, value) {
            Ok(ok) => ok,
            Err(_) => eprintln!("Error while writing to file {}", file_path)
        };
    }
}
