// Cargo.toml
// [dependencies]
// indicatif = "0.16.2"

use indicatif::{ProgressBar, ProgressStyle};

use std::cmp::min;
use std::time::Duration;
use std::thread;

fn main() {
    progress_bar();
    progress_bar_simple();
}

fn sleep(num: u64) {
    thread::sleep(Duration::from_millis(num));
}

fn progress_bar() {
    let mut idx = 0;
    let end = 2000;

    let pb = ProgressBar::new(end);
    pb.set_style(ProgressStyle::default_bar()
        .template("{spinner:.green} [{elapsed_precise}] [{wide_bar:.cyan/blue}] {bytes}/{total_bytes} ({eta})")
        .progress_chars("#>-"));

    while idx < end {
        let new = min(idx + 10, end);
        idx = new;
        pb.set_position(new);
        sleep(15);
    }

    pb.finish_with_message("done");
}

fn progress_bar_simple() {
    let end = 512;

    let pb = ProgressBar::new(end);
    for _ in 0..end {
        pb.inc(1);
        sleep(5);
    }
    pb.finish_with_message("done");
}
