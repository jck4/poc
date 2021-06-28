use structopt::StructOpt;

use sysinfo::{ProcessExt, SystemExt};




/// Search for a pattern in a file and display the lines that contain it.
#[derive(StructOpt)]
struct Cli {
    /// The pattern to look for
    pattern: String,
    /// The path to the file to read
    #[structopt(parse(from_os_str))]
    path: std::path::PathBuf,
}

fn main() {
    let mut system = sysinfo::System::new_all();
    system.refresh_all();

    for (pid, proc_) in system.get_processes() {
        println!("{}:{} => status: {:?}", pid, proc_.name(), proc_.status());
    }

    let args = Cli::from_args();
    let _pattern = args.pattern;
    let _path = args.path;

    system.

    println!("{}", system.get_total_memory());
}




