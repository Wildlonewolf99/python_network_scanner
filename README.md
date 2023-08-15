# Python Network Scanner

# Network Scanner

The Network Scanner is a Python script that scans your local network for used and free IP addresses. It also identifies open ports on the used IP addresses for specified services.

## Features

- Scans the local network for used and free IP addresses.
- Identifies open ports on used IP addresses for specified services (ports can be customized).
- Supports saving the scan results to a text file.

## Requirements

- Python 3.x
- `socket` library
- `concurrent.futures` library
- `tqdm` library (for progress bar)
- `argparse` library (for command-line arguments)

## Usage

1. Clone or download this repository.

2. Install the required libraries using the following command:

   ```bash
   pip install tqdm

3. Run the script with the following command:

        python network_scanner.py [-o OUTPUT]

   
- Use the `-o` option to specify an output file where the scan results will be saved. If not specified, results will be printed to the console.

4. The script will start scanning your local network. It will display progress using a progress bar.

5. Once the scan is complete, the script will display a list of used IP addresses along with their open ports (if any), and a list of free IP addresses.

## Customization

- You can customize the list of known ports to be scanned by modifying the `KNOWN_PORTS` list in the script.

## Example

To scan the network and save the results to an output file named `scan_results.txt`, run the following command:

    python network_scanner.py -o scan_results.txt

## Disclaimer

Please ensure that you have proper authorization to scan your network before using this script. Unauthorized scanning can violate network policies and legal regulations. Use this script responsibly and only on networks where you have explicit permission.

## License

This script is licensed under the [MIT License](LICENSE).


